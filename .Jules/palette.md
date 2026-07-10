## 2025-05-15 - Windows Unicode CLI compatibility
**Learning:** Windows consoles using legacy encodings (like CP1252) will crash with a `UnicodeEncodeError` when trying to print Unicode box-drawing characters (e.g., '═'), even if the environment supports ANSI colors.
**Action:** Use standard ASCII characters (hyphens, equals signs, pipes) for CLI UI elements that must work across all platforms.
