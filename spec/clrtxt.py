#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


TEXT_BYTE_WHITELIST = set(b"\n\r\t\f\b")


def is_probably_binary(data: bytes) -> bool:
    if not data:
        return False

    if data.startswith((b"\xef\xbb\xbf", b"\xff\xfe", b"\xfe\xff")):
        return False

    if b"\x00" in data:
        return True

    suspicious = 0
    for byte in data:
        if byte in TEXT_BYTE_WHITELIST or 32 <= byte <= 126:
            continue
        if byte >= 128:
            continue
        suspicious += 1

    return (suspicious / len(data)) > 0.30


def convert_file(path: Path, dry_run: bool = False) -> bool:
    try:
        data = path.read_bytes()
    except OSError as exc:
        print(f"ERROR  {path} ({exc})")
        return False

    if is_probably_binary(data):
        return False

    if b"\r\n" not in data:
        return False

    converted = data.replace(b"\r\n", b"\n")
    if converted == data:
        return False

    if not dry_run:
        try:
            path.write_bytes(converted)
        except OSError as exc:
            print(f"ERROR  {path} ({exc})")
            return False

    print(f"{'WOULD FIX' if dry_run else 'FIXED    '} {path}")
    return True


def scan_folder(root: Path, dry_run: bool = False) -> tuple[int, int]:
    scanned = 0
    converted = 0

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        scanned += 1
        if convert_file(path, dry_run=dry_run):
            converted += 1

    return scanned, converted


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Recursively convert Windows CRLF text files to Linux LF."
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Folder to scan. Defaults to the current directory.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which files would be converted without modifying them.",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        print(f"Path does not exist: {root}")
        return 1
    if not root.is_dir():
        print(f"Path is not a directory: {root}")
        return 1

    scanned, converted = scan_folder(root, dry_run=args.dry_run)
    print(f"\nScanned {scanned} files. Converted {converted} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
