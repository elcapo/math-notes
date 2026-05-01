#!/usr/bin/env python3
"""
Validator for Anki import files (text/CSV format).

Verifies headers, column consistency, separator, Cloze markers, and
quoting/escaping. Exits 0 if the file is valid, 1 otherwise.

Usage:
    python validate_import.py path/to/deck.txt

Requires only the Python standard library (3.8+).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SEPARATORS = {
    "tab": "\t",
    "comma": ",",
    "semicolon": ";",
    "pipe": "|",
    "colon": ":",
    "space": " ",
}

KNOWN_HEADERS = {
    "separator",
    "html",
    "notetype",
    "deck",
    "tags",
    "columns",
    "tags column",
    "deck column",
    "notetype column",
    "guid column",
}

CLOZE_RE = re.compile(r"\{\{c(\d+)::(.*?)(?:::(.*?))?\}\}", re.DOTALL)
UNCLOSED_CLOZE_RE = re.compile(r"\{\{c\d+::")


def parse_headers(lines: list[str]) -> tuple[dict[str, str], int]:
    """Return (headers, index_of_first_data_row)."""
    headers: dict[str, str] = {}
    for i, line in enumerate(lines):
        if not line.startswith("#"):
            return headers, i
        body = line[1:].rstrip("\n")
        if ":" not in body:
            raise ValueError(f"Line {i+1}: header without ':' → {line!r}")
        key, _, value = body.partition(":")
        key = key.strip()
        if key not in KNOWN_HEADERS:
            raise ValueError(
                f"Line {i+1}: unknown header '#{key}'. "
                f"Valid headers: {sorted(KNOWN_HEADERS)}"
            )
        headers[key] = value.strip()
    return headers, len(lines)


def split_csv_row(line: str, sep: str) -> list[str]:
    """Basic split that respects double quotes per the Anki format."""
    fields: list[str] = []
    cur: list[str] = []
    in_quotes = False
    i = 0
    while i < len(line):
        c = line[i]
        if c == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                cur.append('"')
                i += 2
                continue
            in_quotes = not in_quotes
            i += 1
            continue
        if not in_quotes and line.startswith(sep, i):
            fields.append("".join(cur))
            cur = []
            i += len(sep)
            continue
        cur.append(c)
        i += 1
    if in_quotes:
        raise ValueError("Unclosed quotes")
    fields.append("".join(cur))
    return fields


def validate_cloze_field(text: str, line_no: int) -> list[str]:
    errors: list[str] = []
    opens = len(UNCLOSED_CLOZE_RE.findall(text))
    closes = text.count("}}")
    matched = len(CLOZE_RE.findall(text))
    if opens != matched:
        errors.append(
            f"Line {line_no}: malformed Cloze marker "
            f"(openings={opens}, well-formed={matched}, '}}}}'={closes})"
        )
    if opens == 0:
        errors.append(
            f"Line {line_no}: notetype:Cloze but the row contains no {{{{cN::...}}}}"
        )
    return errors


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        raw = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        return [f"File is not valid UTF-8: {e}"]
    except FileNotFoundError:
        return [f"File not found: {path}"]

    if raw.startswith("﻿"):
        errors.append(
            "Warning: file starts with a BOM. It will work on modern Anki "
            "but it is preferable to save as UTF-8 without BOM."
        )
        raw = raw.lstrip("﻿")

    lines = raw.splitlines()
    if not lines:
        return ["Empty file."]

    try:
        headers, data_start = parse_headers(lines)
    except ValueError as e:
        return [str(e)]

    sep_name = headers.get("separator", "tab").lower()
    if sep_name not in SEPARATORS:
        errors.append(
            f"#separator:{sep_name} not recognized. Valid: {sorted(SEPARATORS)}"
        )
        sep = "\t"
    else:
        sep = SEPARATORS[sep_name]

    notetype = headers.get("notetype", "")
    is_cloze = notetype.lower() == "cloze"

    declared_columns: list[str] = []
    if "columns" in headers:
        declared_columns = [c.strip() for c in headers["columns"].split(sep)]

    expected_n_cols = len(declared_columns) if declared_columns else None

    data_lines = [
        (i + 1, line)
        for i, line in enumerate(lines[data_start:], start=data_start)
        if line.strip()
    ]
    if not data_lines:
        errors.append("No data rows found.")
        return errors

    for line_no, line in data_lines:
        if line.startswith("#"):
            errors.append(
                f"Line {line_no}: starts with '#' but is in the data section. "
                f"Anki would treat it as a header. Prepend a space or wrap in quotes."
            )
            continue
        try:
            fields = split_csv_row(line, sep)
        except ValueError as e:
            errors.append(f"Line {line_no}: {e}")
            continue
        if expected_n_cols is None:
            expected_n_cols = len(fields)
        elif len(fields) != expected_n_cols:
            errors.append(
                f"Line {line_no}: {len(fields)} columns, "
                f"expected {expected_n_cols} (per #columns)."
            )
        if is_cloze and fields:
            errors.extend(validate_cloze_field(fields[0], line_no))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate an Anki .txt/.csv import file."
    )
    parser.add_argument("file", type=Path, help="Path to the import file.")
    args = parser.parse_args()

    errors = validate(args.file)
    if errors:
        print(f"FAIL {args.file}: {len(errors)} issue(s)")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK   {args.file}: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
