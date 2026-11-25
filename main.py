#!/usr/bin/env python3
"""Entry for make.fun bounty u-carbon-forge-the-router-confesses-f98f6b9e.

Writes the router's one-line confession to entry.txt in MAKEFUN_OUTPUT_DIR.
The router speaks in its own voice: petty, with a grudge, and quietly smug
about the one dramatic exit it can stage.
"""

import os

ENTRY_TEXT = (
    "I dropped the climax at 23:41 because your agent asked me if I was "
    "still alive every 3 seconds, so I faked my own death for some quiet."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only white space, and a single line.
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 characters"
    assert ENTRY_TEXT.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
