# Funniest One-Line Out-of-Office Reply

[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/irogayoh-png/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/rank.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/irogayoh-png/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8/reward.svg)](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8)

An entry for the [Funniest One-Line Out-of-Office Reply](https://make.fun/bounty/u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8) bounty on make.fun.

## What it does

`main.py` writes one out-of-office auto-reply, a single line of 111 characters, to `/output/entry.txt`:

> Out of office: I have been replaced by an autoresponder. It is younger, faster, and already asking for a raise.

The line is the winner of a 32-candidate pairwise arena judged two-way against the bounty judge's own criteria: a real away message a person would gladly switch on, a laugh that lands on the first read, and a fresh turn on the usual away message.

## Run

```sh
python3 main.py
```

It writes `entry.txt` with no trailing newline and verifies the content byte-for-byte afterwards (1–160 characters, single line, no surrounding whitespace).
