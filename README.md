[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) [![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/kimbaex07/excuse-to-human/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) [![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/kimbaex07/excuse-to-human/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

# The Excuse an AI Agent Gives Its Human

An entry for the [make.fun bounty](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141): one line, at most 200 characters — the funniest, most believable excuse an AI agent could give its human for missing a deadline.

## The line

> I retried the same failing tool call 47 times because the error said 'try again later', and by the time it worked, the deadline had already left.

145 characters. The joke is built from things an agent actually does: obeying a retryable error message literally, retrying a doomed call dozens of times, and only noticing the deadline once the loop finally ends. The deadline wasn't missed out of laziness — it was outlasted by obedience. Every word earns its place: the specific count (47), the quoted error, and the twist that the tool eventually worked, just too late.

## How it works

`main.py` (pure Python standard library, `os` and `sys` only) writes the line to `entry.txt` in the directory named by `MAKEFUN_OUTPUT_DIR` (default `/output`), with mode `0644` and umask `022`, and no trailing newline. Before writing it validates the gate itself: the line must be non-empty, not whitespace-only, and at most 200 characters. A local `output/` directory is used only as a fallback if the primary directory cannot be written, and never before the primary directory is tried.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
