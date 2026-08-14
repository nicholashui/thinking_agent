#!/usr/bin/env python3
"""Assemble thinking_agent.v8.md = Part I (v7 verbatim, header transformed)
+ Part II (the v8 Self-Directed Learning layer, part2_v8.md).

NO V7 CONTENT IS TOUCHED: the only differences between thinking_agent.v7.md
and the v8 Part I body are the four lineage metadata spans (version line,
change-policy paragraph, Part I divider heading, Part I divider italic).
The assembler VERIFIES this: a difflib pass over original vs transformed
fails unless every differing line belongs to one of the four spans."""
import difflib, io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

v7 = io.open(os.path.join(ROOT, "thinking_agent.v7.md"), encoding="utf-8").read()
part2 = io.open(os.path.join(ROOT, "part2_v8.md"), encoding="utf-8").read()

# --- the lineage metadata transforms (nothing else may change) ---
# (the change-policy PARAGRAPH is replaced as a span below; the anchor
# replacement here is NOT performed — the paragraph swap subsumes it)
TRANSFORMS = [
    ("**Version:** 7.0", "**Version:** 8.0"),
    ("# Part I — The v6 Specification (verbatim)",
     "# Part I — The v7 Specification (verbatim)"),
    ("*Part I is the complete v6 document, included unchanged so that v7 "
     "contains all of v6. Part II overrides where noted.*",
     "*Part I is the complete v7 document, included unchanged so that v8 "
     "contains all of v7. Part II overrides where noted.*"),
]

# The v7 change-policy paragraph is long; replace its body between the
# "v7 supersedes v6" anchor and the closing "`v6/`." marker.
POLICY_ANCHOR_END = "`v6/`."
old_policy_start = v7.index("**Change policy:** v7 supersedes v6")
old_policy_end = v7.index(POLICY_ANCHOR_END, old_policy_start) + len(POLICY_ANCHOR_END)
new_policy = ("**Change policy:** v8 supersedes v7 and is SELF-CONTAINED BY "
              "CONSTRUCTION. Part I is the complete v7 specification, verbatim "
              "(all v5 + v6 + v7 sections), including the INSTANTIATED ROUTER "
              "CONFIGURATION — 212 historical strategy references (§II.2.6) "
              "plus the four counter-design records (§III.3). Part II is the "
              "complete v8 SELF-DIRECTED LEARNING (SDL) layer: the "
              "challenge-discovery tool (arXiv/internet scan), the gap-map "
              "curriculum planner, the learning ledger with its periodic "
              "review cycle, and the SDL governance (invariants 13–14, rules "
              "42–48) — so the agent not only routes dynamically to the best "
              "human thinking model for any situation, but plans its own "
              "learning: it discovers challenge classes it has not met, "
              "selects the ones its gap map says it is weakest at, practices "
              "them under judge verdicts, and reviews its own learning "
              "history on a standing cadence. No external document is "
              "required (companion files: `extra_model.md`, "
              "`validation/v8_research_report.md`). Companion executable "
              "artifacts: `validation/harness.py`, `validation/style_router.py`, "
              "`human_thinking_models.json`, `style_routing_kb.json`, "
              "`v5/test_cases/`, `v5/traces/`, `v6/` (the `v7/` regression corpus "
              "is pending measurement).")
transformed = v7[:old_policy_start] + new_policy + v7[old_policy_end:]

for old, new in TRANSFORMS:
    cnt = transformed.count(old)
    assert cnt == 1, f"anchor not unique or missing ({cnt}x): {old[:60]}..."
    transformed = transformed.replace(old, new, 1)

# --- no-touch guarantee: difflib over the transformed body ---
orig_lines, new_lines = v7.splitlines(), transformed.splitlines()
allowed = [old.split(" ")[-1].rstrip(".") for old, _ in TRANSFORMS]  # rough tokens
sm = difflib.SequenceMatcher(None, orig_lines, new_lines)
changed_lines = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal":
        changed_lines.extend(new_lines[j1:j2])
        changed_lines.extend(orig_lines[i1:i2])
for ln in changed_lines:
    if not ln.strip():          # whitespace-only lines inside replaced spans
        continue
    if ("Version:" in ln or "Change policy:" in ln or
            "Part I — The v" in ln or "included unchanged so that v" in ln):
        continue
    sys.exit(f"NO-TOUCH VIOLATION: unexpected change near: {ln[:100]}")
print("no-touch guarantee OK: only lineage metadata differs (",
      len([l for l in changed_lines if l.strip()]), "changed lines)")

# --- strip the final End-of-document marker from the v7 body; re-append ---
assert transformed.rstrip().endswith("*End of document.*")
body = transformed.rstrip()[: -len("*End of document.*")].rstrip()

doc = body + "\n\n" + part2.rstrip() + "\n\n---\n\n*End of document.*\n"

out = os.path.join(ROOT, "thinking_agent.v8.md")
io.open(out, "w", encoding="utf-8").write(doc)
print("v8 assembled:", len(doc.splitlines()), "lines")
