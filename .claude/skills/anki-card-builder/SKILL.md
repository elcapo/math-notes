---
name: anki-card-builder
description: Use this skill when the user asks to create Anki cards, generate an Anki deck, build flashcards from notes, or convert study material into Anki-importable files (.txt/.csv). Produces text files with Anki's `#`-headers that import natively, and enforces principle-based card design instead of plain fact memorization.
version: 1.0.0
license: MIT
authors:
  - Carlos Capote
keywords:
  - anki
  - spaced-repetition
  - flashcards
  - study
  - learning
compatibility:
  - opencode
  - claude-code
  - claude-agent-sdk
  - cursor
  - continue
  - any-agent-that-reads-markdown-skills
---

# Anki Card Builder

Generate Anki-importable text files that encode **principles**, not isolated facts. Anki has no stable public API, so integration is always file-based: the user imports the file manually via *File → Import* (or by dragging it into the main window).

## When to use this skill

Activate when the request involves generating Anki cards or decks from notes, transcripts, glossaries, vocabulary, formulas, medical/legal/technical principles, etc.

Do **not** use it for conceptual questions about how Anki works internally (FSRS algorithm, sync, plugins) — refer those to <https://docs.ankiweb.net>.

## Guiding principle: encode principles, not facts

Most decks fail because every card is an isolated fact memorized by brute force. The goal here is the opposite: each card must force the learner to **apply** a principle.

Quick rule: **if the card can be answered correctly without understanding the underlying concept, it is a bad card**. If it forces the learner to think — to derive, transfer, or apply — it is a good card.

Bad example (memorizes a fact):

```
Front: What does "orthodontics" mean?
Back: Correction of the teeth.
```

Good example (forces application of the principle "ortho- = correct/straight"):

```
Front: Knowing that the root "ortho-" means "correct/straight", deduce what orthodontics corrects.
Back: The teeth (from "odont-" = tooth). That is why an orthodontist straightens/corrects the dentition.
```

The difference is that the second card also works for *orthopedics*, *orthography*, *orthoptics*, etc. — the principle transfers.

Before generating cards, group the source material by **underlying principles** and design the cards around those principles. If the user supplies a flat list of facts, try to identify the common generative rule and mention it.

> [!TIP]
> Follow this example:
>
> "I notice these five drugs share the principle of crossing the blood-brain barrier; I will generate one card that applies the principle instead of five cards of isolated facts."

For a detailed design guide (Wozniak's 20 rules adapted, minimum-information principle, atomicity, avoiding enumerations, using Cloze for context), see [`card-design-principles.md`](references/card-design-principles.md).

For the foundational rationale of *why* spaced repetition rewards principle-based cards, see [`spaced-repetition-foundations.md`](references/spaced-repetition-foundations.md).

## Output format: importable text file

Anki imports `.txt` or `.csv` files natively when they begin with `#`-headers that control the importer's behavior. **This is the preferred format** because it is human-readable, version-controllable in git, and dependency-free.

### Minimum template

```
#separator:tab
#html:true
#notetype:Basic
#deck:My Deck Name
#columns:Front	Back	Tags
Question 1	Answer 1	tag1 tag2
Question 2	Answer 2	tag1
```

### Supported headers

| Header | Purpose | Typical values |
|---|---|---|
| `#separator:` | Field delimiter | `tab`, `comma`, `semicolon`, `pipe` |
| `#html:` | Whether fields contain HTML | `true`, `false` |
| `#notetype:` | Fixed note type for all rows | `Basic`, `Basic (and reversed card)`, `Cloze` |
| `#deck:` | Target deck (use `::` for nesting) | `Languages::English::Vocabulary` |
| `#tags:` | Tags applied to every row | `tag1 tag2` |
| `#columns:` | Column names | `Front	Back	Tags` |
| `#tags column:` | Column that contains per-row tags | `3` |
| `#deck column:` | Column that contains the per-row deck | `4` |
| `#notetype column:` | Column that contains the per-row note type | `5` |
| `#guid column:` | Column with stable GUID (enables re-import + update) | `1` |

**Critical format rules**:

- The default separator is **tab**. Do not mix tabs with spaces; use literal tab characters.
- If a field contains the separator, a newline, or quotes, wrap it in double quotes (`"..."`) and double any internal quotes (`""`).
- If `#html:true`, line breaks inside a field are written as `<br>` or by wrapping in quotes with a real `\n`.
- Header order does not matter, but every `#`-header must appear before the first data row.
- Headers do not need to be repeated inside the file; one block is enough.

For full format details (escaping, GUIDs, incremental import, edge cases), see [`import-format.md`](references/import-format.md).

## Note types: when to use which

- **Basic**: question → answer. Use when there is a clear front/back formulation.
- **Basic (and reversed card)**: produces two cards (front→back and back→front). Use for bidirectional vocabulary (ES↔EN), term↔definition pairs.
- **Cloze**: hides parts of a passage with `{{c1::text}}`. Use when context matters to understand the answer — e.g. a sentence, a legal definition, a formula. A single Cloze note with `{{c1::...}}`, `{{c2::...}}`, `{{c3::...}}` produces three distinct cards from the same text, all sharing the context.

Cloze syntax:

```
{{c1::hidden content}}
{{c1::hidden content::visible hint}}
```

With the Cloze note type, the main field is called `Text` and there is usually a secondary field `Back Extra` for additional notes.

For custom note type design (fields, templates, CSS), see [`note-types.md`](references/note-types.md).

## Recommended workflow

1. **Clarify the material**: if the user attaches a long text, ask what level of detail they want (summary vs. exhaustive) and roughly how many cards they expect.
2. **Identify the principles**: read the material and extract the principles or generative rules. Internally list principles → derived examples.
3. **Choose the note type**: Basic for direct Q/A, Cloze when context is essential, Basic-reversed for bidirectional vocabulary.
4. **Choose deck name and hierarchy**: use `Topic::Subtopic` for nested decks. Confirm the root name with the user.
5. **Write the file**: produce the `.txt` with `#`-headers, tab separator, and `#html:true` (allows formatting and `<br>`).
6. **Validate**: run `python scripts/validate_import.py <file>.txt` to detect misaligned columns, mixed separators, or invalid headers before delivering it.
7. **Deliver import instructions**: tell the user to open Anki → *File → Import* → select the file → review the column-mapping preview → *Import*.

## Validator

[`scripts/validate_import.py`](scripts/validate_import.py) checks:

- Valid and consistent `#`-headers.
- That every row has the same number of columns as `#columns:`.
- That the declared separator is the one actually used.
- That Cloze markers (`{{cN::...}}`) are well-formed when `#notetype:Cloze`.
- That quoting and escapes are coherent.

Usage:

```bash
python scripts/validate_import.py path/to/deck.txt
```

Exits with code 0 if the file is valid; code 1 with errors listed otherwise. Requires only Python 3.8+ (standard library only).

## Resources

### `references/`

- **[`spaced-repetition-foundations.md`](references/spaced-repetition-foundations.md)** — Why principle-based cards compound and isolated-fact cards collapse. Read this before designing decks for users new to spaced repetition.
- **[`card-design-principles.md`](references/card-design-principles.md)** — Wozniak's 20 rules adapted, minimum-information principle, atomicity, when to split or merge cards, anti-patterns (enumerations, lists, circular definitions).
- **[`import-format.md`](references/import-format.md)** — Full specification of Anki's text import format (separators, escapes, GUIDs, incremental import, duplicate behavior).
- **[`note-types.md`](references/note-types.md)** — Built-in note types (Basic, Basic+reversed, Basic typed, Cloze, Image Occlusion), creation of custom note types, templates with `{{Field}}`, CSS.

### `examples/`

- **[`basic-deck.txt`](examples/basic-deck.txt)** — Basic deck with `#notetype:Basic` and several cards on Greek roots that illustrate principle encoding.
- **[`cloze-principles-deck.txt`](examples/cloze-principles-deck.txt)** — Cloze deck with contextualized medical principles.
- **[`bilingual-deck.txt`](examples/bilingual-deck.txt)** — Bidirectional ES↔EN deck with `Basic (and reversed card)` and per-row tags.

### `scripts/`

- **[`validate_import.py`](scripts/validate_import.py)** — Import-file validator (see section above).

## Anti-patterns to avoid

- **Dump cards**: pasting a whole slide or paragraph onto the back. The card must be answerable in seconds.
- **Flat enumerations**: "List the 7 taxonomic kingdoms" → if one is forgotten, the whole card fails. Split into 7 cards (or use mnemonic + Cloze).
- **Circular definitions**: "What is X?" → "X is what does Y, where Y is defined as X". Break the loop with an applied example.
- **Cards that do not force thinking**: if the front contains the answer or obvious hints, rephrase.
- **Mixing several principles in one card**: violates the minimum-information principle. One card = one atomic idea.
- **Defaulting to `Hard`**: instruct the user to use `Again` or `Good` during review; over-using `Hard` distorts the algorithm.

## Notes for AI agents

- This skill is **model-agnostic**: any agent capable of reading Markdown can follow it. There is no Claude-specific or vendor-specific behavior.
- All file paths in this skill are **relative** to the skill root.
- The validator script depends only on the Python standard library; do not introduce extra dependencies.
- When in doubt about format, prefer reading [`import-format.md`](references/import-format.md) over inventing answers — Anki's importer is strict about headers and separators.
