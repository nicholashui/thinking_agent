#!/usr/bin/env python3
"""Generate the ROUTER CONFIGURATION for thinking_agent.v6.md — the 212
historical strategy references the router is built on and consults at runtime.

Each record: situation signature -> routed style(s) -> historical outcome
(human = the style that won, the strategy to adopt; ai = the protective
route the process machinery produced) -> strategy lesson -> artifacts.

Output: validation/router_config_table.md (inlined into §II.2.6 by
assemble_v6.py)."""
import io, os, csv, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from style_router import signature_of

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "v5")

rows = []
with io.open(os.path.join(CORPUS, "case_verdicts.csv"), encoding="utf-8") as f:
    for r in csv.DictReader(f):
        rows.append(r)

out = []
out.append("### II.2.6 The router configuration — 212 historical strategy references")
out.append("")
out.append("This is the instantiated router configuration: every historical episode the")
out.append("router was learned from and consults at runtime. Each record states the")
out.append("situation signature, the style(s) that succeeded or failed on it, the")
out.append("historical outcome (H = the human style won — the strategy to adopt;")
out.append("A = the AI protective route won — keep the gates), the strategy lesson,")
out.append("and the artifacts (scenario, traces, signals) that ground the record.")
out.append("")
out.append("| Record | Human Thinking Model | Type | Situation signature | Historical outcome (H/A) | Strategy lesson | Artifacts (scenario / traces / signals) |")
out.append("|---|---|---|---|---|---|---|")
for r in rows:
    cid = r["test_case_id"]
    mid = cid.split("-")[0]
    path = os.path.join(CORPUS, "test_cases", cid + ".md")
    sig = ""
    if os.path.exists(path):
        s = signature_of(io.open(path, encoding="utf-8").read())
        parts = []
        if s["domains"]: parts.append("d:" + ",".join(s["domains"]))
        if s["goals"]: parts.append("g:" + ",".join(s["goals"]))
        if s["context"]: parts.append("c:" + ",".join(s["context"]))
        sig = " ".join(parts)
    winner = r["verdict"]
    h, a = r.get("human_overall", ""), r.get("ai_overall", "")
    lesson = (r.get("reason") or "").strip().replace("|", "/")
    refs = (f"test_cases/{cid}.md",
            f"traces/{cid}-human.md / traces/{cid}-ai.md",
            f"learning_signals_raw/{mid}.json")
    out.append(f"| {cid} | {r['human_model']} | {r['case_type'].upper()} | {sig} | "
               f"{winner} ({h}/{a}) | {lesson[:100]} | "
               f"`{refs[0]}` · `{refs[1]}` · `{refs[2]}` |")

out.append("")
out.append("*Generated from case_verdicts.csv + test_cases/ by validation/gen_router_config.py "
           "— re-run to regenerate after any curriculum update.*")
io.open(os.path.join(ROOT, "validation", "router_config_table.md"), "w", encoding="utf-8").write("\n".join(out))
print("router config records:", len(rows))
