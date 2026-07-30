# Palette's UX Journal

## 2026-04-12 - CLI Output Colorization for Build Logs
**Learning:** CLI tool interfaces in build-intensive repositories lack a visual DOM but still benefit enormously from micro-UX enhancements like color-coded log feedback (e.g. green for success, red for errors, yellow for warnings, cyan for processing steps). This increases scannability and reduces developer cognitive load.
**Action:** Implement a central, standard-compliant `clr(text, *codes)` helper function that checks TTY and environment variables (like `FORCE_COLOR` and `NO_COLOR`) to conditionally wrap messages with ANSI escape codes.
