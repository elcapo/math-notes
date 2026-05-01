#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["yt-dlp"]
# ///
"""
Fetch a YouTube video and write a Markdown transcript built from its auto-generated subtitles.

Usage:
    ./fetch-youtube.py <url> <output-stem>

Outputs (next to <output-stem>):
    <stem>.<ext>            video file (gitignored: mp4/mkv/webm)
    <stem>.transcript.md    cleaned transcript with per-minute anchors (committed)

Idempotent: skips work when both video and transcript already exist.

ffmpeg is not required: yt-dlp falls back to the best single-format video when it cannot
merge, and subtitles are parsed in Python (VTT or SRT — whichever YouTube serves).
"""

import re
import shutil
import sys
from pathlib import Path

from yt_dlp import YoutubeDL


VIDEO_EXTS = ("mp4", "mkv", "webm")
SUB_EXTS = ("vtt", "srt")
TIMESTAMP_RE = re.compile(r"(\d{2}):(\d{2}):(\d{2})[.,]\d{3}\s*-->")


def subs_to_markdown(sub_path: Path) -> str:
    """Parse a VTT or SRT subtitle file into Markdown with per-minute anchors and dedup.

    YouTube auto-subs come as paired cues — a word-timed one (with <c> tags) introducing
    new content, then a "settled" plain duplicate. To avoid the rolling-window repetition,
    keep only the last line of each word-timed cue when the file is YouTube-style.
    """
    text = sub_path.read_text(encoding="utf-8")
    is_rolling = "<c>" in text
    blocks = re.split(r"\n\n+", text.strip())
    out: list[str] = []
    last_minute = -1
    last_caption = ""
    skipped_header = False
    for block in blocks:
        rows = [r for r in block.strip().splitlines() if r]
        if not skipped_header and rows and rows[0].startswith("WEBVTT"):
            skipped_header = True
            continue
        ts_idx = next((i for i, r in enumerate(rows) if TIMESTAMP_RE.match(r)), None)
        if ts_idx is None or ts_idx + 1 >= len(rows):
            continue
        m = TIMESTAMP_RE.match(rows[ts_idx])
        assert m is not None
        h, mn, _ = (int(x) for x in m.groups())
        total_minutes = h * 60 + mn
        content_rows = rows[ts_idx + 1:]
        if is_rolling:
            if not any("<c>" in r for r in content_rows):
                continue
            caption = content_rows[-1]
        else:
            caption = " ".join(content_rows)
        caption = re.sub(r"<\d{2}:\d{2}:\d{2}[.,]\d{3}>", "", caption)
        caption = re.sub(r"<[^>]+>", "", caption)
        caption = re.sub(r"\s+", " ", caption).strip()
        if not caption or caption == last_caption:
            continue
        last_caption = caption
        if total_minutes != last_minute:
            out.append(f"\n## {h:02d}:{mn:02d}\n")
            last_minute = total_minutes
        out.append(caption)
    return "\n".join(out).strip() + "\n"


def video_exists(stem: Path) -> bool:
    return any((stem.parent / f"{stem.name}.{ext}").exists() for ext in VIDEO_EXTS)


def find_sub_file(stem: Path) -> Path | None:
    for ext in SUB_EXTS:
        candidates = sorted(stem.parent.glob(f"{stem.name}.*.{ext}"))
        if candidates:
            return candidates[0]
    return None


def fetch(url: str, stem: Path) -> int:
    stem.parent.mkdir(parents=True, exist_ok=True)
    transcript = stem.parent / f"{stem.name}.transcript.md"

    if video_exists(stem) and transcript.exists():
        print(f"[skip] {stem.name} already complete")
        return 0

    has_ffmpeg = shutil.which("ffmpeg") is not None
    ydl_opts = {
        "outtmpl": str(stem) + ".%(ext)s",
        "format": "bv*+ba/b" if has_ffmpeg else "b",
        "merge_output_format": "mp4",
        "writeautomaticsub": True,
        "subtitleslangs": ["en"],
        "no_overwrites": True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    sub_path = find_sub_file(stem)
    if sub_path is None:
        print(f"[warn] no subtitles produced for {stem.name}", file=sys.stderr)
        return 1
    transcript.write_text(subs_to_markdown(sub_path), encoding="utf-8")
    print(f"[ok] {stem.name} -> {transcript.name}")
    return 0


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: fetch-youtube.py <url> <output-stem>", file=sys.stderr)
        return 2
    return fetch(sys.argv[1], Path(sys.argv[2]).resolve())


if __name__ == "__main__":
    sys.exit(main())
