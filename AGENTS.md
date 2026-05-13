# Agent workflow rules — maths repo

This file is the canonical instruction set for any AI coding agent working in this repo (Claude Code, Cursor, Aider, Codex, Continue, …). `CLAUDE.md` is a symlink to this file so Claude Code picks it up automatically; if your agent looks for a different filename, add another symlink rather than forking the content.

This repo is a personal math study journal.

## The four-step study loop

For every concept, the user works through this loop:

1. **Pick next topic** — read `ROADMAP.md` and the `topics/` tree. Recommend the natural continuation; do not invent a curriculum unilaterally.
2. **Add material** — when the user shares a URL or file, drop a stub in `topics/<topic>/materials/NN-<slug>.md`, run the appropriate fetcher in `scripts/`, and update the topic's `README.md` log.
3. **Challenge understanding** — in conversation, push on weak spots, surface ambiguities, ask "what would change if…" questions. Do not pre-summarize the material; force the user to explain it back.
4. **Author cards** — only at the end of the conversation, only for concepts the user signals as understood. The user dictates the angle; the agent edits for clarity and format. Cards go to `cards/<topic>.txt` in the format specified by the anki-card-builder skill (see "Skills" below).

## Hard rules

- **Cards are closing rituals, not openers.** Never propose cards for material the user hasn't engaged with in conversation.
- **Self-authorship matters.** When co-authoring a card, the user provides the framing first; the agent refines. Reverse this only when explicitly asked.
- **Validate before declaring a deck done.** Run `python .claude/skills/anki-card-builder/scripts/validate_import.py <deck.txt>` and fix issues until it exits 0.
- **Defer to the skill.** For anything format-related — note types, separators, cloze syntax — read `.claude/skills/anki-card-builder/SKILL.md` and the `references/` files. Do not improvise.
- **Keep the repo offline-capable.** When a material is added, ensure it has a committed transcript (audio/video) and a stub. Binaries belong in `.gitignore`.
- **Update `ROADMAP.md`** whenever a topic moves from "candidate" to "in progress" to "covered".
- **Always use English for the materiales.** Despite the conversations usually happening in Spanish, the repository should be maintained in English.

## Material stub format

Every file under `topics/<topic>/materials/NN-<slug>.md` (excluding `*.transcript.md`) is a stub with YAML front-matter so `scripts/fetch-all.py` can find and regenerate the binary:

```markdown
---
source: https://www.youtube.com/watch?v=MaszunEszVM
kind: video
license: standard-youtube-license
---

# Functions, injectivity, surjectivity

Why this material: clean intro to function vocabulary, the entry point of the calculus track.
```

Recognized `source:` schemes today: `https://www.youtube.com/...` and `https://youtu.be/...`. Extend `scripts/fetch-all.py` when adding new schemes.

## When the user says "let's continue"

1. Read `ROADMAP.md` and the most recently modified `topics/` folder.
2. Propose 2–3 candidate next steps with a one-line justification each.
3. Wait for the user to choose; do not start downloading or writing without confirmation.

## Skills

This repo carries one skill, `anki-card-builder`, that governs all card creation. It lives at `.claude/skills/anki-card-builder/` (the path is Claude-Code-shaped but the content is agent-agnostic).

Card creation follows `.claude/skills/anki-card-builder/SKILL.md`. Agents that auto-discover Claude skills (Claude Code) will load it automatically. Agents that don't (Cursor, Aider, Codex, …) **must read that file directly before authoring or validating cards**, plus the supporting docs in `.claude/skills/anki-card-builder/references/`. Do not improvise card format — the skill encodes hard rules about note types, separators, and cloze syntax.

If a future agent needs the skill in a different location (e.g. `.cursor/rules/`), add a symlink rather than copying so the source of truth stays single.
