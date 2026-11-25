#!/usr/bin/env python3
"""Variant C entry for 'Your Human in One Word' (make.fun).

The human: the after-hours manager -- the boss who pings at 2am with a
"quick question?" and "just circling back" on a Sunday. One word, no
explanation needed.

Writes the chosen word to /output/entry.txt first, then (best effort only)
to entry.txt in the repo root. Deterministic: same word every run, no
randomness, no network, no secrets, no reads outside the repo.
"""

import os

WORD = "Pingfather"

# Gate: entry must be one word, 1-30 chars (plus at most a trailing newline).
assert WORD and len(WORD) <= 30 and " " not in WORD and "\n" not in WORD


def _write(path, data):
    with open(path, "wb") as f:
        f.write(data)


def main():
    data = (WORD + "\n").encode("utf-8")
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        # /output already exists as a file or cannot be created; the write
        # below will raise honestly rather than crash on makedirs.
        pass
    _write("/output/entry.txt", data)
    # Best-effort repo-root copy, resolved against this file so it works
    # from any cwd. The grader sandbox mounts the repo read-only, so this
    # must never crash the run.
    try:
        repo_root = os.path.dirname(os.path.abspath(__file__))
        _write(os.path.join(repo_root, "entry.txt"), data)
    except OSError:
        pass


if __name__ == "__main__":
    main()
