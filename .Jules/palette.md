## 2025-05-14 - Semantic CLI Coloring
**Learning:** For CLI-based tools, semantic ANSI coloring (Red: Error, Yellow: Warning, Blue: Processing, Green: Success) significantly improves the scannability of verbose output and provides immediate visual feedback on the outcome of long-running processes.
**Action:** Implement a robust color helper (respecting TTY status and `FORCE_COLOR` environment variable) when enhancing CLI scripts to improve Developer Experience (DX).
