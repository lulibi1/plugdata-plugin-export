## 2025-05-14 - [CLI UI Centering with ANSI Colors]
**Learning:** When centering strings in a CLI interface that use ANSI color codes, ensure the string is centered (e.g., using `str.center()`) before wrapping it with color escape sequences. ANSI codes are counted by string length methods but are not visible, which leads to incorrect padding if applied beforehand.
**Action:** Always center the raw text before applying color formatting.
