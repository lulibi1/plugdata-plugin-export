## 2026-05-23 - Semantic CLI Feedback
**Learning:** For CLI tools wrapping verbose build systems (CMake/Ninja), semantic coloring and progress indicators ([i/N]) are critical for micro-DX. They allow users to quickly parse success/failure states and maintain context during long-running tasks.
**Action:** Implement a standard 'clr' helper and progress tracking in all CLI-based build or automation scripts.
## 2025-05-23 - Submodule Auth in CI
**Learning:** Hardcoded usernames in submodule URLs (e.g., Bitbucket) can break automated CI clones. Using git's 'insteadOf' configuration globally before updating submodules is a clean way to resolve this without modifying the upstream .gitmodules file.
**Action:** In GitHub Actions workflows, use 'submodules: false' and a manual update step if upstream submodules have fragile URLs.
