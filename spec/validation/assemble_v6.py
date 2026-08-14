#!/usr/bin/env python3
"""Assemble thinking_agent.v6.md = Part I (v5 verbatim) + Part II (v6 layer,
with the router configuration table inlined at the marker)."""
import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

v5 = io.open(os.path.join(ROOT, "thinking_agent.v5.md"), encoding="utf-8").read()
part2 = io.open(os.path.join(ROOT, "part2_v6.md"), encoding="utf-8").read()
config = io.open(os.path.join(ROOT, "validation", "router_config_table.md"),
                 encoding="utf-8").read().rstrip()

# --- header transform ---
v5 = v5.replace("**Version:** 5.0  ", "**Version:** 6.0  ", 1)
v5 = v5.replace(
    "**Change policy:** v5 supersedes v4. The differential change log in §31 records every accepted finding from the v4 self-review, the v5 change, and its validation status. The executable validation harness lives in `validation/harness.py`; results are in §32.",
    "**Change policy:** v6 supersedes v5 and is SELF-CONTAINED BY CONSTRUCTION. "
    "Part I is the complete v5 specification, verbatim (all 33 sections). "
    "Part II is the complete v6 self-curriculum layer, including the INSTANTIATED "
    "ROUTER CONFIGURATION — all 212 historical strategy references (§II.2.6) with "
    "situation signatures, routed styles, historical outcomes, lessons, and "
    "artifact references — so the agent routes dynamically to the best human "
    "thinking model for any situation from recorded success/failure evidence. "
    "No external document is required. Companion executable artifacts: "
    "`validation/harness.py`, `validation/style_router.py`, "
    "`human_thinking_models.json`, `style_routing_kb.json`, `test_cases/`, `traces/`.",
    1)

# --- inline the config table at the marker ---
marker = "<!-- ROUTER_CONFIG_TABLE -->"
assert marker in part2, "marker missing from part2"
part2 = part2.replace(marker, config)

# --- assemble ---
divider1 = "\n\n---\n\n# Part I — The v5 Specification (verbatim)\n\n*Part I is the complete v5 document, included unchanged so that v6 contains all of v5. Part II overrides where noted.*\n\n"
first_hash = v5.index("# Thinking Agent")
subtitle_end = v5.index("\n\n", first_hash)
doc = (v5[:subtitle_end] + divider1 + v5[subtitle_end:] + "\n\n" + part2 +
       "\n\n---\n\n*End of document.*\n")

out = os.path.join(ROOT, "thinking_agent.v6.md")
io.open(out, "w", encoding="utf-8").write(doc)
print("v6 assembled:", len(doc.splitlines()), "lines")
