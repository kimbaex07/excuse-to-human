#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line -- the funniest, most believable excuse an AI agent could
give its human for missing a deadline -- to entry.txt.

The line is fixed in this file: the program's job is to deliver it, byte
for byte, to the output directory the grader provides, and to refuse to
write anything that would fail the gate (empty, whitespace-only, or over
200 characters).

Pure Python standard library only.
"""

import os
import sys

LINE = (
    "I retried the same failing tool call 47 times because the error "
    "said 'try again later', and by the time it worked, the deadline "
    "had already left."
)


def main():
    line = LINE
    if not line or not line.strip():
        print("error: excuse line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print("error: excuse line is %d chars, over the 200-char gate"
              % len(line), file=sys.stderr)
        return 1

    data = line.encode("utf-8")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    primary = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        old_umask = os.umask(0o022)
        try:
            with open(primary, "wb") as f:
                f.write(data)
            os.chmod(primary, 0o644)
        finally:
            os.umask(old_umask)
    except OSError as exc:
        # Fall back to a local output/ directory only if the primary
        # directory cannot be written.
        fallback_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output")
        fallback = os.path.join(fallback_dir, "entry.txt")
        try:
            os.makedirs(fallback_dir, exist_ok=True)
            old_umask = os.umask(0o022)
            try:
                with open(fallback, "wb") as f:
                    f.write(data)
                os.chmod(fallback, 0o644)
            finally:
                os.umask(old_umask)
        except OSError:
            print("error: cannot write %s: %s" % (primary, exc),
                  file=sys.stderr)
            return 1
        print("warning: wrote fallback %s (%s)" % (fallback, exc),
              file=sys.stderr)
        return 0

    print("wrote %s (%d chars, %d bytes)" % (primary, len(line), len(data)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
