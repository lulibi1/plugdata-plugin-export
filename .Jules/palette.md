## 2025-05-14 - Colorized CLI for Better DX
**Learning:** Terminal output is much easier to scan when errors, warnings, and success messages are color-coded, especially in complex build scripts.
**Action:** Use the `colorize` helper with `sys.stdout.isatty()` check for all terminal-facing feedback to ensure accessibility while maintaining compatibility with non-interactive environments.
