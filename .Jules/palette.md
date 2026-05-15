## 2025-05-15 - [Color-coded terminal output for build script]
**Learning:** Adding terminal color support (ANSI escape codes) to developer tools significantly improves the developer experience (DX) by making logs more scannable. Errors, warnings, and success messages are instantly distinguishable, reducing cognitive load during the build process.
**Action:** Use a helper function like `clr` that detects TTY (using `sys.stdout.isatty()`) and supports `FORCE_COLOR` to safely add color to CLI tools.

## 2025-05-15 - [Arch Linux CI Dependency Fix]
**Learning:** On Arch Linux, the standard `webkit2gtk` package name is no longer sufficient for some build systems; `webkit2gtk-4.1` is the required package for modern webkit support in plugdata-based plugins.
**Action:** When updating CI environments for Arch Linux, ensure specific versioned package names like `webkit2gtk-4.1` are used to avoid "target not found" errors in `pacman`.
