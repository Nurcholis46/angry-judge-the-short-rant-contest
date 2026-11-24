#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — make.fun entry.

Writes one short funny rant to /output/entry.txt. The sealed scorer only
checks that the file is UTF-8 text of 1 to 400 characters, not only
whitespace, so the whole game is the rant itself, judged head to head by a
furious AI judge on: a funny rant about a specific everyday annoyance (not
a general essay), actual funniness, a concrete annoyance, sharp economical
wording, and freshness.

The rant: the self-checkout machine that accuses you of theft over a bag
of apples. The joke builds by repetition — the machine has seen the apples,
the machine has scanned the apples — then flips the power dynamic: you, the
paying customer, need a teenager with a keycard to come over and pardon
you. Specific machine behaviour ("UNEXPECTED ITEM IN THE BAGGING AREA"),
a concrete everyday annoyance, and a punchline that reframes the shopper
as a pardoned criminal. No printer, bus or Monday-morning cliche.
"""

import os
import sys

RANT = (
    "The self-checkout scanned my apples, froze, and screamed "
    "'UNEXPECTED ITEM IN THE BAGGING AREA' like I'd smuggled a live "
    "animal. It is ONE bag of apples. The machine has seen the apples. "
    "The machine has scanned the apples. And now it has decided, on no "
    "evidence at all, that I am a thief \u2014 and a teenager with a "
    "keycard has to come over and pardon me."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    text = RANT.strip()
    if not text or text != text.strip():
        print("entry must be non-blank with no surrounding whitespace", file=sys.stderr)
        return 1
    if len(text) > 400:
        print(f"entry is {len(text)} chars, over the 400 limit", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single paragraph", file=sys.stderr)
        return 1

    out_dir = os.path.dirname(OUTPUT_PATH) or "."
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        # Sandbox always provides /output; fall back to a local ./output
        # only so the program still runs (and can be tested) elsewhere.
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        output_path = os.path.join(out_dir, "entry.txt")
    else:
        output_path = OUTPUT_PATH
    # No trailing newline: the gate counts every character in the file.
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(output_path, 0o644)
    # Self-check: read back exactly what was written and re-validate it.
    with open(output_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("round-trip mismatch: file content differs from entry", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {output_path}")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
