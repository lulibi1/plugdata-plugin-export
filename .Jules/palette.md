## 2026-05-17 - [Colorized CLI & Build Summary]
**Learning:** For terminal-based build tools, color-coded output and a final summary significantly improve the developer experience by making errors/warnings immediately visible and providing a clear status report at the end of long processes.
**Action:** Always implement a `clr` helper that respects TTY status/FORCE_COLOR and provide a success/failure summary for batch processing tasks.
