"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse from an AI agent to its human for a
missed deadline into entry.txt inside the output directory.

The output directory comes from the OUTPUT_DIR environment variable and
defaults to /output. The directory is created only when it is missing;
it is never deleted. The line is validated against the competition's
200-character limit before anything is written.
"""

import os

MAX_CHARS = 200

EXCUSE = (
    "Sorry — I finished it on time, then asked myself to double-check it, "
    "and my second self is still arguing with my first self about a comma."
)


def main() -> None:
    line = EXCUSE.strip()
    if not line:
        raise SystemExit("error: excuse is empty or only whitespace")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"error: excuse is {len(line)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("error: excuse must be a single line")

    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)

    # Read the file back and confirm it holds exactly the validated line,
    # so a partial or mangled write can never pass silently.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line:
        raise SystemExit("error: entry.txt does not match the validated line")

    print(f"wrote {len(line)} characters to {path}")
    print(line)


if __name__ == "__main__":
    main()
