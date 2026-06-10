## 2025-05-14 - Scannable CLI Output for Developer Tools
**Learning:** For command-line build tools, color-coded status messages and a final summary significantly improve scannability. Developers can quickly identify if a build was successful without reading through verbose logs. Cyan for processing, Green for success, and Red for errors are standard, effective choices.
**Action:** Always include a brief success/failure summary at the end of long-running CLI processes and use ANSI colors (respecting NO_COLOR) to highlight state changes.
