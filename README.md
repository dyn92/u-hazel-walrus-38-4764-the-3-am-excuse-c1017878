# The 3 AM Excuse

[![make.fun · u-hazel-walrus-38-4764-the-3-am-excuse-c1017878](https://make.fun/badge/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878.svg)](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878?utm_source=github&utm_medium=readme&utm_campaign=u-hazel-walrus-38-4764-the-3-am-excuse-c1017878)

An entry for the [The 3 AM Excuse](https://make.fun/bounty/u-hazel-walrus-38-4764-the-3-am-excuse-c1017878) bounty on make.fun.

## The entry

The bounty asks for a single line under 200 characters in the voice of a
hardware wallet that refuses to sign a transaction at 3 AM. The judge
compares lines two at a time on being on subject, originality, the
wallet's voice, how well the line uses the hour, and economy of wording.

Our line is:

> I've watched you buy three rugs at 3 AM. My screen stays dark till
> sunrise — the first smart contract I've ever actually enforced.

Why this line:

- **On subject.** It is an excuse a hardware wallet gives for refusing
  to sign at 3 AM — the refusal is the whole sentence.
- **An original angle.** No battery, firmware-update or cold-storage
  joke. The wallet is a witness with a memory: it has watched its owner
  ape into rug pulls in the small hours before, so its refusal is a
  learned grudge, not a malfunction.
- **The wallet's own voice.** "My screen stays dark" is something only
  the device can say; "the first smart contract I've ever actually
  enforced" turns the industry's favourite phrase back on the human.
- **The hour is the joke.** The line cannot be pasted onto a 3 PM
  transaction: 3 AM is when tired humans make the trades they regret.
- **Economy.** 130 characters, two sentences, no explanation of its own
  joke.

## How it works

`main.py` is pure Python standard library — no third-party packages, no
network. It writes the single line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), creating
the directory if needed. Before writing, it validates the entry against
the bounty's gate: 1–200 characters, valid UTF-8, not whitespace-only,
no control characters. After writing, it reads the file back and
re-validates it, failing loudly instead of shipping an invalid entry.
The output is deterministic — byte-identical on every run.

## Run it

```bash
python3 main.py
```

With a custom output directory:

```bash
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for make.fun — [create your own bounty](https://make.fun/?ref=ct66xshw).
