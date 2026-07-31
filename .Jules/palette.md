# Palette's Journal - Critical UX/accessibility learnings

## 2025-07-31 - Resilient CLI UX with ANSI Colors and Dynamic Tables
**Learning:** For terminal-based build scripts, rendering a colored summary table at the end greatly improves Developer Experience (DX) and reduces cognitive overhead. However, hardcoding ANSI sequences or box-drawing characters can cause issues. To build a robust CLI UX:
1. Always implement standard environment variable compliance (`NO_COLOR` disables, `FORCE_COLOR` overrides, and `sys.stdout.isatty()` acts as the default).
2. Measure column padding based on raw visual lengths (e.g. `len(status)`) rather than length of colorized strings with ANSI escape sequences to prevent misalignment.
3. Fall back to standard ASCII characters on Windows to prevent `UnicodeEncodeError` in non-UTF-8 console environments.
**Action:** Apply this lightweight, cross-platform colorizer and table formatting template in any terminal/CLI build tool to ensure bulletproof visual layout.
