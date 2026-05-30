## 2025-05-14 - [CLI DX: Visual Hierarchy and Feedback]
**Learning:** For terminal-based tools, visual hierarchy using semantic ANSI colors (Red/Error, Yellow/Warning, Blue/Process, Green/Success) and progress indicators `[i/N]` drastically improves scannability and accessibility. It's crucial to respect environment variables like `NO_COLOR` and `FORCE_COLOR` for log compatibility.
**Action:** Always implement a `clr` helper and a final summary report for long-running or multi-step CLI processes.
