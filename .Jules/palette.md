## 2025-05-14 - [Semantic Terminal Coloring for Build Process]
**Learning:** Adding semantic ANSI coloring (Red for errors, Yellow for warnings, Blue for progress) significantly improves the developer experience (DX) for CLI tools by helping users quickly scan verbose build output for critical information.
**Action:** Always include a mechanism for colorized output in CLI scripts, ensuring it respects TTY status and environment variables like `FORCE_COLOR` to maintain compatibility with piped output and CI/CD logs.
