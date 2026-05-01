# Anki Card Builder — a model-agnostic AI skill

A portable, vendor-neutral skill that teaches an AI agent how to turn study material into **Anki-importable text files** that encode **principles**, not isolated facts. It works with any agent that can read Markdown skill files: Claude Code, the Claude Agent SDK, Cursor, Continue, custom OpenAI/Anthropic agents, or anything else.

## What this skill does

When you ask an agent something like:

- *"Build me an Anki deck from these notes on Greek roots."*
- *"Generate 20 cards for my pharmacology midterm focused on principles."*
- *"Convert this glossary into a bilingual ES↔EN deck."*

…the agent loads `SKILL.md`, follows the workflow, and produces a `.txt` file you can import into Anki via *File → Import* (or by dragging it into the main window). It will refuse to dump facts onto cards and will instead extract the **underlying principles** so the deck stays small, transferable, and learnable in minutes per day.

## Why "principles, not facts"

Most decks fail because every card is a brittle, isolated fact. Decks that encode the **generative rule** behind a family of facts:

- Are dramatically smaller (often half the card count for the same coverage).
- Transfer to questions never specifically studied.
- Mature faster, so daily review stays under 10 minutes for years.

See [`spaced-repetition-foundations.md`](references/spaced-repetition-foundations.md) for the rationale and [`card-design-principles.md`](references/card-design-principles.md) for the operational rules.

## Repository layout

- [`SKILL.md`](SKILL.md) — AI-facing entry point (with frontmatter)
- [`README.md`](README.md) — this file (human-facing)
- [`LICENSE`](LICENSE) — MIT
- `references/`
  - [`spaced-repetition-foundations.md`](references/spaced-repetition-foundations.md) — why principle-based cards compound
  - [`card-design-principles.md`](references/card-design-principles.md) — Wozniak's 20 rules adapted + anti-patterns
  - [`import-format.md`](references/import-format.md) — Anki text-import format spec
  - [`note-types.md`](references/note-types.md) — built-in and custom note types
- `examples/`
  - [`basic-deck.txt`](examples/basic-deck.txt) — Greek roots, principle-encoded
  - [`cloze-principles-deck.txt`](examples/cloze-principles-deck.txt) — pharmacological principles via Cloze
  - [`bilingual-deck.txt`](examples/bilingual-deck.txt) — ES↔EN phrasal verbs, Basic+reversed
- `scripts/`
  - [`validate_import.py`](scripts/validate_import.py) — stdlib-only validator (Python 3.8+)

[`SKILL.md`](SKILL.md) is the entry point an AI agent should read. `references/` holds the deep documentation it loads on demand. `examples/` are real, validated `.txt` files the agent can pattern-match against. [`validate_import.py`](scripts/validate_import.py) is the pre-flight check the agent runs before delivering a deck.

## How to use this skill with different AI agents

This skill follows a model-agnostic convention: **a directory containing [`SKILL.md`](SKILL.md) with YAML frontmatter (`name`, `description`, optional `version`/`license`/`compatibility`), plus `references/`, `examples/`, and `scripts/` subdirectories.** Any agent that supports loading Markdown skills can use it directly.

### Claude Code

Drop the directory into one of Claude Code's skill locations:

```bash
# Project-scoped
cp -r spaced-repetition/ .claude/skills/anki-card-builder/

# User-scoped (available across all projects)
cp -r spaced-repetition/ ~/.claude/skills/anki-card-builder/
```

Then ask Claude Code to "build me an Anki deck from …" and it will pick up the skill automatically.

### Claude Agent SDK

Reference [`SKILL.md`](SKILL.md) directly in your agent's system prompt or load it as a tool/resource. The frontmatter `description` is short enough to inline, and `references/` can be loaded on demand.

### Cursor / Continue / other IDE agents

Most IDE agents support project-level instruction files. Either:

- Symlink or include [`SKILL.md`](SKILL.md) from your `.cursorrules`, `.continuerc`, or equivalent.
- Point the agent at this directory as a "knowledge base" or "rules folder".

### Custom agents (OpenAI Assistants, LangChain, raw API calls)

Concatenate [`SKILL.md`](SKILL.md) into the system prompt. Lazily fetch files in `references/` when the model calls a `read_file` tool. The validator script can be exposed as a tool the agent can call.

### Just a human reading the docs

Read [`spaced-repetition-foundations.md`](references/spaced-repetition-foundations.md) first, then [`card-design-principles.md`](references/card-design-principles.md). The examples in `examples/` are calibrated illustrations — you can study them as templates and write your own decks by hand.

## Validating a deck

```bash
python scripts/validate_import.py path/to/your-deck.txt
```

Exits 0 if valid; 1 with a list of issues otherwise. No third-party dependencies.

## Importing into Anki

1. Open Anki.
2. *File → Import* (or drag the `.txt` onto the main window).
3. Review the column-mapping preview — the file's `#`-headers should populate it automatically.
4. Click *Import*.

Anki will create the deck, sub-decks, and tags as declared in the headers.

## Compatibility notes

- The skill targets `.txt` import (Anki ≥ 2.1.54, where `#`-headers are supported). For Anki ≥ 23.10, Image Occlusion is built in.
- For richer cases (custom note types with HTML/CSS, embedded media), the skill recommends generating an `.apkg` via [`genanki`](https://github.com/kerrickstaley/genanki) instead of `.txt`. See [`import-format.md`](references/import-format.md).

## License

MIT. See [`LICENSE`](LICENSE). Forks, adaptations, and translations are welcome.

## Credits

The "principles, not facts" framing draws on:

- Alec Palmerton, *I Reviewed 28,655 Flashcards Every Day for 17 Years*, <https://www.youtube.com/watch?v=7WtznlsP6M8>.
- Piotr Wozniak, *Effective learning: Twenty rules of formulating knowledge*, <https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge>.
- The official Anki manual, <https://docs.ankiweb.net/>.
