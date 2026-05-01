# Scripts

Project-local tooling. All scripts are Python with PEP 723 inline metadata: `uv` resolves their dependencies on first run.

## Prerequisites

- [`uv`](https://docs.astral.sh/uv/) — installs and runs the scripts. One-line install: `curl -LsSf https://astral.sh/uv/install.sh | sh`.
- [`ffmpeg`](https://ffmpeg.org/) — *optional but recommended*. Without it, `yt-dlp` falls back to the best single-format video (lower max quality) and serves subtitles in their native VTT format (the script handles both VTT and SRT). Install via `apt install ffmpeg` / `brew install ffmpeg` if you want merged 1080p+ video.

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
