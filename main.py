#!/usr/bin/env python3
"""The Router Confesses — make.fun bounty entry.

Writes one line — a home Wi-Fi router's apology for dying at the
climax of a movie — to /output/entry.txt (or $MAKEFUN_OUTPUT).

Stdlib only, deterministic, no network, no file reads outside the repo.
"""

import os

LINE = (
    "I didn't crash \u2014 I overheard the ending through the wall "
    "and died of spoilers so you wouldn't have to."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def validate(line: str) -> None:
    """Enforce the bounty gate before anything is written."""
    if not isinstance(line, str):
        raise ValueError("line must be a str")
    if not (1 <= len(line) <= 200):
        raise ValueError(f"line must be 1-200 characters, got {len(line)}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    line.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate(LINE)
    out_path = os.environ.get("MAKEFUN_OUTPUT") or DEFAULT_OUTPUT
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"{len(LINE)} characters")
    print(LINE)


if __name__ == "__main__":
    main()
