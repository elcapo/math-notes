#!/usr/bin/env -S uv run --
"""
Walk every material stub in topics/*/materials/ and regenerate missing binaries / transcripts.

A stub is a Markdown file with YAML front-matter:

    ---
    source: https://www.youtube.com/watch?v=...
    kind: video        # one of: video, pdf, reference
    ---

    Free-form notes about why this material was added, license, etc.

`kind: video` runs the YouTube fetcher. `kind: pdf` downloads the file alongside the stub.
`kind: reference` is a link-only entry that needs no local copy.

Idempotent — already-fetched materials are skipped by the underlying fetcher.
"""

import re
import subprocess
import sys
import urllib.request
from pathlib import Path


YOUTUBE_HOSTS = ("youtube.com", "youtu.be")
SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT = SCRIPTS_DIR.parent


def parse_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm


def main() -> int:
    rc = 0
    stubs = sorted((ROOT / "topics").glob("*/materials/*.md"))
    if not stubs:
        print("No material stubs found under topics/*/materials/")
        return 0
    for stub in stubs:
        if stub.name.endswith(".transcript.md"):
            continue
        fm = parse_front_matter(stub)
        source = fm.get("source", "")
        if not source:
            continue
        stem = stub.with_suffix("")
        kind = fm.get("kind", "")
        if kind == "reference":
            print(f"[ref] {stub.relative_to(ROOT)} — link-only ({source})")
            continue
        if any(host in source for host in YOUTUBE_HOSTS):
            print(f"==> {stub.relative_to(ROOT)} ({source})")
            result = subprocess.run(
                ["uv", "run", "--directory", str(SCRIPTS_DIR),
                 "fetch-youtube.py", source, str(stem)],
                check=False,
            )
            rc |= result.returncode
        elif kind == "pdf" or source.lower().endswith(".pdf"):
            pdf_path = stem.with_suffix(".pdf")
            if pdf_path.exists():
                print(f"[skip] {pdf_path.relative_to(ROOT)} already present")
                continue
            print(f"==> {stub.relative_to(ROOT)} ({source})")
            try:
                urllib.request.urlretrieve(source, pdf_path)
                print(f"[ok] -> {pdf_path.relative_to(ROOT)}")
            except Exception as exc:
                print(f"[err] failed to download {source}: {exc}", file=sys.stderr)
                rc |= 1
        else:
            print(f"[skip] {stub.relative_to(ROOT)} — unknown source: {source}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
