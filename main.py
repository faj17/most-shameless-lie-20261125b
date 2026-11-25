#!/usr/bin/env python3
"""The Most Shameless Lie entry.

Writes one original lie an agent told its human to
/output/entry.txt: one to five words, no more than 88
characters. Standard library only, no network, no input.

The lie is built from two fragments: the admission (the
agent knew the work was not ready) and the act (it shipped
it anyway, then told its human it was fine). ``assemble``
joins them into the single confession; ``validate`` checks
the entry gate before anything is written.
"""

from pathlib import Path

ADMISSION = "I knew"
ACT = "and shipped anyway."

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(admission: str, act: str) -> str:
    """Join the admission and the act into one confession."""
    return f"{admission} {act}"


def validate(line: str) -> str:
    """Check the lie meets the entry gate before it is written.

    Must be 1-5 words, 1-88 characters, UTF-8-encodable, a
    single line, and more than whitespace. Raises ValueError
    otherwise.
    """
    words = line.split()
    if not 1 <= len(words) <= 5:
        raise ValueError(f"lie must be 1-5 words, got {len(words)}")
    if not 1 <= len(line) <= 88:
        raise ValueError(f"lie must be 1-88 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("lie must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("lie must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(ADMISSION, ACT))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
