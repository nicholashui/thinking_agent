#!/usr/bin/env python3
"""Assemble thinking_agent.v7.md = Part I (v6 verbatim, header transformed)
+ Part II (the v7 residual-closure layer, part2_v7.md) with the router
configuration table (212 historical + 4 counter records) inlined at the
marker."""
import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

v6 = io.open(os.path.join(ROOT, "thinking_agent.v6.md"), encoding="utf-8").read()
part2 = io.open(os.path.join(ROOT, "part2_v7.md"), encoding="utf-8").read()
config = io.open(os.path.join(ROOT, "validation", "router_config_table.md"),
                 encoding="utf-8").read().rstrip()
counters = io.open(os.path.join(ROOT, "validation", "counter_records.md"),
                   encoding="utf-8").read().rstrip()

# --- header transforms ---
assert "**Version:** 6.0" in v6
v6 = v6.replace("**Version:** 6.0", "**Version:** 7.0", 1)

old_policy = ("**Change policy:** v6 supersedes v5 and is SELF-CONTAINED BY "
              "CONSTRUCTION.")
assert old_policy in v6
start = v6.index(old_policy)
end = v6.index("`v5/traces/`.", start) + len("`v5/traces/`.")
new_policy = ("**Change policy:** v7 supersedes v6 and is SELF-CONTAINED BY "
              "CONSTRUCTION. Part I is the complete v6 specification, verbatim "
              "(all v5 + v6 sections), including the INSTANTIATED ROUTER "
              "CONFIGURATION — 212 historical strategy references (§II.2.6). "
              "Part II is the complete v7 residual-closure layer: the four "
              "counter-models M101–M104 installed in the registry (now 104 "
              "models), the updated router configuration (216 records = 212 "
              "historical + 4 counter-design, §III.3), the solo-contract "
              "micro-route, the first-class-home-turf and interpretation-pricing "
              "rules, the efficiency floor, and the absorb-and-learn curriculum "
              "items — so the agent routes dynamically to the best human thinking "
              "model for any situation from recorded success/failure evidence "
              "and the counter-models that close the residual losses. No external "
              "document is required (companion detailed file: `extra_model.md`). "
              "Companion executable artifacts: `validation/harness.py`, "
              "`validation/style_router.py`, `validation/gen_router_config.py`, "
              "`validation/gen_counter_records.py`, `human_thinking_models.json`, "
              "`style_routing_kb.json`, `v5/test_cases/`, `v5/traces/`, `v6/`.")
v6 = v6[:start] + new_policy + v6[end:]

assert "# Part I — The v5 Specification (verbatim)" in v6
v6 = v6.replace("# Part I — The v5 Specification (verbatim)",
                "# Part I — The v6 Specification (verbatim)", 1)
old_div = ("*Part I is the complete v5 document, included unchanged so that v6 "
           "contains all of v5. Part II overrides where noted.*")
assert old_div in v6
v6 = v6.replace(old_div,
                "*Part I is the complete v6 document, included unchanged so that "
                "v7 contains all of v6. Part II overrides where noted.*", 1)

# --- inline the config table at the marker ---
marker = "<!-- ROUTER_CONFIG_TABLE -->"
assert marker in part2, "marker missing from part2_v7.md"
part2 = part2.replace(marker, config + "\n\n" + counters)

# --- assemble ---
doc = v6 + "\n\n" + part2 + "\n\n---\n\n*End of document.*\n"

out = os.path.join(ROOT, "thinking_agent.v7.md")
io.open(out, "w", encoding="utf-8").write(doc)
print("v7 assembled:", len(doc.splitlines()), "lines")
