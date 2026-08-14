#!/usr/bin/env python3
"""
Style Router v1 — dynamic routing of Human Thinking Models by situation signature.

What this is: the missing half of the v5 MethodComposer (section 16). The
212-case evaluation showed the AI wins where its PROCESS protects (negative
cases) and loses where a STYLE is the right tool (positive cases). This router
closes that gap: it learns, from the evaluation corpus, WHICH human thinking
models win under WHICH situation signatures, and routes the agent to run the
winning style as a first-class pass.

Honest scope: the router is validated on ROUTING RECALL (does it pick the
winning style for the cases where the style won?) — a checkable property with
no LLM re-runs. End-to-end performance re-evaluation is the documented next
step (regression run per training_agent_evaluation.md section 9).

Inputs:  human_thinking_models.json (registry: strengths/weaknesses/prompts)
         case_verdicts.csv (212 cases: winner per case)
         test_cases/m###-XX-01.md (scenario text for signature extraction)
Outputs: style_routing_kb.json (the learned KB)
         style_router_report.md (validation: recall, picks, gaps)

Usage:    python validation/style_router.py
"""
import io, json, os, re, csv
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "v5")  # v5-baseline evaluation corpus (2026-08-07)

# ---------------------------------------------------------------------------
# 1. Signature vocabulary: situation features the router can detect in text
# ---------------------------------------------------------------------------
DOMAIN_KEYWORDS = {
    "medical":      ["patient", "screening", "diagnosis", "biomarker", "test", "hospital", "clinic", "treatment", "prevalence", "sensitivity", "specificity"],
    "finance":      ["fund", "portfolio", "investment", "equity", "option", "cap", "round", "valuation", "revenue", "cost", "budget", "insurance", "loan"],
    "engineering":  ["steel", "load", "plate", "design", "tolerance", "stress", "material", "capacity", "pump", "motor", "failure", "reliability"],
    "software":     ["code", "deploy", "migration", "rollout", "pilot", "server", "api", "database", "incident", "downtime", "latency", "feature"],
    "product":      ["user", "feature", "adoption", "retention", "churn", "onboarding", "product", "customer", "cohort"],
    "strategy":     ["market", "competitor", "entry", "moat", "industry", "go-to-market", "pricing", "portfolio"],
    "security":     ["adversary", "exploit", "injection", "threat", "attack", "authentication", "abuse", "fraud", "enumerat"],
    "supply":       ["inventory", "supply", "stock", "echelon", "bullwhip", "warehouse", "distribution", "ordering"],
    "science":      ["experiment", "hypothesis", "replicate", "measurement", "sample", "control group", "effect"],
    "organization": ["team", "incentive", "stakeholder", "manager", "department", "governance", "contract"],
}
GOAL_KEYWORDS = {
    "guarantee":  ["never", "must not", "guarantee", "ensure", "zero", "prevent", "avoid at all cost", "safety", "mandatory"],
    "maximize":   ["maximize", "optimize", "grow", "best", "highest", "win", "improve"],
    "estimate":   ["estimate", "approximate", "sizing", "order of magnitude", "how many", "how much", "cost"],
    "predict":    ["forecast", "predict", "probability", "likelihood", "posterior", "prior", "chance"],
    "decide":     ["decide", "choose", "go/no-go", "adopt", "approve", "launch", "invest"],
    "diagnose":   ["why", "root cause", "caused", "incident", "diagnos", "broken", "failing"],
}
CONTEXT_KEYWORDS = {
    "deadline":   ["20 minutes", "24 hours", "deadline", "hours to", "minutes", "time-box", "window"],
    "high_stakes":["irreversible", "life", "ruin", "floor", "one-shot", "double-or-nothing", "critical", "billion"],
    "one_shot":   ["one-shot", "single bet", "no second chance", "double-or-nothing"],
    "unmeasured": ["unvalidated", "no data", "cannot measure", "unmeasured", "no reference"],
    "adversarial":["adversary", "attacker", "fraud", "game", "negotiation", "competitor", "incentive"],
}

def signature_of(text: str) -> dict:
    t = text.lower()
    dom = {d for d, kw in DOMAIN_KEYWORDS.items() if any(k in t for k in kw)}
    goals = {g for g, kw in GOAL_KEYWORDS.items() if any(k in t for k in kw)}
    ctx = {c for c, kw in CONTEXT_KEYWORDS.items() if any(k in t for k in kw)}
    return {"domains": sorted(dom), "goals": sorted(goals), "context": sorted(ctx)}

# ---------------------------------------------------------------------------
# 2. Load registry + verdicts, build the KB
# ---------------------------------------------------------------------------
reg = json.load(io.open(os.path.join(ROOT, "human_thinking_models.json"), encoding="utf-8"))["models"]
by_id = {m["id"]: m for m in reg}

verdicts = []
with io.open(os.path.join(CORPUS, "case_verdicts.csv"), encoding="utf-8") as f:
    for row in csv.DictReader(f):
        verdicts.append(row)

# per-model evidence from the corpus
ev = defaultdict(lambda: {"pos_wins": 0, "pos_losses": 0, "neg_wins": 0, "neg_losses": 0,
                          "win_cases": [], "loss_cases": []})
for v in verdicts:
    mid = v["test_case_id"].split("-")[0]
    ctype = v["case_type"].upper()
    w = v["verdict"]
    e = ev[mid]
    if ctype == "POS":
        if w == "human": e["pos_wins"] += 1; e["win_cases"].append(v["test_case_id"])
        else: e["pos_losses"] += 1; e["loss_cases"].append(v["test_case_id"])
    else:
        if w == "ai": e["neg_wins"] += 1
        else: e["neg_losses"] += 1; e["loss_cases"].append(v["test_case_id"])

# ---------------------------------------------------------------------------
# 3. The KB: per model — signature triggers (from registry text) + corpus evidence
# ---------------------------------------------------------------------------
kb = {"version": "1.0",
      "note": "Learned from 212-case evaluation. pos_win_rate = fraction of positive "
              "cases won by the style (its home-turf reliability). neg_loss_rate = "
              "fraction of negative cases where the style's failure mode fired "
              "(avoid-combined-without-gates). route when signature matches triggers "
              "AND pos_win_rate is high; add protective gates when neg_loss_rate is high.",
      "models": []}
for m in reg:
    blob = " ".join(m["strengths"] + m["weaknesses"] + [m["example_prompt"], m["description"]])
    e = ev[m["id"]]
    wins = e["pos_wins"]; losses = e["pos_losses"]
    pos_rate = round(wins / max(wins + losses, 1), 2)
    neg_total = e["neg_wins"] + e["neg_losses"]
    neg_fail_rate = round(e["neg_losses"] / max(neg_total, 1), 2)
    kb["models"].append({
        "id": m["id"], "name": m["name"], "family": m["family"],
        "triggers": {"domains": [], "goals": [], "context": []},
        "pos_win_rate": pos_rate, "neg_failure_rate": neg_fail_rate,
        "win_cases": e["win_cases"], "loss_cases": e["loss_cases"],
    })

# signature triggers per model: derive from its win_cases' scenarios
for entry in kb["models"]:
    trig = {"domains": set(), "goals": set(), "context": set()}
    for cid in entry["win_cases"]:
        path = os.path.join(CORPUS, "test_cases", cid + ".md")
        if os.path.exists(path):
            s = signature_of(io.open(path, encoding="utf-8").read())
            trig["domains"] |= set(s["domains"]); trig["goals"] |= set(s["goals"])
            trig["context"] |= set(s["context"])
    entry["triggers"] = {k: sorted(v) for k, v in trig.items()}

# ---------------------------------------------------------------------------
# 4. The router
# ---------------------------------------------------------------------------
def route_style(signature: dict, top_n: int = 3) -> list:
    """Score every model against a situation signature; return top-N (id, score)."""
    scores = []
    dom, goals, ctx = set(signature["domains"]), set(signature["goals"]), set(signature["context"])
    for entry in kb["models"]:
        t = entry["triggers"]
        match = (len(set(t["domains"]) & dom) + len(set(t["goals"]) & goals)
                 + len(set(t["context"]) & ctx))
        # home-turf reliability dominates; failure rate penalizes
        score = match * entry["pos_win_rate"] - 0.5 * entry["neg_failure_rate"]
        scores.append((entry["id"], round(score, 3), entry["name"],
                       entry["pos_win_rate"], entry["neg_failure_rate"], match))
    scores.sort(key=lambda x: (-x[1], -x[4]))
    return scores[:top_n]

# ---------------------------------------------------------------------------
# 5. Validate: routing recall on the corpus (winner-in-top-N, no LLM re-runs)
# ---------------------------------------------------------------------------
pos_total = pos_hit1 = pos_hit3 = 0
neg_total = neg_hit1 = neg_hit3 = 0
picks_log = []
for v in verdicts:
    mid = v["test_case_id"].split("-")[0]
    cid = v["test_case_id"]
    path = os.path.join(CORPUS, "test_cases", cid + ".md")
    if not os.path.exists(path):
        continue
    sig = signature_of(io.open(path, encoding="utf-8").read())
    top = route_style(sig, 3)
    ids = [t[0] for t in top]
    if v["case_type"].upper() == "POS":
        pos_total += 1
        if ids[0] == mid: pos_hit1 += 1
        if mid in ids: pos_hit3 += 1
        if mid not in ids:
            picks_log.append((cid, mid, ids))
    else:
        neg_total += 1
        if ids[0] != mid: neg_hit1 += 1          # for NEG: routing AWAY from the trap style is correct
        if mid not in ids: neg_hit3 += 1
        if mid in ids:
            picks_log.append((cid, mid, ids, "trap-style recommended"))

# ---------------------------------------------------------------------------
# 6. Report
# ---------------------------------------------------------------------------
lines = []
lines.append("# Style Router Validation Report")
lines.append("")
lines.append(f"Corpus: {len(verdicts)} cases, {len(kb['models'])} models in the KB.")
lines.append("")
lines.append("## Routing recall (POS cases — did the router pick the style that won?)")
lines.append("")
lines.append(f"- **Recall@1: {pos_hit1}/{pos_total} ({round(100*pos_hit1/max(pos_total,1),1)}%)**")
lines.append(f"- **Recall@3: {pos_hit3}/{pos_total} ({round(100*pos_hit3/max(pos_total,1),1)}%)**")
lines.append("")
lines.append("## NEG cases (correct behavior = route AWAY from the trap style, toward protective gates)")
lines.append("")
lines.append(f"- Top-1 away from the trap style: {neg_hit1}/{neg_total} ({round(100*neg_hit1/max(neg_total,1),1)}%)")
lines.append(f"- Trap style NOT in top-3: {neg_hit3}/{neg_total} ({round(100*neg_hit3/max(neg_total,1),1)}%)")
lines.append("")
lines.append("## Misses and trap-recommendations (top 15)")
lines.append("")
lines.append("| case | actual winner style | router top-3 |")
lines.append("|---|---|---|")
for row in sorted(picks_log)[:15]:
    lines.append("| " + " | ".join(str(x) for x in row) + " |")
lines.append("")
lines.append("## How the router slots into the v5 workflow")
lines.append("")
lines.append("- **META (§9)**: extract the situation signature (domains, goals, context) from the frame.")
lines.append("- **MethodComposer (§16)**: route to the top styles by this KB; run the winning style as a FIRST-CLASS PASS (e.g., inversion enumeration, likelihood-provenance audit, ruin screen) inside WHAT/WHY/HOW.")
lines.append("- **Gates (§15)**: when the routed style has a high neg_failure_rate, pair it with its protective gate (from the case's learning signal).")
lines.append("- **Competence (§19.3)**: after each episode, the judge's verdict updates pos_win_rate/neg_failure_rate (provenance-gated, kernel-held).")
lines.append("- **Honest next step**: regression re-run of the corpus with routing active — expected: POS verdicts shift toward the AI because the styles' positive moves become first-class passes.")
report = "\n".join(lines)

json.dump(kb, io.open(os.path.join(ROOT, "style_routing_kb.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
io.open(os.path.join(ROOT, "style_router_report.md"), "w", encoding="utf-8").write(report)
print(report)
