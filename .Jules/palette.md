# Palette's Journal - PlugData Automated Build System

This journal tracks critical UX and accessibility learnings discovered during the development of this project.

## 2024-07-15 - CLI Build Summaries
**Learning:** For CLI tools performing batch operations (like multi-plugin builds), a color-coded status summary at the end of the execution provides immediate clarity and reduces cognitive load compared to verbose scrolling logs.
**Action:** Always implement a summary table for multi-step or multi-target processes.

## 2024-07-15 - Audio Plugin Path Validation
**Learning:** Audio plugin "paths" are often directories (bundles like .vst3, .component, or macOS .app folders), so validation logic must allow for both files and directories to avoid frustrating false-positive errors.
**Action:** Use `.exists()` instead of `.is_file()` when validating paths that might be directory-based bundles.

## 2024-07-15 - Arch Linux Package Naming
**Learning:** On Arch Linux, the required package for webkit support in plugdata plugins is `webkit2gtk-4.1`. The generic `webkit2gtk` package is outdated or unavailable in core repositories.
**Action:** Use `webkit2gtk-4.1` in `pacman` installation commands for projects requiring webkit support.
