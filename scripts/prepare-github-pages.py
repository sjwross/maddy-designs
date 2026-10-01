#!/usr/bin/env python3
"""Rewrite absolute / paths for GitHub project Pages (/maddy-designs)."""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
BASE = "/maddy-designs"
TEXT_SUFFIXES = {".html", ".htm", ".js", ".css", ".json", ".txt", ".xml", ".svg", ".map"}

PATH_RE = re.compile(
    r'(?<![\w./-])(/(?:_next|favicon\.ico|maddy-penny-logo\.png|cuban-chain-ref\.jpg)(?:[^"\'\s)\\]*)?)'
)


def rewrite(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        path = match.group(1)
        if path.startswith(BASE + "/") or path == BASE:
            return path
        return BASE + path

    return PATH_RE.sub(repl, text)


def main() -> int:
    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            original = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        updated = rewrite(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
            print(f"updated {path.relative_to(ROOT)}")

    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"done; files changed: {changed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
