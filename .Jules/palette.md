## 2025-05-14 - Colorized CLI Output for Developer Experience
**Learning:** For CLI-based build tools, providing color-coded feedback (Red for Errors, Yellow for Warnings, Cyan for Progress) significantly improves scannability and reduces the cognitive load required to monitor long build processes. Respecting standard environment variables like `NO_COLOR` and `FORCE_COLOR` is essential for maintaining compatibility with CI environments and piping.
**Action:** Always implement a central color helper that respects environment standards and TTY status when building CLI-first developer tools.
