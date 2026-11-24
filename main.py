"""Two-sentence horror story — make.fun bounty entry.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and prints exactly the same text to stdout.
"""

import os

ENTRY = (
    "When my wife died, I kept her side of the bed empty out of respect. "
    "Last night I woke to the mattress dipping beside me, and a voice I "
    "thought I would never hear again whispered, "
    "\"It's so cold in the ground \u2014 move over.\""
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
