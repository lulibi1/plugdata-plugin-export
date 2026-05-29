## 2025-05-14 - CLI Semantic Coloring
**Learning:** For terminal-based build systems, using semantic ANSI colors (Red for Error, Yellow for Warning, Blue for Progress) significantly improves the ability of developers to quickly scan verbose logs and identify issues. Supporting the `FORCE_COLOR` environment variable ensures CI systems can also benefit from these visual cues.
**Action:** Always implement a centralized `clr` helper that respects TTY status and standard environment variables like `FORCE_COLOR` or `NO_COLOR`.
