## 2025-02-15 - ANSI Terminal Colorization Standards in CLI Tools
**Learning:** CLI tools formatting errors and progress output with ANSI escape sequences must respect `NO_COLOR`, `FORCE_COLOR`, and `isatty()` checks while leaving raw error string data structures unpolluted for downstream processing.
**Action:** Always wrap stdout print statements with a `clr(text, code)` helper function rather than injecting ANSI escape sequences into error message arrays directly.
