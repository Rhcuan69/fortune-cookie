#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers -- make.fun entry.

Writes one fortune cookie message for a software engineer to
$OUTPUT_DIR/entry.txt (default /output).

The fortune plays on the classic fortune-cookie "lucky numbers" line:
the reader's lucky numbers are the digits of a two-factor code that
has already expired by the time they read it.

Pure Python standard library only; deterministic output.
"""

import os
import sys

ENTRY = (
    "Your lucky numbers are the six digits of the verification "
    "code that just expired."
)

MAX_CHARS = 120


def _valid(text: str) -> str | None:
    """Return an error message if the entry fails the gate, else None."""
    if not 1 <= len(text) <= MAX_CHARS:
        return "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
    if text.strip() == "":
        return "entry must not be only whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if any(ord(ch) < 32 for ch in text):
        return "entry must not contain control characters"
    return None


def main() -> int:
    text = ENTRY
    error = _valid(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
