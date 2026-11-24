#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes the entry line to /output/entry.txt. The gate requires UTF-8
text of 1 to 220 characters, not only white space; the brief requires
exactly one sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance.
"""

import os
import sys

LINE = (
    "The Mosquito Bouncer: a coin-sized bedside drone that finds the one "
    "mosquito you can hear at 3 a.m. but never see, and escorts it out of "
    "the window like a bouncer removing a regular."
)

MAX_CHARS = 220


def check(line: str) -> None:
    """Raise ValueError if the line breaks the gate or the one-sentence brief."""
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    if line.strip() != line or not line.strip():
        raise ValueError("entry must not be blank or padded with white space")
    if any(ord(c) < 32 or ord(c) == 127 for c in line):
        raise ValueError("entry must not contain control characters")
    # One sentence: after removing the "a.m." abbreviation, the only
    # full stop allowed is the final one.
    body = line.replace("a.m.", "am")
    if not body.endswith(".") or body[:-1].count(".") != 0:
        raise ValueError("entry must be exactly one sentence")


def main(argv: list) -> int:
    check(LINE)
    if "--check" in argv:
        print(f"ok: entry is valid ({len(LINE)} chars, one sentence)")
        return 0
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "rb") as f:
        written = f.read()
    if written != LINE.encode("utf-8"):
        raise ValueError("written file does not match the entry byte for byte")
    print(f"wrote {path} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
