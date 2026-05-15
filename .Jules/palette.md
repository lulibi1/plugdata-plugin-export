## 2025-05-15 - [Color-coded terminal output for build script]
**Learning:** Adding terminal color support (ANSI escape codes) to developer tools significantly improves the developer experience (DX) by making logs more scannable. Errors, warnings, and success messages are instantly distinguishable, reducing cognitive load during the build process.
**Action:** Use a helper function like `clr` that detects TTY (using `sys.stdout.isatty()`) and supports `FORCE_COLOR` to safely add color to CLI tools.
