## 2025-05-14 - [Colorized CLI Output]
**Learning:** Adding colorized status indicators (Error, Warning, Success) to CLI tools significantly improves scannability and reduces cognitive load during development and CI monitoring.
**Action:** Always include a helper function for ANSI colors in CLI tools that detects TTY and respects standard environment variables like NO_COLOR and FORCE_COLOR.
