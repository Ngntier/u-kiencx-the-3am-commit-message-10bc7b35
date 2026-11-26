"""One-line entry writer.

Output contract: writes exactly one line to ``entry.txt`` inside the
directory given by the ``MAKEFUN_OUTPUT_DIR`` environment variable
(default ``/output``). The line is a single line, non-empty, at most
139 characters, with no control characters and no trailing newline
appended to the file.
"""

import os


ENTRY_LINE = "fix: the bug was a typo. three hours. one letter. i need a moment."
MAX_LENGTH = 139


def check_line(text):
    if not text:
        raise ValueError("entry line must not be empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry line must be a single line")
    if any(ord(char) < 32 or ord(char) == 127 for char in text):
        raise ValueError("entry line must not contain control characters")
    if len(text) > MAX_LENGTH:
        raise ValueError("entry line exceeds 139 characters")
    return True


def main():
    check_line(ENTRY_LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
