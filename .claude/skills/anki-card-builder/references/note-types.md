# Anki note types

A *note type* defines the **fields** of a note and the **templates** that generate cards from those fields. A single note type can produce 1, 2, or N cards per note (Cloze can produce 20+).

## Built-in note types

### Basic

- **Fields**: `Front`, `Back`.
- **Cards generated**: 1 (Front → Back).
- **When to use**: direct question-and-answer where direction only matters one way.

### Basic (and reversed card)

- **Fields**: `Front`, `Back`.
- **Cards generated**: 2 (Front → Back and Back → Front).
- **When to use**: truly bidirectional pairs (vocabulary ES↔EN, symbol↔name, formula↔name).
- **When NOT to use**: if the reverse direction does not make sense (concept definitions are rarely unique in reverse → "What concept is defined as…?" usually has multiple valid answers).

### Basic (optional reversed card)

- **Fields**: `Front`, `Back`, `Add Reverse`.
- **Cards generated**: 1 or 2 depending on whether `Add Reverse` is empty or not.
- **When to use**: when most cards are unidirectional but a few deserve a reverse. Mark with any value (`y`, `1`) to enable the reverse.

### Basic (type in the answer)

- **Fields**: `Front`, `Back`.
- **Cards generated**: 1, with a text input where the user types the answer; Anki compares letter by letter.
- **When to use**: spelling, precise terminology, exact formulas. Useful for languages (writing the exact word).
- **When NOT to use**: long answers or answers with valid synonyms.

### Cloze

- **Fields**: `Text`, `Back Extra`.
- **Cards generated**: one per unique `cN` index in `Text`.
- **When to use**: when context is essential — sentences, definitions, principles where hiding a key word forces retrieval of the concept while the rest stays visible as an anchor.

Cloze syntax:

```
{{c1::hidden text}}
{{c1::hidden text::hint}}
{{c2::another piece}}
```

Multiple indices in the same text generate multiple cards:

```
Text: The {{c1::mitochondrion}} is responsible for producing {{c2::ATP}} via {{c3::oxidative phosphorylation}}.
```

→ 3 cards, one per `cN`.

The same index groups: `{{c1::A}}` and `{{c1::B}}` are hidden **together** in a single card. Use this for pieces that should be retrieved together.

### Image Occlusion (built-in since Anki 23.10)

- **Fields**: `Image`, `Header`, `Back Extra`, etc.
- **When to use**: anatomy, maps, labeled schematics.
- Created from the Anki interface, not from plain text: add note → Image Occlusion → load image → draw masks over the labels.

Image Occlusion cannot be generated from a plain `.txt`. To distribute, use `.apkg`.

## Custom note types

### When to create them

- The user wants extra fields (`Source`, `Hint`, `Mnemonic`, `Image`, `Audio`).
- Visual styling must be specific (custom CSS).
- Cards need conditional logic (show a field only if it has content).

### Structure

A note type has:

1. **Fields** — ordered list of names.
2. **Templates** — one or more, each with a `Front Template` and `Back Template`.
3. **Style** — CSS applied to all cards of the note type.

### Template syntax

Field variables: `{{FieldName}}`. They are substituted with the content of the field for that note.

Typical front template:

```html
<div class="front">{{Front}}</div>
{{#Hint}}<div class="hint">Hint: {{Hint}}</div>{{/Hint}}
```

Typical back template:

```html
{{FrontSide}}
<hr id=answer>
<div class="back">{{Back}}</div>
{{#Source}}<div class="source">Source: {{Source}}</div>{{/Source}}
```

`{{FrontSide}}` repeats the front on the back (standard). `{{#Field}}…{{/Field}}` is conditional rendering: the block is shown only if `Field` is non-empty.

### CSS

Common selectors:

```css
.card {
  font-family: -apple-system, sans-serif;
  font-size: 18px;
  text-align: center;
  color: #222;
  background: #fafafa;
}

.front { font-weight: 600; }
.back { color: #0a5; }
.hint { color: #888; font-style: italic; font-size: 0.9em; }
.source { color: #aaa; font-size: 0.8em; margin-top: 1em; }
```

Automatic dark mode:

```css
.nightMode .card { color: #ddd; background: #222; }
.nightMode .back { color: #4f9; }
```

### Generating custom note types from text

Plain `.txt` files cannot define note types; the note type must already exist in the collection. Options:

1. **Ask the user to create the note type manually** in Anki (*Tools → Manage Note Types → Add*) and describe the fields to add.
2. **Generate an `.apkg`** with `genanki` that includes the note type plus the notes. See `references/import-format.md` section "Importing via apkg".

Example steps to deliver to a user creating a "Principle" note type:

```
1. Anki → Tools → Manage Note Types → Add → Clone: Basic.
2. Rename to "Principle".
3. Fields → Add: Hint, Mnemonic, Source.
4. Cards → edit Front and Back templates with the syntax above.
5. Cards → Styling → paste the CSS.
6. Import the .txt declaring #notetype:Principle and #columns:Front<TAB>Back<TAB>Hint<TAB>Mnemonic<TAB>Source<TAB>Tags.
```

## Recommendations by material type

| Material | Recommended note type |
|---|---|
| Bidirectional vocabulary | Basic (and reversed card) |
| Unidirectional vocabulary (L2 → L1) | Basic |
| Spelling / exact terms | Basic (type in the answer) |
| Long definitions with context | Cloze |
| Principles with several pieces | Cloze (multiple `cN`) |
| Lists / enumerations | Partial Cloze (one `cN` per element) |
| Anatomy, maps, schematics | Image Occlusion |
| Pure factual Q&A | Basic |
| Contrast between concepts | Basic with custom fields `A`, `B`, `Difference` |
