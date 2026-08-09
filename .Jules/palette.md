# Palette's Journal

## 2026-04-12 - Support directory-based paths in plugin configuration scripts
**Learning:** In headless build tools and CLI scripts, strict single-format validation (e.g., enforcing only files or only ZIPs) creates friction for developers who want to work with raw directory configurations locally. Accepting both files and directories seamlessly aligns with user intent and complies with the config specification, dramatically improving developer experience (DX).
**Action:** When validating asset or project paths in configuration and build tools, always check if the path exists and matches either directory or file formats before throwing errors.
