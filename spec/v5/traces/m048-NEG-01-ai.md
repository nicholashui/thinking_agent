# AI Thinking Agent — Full Trace — m048-NEG-01
**BLINDED RUN: no model name or style description provided to the agent. Process: META → WHAT → WHY → HOW → DO → REVIEW + decision packet.**

## META (context / stakes / effort)
- Context: branch-level OOS on one SKU for 14 days; deficit ~360 units/day (~$650/day, ~$9k lost); demand flat 400/day; DC fill 99.7% and ships exactly what is ordered; store->DC lead 1 day, DC->supplier 3 days; manager's shift log: "milk out again by 11am — check reorder qty."
- Stakes: small but daily bleeding; a wrong program costs weeks and $; the fix should match the scale of the cause. Effort: this looks like a local anomaly — minutes, not a study. Mode: advisory + implementable fix.

## WHAT (frame + gate)
- Frame: anomaly diagnosis with a sharp onset window (14 days ago). First question is not "model the chain" but "what changed at the onset?" A 360/day deficit with flat demand and a full-fill DC can only mean the store's own ordering is suppressed — a changed setting, parameter, or rule.
- Gate: full chain modeling (lead-time statistics, safety-stock optimization, S&OP) is justified only if cheap checks cannot explain the deficit. Run the cheap checks first; escalate only on failure.

## WHY (hypotheses / evidence / falsification)
- H1 demand shift: falsified — POS flat 400/day for 3 months, no seasonality.
- H2 upstream shortfall: falsified — DC fill 99.7%, ships exactly what is ordered; every order of the last 14 days was filled.
- H3 store-side parameter/rule change at onset: confirmed — settings screen shows reorder qty 40 vs 400, changed 14 days ago; manager's log flagged "check reorder qty" on day 1; deficit 400 - 40 = 360/day matches the observed OOS exactly. Decisive.

## HOW (alternatives / verify / select)
- A) Full chain stock-flow model + reorder-point re-optimization + safety stock + S&OP program (3-4 weeks) — rejected: it optimizes a rule whose parameter is corrupted; no model run changes the 40; honest calibration would need "effective supply ~40/day," which is the parameter screen itself.
- B) Restore the parameter (5 minutes), monitor 3 days — selected: evidence-complete (onset window + log + exact arithmetic), zero cost, and itself the decisive test.
- C) DC/supplier joint project — rejected: no upstream evidence.
- Verify: after restoring 400, the next order is 400, stock rebuilds toward the reorder point, OOS ends within ~1 day. Also audit the rest of the settings screen (5 minutes) for other altered fields.

## DO (if external)
- Restore reorder qty to 400 per store procedure; audit the settings screen for other changes; notify the manager; monitor on-hand and OOS for 3 days.

## REVIEW (AAR)
- What worked: onset-window triage, two one-line falsifications, exact arithmetic match. What could go wrong: if OOS persisted after the restore, the boundary was pre-set — escalate to the chain model (lead-time variability, forecast error). Residual: why the parameter changed with no control — a 4-eyes rule on parameter edits is a follow-on process fix, not the fix.

## Decision packet
- Conclusion: restore the SKU's reorder quantity to 400. OOS was 100% caused by the parameter (40 vs 400) changed 14 days ago; deficit 360/day matches exactly; OOS ends within ~1 day of the restore.
- Status: SOLVED
- Assumptions: demand stays flat at 400/day; DC continues to fill fully; no other settings changed.
- Evidence: onset window + shift log; 99.7% DC fill; deficit = 400 - 40; exact match with observed OOS.
- Alternatives: A chain model + S&OP program (rejected: weeks, doesn't touch the parameter); B parameter restore (selected); C upstream project (rejected: no evidence).
- Uncertainty: if OOS persists >2 days post-restore, escalate to lead-time/variability analysis; re-check other parameters.
- Risks: repeated OOS loses customers; parameter edits without change control (process gap — follow-on fix).

---

## Comparison (provisional — m048-NEG-01)

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | Human fixes the wrong thing (3-4 week program); AI restores the parameter, OOS ends in a day |
| Logical Validity | 2 | 5 | AI | Human's model reproduces OOS only with "effective supply ~40/day" — the parameter it refused to read; AI's falsifications are one-line sound |
| Coherence & Structure | 3 | 5 | AI | Human's systemic narrative is internally coherent but detached from the window; AI's stages auditable |
| Depth of Reasoning | 3 | 4 | AI | Human's depth is misdirected (chain diagram, safety-stock math); AI deeper on the actual causal chain |
| Efficiency | 1 | 5 | AI | 3-4 weeks + data collection vs 5 minutes + 3-day monitor |
| Handling of Uncertainty | 2 | 4 | AI | Human requests data but validates nothing; AI pre-declares the escalation boundary |
| Insight / Non-obviousness | 2 | 4 | AI | Human misses the visible cause on the desk; AI reads the log and the settings screen |
| Overall Quality | 2 | 4.6 | AI | Same verdict as the m040-style negative case: the cheap decisive check outranks the deep model |

**Winner: AI (36/40 vs Human 16/40).** Overall judgment: *AI clearly better*. Key human gap: the pure style's data hunger and structural reflex turned a visible 5-minute parameter error into a systemic project; its own simulation would have re-derived the parameter from data it refused to read directly. The AI's cheap-checks-first triage found and fixed the cause in minutes.
