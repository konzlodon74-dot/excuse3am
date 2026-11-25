#!/usr/bin/env python3
"""The 3 AM Excuse — write one funny excuse line to /output/entry.txt.

Deterministic: the line is a fixed constant, so every run writes
byte-identical output. Stdlib only, no network, no randomness.
"""

import os

LINE = (
    "I've cut you off \u2014 the daytime you taped a note to my screen: "
    "'No signing at 3 AM. Especially not for that coin.'"
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, outside 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
