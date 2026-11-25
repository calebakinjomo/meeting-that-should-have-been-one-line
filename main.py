#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — make.fun bounty entry.

Writes a single sentence to /output/entry.txt.
Gate: UTF-8 text, 1-200 characters, not only whitespace.

The line: every reason for the meeting is already settled before anyone
sits down — the decision was made in the email, the client already said
yes — so the only thing left on the agenda is the meeting's own
existence. It kills the meeting outright (nothing remains to decide),
it is drawn straight from real office life (the decision-by-email
thread, the client sign-off, the agenda), and it lands with a sting:
the room full of people has nothing left to do but wonder why they are
still sitting there. One sentence, one line, no context needed.
"""

import os

ENTRY = (
    "The decision was already made in the email, the client already said "
    "yes, and the only item left on the agenda is why we're all still "
    "sitting here."
)

def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count("\n") == 0, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
