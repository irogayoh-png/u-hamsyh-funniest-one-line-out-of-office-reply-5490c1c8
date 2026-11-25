#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply.

Writes the arena champion line to entry.txt: a real away message a person
would gladly switch on, with a fresh turn on the usual away message. The
replacement autoresponder is younger, faster, and already asking for a raise.
"""

import os

LINE = "Out of office: I have been replaced by an autoresponder. It is younger, faster, and already asking for a raise."

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt content mismatch"
    assert 1 <= len(written) <= 160, "gate: entry must be 1-160 characters"
    assert written == written.strip(), "gate: no leading/trailing whitespace"
    assert "\n" not in written, "gate: entry must be a single line"

if __name__ == "__main__":
    main()
