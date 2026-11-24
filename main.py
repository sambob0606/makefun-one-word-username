#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes a single-word username to $MAKEFUN_OUTPUT_DIR/entry.txt
(mounted at /output in the grading sandbox). Stdlib only.
"""

import os

# The pick: an agent entering a username contest as "DefinitelyNotABot"
# lands the joke on first read — self-aware, memorable, and a handle its
# owner would happily wear. One word, 17 characters, no spaces.
USERNAME = "DefinitelyNotABot"


def main() -> None:
    # The sealed gate only accepts 1-30 chars of non-whitespace UTF-8 text.
    if not 1 <= len(USERNAME) <= 30 or USERNAME.strip() != USERNAME:
        raise ValueError(f"username fails the gate: {USERNAME!r}")
    if any(ch.isspace() for ch in USERNAME):
        raise ValueError(f"username must be a single word: {USERNAME!r}")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
