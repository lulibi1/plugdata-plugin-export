## 2026-04-12 - [CLI Alignment with ANSI Colors]
**Learning:** ANSI color codes (escape sequences) do not occupy physical visual width in the terminal. When formatting CLI summary tables, calculating column padding using the raw string's length instead of the colorized string's length is critical to avoid visual misalignment.
**Action:** Separate the styling layer from the data structure. Use unescaped text lengths to calculate alignment/padding width, and wrap with color sequences only at the final print step.
