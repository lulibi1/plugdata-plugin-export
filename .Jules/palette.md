## 2025-05-14 - Over-restrictive path validation in build system
**Learning:** The build script's validation logic was more restrictive than the documented requirements, causing valid configurations (like using a directory for the plugin path) to fail. This creates a frustrating DX where the user follows the README but the tool errors out.
**Action:** Align validation logic with documentation and improve error visibility using ANSI colors to help users quickly identify and fix configuration issues.
