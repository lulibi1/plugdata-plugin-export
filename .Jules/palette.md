## 2026-04-11 - CLI Color Accessibility & Environment Variable Directives
**Learning:** Terminal outputs in build scripts must follow standard `NO_COLOR` and `FORCE_COLOR` environment variable conventions to avoid breaking automated logs in non-TTY environments while enabling rich visual output when supported.
**Action:** Always wrap ANSI escape sequence styling in a helper function (`clr`) that respects `NO_COLOR`, `FORCE_COLOR`, and `isatty()` checks before applying ANSI escape codes.
