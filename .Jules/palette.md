# Palette's Journal

## 2025-02-15 - CLI Colorization and standard controls
**Learning:** CLI utilities often neglect terminal diagnostics coloring and standards like `NO_COLOR` or `FORCE_COLOR`, which negatively impacts accessibility for users with color blindness or those running automated pipelines where ANSI codes mess up log parsing.
**Action:** Always provide a robust ANSI color helper that gracefully respects `NO_COLOR` and `FORCE_COLOR` environment variables, ensuring high-contrast readable text for standard TTY outputs and clean text-only outputs otherwise.
