import json
import subprocess
from pathlib import Path
import platform
import os
import shutil
import argparse
import re
import sys

def clr(t: str, *c) -> str:
    """Colorize text using ANSI escape sequences if colors are enabled."""
    if "NO_COLOR" in os.environ:
        return t
    if sys.stdout.isatty() or os.environ.get("FORCE_COLOR"):
        codes = ";".join(str(x) for x in c)
        return f"\033[{codes}m{t}\033[0m"
    return t

parser = argparse.ArgumentParser(description="Build plugins with CMake")
parser.add_argument(
    "--compiler-launcher",
    type=str,
    help="Optional compiler launcher (e.g., ccache, sccache)"
)
parser.add_argument(
    "--generator",
    choices=["ninja", "xcode", "visualstudio"],
    default="ninja",
    help="CMake generator to use: ninja (default), xcode, or visualstudio"
)
parser.add_argument(
    "--configure-only",
    action="store_true",
    help="Only run CMake configuration, skip the build step"
)

args = parser.parse_args()

# ── Sanity-check helpers ────────────────────────────────────────────────────

KNOWN_FORMATS = {"VST3", "AU", "LV2", "CLAP", "Standalone"}
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")

errors = []   # fatal problems  – abort after collecting all of them
warnings = [] # non-fatal oddities
build_results = [] # track (plugin_name, target, status) where status is 'SUCCESS' or 'FAILED'

def error(msg: str):
    errors.append(clr(f"  ERROR: {msg}", 91))

def warn(msg: str):
    warnings.append(clr(f"  WARNING: {msg}", 93))

def validate_config(path: str) -> list:
    """Load and validate config.json. Returns the parsed list or exits."""
    if not os.path.isfile(path):
        print(clr(f"FATAL: config.json not found at '{os.path.abspath(path)}'", 1, 91))
        sys.exit(1)

    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(clr(f"FATAL: config.json is not valid JSON – {e}", 1, 91))
        sys.exit(1)

    if not isinstance(data, list):
        print(clr("FATAL: config.json must contain a JSON array of plugin objects.", 1, 91))
        sys.exit(1)

    if len(data) == 0:
        warn("config.json contains no plugins – nothing to build.")

    return data

def validate_plugin(plugin: dict, index: int):
    prefix = f"Plugin[{index}]"

    # ── Required fields ──────────────────────────────────────────────────────
    name = plugin.get("name")
    if not name:
        error(f"{prefix}: missing required field 'name'.")
    elif not isinstance(name, str) or not name.strip():
        error(f"{prefix}: 'name' must be a non-empty string (got {name!r}).")

    path = plugin.get("path")
    if not path:
        error(f"{prefix} ({name!r}): missing required field 'path'.")
    else:
        resolved = Path(path).resolve()
        if not resolved.exists():
            error(f"{prefix} ({name!r}): plugin path does not exist: '{resolved}'")
        elif not (resolved.is_file() or resolved.is_dir()):
            error(f"{prefix} ({name!r}): plugin path must be a file or a folder: '{resolved}'")

    # ── Optional but validated fields ────────────────────────────────────────
    formats = plugin.get("formats", [])
    if not isinstance(formats, list):
        error(f"{prefix} ({name!r}): 'formats' must be a list, got {type(formats).__name__}.")
    else:
        if len(formats) == 0:
            warn(f"{prefix} ({name!r}): 'formats' is empty – no build targets will be produced.")
        for fmt in formats:
            if fmt not in KNOWN_FORMATS:
                warn(f"{prefix} ({name!r}): unknown format '{fmt}'. "
                     f"Known formats are: {', '.join(sorted(KNOWN_FORMATS))}.")

    plugin_type = plugin.get("type", "")
    if plugin_type and plugin_type.lower() not in ("fx", "instrument", ""):
        warn(f"{prefix} ({name!r}): unexpected 'type' value '{plugin_type}'. "
             f"Expected 'fx' or 'instrument'.")

    version = plugin.get("version", "1.0.0")
    if not VERSION_RE.match(str(version)):
        warn(f"{prefix} ({name!r}): 'version' value '{version}' does not follow "
             f"MAJOR.MINOR.PATCH format.")

    for bool_field in ("enable_gem", "enable_sfizz", "enable_ffmpeg"):
        val = plugin.get(bool_field)
        if val is not None and not isinstance(val, bool):
            warn(f"{prefix} ({name!r}): '{bool_field}' should be a boolean, got {val!r}.")

# ── Run validation ───────────────────────────────────────────────────────────

plugins_config = validate_config("config.json")

for i, plugin in enumerate(plugins_config):
    if not isinstance(plugin, dict):
        error(f"Plugin[{i}]: expected an object, got {type(plugin).__name__}.")
        continue
    validate_plugin(plugin, i)

if warnings:
    print(clr("Build warnings:", 1, 93))
    for w in warnings:
        print(w)
    print()

if errors:
    print(clr("Build errors – cannot continue:", 1, 91))
    for e in errors:
        print(e)
    sys.exit(1)

# ── Continue with the rest of the build ─────────────────────────────────────

system = platform.system()
if system == "Windows":
    cmake_compiler = ["-DCMAKE_C_COMPILER=cl", "-DCMAKE_CXX_COMPILER=cl"]
else:
    cmake_compiler = []

if args.generator == "xcode":
    cmake_generator = ["-GXcode"]
elif args.generator == "visualstudio":
    cmake_generator = ["-GVisual Studio 17 2022", "-A x64"]
    cmake_compiler = []
else:
    cmake_generator = ["-GNinja"]

plugdata_dir = Path("plugdata").resolve()
builds_parent_dir = plugdata_dir.parent

plugins_dir = os.path.join("plugdata", "Plugins")
build_output_dir = os.path.join("Build")
os.makedirs(build_output_dir, exist_ok=True)

if not plugdata_dir.is_dir():
    print(clr(f"FATAL: plugdata directory not found at '{plugdata_dir}'. "
          f"Make sure you're running this script from the repo root and that "
          f"the plugdata submodule has been initialised (git submodule update --init).", 1, 91))
    sys.exit(1)

for plugin in plugins_config:
    name = plugin["name"]
    zip_path = Path(plugin["path"]).resolve()
    patch = plugin["patch"]
    formats = plugin.get("formats", [])
    is_fx = plugin.get("type", "").lower() == "fx"

    build_dir = builds_parent_dir / f"{args.generator}-{name}"
    print(f"\n{clr('Processing:', 36)} {clr(name, 1)}")

    author = plugin.get("author", False)
    version = plugin.get("version", "1.0.0")
    enable_gem = plugin.get("enable_gem", False)
    enable_sfizz = plugin.get("enable_sfizz", False)
    enable_ffmpeg = plugin.get("enable_ffmpeg", False)

    cmake_configure = [
        "cmake",
        "-GNinja",
        *cmake_generator,
        *cmake_compiler,
        f"-B{build_dir}",
        f"-DCUSTOM_PLUGIN_NAME={name}",
        f"-DCUSTOM_PLUGIN_PATCH={patch}",
        f"-DCUSTOM_PLUGIN_PATH={zip_path}",
        f"-DCUSTOM_PLUGIN_COMPANY={author}",
        f"-DCUSTOM_PLUGIN_VERSION={version}",
        "-DCMAKE_BUILD_TYPE=Release",
        f"-DENABLE_GEM={'1' if enable_gem else '0'}",
        f"-DENABLE_SFIZZ={'1' if enable_sfizz else '0'}",
        f"-DENABLE_FFMPEG={'1' if enable_ffmpeg else '0'}",
        f"-DCUSTOM_PLUGIN_IS_FX={'1' if is_fx else '0'}"
    ]

    if args.compiler_launcher:
        cmake_configure.append(f"-DCMAKE_C_COMPILER_LAUNCHER={args.compiler_launcher}")
        cmake_configure.append(f"-DCMAKE_CXX_COMPILER_LAUNCHER={args.compiler_launcher}")

    result_configure = subprocess.run(cmake_configure, cwd=plugdata_dir)
    if result_configure.returncode != 0:
        print(clr(f"Failed cmake configure for {name}", 91))
        build_results.append((name, "CMake Configure", "FAILED"))
        continue
    else:
        build_results.append((name, "CMake Configure", "SUCCESS"))

    if not args.configure_only:
        for fmt in formats:
            if system != "Darwin" and fmt == "AU":
                continue
            target = f"plugdata_{'fx_' if is_fx else ''}{fmt}"
            if fmt == "Standalone":
                target = "plugdata_standalone"

            cmake_build = [
                "cmake",
                "--build", str(build_dir),
                "--target", target,
                "--config Release"
            ]
            print(f"{clr('Building target:', 36)} {clr(target, 1)}")
            result_build = subprocess.run(cmake_build, cwd=plugdata_dir)
            if result_build.returncode != 0:
                print(clr(f"Failed to build target: {target}", 91))
                build_results.append((name, target, "FAILED"))
            else:
                print(clr(f"Successfully built: {target}", 92))
                build_results.append((name, target, "SUCCESS"))
            format_path = os.path.join(plugins_dir, fmt)
            target_dir = os.path.join(build_output_dir, fmt)

            if fmt == "Standalone":
                if os.path.isdir(format_path):
                    if os.path.exists(target_dir):
                        shutil.rmtree(target_dir)
                    shutil.copytree(format_path, target_dir)
            else:
                extension = ""
                if fmt == "VST3":
                    extension = ".vst3"
                elif fmt == "AU":
                    extension = ".component"
                elif fmt == "LV2":
                    extension = ".lv2"
                elif fmt == "CLAP":
                    extension = ".clap"

                plugin_filename = name + extension
                os.makedirs(target_dir, exist_ok=True)
                src = os.path.join(format_path, plugin_filename)
                dst = os.path.join(target_dir, plugin_filename)
                if os.path.isdir(src):
                    if os.path.exists(dst):
                        shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                else:
                    if os.path.exists(dst):
                        os.remove(dst)
                    shutil.copy2(src, dst)

# ── Summary Table ───────────────────────────────────────────────────────────

if build_results:
    # Header names and their minimum widths to guarantee proper alignment
    h_plugin = "Plugin"
    h_target = "Target"
    h_status = "Status"

    p_width = max(len(h_plugin), max(len(row[0]) for row in build_results))
    t_width = max(len(h_target), max(len(row[1]) for row in build_results))

    # We want a top/bottom border that spans the exact width of the table columns.
    # Formula: p_width + t_width + 20 (accounting for padding, borders, and margins)
    border_len = p_width + t_width + 20
    border_line = "-" * border_len

    print("\n" + clr(border_line, 1, 34))
    print(clr(f"| {h_plugin:<{p_width}} | {h_target:<{t_width}} | {h_status:<10} |", 1, 34))
    print(clr(border_line, 1, 34))

    for plugin_name, target, status in build_results:
        if status == "SUCCESS":
            status_text = clr(status, 92) # Green SUCCESS
        else:
            status_text = clr(status, 91) # Red FAILED

        # Calculate padding to keep alignment perfect in terminal (since ANSI escape codes don't take visual space).
        # Header's status column width is 10. `status_text` has visual length equal to len(status).
        padding = " " * (10 - len(status))
        print(f"| {plugin_name:<{p_width}} | {target:<{t_width}} | {status_text}{padding} |")

    print(clr(border_line, 1, 34) + "\n")
