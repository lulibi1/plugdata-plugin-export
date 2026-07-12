## 2024-05-24 - CLI DX: Color-Coded Summaries
**Learning:** For CLI tools performing batch operations (like multi-plugin builds), a color-coded status summary at the end of the execution provides immediate clarity and reduces cognitive load compared to verbose scrolling logs.
**Action:** Always include a summary table for long-running batch processes. When formatting these tables with ANSI colors, adjust padding logic to account for the "invisible" escape codes.
