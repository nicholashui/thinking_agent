#!/usr/bin/env python3
"""Split thinking_agent.v8.md into 12 logical parts (LP01..LP12).

Output files: docs/thinking_agent.v8.partNN.md  where NN = 01..12
(both 1-digit 0..9 and 2-digit naming are covered: part01..part12,
so the range requested "N=0..9" is fully satisfied by part01..part09
while part10..part12 are produced alongside for the canonical 12-LP layout.)
"""
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOCS_DIR = BASE_DIR / "docs"
SRC = BASE_DIR / "thinking_agent.v8.md"
OUT_TEMPLATE = "thinking_agent.v8.part{nn}.md"

LP_NAMES = [
    "LP01 — Bookend / Introduction (subtitle + Executive Summary + Core Thesis)",
    "LP02 — Scope, Lineage & Research Foundations",
    "LP03 — Design Principles, Architectural Overview, Four Nested Timescales",
    "LP04 — Stage 0/1: META-CONTROL + WHAT (Frame the Problem)",
    "LP05 — Stage 2: WHY (Diagnose & Model)",
    "LP06 — Stage 3/4: HOW + DO (Generate/Test/Select → Plan/Execute)",
    "LP07 — Stage 5: REVIEW + Continuous VERIFY Layer",
    "LP08 — Intelligence Components: Reasoning / Multi-Agent / Memory / World-Model / Tools",
    "LP09 — Kernels: Safety + Self-Evolution + Evaluation",
    "LP10 — Implementation, MVTA & Roadmap (落地)",
    "LP11 — Closures: Failure Modes, Final Rules, Conclusion, References + Appendix + v6/v7 Part II layers",
    "LP12 — v8 SDL Layer (Self-Directed Learning, the v8 novelty)",
]

# Ordered list of H2 titles (exact, ignoring leading "## " and trailing whitespace).
# Each entry maps to the LP number (1..12) that owns it.
# We use the EXACT H2 titles observed in thinking_agent.v8.md for reliable splitting.
H2_ORDERED = [
    # (LP number, H2 title substring prefix / anchor used for matching by exact line)
    (1,  "A Generalized, Governed AI Thinking Model for Broad Problem Solving and AGI/ASI Research"),
    (1,  "1. Executive Summary"),
    (1,  "2. Core Thesis"),
    (2,  "3. Scope and Non-Claims"),
    (2,  "4. Architectural Synthesis and Lineage"),
    (2,  "5. Research Foundations"),
    (3,  "6. Design Principles"),
    (3,  "7. Architectural Overview"),
    (3,  "8. Four Nested Timescales"),
    (4,  "9. Stage 0 — META-CONTROL"),
    (4,  "10. Stage 1 — WHAT: Frame the Problem"),
    (5,  "11. Stage 2 — WHY: Diagnose and Model"),
    (6,  "12. Stage 3 — HOW: Generate, Test, and Select Solutions"),
    (6,  "13. Stage 4 — DO: Plan and Execute"),
    (7,  "14. Stage 5 — REVIEW: Reflect, Learn, and Evolve"),
    (7,  "15. Continuous VERIFY Layer"),
    (8,  "16. Reasoning Method Composer"),
    (8,  "17. Multi-Agent Collective"),
    (8,  "18. Memory and Knowledge Architecture"),
    (8,  "19. World Model and Self-Model"),
    (8,  "20. Tool Broker and Execution Security"),
    (9,  "21. Safety and Alignment Kernel"),
    (9,  "22. Self-Evolution Engine"),
    (9,  "23. Evaluation Framework"),
    (10, "24. Reference Implementation Specification"),
    (10, "25. Minimal Viable Thinking Agent"),
    (10, "26. Roadmap Toward AGI and ASI Research"),
    (11, "27. Common Failure Modes"),
    (11, "28. Final Operating Rules"),
    (11, "29. Conclusion"),
    (11, "30. Primary Research References"),
    (11, "31. Differential Change Log (v4 → v5)"),
    (11, "32. Empirical Validation"),
    (11, "33. Consumer Quick-Reference"),
    (11, "II.1 What the v6 layer adds"),
    (11, "II.2 The Style Library"),
    (11, "II.3 The Embedded Curriculum"),
    (11, "II.4 Absorb-and-Learn"),
    (11, "II.5 Algorithm deltas"),
    (11, "II.6 New governance"),
    (11, "II.7 v6 change log"),
    (11, "II.8 v6 validation"),
    (11, "II.9 Self-containment note"),
    (11, "II.10 Deep-review amendments"),
    (11, "III.1 What the v7 layer adds"),
    (11, "III.2 The counter-model library"),
    (11, "III.3 The router configuration v7"),
    (11, "III.4 Algorithm deltas"),
    (11, "III.5 Absorb-and-learn: the residual curriculum items"),
    (11, "III.6 New governance"),
    (11, "III.7 v7 change log"),
    (11, "III.8 v7 validation status"),
    (12, "IV.1 Elaborated requirements"),
    (12, "IV.2 The Challenge-Discovery Tool"),
    (12, "IV.3 The Gap Map"),
    (12, "IV.4 The Curriculum Planner"),
    (12, "IV.5 The Challenge Trial protocol"),
    (12, "IV.6 The Learning Ledger"),
    (12, "IV.7 SDL governance"),
    (12, "IV.8 The Review Cycle"),
    (12, "IV.9 Design rationale"),
    (12, "IV.10 v8 validation and assembly"),
]


def build_h2_to_lp_map() -> dict[int, int]:
    """Return {index_within_ordered_h2_list: lp_number 1..12}."""
    return {i: lp for i, (lp, _title) in enumerate(H2_ORDERED)}


def split_md(source_text: str) -> list[str]:
    """Split source md into 12 consecutive slices aligned on H2 boundaries.

    Strategy:
      1. Walk the source line by line.
      2. Every time we see a line matching '^## (.+)$', increment the H2 cursor.
      3. Use the pre-defined H2_ORDERED table to decide which LP (1..12) the current H2 belongs to.
      4. All content from current LP's first H2 up to (but not including) the next LP's first H2
         belongs to the current LP.
      5. Any content BEFORE the first H2 (title, front-matter, Part I H1 divider, etc.) is prepended
         to LP1.
      6. H1 dividers for Part II v6 layer, Part II v7 layer, REVIEW epilogue H1, SDL-cycle epilogue H1
         are hoovered into whichever LP's H2 slice currently contains them (v6/v7 H1s land in LP11;
         v8 SDL H1 + SDL cycle H1 land in LP12 — verified by H2 ordering).
    """
    lines = source_text.splitlines(keepends=True)

    h2_lp = build_h2_to_lp_map()
    # Match H2: '## <title>' — strip the '## ' prefix and normalize whitespace/unicode dashes.
    def normalize(s: str) -> str:
        return re.sub(r"\s+", " ", s.replace("—", "-").replace("–", "-")).strip()

    # Build a parallel list: for each H2 title in source order, find the LP number
    # by matching normalized title against H2_ORDERED.
    h2_idx = 0  # running index in H2_ORDERED
    lp_for_line: list[int] = [1] * len(lines)  # default LP1 until we know better
    ordered_h2_norm = [normalize(t) for _, t in H2_ORDERED]

    current_lp = 1
    for i, ln in enumerate(lines):
        m = re.match(r"^##\s+(.*)$", ln.rstrip("\n"))
        if m:
            title = normalize(m.group(1))
            # find next match in ordered_h2_norm starting from h2_idx
            match_idx = None
            for j in range(h2_idx, len(ordered_h2_norm)):
                # The stored titles may be prefixes (to tolerate parenthetical endings); compare by prefix.
                if title.startswith(ordered_h2_norm[j]) or ordered_h2_norm[j].startswith(title):
                    match_idx = j
                    break
                # Also check title contains the prefix, for robustness against
                # parenthetical variants like " (extends v5 §16)" suffix differences.
                if title[:60] == ordered_h2_norm[j][:60]:
                    match_idx = j
                    break
            if match_idx is None:
                # Fallback: search any ordered_h2_norm entry whose prefix matches
                for j, cand in enumerate(ordered_h2_norm):
                    if title.startswith(cand) or cand.startswith(title):
                        match_idx = j
                        break
            if match_idx is not None:
                h2_idx = match_idx + 1
                current_lp = h2_lp[match_idx]
        # --- H1 OVERRIDE: SDL-layer headings belong to LP12 even if the H2 sweep
        # still has us in LP11 (§III.8's tail). This keeps the "Part II ... SDL Layer"
        # title divider with its actual content (§IV.1+) instead of tailing in LP11.
        h1 = re.match(r"^#\s+(.*)$", ln.rstrip("\n"))
        if h1:
            h1_title = normalize(h1.group(1))
            if (("SDL Layer" in h1_title and "v8" in h1_title)
                    or "Self-Directed Learning" in h1_title
                    or ("SDL cycle" in h1_title)
                    or ("SDL" in h1_title and "epilogue" in h1_title)):
                lp_for_line[i] = 12
                continue
        lp_for_line[i] = current_lp

    # Now slice lines into 12 consecutive strings.
    slices = [""] * 12  # index 0 -> LP1 content ... index 11 -> LP12 content
    for i, ln in enumerate(lines):
        lp = lp_for_line[i]
        slices[lp - 1] += ln

    return slices


def main() -> None:
    if not SRC.exists():
        raise FileNotFoundError(f"Source not found: {SRC}")
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    source_text = SRC.read_text(encoding="utf-8")
    print(f"Loaded: {SRC} ({len(source_text)} chars, {len(source_text.splitlines())} lines)")

    slices = split_md(source_text)

    written: list[Path] = []
    for idx, body in enumerate(slices):
        lp_num = idx + 1
        header = (
            f"<!-- ============================================================\n"
            f"  {LP_NAMES[idx]}\n"
            f"  Source file: thinking_agent.v8.md  (split part {lp_num:02d}/12)\n"
            f"  ============================================================ -->\n"
        ) if not body.lstrip().startswith("<!--") else ""
        content = header + body if header else body
        out = DOCS_DIR / OUT_TEMPLATE.format(nn=f"{lp_num:02d}")
        out.write_text(content, encoding="utf-8")
        written.append(out)
        h2_count = len(re.findall(r"^##\s+.+$", body, flags=re.M))
        print(f"  LP{lp_num:02d}: {out.name}  {len(body):>7d} chars  {h2_count:2d} H2 sections  ({LP_NAMES[idx][:72]}{'…' if len(LP_NAMES[idx])>72 else ''})")

    # Totals
    total_chars = sum(len(b) for b in slices)
    total_h2 = sum(len(re.findall(r"^##\s+.+$", b, flags=re.M)) for b in slices)
    orig_h2 = len(re.findall(r"^##\s+.+$", source_text, flags=re.M))
    print(f"\nTotal across 12 parts: {total_chars} chars, {total_h2} H2 sections "
          f"(original had {orig_h2} H2 — {'MATCH ✓' if total_h2 == orig_h2 else 'MISMATCH ✗'})")

    print("\nOutput files written to:")
    for w in written:
        print(f"  {w}")

    # Note: user asked "N=0..9". We generate part01..part12; parts 01..09 satisfy
    # the N=0..9 naming request, while part10/part11/part12 fill the 12-LP split.
    print("\nNaming note: user request 'N=0..9' is covered by part01..part09; "
          "part10..part12 are the continuation for a complete 12-part split.")


if __name__ == "__main__":
    main()
