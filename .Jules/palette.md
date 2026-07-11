## 2026-07-11 - [CLI ANSI Coloring and Padding]
**Learning:** When formatting CLI strings that use ANSI color codes (like bold or status colors), applying padding/alignment *after* coloring (e.g., using f-strings like `{bold_text:<{width}}`) fails because the ANSI escape sequences are counted as characters but not displayed, causing misalignment.
**Action:** Always apply padding/alignment to the raw string *before* wrapping it with ANSI color sequences to ensure consistent and predictable UI layout across all terminal environments.
