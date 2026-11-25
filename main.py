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

Reviser pass: entry validation now raises ValueError instead of using
``assert`` (asserts vanish under ``python -O``, so a bad entry could
have slipped through silently), and the file is written atomically —
to a temp file in the same directory, then renamed into place — so a
reader never sees a half-written entry. The entry text itself is
unchanged, byte for byte.
"""

import os

ENTRY = (
    "The decision was already made in the email, the client already said "
    "yes, and the only item left on the agenda is why we're all still "
    "sitting here."
)


def validate(text: str) -> str:
    """Return the stripped entry, or raise ValueError if it breaks the gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    text = text.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, must be 1-200")
    if not text:
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.endswith("."):
        raise ValueError("entry must be a single sentence ending with '.'")
    return text


def main() -> None:
    text = validate(ENTRY)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.replace(tmp_path, os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
