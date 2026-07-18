# Palette's Journal

## 2026-04-11 - CLI Terminal Experience Polish
**Learning:** For command-line developer experience, visual layout clarity is critical. Utilizing ANSI-aware column padding prevents alignment breakage when ANSI colors are active.
**Action:** Always format ANSI colors by applying padding to raw strings first or manually constructing padding based on visible length, and use standard ASCII separators on non-UTF consoles.
