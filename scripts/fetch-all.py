#!/usr/bin/env -S uv run --
"""
Walk every material stub in topics/*/materials/ and regenerate missing binaries / transcripts.

A stub is a Markdown file with YAML front-matter:

    ---
    source: https://www.youtube.com/watch?v=...
    ---

    Free-form notes about why this material was added, license, etc.

Idempotent — already-fetched materials are skipped by the underlying fetcher.
"""

import re
import subprocess
import sys
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
        if any(host in source for host in YOUTUBE_HOSTS):
            print(f"==> {stub.relative_to(ROOT)} ({source})")
            result = subprocess.run(
                ["uv", "run", "--directory", str(SCRIPTS_DIR),
                 "fetch-youtube.py", source, str(stem)],
                check=False,
            )
            rc |= result.returncode
        else:
            print(f"[skip] {stub.relative_to(ROOT)} — unknown source: {source}")
    return rc


if __name__ == "__main__":
    sys.exit(main())
