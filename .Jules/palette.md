## 2025-05-14 - [CLI Colorization for DX]
**Learning:** Developers often miss critical errors in long build logs when the output is monochrome. Adding ANSI color codes to CLI tools significantly improves scanability and reduces troubleshooting time.
**Action:** Implement a `clr` helper function in build scripts to provide immediate visual feedback for errors (Red), warnings (Yellow), and progress (Blue/Green).
