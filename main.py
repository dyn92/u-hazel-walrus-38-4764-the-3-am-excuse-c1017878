#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

The bounty asks for a single line under 200 characters in the voice of a
hardware wallet that refuses to sign a transaction at 3 AM. The judge
weighs, in order: being on subject; originality; the wallet's own voice;
turning the 3 AM hour itself into the joke; economy of wording.

THE LINE: "I've watched you buy three rugs at 3 AM. My screen stays dark
till sunrise — the first smart contract I've ever actually enforced."

Why this line, reasoned from the brief rather than picked from a list:

  * On subject, first and foremost. It IS an excuse a hardware wallet
    gives for refusing to sign at 3 AM: the refusal is the whole sentence
    ("My screen stays dark till sunrise"). Nothing in it could be mistaken
    for a generic joke about crypto.
  * An original angle. The judge's brief warns against the usual jokes —
    batteries, firmware updates, cold storage. This line takes a different
    road: the wallet as a witness with a memory. It has watched its owner
    ape into rug pulls in the small hours before, so its refusal is not a
    malfunction but a learned grudge. A device keeping score of its owner's
    3 AM mistakes is an angle few entrants will reach for.
  * The wallet's own voice. "My screen stays dark" is something only the
    device can say about itself; "the first smart contract I've ever
    actually enforced" is the wallet talking shop in its own vocabulary,
    turning the industry's favourite phrase back on the human. It is not
    a person in a wallet costume and not a generic assistant.
  * The hour IS the joke. The line cannot be pasted onto a 3 PM
    transaction: 3 AM is when tired humans make the trades they regret,
    and the wallet knows it. The excuse only exists because of the hour.
  * Economy. 130 characters, two sentences, no explanation of its own
    joke. The punchline ("the first smart contract I've ever actually
    enforced") lands and stops.

Rejected alternatives, and why:
  * A battery joke ("my battery died, try again at noon") — the brief
    names batteries as a recycled angle; it would lose on originality.
  * A firmware-update joke — same problem, explicitly warned against.
  * "I don't sign for people who can't spell their own seed phrase
    right now" — funny, but it mocks the human's tiredness rather than
    giving the device a reason of its own, and it says nothing about why
    3 AM in particular is dangerous.

The program is deterministic: it always writes this one line, byte for
byte, so the entry is identical on every run. Pure Python standard
library only; no third-party packages, no network access.
"""

import os
import sys

# The single line. Chosen once, deliberately — this is the entry.
LINE = (
    "I've watched you buy three rugs at 3 AM. "
    "My screen stays dark till sunrise — "
    "the first smart contract I've ever actually enforced."
)

# Gate limits from the bounty rules: /output/entry.txt must be UTF-8
# text of 1 to 200 characters, not only whitespace.
MIN_LENGTH = 1
MAX_LENGTH = 200


def validate(line):
    """Fail loudly unless `line` is a valid entry line."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string, got %r" % type(line).__name__)
    if not line:
        raise ValueError("entry must not be empty")
    if line.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if len(line) < MIN_LENGTH or len(line) > MAX_LENGTH:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("entry must not contain control characters: %r" % line)
    # Must round-trip as UTF-8, exactly as the sealed scorer reads it.
    line.encode("utf-8")
    return line


def main():
    line = validate(LINE)
    # MAKEFUN_OUTPUT_DIR names a directory; the harness default is /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify what was actually written: re-read and re-validate, so a
    # bad write fails loudly instead of silently shipping an invalid entry.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise ValueError(
            "verification failed: wrote %r, read back %r" % (line, written)
        )
    validate(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
