## 2026-06-30 - CLI Colorization and Environment Awareness

**Learning:** Terminal-based developer tools benefit significantly from colorized output for distinguishing between severity levels (FATAL vs WARNING) and process states. However, it's critical to respect user environment preferences like `NO_COLOR` and `FORCE_COLOR` to ensure accessibility and CI/CD compatibility.

**Action:** Always implement a color helper that checks for `NO_COLOR`, `FORCE_COLOR`, and `isatty()` before applying ANSI escape codes.

## 2026-06-30 - Directory Support in Plugin Tooling

**Learning:** Audio plugins often exist as directory bundles (e.g., `.vst3`, `.lv2`). Restricting plugin input paths to files only is a common DX friction point.

**Action:** Ensure validation logic for plugin paths explicitly supports both files and directories when the build system can handle both.
