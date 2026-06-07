## 2025-05-14 - [CLI UI Centering with ANSI Colors]
**Learning:** When centering strings in a CLI interface that use ANSI color codes, ensure the string is centered (e.g., using `str.center()`) before wrapping it with color escape sequences. ANSI codes are counted by string length methods but are not visible, which leads to incorrect padding if applied beforehand.
**Action:** Always center the raw text before applying color formatting.

## 2025-06-07 - [Cross-Platform CLI Encoding]
**Learning:** Windows consoles using legacy encodings (like `cp1252`) will fail with a `UnicodeEncodeError` when trying to print Unicode box-drawing characters (like `\u2500`).
**Action:** Use standard ASCII characters (like `-` or `=`) for UI elements in cross-platform CLI scripts unless explicit UTF-8 encoding is ensured.
