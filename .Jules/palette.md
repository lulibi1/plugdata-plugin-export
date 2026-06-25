## 2025-05-15 - CLI UX: Color-coded Summaries and ANSI Centering

**Learning:** For CLI tools performing batch operations, a color-coded status summary provides immediate clarity. When centering such strings, always apply padding (e.g., `str.center()`) *before* wrapping with ANSI escape codes, as these codes are counted by length methods but invisible in the terminal, leading to offset alignment.

**Action:** Use the `clr` helper pattern for consistent CLI feedback and ensure centering logic precedes color wrapping.
