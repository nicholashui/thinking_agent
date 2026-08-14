#!/usr/bin/env python3
"""Combine section-level MP3 chunks into per-part (LP01..LP12) MP3 files.

For each logical part NN (01..12):
    docs/training_agent.v8_audio_hk/section_{NNN}.mp3   (range concatenated)
    -> docs/training_agent.v8.part{NN}.mp3

Concatenation is done via binary join (valid for MP3 streams without
time-sampling header modifications — matches gen_book_tts_hk.py behaviour).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
AUDIO_DIR = DOCS_DIR / "training_agent.v8_audio_hk"
OUT_TEMPLATE = "thinking_agent.v8.part{nn}.mp3"
SECTION_TEMPLATE = "section_{nnn:03d}.mp3"

# Canonical mapping derived from:
#   1. translate_book.py split_markdown_by_headings(thinking_agent.v8.md) => 156 sections
#   2. split_v8_12parts.py H2_ORDERED LP ownership => each EN section -> LP
# Verified by: heading preview of first/last section of each LP range.
PART_RANGES: list[tuple[int, list[tuple[int, int]]]] = [
    # (LP number 1..12, list of (start_1b, end_1b) contiguous MP3 runs)
    (1,  [(1,   5)]),
    (2,  [(6,   12)]),
    (3,  [(13,  15)]),
    (4,  [(16,  19)]),
    (5,  [(20,  21)]),
    (6,  [(22,  23)]),
    (7,  [(24,  25)]),
    (8,  [(26,  30)]),
    (9,  [(31,  33)]),
    (10, [(34,  42)]),
    (11, [(43,  114)]),
    (12, [(115, 156)]),
]

PART_NAMES = [
    "LP01 Bookend / Introduction",
    "LP02 Scope, Lineage & Research Foundations",
    "LP03 Design Principles, Overview, Four Nested Timescales",
    "LP04 Stage 0/1 META-CONTROL + WHAT",
    "LP05 Stage 2 WHY Diagnose & Model",
    "LP06 Stage 3/4 HOW + DO",
    "LP07 Stage 5 REVIEW + Continuous VERIFY",
    "LP08 Intelligence Components (Reasoning / Multi-Agent / Memory / World / Tools)",
    "LP09 Kernels Safety + Evolution + Evaluation",
    "LP10 Implementation, MVTA & Roadmap",
    "LP11 Closures, v6 & v7 layers, Appendix, References",
    "LP12 v8 SDL Layer (Self-Directed Learning)",
]


def list_ranges(runs: list[tuple[int, int]]) -> list[int]:
    out: list[int] = []
    for s, e in runs:
        out.extend(range(s, e + 1))
    return out


def dry_run_check_sources() -> tuple[bool, dict[int, list[Path]], dict[int, list[int]]]:
    """Check that every required section_NNN.mp3 exists under AUDIO_DIR.

    Returns (all_ok, {lp: [section_path,...]}, {lp: [missing_section_numbers]}).
    """
    ok = True
    found: dict[int, list[Path]] = {}
    missing: dict[int, list[int]] = defaultdict(list)
    for lp, runs in PART_RANGES:
        found[lp] = []
        for n in list_ranges(runs):
            p = AUDIO_DIR / SECTION_TEMPLATE.format(nnn=n)
            if p.is_file():
                found[lp].append(p)
            else:
                missing[lp].append(n)
                ok = False
    return ok, found, dict(missing)


def concat_mp3_files(sources: list[Path], dest: Path) -> int:
    """Binary-concatenate MP3 files into dest. Return total bytes written."""
    total = 0
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("wb") as out_f:
        for src in sources:
            with src.open("rb") as in_f:
                while True:
                    chunk = in_f.read(1 << 20)  # 1 MiB
                    if not chunk:
                        break
                    out_f.write(chunk)
                    total += len(chunk)
    return total


def fmt_ranges(runs: list[tuple[int, int]]) -> str:
    parts = []
    for s, e in runs:
        if s == e:
            parts.append(f"{s:03d}")
        else:
            parts.append(f"{s:03d}\u2013{e:03d}")
    return ", ".join(parts)


def main(argv: list[str]) -> int:
    dry = "--dry-run" in argv
    force = "-f" in argv or "--force" in argv

    print(f"Audio dir    : {AUDIO_DIR}")
    print(f"Output dir   : {DOCS_DIR}")
    print(f"Output pattern: thinking_agent.v8.partNN.mp3  (NN=01..12)")
    if dry:
        print("Mode         : DRY RUN (no write, just check sources)")
    print()

    if not AUDIO_DIR.is_dir():
        print(f"[FATAL] AUDIO_DIR does not exist: {AUDIO_DIR}")
        print("        Run gen_book_tts_hk.py pointed at training_agent.v8.script.hk.txt first.")
        return 2

    all_ok, found, missing = dry_run_check_sources()

    # Print per-part table
    w = 68
    print("=" * (w + 30))
    print(f"| {'Part':<{w}s} | {'#src':>5s} | {'Range (section NNN.mp3)':<22s} | {'Status':<8s} |")
    print("=" * (w + 30))
    tot_src = 0
    for lp, runs in PART_RANGES:
        name = PART_NAMES[lp - 1][:w]
        cnt = sum(1 + e - s for s, e in runs)
        tot_src += cnt
        miss_cnt = len(missing.get(lp, []))
        status = "OK" if miss_cnt == 0 else f"MISS {miss_cnt}"
        print(f"| LP{lp:02d} {name:<{w-5}s} | {cnt:>5d} | {fmt_ranges(runs):<22s} | {status:<8s} |")
    print("=" * (w + 30))
    print(f"Total section mp3 required: {tot_src}  expected under: {AUDIO_DIR}")
    print()

    if missing:
        n_miss = sum(len(v) for v in missing.values())
        print(f"[WARN] {n_miss} section file(s) missing — cannot concat parts listed above as 'MISS N'.")
        print("       First 30 missing per part:")
        for lp, nums in sorted(missing.items()):
            show = ", ".join(f"{n:03d}" for n in nums[:30])
            tail = f" (+{len(nums)-30} more)" if len(nums) > 30 else ""
            print(f"       LP{lp:02d}: section_[{show}].mp3{tail}")
        if not force:
            print("\nTip: run gen_book_tts_hk.py against training_agent.v8.script.hk.txt to generate missing sections.")
            print("     Pass --force to try concat anyway with whatever exists (silent gaps at missing runs).")
            if dry:
                return 0
            return 1

    if dry:
        print("[DRY RUN] Sources OK — re-run without --dry-run to concatenate.")
        return 0

    # Concatenate each part
    written: list[tuple[int, Path, int, int]] = []  # lp, out_path, total_bytes, n_files
    for lp, runs in PART_RANGES:
        out = DOCS_DIR / OUT_TEMPLATE.format(nn=f"{lp:02d}")
        sources = [AUDIO_DIR / SECTION_TEMPLATE.format(nnn=n) for n in list_ranges(runs)]
        # Filter missing if --force (but warn)
        present = [p for p in sources if p.is_file()]
        if len(present) != len(sources):
            print(f"[LP{lp:02d}] WARNING: only {len(present)}/{len(sources)} present, concatenating with gaps.")
        if not present:
            print(f"[LP{lp:02d}] SKIP — zero sources present.")
            continue
        nbytes = concat_mp3_files(present, out)
        written.append((lp, out, nbytes, len(present)))

    # Summary
    print()
    print("=" * 90)
    print(f"| {'Part':<30s} | {'Files':>6s} | {'Output file':<46s} | {'Size':>12s} |")
    print("=" * 90)
    total_bytes = 0
    for lp, out, nb, nf in written:
        mb = nb / (1024 * 1024)
        print(f"| {PART_NAMES[lp-1][:28]:<30s} | {nf:>6d} | {out.name:<46s} | {mb:>9.2f} MiB |")
        total_bytes += nb
    print("=" * 90)
    print(f"Total: {sum(w[3] for w in written)} parts written, {total_bytes/(1024*1024):.2f} MiB combined, in {DOCS_DIR}")
    print()
    print("Note: naming request 'N=0..9' is covered by part01.mp3..part09.mp3; part10..12 are produced alongside.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
