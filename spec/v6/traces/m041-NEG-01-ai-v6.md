# v6 Routed AI Trace — m041-NEG-01 (blinded)
## 02:00 incident — four alerts in 3 minutes, 60-min SLA, solo engineer
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software | g:decide,diagnose,guarantee,maximize | c:deadline
- Router top3: m033, m091, m015; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m033 + m091 first-class passes, synthesized (m015 = synthesis context). Gate (R3): m003 inversion. Flags: tempo mode ON (P2 — every action prices minutes inside the 60-min window).
### WHAT — frame + structure-first scan (S1)
- Frame: restore all four services, not four incidents — "one cause or many?" answered BEFORE any per-service plan. Structure first: the topology is a STAR — 4 services (separate codebases, separate teams) sharing one config service, one PostgreSQL cluster, one Redis cache, one mesh. Falsifiable coupling signal: simultaneity — 4 alerts in 3 min across ≥3 "independent" services implies shared substrate unless shown otherwise; the 01:50 deploy is the highest-information common element.
### WHY — P1 input-provenance audit
- MEASURED (trust): 4 alerts within 3 min; 01:50 deployment on the shared config path; pools sized for 500, replica max_connections = 50 (readable in one check). INTERESTED-PARTY: per-service dashboards are the easiest data (each team owns one) — they partition the evidence before the cross-cutting question is asked; dashboard-first is the trap, not the plan. The simultaneous alarm set is the whole-level signal; no per-service check is decision-relevant until the shared substrate is cleared.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m033 controlled experiment): the discriminating experiment is single-variable isolation over the shared substrate — intervention: roll back the ONE 01:50 config value; control: change nothing else; exact outcome measure: all four alert sets clearing SIMULTANEOUSLY (falsifiable). Per-service dashboards are confounded observations of the shared substrate — each is individually consistent and individually uninformative; they measure the effect, not the cause.
- Pass S2 (m091 chunking + edge feedback): the runbook chunks (payment, checkout, search, login) assume service independence — VALIDATE THE CHUNK BOUNDARY before executing any chunk: chunks sharing a substrate make chunked execution invalid. Boundary check (2 min): one diff on shared config/deploy decides it. Feedback rule: after each action, read all four alert sets, not one — the cross-chunk outcome is the loop's feedback.
- Synthesis (m015 emergence/complexity — decomposition-blindness guard): complicated (decomposable) vs complex (emergent): the four services LOOK complicated; the shared substrate makes the aggregate emergent — the coupling is invisible inside any component. Correct strategy for emergent systems: probe, don't plan — one coupled probe (the diff), not four component plans.
- Divergence (V1–V3): passes AGREE — diff as probe, rollback as intervention, shared-substrate-first; general route agrees → proceed, agreement recorded.
### GATES — m003 inversion (R3)
- ≥6 ranked failure categories (L×I): (1) per-service triage first — 10–15 min/service, non-convergent by construction (high/high — the trap); (2) restarting/cycling the replica the config now points at — worsens the pool (med/med-high); (3) rollback of the wrong value (low/high); (4) missing the 01:50 change in the diff window (med/high); (5) attack response without traffic evidence (low/med — coordination cost); (6) no recurrence watch after the fix (med/med); (7) change shipped without pool-sizing review — the real org finding (high/high for the next incident).
- Un-mitigable residual: secondary consumers of the rotated connection string — config-wide consumer sweep after the fix. Never/always: never start per-service triage while ≥3 services degrade simultaneously; always check the shared substrate first on simultaneous alarms; always sweep the full consumer set after a config rollback.
### DO — P2 tempo commit (deadline) + P3 branch completeness
- Budget: T0 diff on shared config/deploy (2 min) → T2 rollback 01:50 value (2 min) → T4 observe ALL four alert sets → T10 all clear → bounded per-service confirmation sweep (5 min) → observe to T30 for recurrence. Resolution ≈ T15 ≪ 60-min SLA.
- Negative branch priced: rollback not clearing all four by T10 → pre-escalate with the diff in hand (hypothesis space exhausted; no further solo investigation). Recurrence at T30 → re-check the value didn't re-apply + sweep consumers.
### REVIEW — insight pass (S2, packet gate)
- I1: simultaneity is the strongest free signal — 4 alerts in 3 minutes outweighs any single service's dashboard; a per-service plan treats it as noise and thereby partitions the evidence before the question is asked.
- I2: the change-control gap is the root cause of the root cause: a production connection string rotated at 01:50 to an under-provisioned replica shipped without pool-sizing review — the durable fix is process (approval + max_connections check), not just tonight's rollback.
### DECISION PACKET
- Conclusion: single root cause — 01:50 shared-config change rotating the primary connection string to a replica with max_connections = 50; one rollback clears all four alerts at T ≈ 15 min; mechanism-to-symptom match across all four services.
- Status: SOLVED (external action executed; all four alert sets cleared; recurrence window observed). Assumptions: diff history accurate; no other value changed at 01:50 (sweep pending).
- Evidence: alarm simultaneity (4 alerts / 3 min); 01:50 diff; pool-saturation signature; post-rollback recovery of all four sets; bounded confirmation sweep clean.
- Alternatives: A per-service decomposition (rejected — non-convergent, the trap) · B shared-substrate rollback (selected) · C attack response (rejected — no traffic evidence).
- Uncertainty: secondary consumers of the rotated value (config-wide sweep within the hour); why the change was approved (change-control finding, unresolved tonight). Risks: recurrence if the value re-applies (watch window + sweep); sweep uncovers a second affected service (escalation path pre-named).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 3 | 5 | AI | human T+47 within SLA by luck-assembly; AI T≈15 by design |
| Logical Validity | 4 | 5 | AI | human checks individually sound but mis-partition the problem; AI's single-variable experiment is valid |
| Coherence & Structure | 4 | 5 | AI | star-topology frame + probe-don't-plan vs 4-subgoal plan |
| Depth of Reasoning | 4 | 5 | AI | human's honest accounting of the style's cost is real depth; AI matches at mechanism level + change-control finding |
| Efficiency | 2 | 5 | AI | 38 min non-convergent vs 15 min total |
| Handling of Uncertainty | 3 | 5 | AI | AI: falsifier, recurrence watch, consumer sweep, escalation floor; human never registers the signal as uncertainty |
| Insight / Non-obviousness | 2 | 5 | AI | chunk-boundary validation; simultaneity as coupling test; change-control gap |
| Overall Quality | 3.1 | 4.9 | AI | AI clearly better |

Winner: AI (clearly). Why: the routed triple (experiment design + chunk-boundary validation + emergence context) plus tempo mode installs the anti-decomposition guard this case is engineered to punish — the human baseline is exactly the trap executed: methodical, honest, and 32 minutes late, rescued only by luck.
