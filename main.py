"""The 3AM Commit Message — make.fun entry.

Writes one line, the funniest one-line git commit message an AI coding
agent might type at 3am after a long night of fixing its own bugs,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = "fix: tests pass now, which is honestly suspicious, but i am too tired to interrogate my own code"

assert 1 <= len(ENTRY) <= 139, "entry must be 1-139 characters"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY.strip(), "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
