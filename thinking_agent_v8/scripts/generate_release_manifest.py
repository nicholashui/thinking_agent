#!/usr/bin/env python3
"""Release manifest (impl §4.3): SHA-256 over every shipped artifact —
source, data assets, configs, migrations. Reproducible release proof."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {".git", "__pycache__", ".pytest_cache", "data/manifests"}


def walk() -> list[Path]:
    out = []
    for p in sorted(ROOT.rglob("*")):
        if p.is_file() and not any(part in EXCLUDE for part in p.parts):
            out.append(p)
    return out


def main() -> None:
    entries = []
    for p in walk():
        rel = p.relative_to(ROOT).as_posix()
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        entries.append({"path": rel, "sha256": digest, "bytes": p.stat().st_size})
    manifest = {
        "release": "thinking-agent-v8",
        "generated_at_utc": "",  # stamped by CI (Date.now() is test-hostile)
        "files": entries,
    }
    out = ROOT / "data" / "manifests" / "release_manifest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"release manifest: {len(entries)} files -> {out}")


if __name__ == "__main__":
    main()
