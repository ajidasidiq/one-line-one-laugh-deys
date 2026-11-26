#!/usr/bin/env python3
"""One Line, One Laugh - writes a single original one-liner to /output/entry.txt.

The joke: a smart fridge that judges you out loud, and the midnight-snack
eater reduced to a raccoon with a mortgage. One setup, one twist, no setup
paragraph, no meme, no explanation. Deterministic: same line every run,
no input, no network, no randomness.
"""

import os

LINE = "My smart fridge judges my midnight snacks out loud now, so I eat standing in the dark like a raccoon with a mortgage."


def main() -> None:
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single non-empty line")
    if len(line) > 140:
        raise ValueError(f"entry is {len(line)} characters, over the 140 cap")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open("/output/entry.txt", "rb") as handle:
        raw = handle.read()
    if raw.decode("utf-8") != line:
        raise ValueError("entry.txt does not match the validated line")
    if not 1 <= len(raw.decode("utf-8")) <= 140:
        raise ValueError("entry.txt fails the 1-140 character gate")


if __name__ == "__main__":
    main()
