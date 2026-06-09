## 2025-05-15 - [CLI Micro-UX: Colorized Progress & Summaries]
**Learning:** Developers often rely on raw terminal output for feedback. Adding a lightweight, standard-compliant color helper (respecting `NO_COLOR`) and a clear `[n/m]` progress indicator significantly reduces cognitive load and makes failures immediately obvious.
**Action:** Always include a final build summary and non-zero exit codes on failure for any CLI-based automation tools to ensure they are both human-friendly and CI-ready.
