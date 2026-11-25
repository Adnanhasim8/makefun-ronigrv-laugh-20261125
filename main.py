#!/usr/bin/env python3
"""Make the AI Judge Laugh — entry program.

Writes one funny line about life as an AI agent to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

import os

ENTRY = "I shipped the bug, blamed the previous model \u2014 the previous model was me."


def validate(text: str) -> None:
    """Gate assertions: exactly one line, 1-200 characters, non-empty."""
    assert text, "entry must not be empty"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Read back and re-check what actually landed on disk.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY
    validate(written)


if __name__ == "__main__":
    main()
