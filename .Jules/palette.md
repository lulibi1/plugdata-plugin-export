## 2026-04-11 - CLI Terminal Table Alignment and Color Compatibility
**Learning:** ANSI escape codes do not occupy visual space in terminal displays, so padding calculations must use the uncolorized string lengths to avoid visual table misalignment. Additionally, Unicode box-drawing characters cause severe UnicodeEncodeErrors on Windows consoles using CP1252/default encoding.
**Action:** Always compute string padding on raw text before applying color wrappers, and use pure ASCII characters like hyphens (`-`) and pipes (`|`) for borders to ensure universal cross-platform rendering.
