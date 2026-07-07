# Palette's Journal - Critical UX/Accessibility Learnings

## 2025-05-14 - Color-coded CLI Feedback
**Learning:** For CLI-based build tools, color-coded status updates (Red for errors, Green for success, Cyan for headers) significantly reduce cognitive load. It allows developers to immediately distinguish between expected progress and critical failures without parsing dense log text.
**Action:** Always implement a robust, standard-respecting (NO_COLOR/FORCE_COLOR) colorization helper when working on terminal-heavy developer tools.
