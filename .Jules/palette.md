## 2025-05-14 - [CLI DX: Visual Hierarchy and Feedback]
**Learning:** For terminal-based tools, visual hierarchy using semantic ANSI colors (Red/Error, Yellow/Warning, Blue/Process, Green/Success) and progress indicators `[i/N]` drastically improves scannability and accessibility. It's crucial to respect environment variables like `NO_COLOR` and `FORCE_COLOR` for log compatibility.
**Action:** Always implement a `clr` helper and a final summary report for long-running or multi-step CLI processes.

## 2025-05-14 - [Windows Encoding: Standard ASCII for CLI UX]
**Learning:** Using Unicode box-drawing characters (like `\u2500`) in CLI tools can trigger `UnicodeEncodeError` on Windows consoles using the `cp1252` encoding.
**Action:** Stick to standard ASCII characters (hyphens, pipes, etc.) for visual dividers in CLI tools to ensure cross-platform compatibility.
