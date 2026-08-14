<!-- ============================================================
  LP07 — Stage 5: REVIEW + Continuous VERIFY Layer
  Source file: thinking_agent.v8.md  (split part 07/12)
  ============================================================ -->
## 14. Stage 5 — REVIEW: Reflect, Learn, and Evolve

*(AAR with in-loop review §14.1, single/double-loop §14.2–14.3, consolidation §14.4, Kaizen §14.5 per v4, plus:)*

- **Gated reviews (V7):** the in-loop review runs only on candidate/observation deltas; the epilogue review runs only when a decision was made, actions executed, or lessons are possible — classify-before-decision exits (S5/S6/S16/S25/S41/S42) no longer pay for reviews of nothing (C13's promise, restored; S29's L3 exit occurs after selection, so its epilogue review runs — 11 tokens include it).
- **Competence provenance gate (V2):** `competence_model.update` rejects calibration whose source is not kernel/EvaluationPlane; the accuracy comes from the **kernel domain-accuracy registry** (world facts), never from task-declared `calibration_accuracy`. §32 S45: a task declaring accuracy 1.0 is ignored; routing changes only on the kernel feed.
- **Minting (V1):** the procedural-write authorization is a world-facts policy decision, not a task flag; the positive commit path is scenario-validated (S33) and the negative quarantine path unchanged (S8).

***

## 15. Continuous VERIFY Layer

*(Registry §15.1 with the kernel calibration registry and identity-count second-verifier rule; no-verifier ladder §15.2 with all three levels executable (S25/S5/S29); packet §15.3; SOLVED threshold §15.4 — bars keyed by max(attested, declared) with unknown→A5, enforced pre-DO and at verify, second-verifier kernel-computed (V4); approximation §15.5; delta verification §15.6 — SHA-256 caches for candidates AND outcomes (V7).)*

***

