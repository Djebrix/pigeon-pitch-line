#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun entry.

Writes exactly one line (1-200 characters): the elevator pitch a city
pigeon gives investors for its startup.

The line is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. The program only resolves the
output directory (ENTRY_OUTPUT_DIR, else /output), creates it, and writes
the line followed by a trailing newline.
"""

import os

LINE = (
    "We're Coo — 40,000 pigeons already running your city's last-mile "
    "delivery: zero wages, paid in crumbs, and every statue downtown is "
    "a billboard we own. Invest before the seagulls unionize."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
