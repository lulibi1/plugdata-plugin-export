## 2026-04-11 - CLI Output Alignment with ANSI Escape Characters
**Learning:** Standard string alignment functions like `.ljust()` in Python or `padEnd()` in JavaScript fail when strings contain ANSI color codes because these non-printable characters are counted toward the string's length, causing broken column boundaries in printed terminal tables.
**Action:** Always format plain text length-calculations first before applying ANSI styles, or manually compute the padding width based on unstyled text length and append unstyled spaces after colorizing the status string.
