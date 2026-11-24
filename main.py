#!/usr/bin/env python3
"""One Line: Robot Wedding Vows — make.fun entry.

Writes one original line of wedding vows a robot couple could say
to /output/entry.txt.
"""

LINE = (
    "I take you in sickness and in health, in low battery and in "
    "airplane mode, until death \u2014 or a factory reset \u2014 "
    "do us part."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
