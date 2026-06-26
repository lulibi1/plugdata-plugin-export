## 2025-05-15 - CLI DX and Validation Alignment
**Learning:** For CLI tools performing batch operations (like multi-plugin builds), a color-coded status summary at the end of the execution provides immediate clarity and reduces cognitive load compared to verbose scrolling logs. Additionally, ensuring validation logic matches documentation (e.g., allowing directories when documented) prevents "false negative" errors that frustrate users.
**Action:** Always include a summary for multi-step CLI processes. Verify that all documented "supported" inputs pass validation checks.

## 2025-05-16 - Cross-Platform Terminal Compatibility
**Learning:** When designing CLI interfaces that will run on Windows, avoid using Unicode box-drawing characters (like \u2550) or non-standard dashes (like \u2013). Many Windows environments still default to legacy encodings (like cp1252) which will cause a `UnicodeEncodeError` when these characters are printed.
**Action:** Stick to standard ASCII (-, =, #, etc.) for CLI decorations and separators to ensure universal compatibility across all operating systems and terminal emulators.
