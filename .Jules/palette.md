## 2025-05-14 - Semantic Color in CLI DX
**Learning:** For terminal-based tools, using semantic ANSI coloring (Red for errors, Green for success, Blue for processing) significantly reduces cognitive load by allowing users to parse verbose build output at a glance.
**Action:** Always check `sys.stdout.isatty()` and a `FORCE_COLOR` environment variable before emitting ANSI codes to ensure compatibility with both interactive terminals and CI/piped environments.

## 2025-05-14 - Plugin Path Flexibility
**Learning:** In audio plugin development, the "source" path for a plugin might be a single file (.pd) or a bundle directory. Over-restricting validation to `is_file()` can prevent valid multi-file setups from working.
**Action:** When validating paths for multi-platform build systems, ensure that both file and directory structures are supported if the downstream tools (like CMake) can handle them.
