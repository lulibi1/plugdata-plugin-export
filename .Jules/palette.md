## 2025-05-15 - CLI UX Semantic Coloring
**Learning:** For developer-facing CLI tools with verbose output (like build scripts), semantic ANSI coloring significantly reduces cognitive load by highlighting critical status changes and errors.
**Action:** Always implement a `clr` helper with TTY detection and `FORCE_COLOR` support for any CLI tools I modify or create.

## 2025-05-15 - Audio Plugin Bundle Validation
**Learning:** Audio plugin formats like VST3 and AU are often distributed as directory "bundles" rather than single files. Strict file-only validation on plugin paths will break common developer workflows.
**Action:** Use `Path.exists()` instead of `Path.is_file()` for validating paths to plugin source artifacts unless a specific file format is strictly required.
