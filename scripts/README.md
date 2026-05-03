# Scripts

Project-local tooling. This directory is a `uv` project (`pyproject.toml` + `uv.lock`); a single virtual environment serves every script.

## Prerequisites

- [`uv`](https://docs.astral.sh/uv/) — manages the venv and runs the scripts. One-line install: `curl -LsSf https://astral.sh/uv/install.sh | sh`.
- [`ffmpeg`](https://ffmpeg.org/) — *optional but recommended* for `fetch-youtube.py`. Without it, `yt-dlp` falls back to the best single-format video (lower max quality) and serves subtitles in their native VTT format (the script handles both VTT and SRT). Install via `apt install ffmpeg` / `brew install ffmpeg` if you want merged 1080p+ video.

## Running

The scripts use a `uv run --` shebang, so they self-bootstrap the venv on first run as long as the working directory is `scripts/`. Two equivalent invocations:

```bash
cd scripts && ./fetch-youtube.py <args...>
# or, from the repo root:
uv run --directory scripts/ scripts/fetch-youtube.py <args...>
```

## Scripts

### `fetch-youtube.py`

Download a YouTube video and write a clean Markdown transcript from its auto-generated subtitles.

```bash
./fetch-youtube.py <url> <output-stem>
```

Example:

```bash
./fetch-youtube.py https://www.youtube.com/watch?v=MaszunEszVM \
    ../topics/calculus-foundations/materials/01-functions-basics
```

Produces `01-functions-basics.mp4` (gitignored) and `01-functions-basics.transcript.md` (committed).

### `fetch-all.py`

Walk every material stub in `topics/*/materials/*.md`, read its `source:` front-matter field, and invoke the right fetcher. Idempotent — already-fetched materials are skipped.

```bash
./fetch-all.py
```

### `graph-quiz.py`

Render PNGs to study the formula ↔ graph correspondence. Three subcommands.

**Plot a known formula** (use to predict the shape, then check):

```bash
./graph-quiz.py plot "x**2 - 2*x" --domain -5 5 --out /tmp/graph-quiz.png
./graph-quiz.py plot "sin(x)"       --domain -6.3 6.3
```

Allowed names in the expression: `x`, `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, `abs`, `pi`, `e`. Default output is `/tmp/graph-quiz.png`.

**Random graph from the catalog** (use to identify family + recover coefficients):

```bash
./graph-quiz.py random                       # any family
./graph-quiz.py random --family rational     # restrict to a family
./graph-quiz.py random --seed 42             # reproducible pick
```

The PNG is rendered without label or title; the answer is written to `<out>.answer.txt`.

**Reveal the answer** for the most recent random plot:

```bash
./graph-quiz.py reveal
./graph-quiz.py reveal --out /tmp/graph-quiz.png
```

Catalog: `linear`, `quadratic`, `rational`, `exponential`, `logarithmic`, `sine`, `absolute`. Coefficients are drawn from small "clean" sets so reverse-engineering from visible points stays a reasoning exercise rather than parameter fitting.
