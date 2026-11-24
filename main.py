#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

The entry is a single fixed line: the sender is so thoroughly
disconnected that they forgot they even set the auto-reply, and the
reply itself is as surprised as the reader. Deterministic by design:
no input, no randomness, no time, no network -- every run writes the
same bytes.
"""

import os

ENTRY = (
    "Gone until the 14th. I've stopped checking email so completely "
    "that I forgot I set this reply. This message is a surprise to me too."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
