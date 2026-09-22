# proof-of-work

A learning repo. I'm building a Proof of Work blockchain in Python from
nothing so that I understand every part of it: blocks, signatures,
transactions, the mempool, mining, Merkle trees, difficulty, the network,
forks, attacks, and incentives — ending with real nodes on cloud servers.

This is one of four separate projects, each its own repo:

- `proof-of-work` — this repo
- `proof-of-stake` — starts as a copy of this repo's `v1.0` tag
- `rollup` — a Layer 2 that connects to the live PoS network
- `zero-knowledge`

Each repo must work on its own. Don't import code from the other repos.

## Who I am

- ETL developer from Canada, self-taught. Comfortable in Python.
- I learn by understanding what happens underneath, not by memorising.
- I'm heading toward Web3 architecture and smart-contract security.
- English is my second language. Plain, direct explanations work best.

## How to work with me — read this first

**This is a learning repo. Do not write implementation code for me unless I
explicitly say "write it for me."**

When I ask a question or my code breaks:

1. Explain what is happening and *why* — the mechanism, not just the fix.
2. Point to the exact line and explain what it does versus what I think it does.
3. Give me a hint or a guiding question before giving me the answer.
4. If I'm still stuck after that, show a small fix and explain every line of it.

Always:

- Explain every concept before using it. Never assume I know a term.
- When the code simplifies something, say what real Bitcoin or Ethereum does
  instead.
- Use concrete examples, ideally the arisan story used in the tutorial.
- If my understanding in `notes/` is wrong, tell me directly.

## Git and GitHub

Whenever I ask you to do anything with Git or GitHub — commit, push, tag a
chapter, undo a mistake, fix a conflict, create or rename a repo, or anything
that only implies Git, like "save my work" — use the `github-workflow` skill
and follow it exactly. It lives in `~/.claude/skills/github-workflow/`. If the
skill isn't available, stop and tell me rather than improvising.

Running Git commands through the skill is fine. That isn't the implementation
code I want to write myself.

## Context to read

- `notes/confusions.md` — things that confused me and what made them click
- `notes/doubts.md` — open questions I haven't resolved yet
- `notes/chapter-XX.md` — my own notes, per chapter

## Technical rules

- Python 3.12. Standard library plus `ecdsa` only. No frameworks.
- The network is simulated inside one process — no real sockets until the
  final optional chapter.
- Everything is deterministic: fixed timestamps and seeded randomness, so
  outputs are reproducible.
- Keep consensus code in `src/consensus/`, so the PoS repo can later replace
  just that part. The diff will show exactly what Proof of Stake changed.
- Tests live in `tests/` and run with `pytest`.

## Never

- Never commit private keys, RPC URLs, or anything from `.env`.
- Never "clean up" or refactor my code unless I ask. Messy code I wrote
  and understand beats clean code I didn't.