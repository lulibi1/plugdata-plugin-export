# Palette's Journal - UX & Accessibility Learnings

## 2026-06-01 - CLI Visual Hierarchy and Progress Feedback
**Learning:** For terminal-based developer tools, semantic coloring (Red for errors, Cyan for progress) combined with `[i/N]` progress indicators significantly improves the scannability of verbose build logs. It allows developers to quickly identify which step failed and how much work is remaining.
**Action:** Always implement a centralized color helper that respects `NO_COLOR`/`FORCE_COLOR` standards to ensure a consistent and accessible experience across different terminal environments.
