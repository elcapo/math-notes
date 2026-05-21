# Maths

Personal study repository for filling foundational gaps in mathematics and retaining what I learn.

## Purpose

I'm rebuilding mathematical foundations from the ground up. This repo is the long-term home for:

- Study materials I work through (videos, articles, papers, books — all sources in English).
- The notes and challenges that come out of working with them.
- The Anki decks that keep what I've understood from decaying.

## Methodology

The loop, repeated indefinitely:

1. **Pick the next topic** — given what's already in `topics/` and `ROADMAP.md`, choose the natural continuation.
2. **Add a study material** — drop the source (URL, PDF, etc.) into the appropriate topic folder. If it's audio or video, the script downloads a local copy and a transcript.
3. **Challenge understanding in conversation** — work through the material with Claude, who pushes on weak spots until the concept is solid.
4. **Close with self-authored cards** — only for the concepts I have understood, write Anki cards myself. Self-authored cards stick ~3× better than canned decks.

Cards are a *closing ritual*, never an opener. If I don't yet understand something, I don't make a card for it.

## Repository layout

```
maths/
├── README.md            ← you are here
├── AGENTS.md            ← workflow rules every AI agent follows in this repo
├── CLAUDE.md            ← symlink to AGENTS.md (for Claude Code auto-discovery)
├── ROADMAP.md           ← topics covered + candidates for what's next
├── .claude/skills/      ← discoverable skills (anki-card-builder)
├── topics/              ← one folder per topic; materials, transcripts, notes
├── cards/               ← Anki-importable .txt decks, one per topic
├── notebooks/           ← interactive Marimo notebooks (uv-managed Python)
└── scripts/             ← project-local tooling (uv-managed Python)
```

## Working with materials

Materials live in `topics/<topic>/materials/`. For each material:

- A small `*.md` stub is committed with the source URL and metadata.
- The audio/video binary is **gitignored** — anyone with the repo can regenerate it with the fetcher.
- The transcript is **committed** so the repo is searchable and offline-readable.

To regenerate every missing binary in the repo:

```bash
cd scripts

uv run fetch-all.py
```

To fetch a single YouTube video manually:

```bash
# Pattern
uv run fetch-youtube.py <url> <output-stem>

# Example
uv run fetch-youtube.py https://www.youtube.com/watch?v=MaszunEszVM \
    topics/calculus-foundations/materials/01-functions-basics
```

Scripts use [`uv`](https://docs.astral.sh/uv/) and bootstrap their own Python dependencies on first run. Install `uv` once:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Make sure `ffmpeg` is on your PATH, and the rest is automatic.

## Running notebooks

The `notebooks/` folder holds interactive [Marimo](https://marimo.io/) notebooks for experimenting with concepts visually (plotting expressions, comparing functions, etc.). It is a self-contained `uv` project with its own `pyproject.toml` and `uv.lock`.

Two run modes:

```bash
cd notebooks

# Reactive editor (the usual mode while studying)
uv run marimo edit expression-plotter.py

# Read-only "app" mode (hides the code)
uv run marimo run expression-plotter.py
```

The first run installs dependencies into `notebooks/.venv/` (gitignored). See `notebooks/README.md` for the catalogue of available notebooks and their parameters.

## Spaced repetition

Anki is the spaced repetition system. Decks live in `cards/<topic>.txt` as Anki-importable plain-text files. To import:

1. Open Anki → *File → Import*.
2. Pick the `.txt` file.
3. Confirm the column mapping; click *Import*.

The card-design philosophy and exact format spec uses the [spaced-repetition-skill](https://github.com/elcapo/spaced-repetition-skill).

## Conventions

- All committed files are in **English**.
- Topic folders use **descriptive slugs** (`calculus-foundations`, `linear-algebra`); ordering is tracked in `ROADMAP.md`.
- Lessons / materials inside a topic use a **two-digit numeric prefix** (`01-`, `02-`) so they sort in study order.
- Avoid using acronyms (prefer "spaced repetition" over "SR").
- When writting math Markdown, prefer $x \in A$ over `x ∈ A`.