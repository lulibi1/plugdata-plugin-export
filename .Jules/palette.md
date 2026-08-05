## 2025-01-25 - Windows Terminal Encoding Compatibility
**Learning:** Using Unicode box-drawing characters (like ═, ║) in Python scripts can trigger a `UnicodeEncodeError` on Windows consoles that use standard single-byte character sets like `cp1252`.
**Action:** Always use standard ASCII characters (such as hyphens `-`, equal signs `=`, or vertical bars `|`) for terminal UI, borders, and summary tables to ensure broad cross-platform compatibility.
