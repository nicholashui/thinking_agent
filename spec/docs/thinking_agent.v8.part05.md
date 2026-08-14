<!-- ============================================================
  LP05 — Stage 2: WHY (Diagnose & Model)
  Source file: thinking_agent.v8.md  (split part 05/12)
  ============================================================ -->
## 11. Stage 2 — WHY: Diagnose and Model

*(§11.1–11.6 per v4, plus:)*

- **Memory read-back (V6):** `memory_manager.retrieve` runs **before** hypothesis formation, queries task-derived terms (world `knowledge_terms`) plus the stored-knowledge store, and is **priced by result** — an empty retrieval is a deterministic no-op at 0 tokens; a hit costs 1 and extends evidence. §32 S40 demonstrates a genuine fill changing the outcome; S34's gap is filled by retrieval, not a flag (V11).
- **G-WHY gate fully evaluated and exercisable (V8):** predicates include falsification presence (G-WHY-5 — `no_falsification` blocks, S42) and VOI ≤ cost (G-WHY-4); failures clear hypotheses and re-enter, bounded by the gate budget (C15).

### 11.7 Exit gate and early classifier

```text
G-WHY-1  leading hypothesis has decision-relevant evidence
G-WHY-2  significant alternatives considered
G-WHY-3  residual uncertainty recorded
G-WHY-4  estimated VOI of further diagnosis ≤ cost
G-WHY-5  falsification_evidence non-empty
```

Early classifier entry after the gate when `missing_evidence` (unfillable), `probe_available`, or `verifier_outage` — with two refinements: a world-fillable gap is **actually filled by retrieval** (V11), and **external A3+ outage tasks proceed to attest time**, where L3 fires on the attested class (V5, §32 S29).

***

