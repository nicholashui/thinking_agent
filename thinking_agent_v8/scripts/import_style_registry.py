#!/usr/bin/env python3
"""Import the 104-model registry + routing records into data/ (Phase 0 asset import).

Reads from the frozen spec assets (../../spec/) and writes:
  data/human_thinking_models.json          — 104 models
  data/routing_records/measured_records.jsonl — 212 measured (case_verdicts.csv)
  data/routing_records/design_records.jsonl   — 4 DESIGN counter records
"""

import csv
import io
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT.parent / "spec"  # thinking_agent/spec

DATA = ROOT / "data"
RECORDS = DATA / "routing_records"
RECORDS.mkdir(parents=True, exist_ok=True)


def import_registry() -> None:
    src = json.load(io.open(SPEC / "human_thinking_models.json", encoding="utf-8"))
    models = src["models"] if isinstance(src, list) else src.get("models", [])
    assert len(models) == 104, f"expected 104 models, got {len(models)}"
    assert len({m["id"] for m in models}) == 104, "duplicate model ids"

    # merge learned triggers + rates from the routing KB (style_routing_kb.json)
    kb = json.load(io.open(SPEC / "style_routing_kb.json", encoding="utf-8"))
    kb_models = {m["id"]: m for m in kb.get("models", [])}
    for m in models:
        kb_m = kb_models.get(m["id"], {})
        triggers = kb_m.get("triggers") or {}
        flat = [str(t) for group in ("domains", "goals", "context")
                for t in (triggers.get(group) or [])]
        m["triggers"] = flat
        if kb_m.get("pos_win_rate") is not None:
            m["pos_win_rate"] = kb_m["pos_win_rate"]
        if kb_m.get("neg_failure_rate") is not None:
            m["neg_failure_rate"] = kb_m["neg_failure_rate"]
    (DATA / "human_thinking_models.json").write_text(
        json.dumps(src, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"registry imported: {len(models)} models (with KB triggers + rates)")


def import_measured_records() -> None:
    rows = list(csv.DictReader(io.open(SPEC / "v5" / "case_verdicts.csv", encoding="utf-8")))
    out = []
    for r in rows:
        out.append({
            "record_id": r["test_case_id"],
            "human_model": r["human_model"],
            "case_type": r["case_type"].upper(),
            "outcome": r["verdict"],
            "human_overall": float(r["human_overall"]) if r.get("human_overall") else None,
            "ai_overall": float(r["ai_overall"]) if r.get("ai_overall") else None,
            "strategy_lesson": (r.get("reason") or "").strip()[:600],
            "evidence_status": "MEASURED",
        })
    assert len(out) == 212, f"expected 212 measured records, got {len(out)}"
    with io.open(RECORDS / "measured_records.jsonl", "w", encoding="utf-8") as f:
        for rec in out:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"measured records imported: {len(out)}")


DESIGN_RECORDS = [
    ("m101-POS-01", "M101 Solo-Contract Bayesian Precision (counter)", "POS",
     "d:medical,science g:diagnose,predict"),
    ("m102-NEG-01", "M102 Likelihood-Audit Gatekeeper (counter)", "NEG",
     "d:engineering,finance,medical,strategy g:decide,estimate,guarantee,maximize,predict c:adversarial,unmeasured"),
    ("m103-POS-01", "M103 Sequential Constraint Engine (counter)", "POS",
     "d:engineering,finance,medical,organization,science,security g:estimate,guarantee,maximize,predict c:deadline"),
    ("m104-POS-01", "M104 Dynamic Five-Forces Verdict (counter)", "POS",
     "d:engineering,finance,medical,organization,security,software,strategy,supply g:decide,estimate"),
]


def import_design_records() -> None:
    out = []
    for rid, model, ctype, sig in DESIGN_RECORDS:
        out.append({
            "record_id": rid, "human_model": model, "case_type": ctype,
            "outcome": "design-ai", "signature_text": sig,
            "strategy_lesson": "Counter-design prediction; advisory only (invariant 12).",
            "evidence_status": "DESIGN",
        })
    with io.open(RECORDS / "design_records.jsonl", "w", encoding="utf-8") as f:
        for rec in out:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"design records imported: {len(out)} (DESIGN — never aggregate into rates)")


if __name__ == "__main__":
    import_registry()
    import_measured_records()
    import_design_records()
    print("total routing records: 216 (212 MEASURED + 4 DESIGN)")
