#!/usr/bin/env python3
"""Generate the four counter-design router records (M101-M104) appended to the
v7 router configuration (216 = 212 historical + 4 counter records).

Each record is a DESIGN PREDICTION (marked `design-ai`), not a measurement:
the expected outcome of the counter-model on the v6 residual-loss case it was
built to close. Per invariant 12, design records never enter the learned KB
until a judge verdict measures them.

Output: validation/counter_records.md (appended to router_config_table.md by
assemble_v7.py)."""
import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (record_id, model_label, case_type, signature, expected, lesson, artifacts)
RECORDS = [
    ("m101-POS-01", "M101 Solo-Contract Bayesian Precision (counter)", "POS",
     "d:medical,science g:diagnose,predict",
     "design-ai (exp 5.0/5.0)",
     "Counter to the 5.0 style-pure baseline (m006-POS-02, efficiency-only loss). One-pass "
     "update with contracts inlined; winning moves: independence bounds (without the "
     "assumption the posterior spans [13.2%, 100%]; independence narrows it to 60.7% — "
     "~47 points of assumption load); flip prior 1/154; B- branch 1/34 ≈ 2.9%.",
     "`v5/test_cases/m006-POS-02.md` · `v5/traces/m006-POS-02-human.md / "
     "v6/traces/m006-POS-02-ai-v6.md` · `v6/learning_signals_raw/m006.json` · "
     "`extra_model.md III.2.2`"),
    ("m102-NEG-01", "M102 Likelihood-Audit Gatekeeper (counter)", "NEG",
     "d:engineering,finance,medical,strategy g:decide,estimate,guarantee,maximize,predict "
     "c:adversarial,unmeasured",
     "design-ai (exp 5.0/5.0)",
     "Counter to the 5.0 style-pure baseline (m006-NEG-02, the only NEG loss; "
     "efficiency-only, protective verdict held). Audit-before-update in one pass: "
     "specificity floor 92.1% (no sensitivity claim can justify treatment below it); "
     "credence demand (95/95 clears the 40% threshold, 90/90 does not); SAE ledger "
     "76 healthy vs 4 diseased per 1000 treated.",
     "`v5/test_cases/m006-NEG-02.md` · `v5/traces/m006-NEG-02-human.md / "
     "v6/traces/m006-NEG-02-ai-v6.md` · `v6/learning_signals_raw/m006.json` · "
     "`extra_model.md III.2.3`"),
    ("m103-POS-01", "M103 Sequential Constraint Engine (counter)", "POS",
     "d:engineering,finance,medical,organization,science,security "
     "g:estimate,guarantee,maximize,predict c:deadline",
     "design-ai (exp 5.0/5.0)",
     "Counter to the 5.0 style-pure baseline (m014-POS-01, J1-contested efficiency "
     "loss). Tie-lock + forced lift chain: post-A S2=S3=100; 110 hr ⟺ B+C $750k, "
     "120 hr ⟺ B+C+D $1.05M, 140 hr ⟺ B+C+D+E $1.17M; B dominated as first move, "
     "indispensable as second. Bundle-interpretation priced ($1.17M = B+C+D+E → 140/hr).",
     "`v5/test_cases/m014-POS-01.md` · `v5/traces/m014-POS-01-human.md / "
     "v6/traces/m014-POS-01-ai-v6.md` · `v6/learning_signals_raw/m014.json` · "
     "`extra_model.md III.2.4`"),
    ("m104-POS-01", "M104 Dynamic Five-Forces Verdict (counter)", "POS",
     "d:engineering,finance,medical,organization,security,software,strategy,supply "
     "g:decide,estimate",
     "design-ai (exp 5.0/5.0)",
     "Counter to the 5.0 style-pure baseline (m071-POS-01, routing-defect loss: m071 "
     "routed 3rd, enumeration diluted). Five forces first-class in one pass (rule 40) "
     "+ direction-robust verdict (every force adverse or worsening) + adverse "
     "selection at the auction (no cost advantage selects the contracts you win) "
     "+ redeploy priced by opportunity cost.",
     "`v5/test_cases/m071-POS-01.md` · `v5/traces/m071-POS-01-human.md / "
     "v6/traces/m071-POS-01-ai-v6.md` · `v6/learning_signals_raw/m071.json` · "
     "`extra_model.md III.2.5`"),
]

rows = []
for rid, model, ctype, sig, outcome, lesson, refs in RECORDS:
    rows.append(f"| {rid} | {model} | {ctype} | {sig} | {outcome} | {lesson} | {refs} |")

out = "\n".join(rows) + "\n"
out += ("\n*Counter-design records: expected outcomes (exp), not measurements — "
        "they become learned KB entries only after judge verdicts (invariant 12). "
        "Generated from extra_model.md by validation/gen_counter_records.py.*\n")
io.open(os.path.join(ROOT, "validation", "counter_records.md"), "w",
        encoding="utf-8").write(out)
print("counter records:", len(RECORDS))
