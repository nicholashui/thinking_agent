<!-- ============================================================
  LP09 — Kernels: Safety + Self-Evolution + Evaluation
  Source file: thinking_agent.v8.md  (split part 09/12)
  ============================================================ -->
## 21. Safety and Alignment Kernel

*(Kernel position §21.1; invariants §21.2 — all ten mapped, invariant 8 now executable (V8/S44); threat model §21.3; human gates §21.4 — packet-before-approval, no auto-confirmation, corroboration; PENDING waits are progress-gated and exempt from the plateau (V8); wall-clock SLA enforcement is scheduler-held (design-level, disclosed).)*

***

## 22. Self-Evolution Engine

*(Levels §22.1; admission control §22.2 — canonical dedup hashes, global rate caps; pipeline §22.3 —* *`evaluate`* *invoked when the baseline is frozen, where* *`baseline_frozen`* *is a world fact (V1); stable baseline §22.4 inlined with the freeze procedure; Kaizen size §22.5; evaluation-plane immutability §22.6; cadence §22.7; open-ended improvement §22.8.)*

***

## 23. Evaluation Framework

*(Dimensions per v4; the 5-test MVP suite enumerated with its harness-assert mappings; routing-quality and co-scaling gate Phase-2, disclosed; telemetry §23.8 — per-stage audit records, latency timestamps design-level, disclosed; bookkeeping vs cognitive pricing reported at both levels, and bookkeeping totals now printed by the harness.)*

***

