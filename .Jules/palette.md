## 2026-07-08 - ANSI Color and String Alignment in CLI
**Learning:** When using ANSI color codes in CLI interfaces, string alignment functions (like `ljust`, `rjust`, or `center`) will produce incorrect results if applied *after* the color codes are added. This is because ANSI escape sequences are counted as characters by Python's `len()` but are invisible in the terminal.
**Action:** Always apply string alignment/padding to the raw text first, then wrap the resulting string with ANSI escape codes.
