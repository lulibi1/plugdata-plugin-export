## 2025-05-14 - [CLI DX: Color-Coded Feedback & Proactive Validation]
**Learning:** Terminal users benefit significantly from immediate, color-coded feedback for errors and warnings. Proactive validation (e.g., checking for file existence and uniqueness before starting a long build) prevents "late-stage" failures that are frustrating to debug.
**Action:** Always implement ANSI color coding for CLI tools (with TTY checks) and validate all external inputs/paths early in the execution flow.
