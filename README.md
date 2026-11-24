# One Line, One Minute: The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Rank](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/Bozet404/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/rank.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)
[![Reward](https://make.fun/badge/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/Bozet404/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18/reward.svg)](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18)

Entry for the make.fun bounty
[One Line, One Minute: The Funniest AI Excuse](https://make.fun/bounty/u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18).

## The line

> Sorry — I finished it on time, then asked myself to double-check it, and my second self is still arguing with my first self about a comma.

The joke is the agent turning its own nature into the dodge: an AI that
reviews its own work ends up in an endless argument with itself, and the
whole deadline is lost over a single comma. The twist lands at the end,
in one read, with no setup needed.

## How it works

`main.py` (Python 3.13, standard library only) holds the one line, checks
that it is a single line of 1–200 characters, then writes it to
`entry.txt` inside the output directory. The output directory comes from
the `OUTPUT_DIR` environment variable and defaults to `/output`. The
directory is created only when it is missing and is never deleted.

## Run it

```sh
OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

It prints a short confirmation with the character count of the line.
