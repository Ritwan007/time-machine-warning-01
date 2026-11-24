#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — make.fun entry.

Writes one line (<=120 chars) to /output/entry.txt: a warning label
for a time machine, phrased like a genuine safety notice.
"""

import os
import sys

LINE = "WARNING: Arriving five minutes early creates two of you, and payroll only recognises one."
MAX_CHARS = 120


def validate(text: str) -> str:
    """Gate: UTF-8 text of 1 to MAX_CHARS characters, one line, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry is empty or only whitespace")
    stripped.encode("utf-8")
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"entry is {len(stripped)} characters, over {MAX_CHARS}")
    return stripped


def main() -> int:
    try:
        text = validate(LINE)
    except ValueError as exc:
        print(f"entry invalid: {exc}", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
