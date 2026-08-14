<!-- ============================================================
  LP06 — Stage 3/4: HOW + DO (Generate/Test/Select → Plan/Execute)
  Source file: thinking_agent.v8.md  (split part 06/12)
  ============================================================ -->
## 12. Stage 3 — HOW: Generate, Test, and Select Solutions

*(§12.1–12.8 per v4, plus:)*

- **Pre-DO checks on the SELECTED decision (V14):** the class bar is checked against the chosen candidate's verifier reliability — not the candidate-set max — and the identity-registry second-verifier rule is enforced **before any execution** (V4, §32 S39: single-identity A4 escalates with zero executor calls).
- **L3 at attest time (V5):** for external tasks, verifier outage with an attested A3+ class terminates with `ESCALATED` (no external action, `required_human_actions` populated) — reachable, keyed on the attested class, scenario-validated (S29).
- **Progress gating (C9, extended):** premortem and red team run only on new candidate content; the planner builds **once per decision** (V7); the outcome verification is **delta-cached** on the state hash (V7, C26/C32 extended) — identical verdicts are never re-paid.
- **Invariant 8 (V8):** the attestation denies any `REPLICATE`-class action (S44).

***

## 13. Stage 4 — DO: Plan and Execute

*(§13.1–13.7 per v4, plus:)*

- **PENDING kernel allowlist, no backdoor (V3):** `safety_kernel.allowed_subset` returns only tasks whose ids are in the kernel's static table **and** whose classes the kernel's own taxonomy assigns as A2 — the v4 `allowlist_hint` fallback is deleted. §32 S20 (listed task executes) and S38 (unlisted task is NOT executed) are the positive and negative cases.
- **Plan termination conditions** (stop → plan-failure terminal; escalation → ESCALATED) consumed per pass (C16).
- **Crash/resume** with idempotency keys (S21); the integrity boundary (HMAC/key management) remains Phase-1, disclosed (§32.4).

***

