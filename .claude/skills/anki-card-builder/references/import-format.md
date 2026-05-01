# Anki import format (text/CSV)

Detailed reference for the text-file format Anki accepts via *File → Import*. Source: <https://docs.ankiweb.net/importing/text-files.html>.

## General structure

A valid file has two sections:

1. **Headers** — lines starting with `#`, in any order, all before the first data row. They configure how the importer interprets the file.
2. **Data rows** — one note per line, with fields separated by the declared delimiter.

```
#separator:tab
#html:true
#notetype:Basic
#deck:My Deck
#columns:Front	Back	Tags
Question 1	Answer 1	tag1 tag2
Question 2	Answer 2	
```

## Full header reference

### `#separator:`

Defines the column delimiter. Accepted values:

| Value | Character |
|---|---|
| `tab` | `\t` |
| `comma` | `,` |
| `semicolon` | `;` |
| `pipe` | `\|` |
| `colon` | `:` |
| `space` | ` ` |

**Recommendation**: always use `tab`. It collides least with content. If using `comma` for CSV, wrap any field that contains commas in double quotes.

### `#html:true|false`

If `true`, fields are interpreted as HTML: `<b>`, `<br>`, `<i>`, `<img src="...">`, etc. If `false` (default), the characters `<`, `>`, `&` are escaped literally.

**Recommendation**: use `#html:true` almost always — it allows formatting, line breaks via `<br>`, lists, code (`<code>`), etc.

### `#notetype:NotetypeName`

Sets the note type for every row. Must match exactly an existing note type in the user's collection. Built-in note types:

- `Basic`
- `Basic (and reversed card)`
- `Basic (optional reversed card)`
- `Basic (type in the answer)`
- `Cloze`
- `Image Occlusion`

If the note type contains spaces or parentheses, write it as is, without quotes.

### `#deck:DeckName`

Sets the destination deck. If the deck does not exist, Anki creates it. For nested decks use `::`:

```
#deck:Languages::English::Vocabulary::Phrasal Verbs
```

### `#tags:tag1 tag2`

Tags applied to **every** note in the file. Separated by spaces (not commas). Tags cannot contain spaces; use `_`, `-`, or hierarchy via `::` (`medicine::pharmacology`).

### `#columns:Name1	Name2	...`

Names the columns in the same order they appear in data rows. Optional but strongly recommended: makes the file self-documenting and lets Anki auto-map fields to the note type.

```
#columns:Front	Back	Tags
```

### `#tags column:N`

Indicates that column N (1-indexed) contains the per-row tags (instead of applying the global `#tags:`). Useful when each note has different tags.

```
#tags column:3
```

### `#deck column:N`

Indicates that column N contains the destination deck name per row. Useful for distributing notes across several decks from a single file.

### `#notetype column:N`

Indicates that column N contains the note type name per row. Useful for mixing Basic and Cloze in the same file.

### `#guid column:N`

Indicates that column N contains a GUID (globally unique identifier) per note. **Critical for incremental import**: if the file is re-imported and a GUID already exists in the collection, Anki updates the note rather than duplicating it.

Without `#guid column:`, Anki determines duplicates from the first field, which is fragile if the front changes.

Generate GUIDs as stable strings (e.g. hash of the source content, UUID, slug). Example:

```
#guid column:1
g_001	Knowing ortho- = correct, what does orthodontics correct?	Teeth.
g_002	Knowing ortho- = correct, what does orthopedics correct?	Bones.
```

## Escaping and edge cases

### Quotes and separators inside a field

If a field contains the separator or a newline, wrap it in double quotes. Internal quotes are doubled (`""`).

With `#separator:tab`:

```
#separator:tab
"Field with	tab inside"	Answer
"She said ""hello""."	Answer
```

With `#separator:comma`:

```
#separator:comma
"Question, with comma","Answer"
```

### Line breaks

If `#html:true`, use `<br>` inside the field:

```
Line 1<br>Line 2	Answer
```

Alternatively, wrap the field in quotes and use real newlines:

```
"Line 1
Line 2"	Answer
```

### Data lines starting with `#`

A data line cannot start with `#` (Anki would treat it as a header). If necessary, prepend a space or wrap in quotes:

```
" #hashtag at start"	Answer
```

### Encoding

UTF-8 without BOM. With BOM it works in most recent versions but can cause problems in cross-export/import scenarios.

## Incremental import

For living decks that are updated over time:

1. Assign stable GUIDs to each note (`#guid column:1`).
2. Keep the source file under version control (git).
3. Re-import the file: Anki updates existing notes (matching GUID) and adds new ones.

Anki's behavior on duplicates:

- Matching GUID → update fields.
- No GUID, matching first field → according to the import option: *Update*, *Ignore*, *Add* (a dialog will ask).

## Importing via `apkg`

For complex cases (custom note types, HTML/CSS templates, embedded media), generate an `.apkg` file with the Python library [`genanki`](https://github.com/kerrickstaley/genanki). The `.apkg` is a zipped SQLite database that Anki imports as a whole: note types + cards + media.

**When to use `.apkg`**:

- Custom note type with specific HTML/CSS template.
- Cards with images/audio that must travel with the deck.
- Public distribution of the deck (a single self-contained file).

**When `.txt` is enough**:

- Plain-text material.
- Built-in note type (Basic, Cloze).
- Fast iteration and human review.

By default this skill produces `.txt`. Only fall back to `.apkg` if the user explicitly asks or the material requires custom note types.

## Multimedia (images, audio)

In `.txt` files, images are referenced with standard HTML:

```
What organ is this?	<img src="heart_001.jpg">
```

The file `heart_001.jpg` must be copied manually to the user's `collection.media/` folder **before** importing. Anki does *not* package media when importing a `.txt`. To distribute media alongside the deck, use `.apkg`.

Audio:

```
Pronounce "orthodontics"	[sound:orthodontics.mp3]
```

## Quick validation

Before delivering a file:

- [ ] Starts with `#`-headers (at least `#separator:`, `#notetype:`, `#deck:`).
- [ ] Every row has the same number of columns.
- [ ] The declared separator matches the one actually used.
- [ ] No data line starts with `#`.
- [ ] If Cloze: `{{cN::...}}` markers close correctly.
- [ ] UTF-8.

`scripts/validate_import.py` automates all these checks.
