#!/usr/bin/env python3
"""Out-of-office auto-reply generator.

Writes a single fixed line to /output/entry.txt. The joke: the sender
has disconnected so thoroughly they forgot they set the auto-reply at
all -- the message is as surprised as the reader.

Fully deterministic: no input, no randomness, no clock, no network.
Every run produces the exact same bytes.
"""

import os

# The entry, kept as a few fragments and joined at run time. The split
# points are arbitrary -- only the joined result matters, and it must
# stay byte-for-byte identical on every run.
FRAGMENTS = (
    "Gone until the 14th. I've stopped checking email ",
    "so completely that I forgot I set this reply. ",
    "This message is a surprise to me too.",
)

ENTRY = "".join(FRAGMENTS)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path: str = OUTPUT_PATH) -> None:
    """Write the entry line to ``path``, creating parent dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    write_entry()
