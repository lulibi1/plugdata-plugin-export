## 2025-05-14 - Colorized CLI Feedback and Summaries
**Learning:** In CLI-only environments, color-coded status prefixes (ERROR/SUCCESS) and a final summary block significantly improve the scannability of long build logs, especially when multiple targets are processed.
**Action:** Use a 'clr' helper to wrap status messages and provide a visual separator for the final build status summary.
