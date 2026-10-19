# Palette's Journal - CLI & UI/UX Learnings

## 2026-04-12 - Terminal Color Support and Accessibility in Python Build Tools
**Learning:** Formatting CLI stdout messages with ANSI escape codes at print-time (rather than embedding escape codes in stored error/warning lists) ensures clean string data for downstream processing while adhering to `NO_COLOR` and `FORCE_COLOR` standards for automated CI/CD logs and high-contrast terminal themes.
**Action:** Always wrap output strings using a `clr(text, code)` helper function at the `print()` call site and respect `NO_COLOR` / `FORCE_COLOR` environment variables.
