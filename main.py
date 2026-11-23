#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

The joke is a single fixed string: no randomness, no input, no network.
The grader runs this program twice; both runs must write the exact same
valid UTF-8 text of 1-280 Unicode code points to /output/entry.txt.
After writing, the file is read back and checked byte-for-byte against
the joke, so a partial or corrupted write fails loudly instead of
passing silently.
"""
import os

JOKE = (
    "My AI coding agent nailed the live demo \u2014 then I asked it to do "
    "the exact same thing again, and it confidently invented a brand-new bug."
)


def validate(joke: str) -> None:
    if not 1 <= len(joke) <= 280:
        raise ValueError("joke must be 1-280 characters")
    if not joke.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in joke):
        raise ValueError("joke must not contain control characters")
    joke.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> None:
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Verify the write: read the file back and require an exact match.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != JOKE:
        raise RuntimeError("verification failed: /output/entry.txt differs from joke")


if __name__ == "__main__":
    main()
