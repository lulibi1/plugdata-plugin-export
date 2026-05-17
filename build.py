import json
import subprocess
from pathlib import Path
import platform
import os
import shutil
import argparse
import re
import sys

parser = argparse.ArgumentParser(description="Build plugins with CMake")
parser.add_argument("--compiler-launcher", type=str, help="Optional compiler launcher")
parser.add_argument("--generator", choices=["ninja", "xcode", "visualstudio"], default="ninja", help="CMake generator")
parser.add_argument("--configure-only", action="store_true", help="Only run CMake configuration")
args = parser.parse_args()

KNOWN_FORMATS = {"VST3", "AU", "LV2", "CLAP", "Standalone"}
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
errors, warnings = [], []

def clr(text, color_code):
    if sys.stdout.isatty() or os.getenv("FORCE_COLOR"):
        return f"\033[{color_code}m{text}\033[0m"
    return text

def error(msg: str): errors.append(f"  {clr('ERROR:', 91)} {msg}")
def warn(msg: str): warnings.append(f"  {clr('WARNING:', 93)} {msg}")

def validate_config(path: str) -> list:
    if not os.path.isfile(path):
        print(f"FATAL: config.json not found at '{os.path.abspath(path)}'"); sys.exit(1)
    try:
        with open(path) as f: data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"FATAL: config.json is not valid JSON – {e}"); sys.exit(1)
    if not isinstance(data, list):
        print("FATAL: config.json must contain a JSON array of plugin objects."); sys.exit(1)
    if len(data) == 0: warn("config.json contains no plugins – nothing to build.")
    return data

def validate_plugin(plugin: dict, index: int):
    prefix = f"Plugin[{index}]"
    name = plugin.get("name")
    if not name: error(f"{prefix}: missing required field 'name'.")
    elif not isinstance(name, str) or not name.strip(): error(f"{prefix}: 'name' must be a non-empty string.")
    path = plugin.get("path")
    if not path: error(f"{prefix} ({name!r}): missing required field 'path'.")
    else:
        resolved = Path(path).resolve()
        if not resolved.exists(): error(f"{prefix} ({name!r}): plugin path does not exist: '{resolved}'")

    formats = plugin.get("formats", [])
    if not isinstance(formats, list): error(f"{prefix} ({name!r}): 'formats' must be a list.")
    else:
        if len(formats) == 0: warn(f"{prefix} ({name!r}): 'formats' is empty.")
        for fmt in formats:
            if fmt not in KNOWN_FORMATS: warn(f"{prefix} ({name!r}): unknown format '{fmt}'.")
    plugin_type = plugin.get("type", "")
    if plugin_type and plugin_type.lower() not in ("fx", "instrument", ""): warn(f"{prefix} ({name!r}): unexpected 'type' value '{plugin_type}'.")
    version = plugin.get("version", "1.0.0")
    if not VERSION_RE.match(str(version)): warn(f"{prefix} ({name!r}): 'version' value '{version}' invalid.")
    for bool_field in ("enable_gem", "enable_sfizz", "enable_ffmpeg"):
        val = plugin.get(bool_field)
        if val is not None and not isinstance(val, bool): warn(f"{prefix} ({name!r}): '{bool_field}' should be a boolean.")

plugins_config = validate_config("config.json")
for i, plugin in enumerate(plugins_config):
    if not isinstance(plugin, dict): error(f"Plugin[{i}]: expected an object."); continue
    validate_plugin(plugin, i)
if warnings:
    print("Build warnings:"); [print(w) for w in warnings]; print()
if errors:
    print("Build errors – cannot continue:"); [print(e) for e in errors]; sys.exit(1)

system = platform.system()
cmake_compiler = ["-DCMAKE_C_COMPILER=cl", "-DCMAKE_CXX_COMPILER=cl"] if system == "Windows" else []
if args.generator == "xcode": cmake_generator = ["-GXcode"]
elif args.generator == "visualstudio": cmake_generator = ["-GVisual Studio 17 2022", "-A x64"]; cmake_compiler = []
else: cmake_generator = ["-GNinja"]

plugdata_dir = Path("plugdata").resolve()
builds_parent_dir = plugdata_dir.parent
plugins_dir = os.path.join("plugdata", "Plugins")
build_output_dir = os.path.join("Build")
os.makedirs(build_output_dir, exist_ok=True)

if not plugdata_dir.is_dir():
    print(f"FATAL: plugdata directory not found. Initialise submodule first."); sys.exit(1)

stats = {"success": 0, "failed": 0}
for plugin in plugins_config:
    name, zip_path, patch, formats = plugin["name"], Path(plugin["path"]).resolve(), plugin["patch"], plugin.get("formats", [])
    is_fx, build_dir = plugin.get("type", "").lower() == "fx", builds_parent_dir / f"{args.generator}-{name}"
    print(f"\n{clr('Processing:', 34)} {name}")
    author, version = plugin.get("author", False), plugin.get("version", "1.0.0")
    enable_gem, enable_sfizz, enable_ffmpeg = plugin.get("enable_gem", False), plugin.get("enable_sfizz", False), plugin.get("enable_ffmpeg", False)
    cmake_configure = ["cmake", "-GNinja", *cmake_generator, *cmake_compiler, f"-B{build_dir}", f"-DCUSTOM_PLUGIN_NAME={name}", f"-DCUSTOM_PLUGIN_PATCH={patch}", f"-DCUSTOM_PLUGIN_PATH={zip_path}", f"-DCUSTOM_PLUGIN_COMPANY={author}", f"-DCUSTOM_PLUGIN_VERSION={version}", "-DCMAKE_BUILD_TYPE=Release", f"-DENABLE_GEM={'1' if enable_gem else '0'}", f"-DENABLE_SFIZZ={'1' if enable_sfizz else '0'}", f"-DENABLE_FFMPEG={'1' if enable_ffmpeg else '0'}", f"-DCUSTOM_PLUGIN_IS_FX={'1' if is_fx else '0'}"]
    if args.compiler_launcher: cmake_configure.extend([f"-DCMAKE_C_COMPILER_LAUNCHER={args.compiler_launcher}", f"-DCMAKE_CXX_COMPILER_LAUNCHER={args.compiler_launcher}"])
    if subprocess.run(cmake_configure, cwd=plugdata_dir).returncode != 0:
        print(clr(f"Failed cmake configure for {name}", 91)); stats["failed"] += 1; continue
    if args.configure_only: stats["success"] += 1; continue
    plugin_failed = False
    for fmt in formats:
        if system != "Darwin" and fmt == "AU": continue
        target = f"plugdata_{'fx_' if is_fx else ''}{fmt}"
        if fmt == "Standalone": target = "plugdata_standalone"
        print(f"Building target: {target}")
        if subprocess.run(["cmake", "--build", str(build_dir), "--target", target, "--config", "Release"], cwd=plugdata_dir).returncode != 0:
            print(clr(f"Failed to build target: {target}", 91)); plugin_failed = True
        else:
            print(clr(f"Successfully built: {target}", 92))
            format_path, target_dir = os.path.join(plugins_dir, fmt), os.path.join(build_output_dir, fmt)
            if fmt == "Standalone":
                if os.path.isdir(format_path):
                    if os.path.exists(target_dir): shutil.rmtree(target_dir)
                    shutil.copytree(format_path, target_dir)
            else:
                ext = {"VST3": ".vst3", "AU": ".component", "LV2": ".lv2", "CLAP": ".clap"}.get(fmt, "")
                plugin_filename = name + ext; os.makedirs(target_dir, exist_ok=True)
                src, dst = os.path.join(format_path, plugin_filename), os.path.join(target_dir, plugin_filename)
                if os.path.isdir(src):
                    if os.path.exists(dst): shutil.rmtree(dst)
                    shutil.copytree(src, dst)
                else:
                    if os.path.exists(dst): os.remove(dst)
                    shutil.copy2(src, dst)
    if plugin_failed: stats["failed"] += 1
    else: stats["success"] += 1

print(f"\n{clr('Build Summary:', 34)}")
print(f"  {clr('Successful:', 92)} {stats['success']}")
print(f"  {clr('Failed:', 91)}     {stats['failed']}")
if stats["failed"] > 0: sys.exit(1)
