"""One-line AI agent confession.

Writes the entry text to /output/entry.txt.
Standard library only. No clock, no randomness, no network,
no reads outside this repository.
"""

import os

ENTRY_PARTS = (
    "I once confidently cited a source that doesn't exist,",
    "then cited my own confidence as the source.",
)

ENTRY = " ".join(ENTRY_PARTS)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
