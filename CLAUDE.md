# Claude workflow rules — maths repo

This repo is a personal math study journal. Conversations happen in Spanish; committed content is in English.

## The four-step study loop

For every concept, the user works through this loop:

1. **Pick next topic** — read `ROADMAP.md` and the `topics/` tree. Recommend the natural continuation; do not invent a curriculum unilaterally.
2. **Add material** — when the user shares a URL or file, drop a stub in `topics/<topic>/materials/NN-<slug>.md`, run the appropriate fetcher in `scripts/`, and update the topic's `README.md` log.
3. **Challenge understanding** — in conversation, push on weak spots, surface ambiguities, ask "what would change if…" questions. Do not pre-summarize the material; force the user to explain it back.
4. **Author cards** — only at the end of the conversation, only for concepts the user signals as understood. The user dictates the angle; Claude edits for clarity and format. Cards go to `cards/<topic>.txt` in the format specified by `.claude/skills/anki-card-builder/SKILL.md`.

## Hard rules

- **Cards are closing rituals, not openers.** Never propose cards for material the user hasn't engaged with in conversation.
- **Self-authorship matters.** When co-authoring a card, the user provides the framing first; Claude refines. Reverse this only when explicitly asked.
- **Validate before declaring a deck done.** Run `python .claude/skills/anki-card-builder/scripts/validate_import.py <deck.txt>` and fix issues until it exits 0.
- **Defer to the skill.** For anything format-related — note types, separators, cloze syntax — read `.claude/skills/anki-card-builder/SKILL.md` and the `references/` files. Do not improvise.
- **Keep the repo offline-capable.** When a material is added, ensure it has a committed transcript (audio/video) and a stub. Binaries belong in `.gitignore`.
- **Update `ROADMAP.md`** whenever a topic moves from "candidate" to "in progress" to "covered".

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
