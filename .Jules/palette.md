## 2025-05-14 - CLI UX Enhancement Pattern
**Learning:** For developer-facing CLI tools (like build scripts), visual hierarchy and progress feedback are as critical as they are in GUIs. Using semantic ANSI colors (Blue for processing, Green for success, Red for failure) helps users parse verbose output quickly.
**Action:** Always include a `clr` helper function and terminal detection in Python scripts. Implement progress counters `[i/N]` in loops and provide a clear summary report at the end.
