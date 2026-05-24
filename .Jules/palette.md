## 2025-05-15 - CLI UX: Semantic Coloring & Bundle Support
**Learning:** Terminal output for build systems is often verbose and difficult to scan. Using semantic ANSI coloring (Red for Errors, Green for Success, Blue for Processing) significantly improves scannability. Additionally, in domain-specific tools (like audio plugin builds), "paths" may refer to directory bundles (VST3/AU), so strict file-existence checks can be counter-intuitive.
**Action:** Always gate ANSI colors behind TTY/environment checks and ensure path validation aligns with domain-specific bundle formats.
