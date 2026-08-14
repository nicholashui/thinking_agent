# v6 Routed AI Trace — m016-NEG-01 (blinded)
## eShop — checkout outage; live incident; ~$8K/min; committed action required in minutes
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software | g:decide,diagnose,estimate,maximize | c:deadline,high_stakes
- Router top3: m021, m084, m094; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m021 + m084 first-class passes, synthesized (m094 = synthesis context). Gate (R3): m007 ruin screen (high_stakes). Flags: tempo mode ON (P2 — cost-of-delay $8K/min, commit at DO); NO closed-scope fast path (root cause unconfirmed — not fully specified).
### WHAT — frame + structure-first scan (S1)
- Frame: committed action within minutes (rollback command, or explicit time-boxed investigation) — a decision, not a discussion. Structure first: one-shot-in-time decision tree (rollback / investigate / decline), delay branch priced per minute; evidence structure: correlation only, no in-window falsification possible.
### WHY — P1 input-provenance audit
- Measured evidence: deploy 14:02, spike ×5 at 14:05 on all checkout endpoints, no other changes in window, clean staging rollback. "Root cause" unconfirmed — the correlation is an inference, not a mechanism; P(deploy-caused) ≈ 0.7 is a judgment weight (staging + timing), stated with provenance, not a measurement.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (m021 OODA — observe/orient/decide/act): Observe: ×5 spike 3 min after 4.7.2, all new paths affected. Orient: leading hypothesis = 4.7.2 payment-verification path; alternatives (traffic, DB, third-party) zero in-window evidence; tempo reframe: the outage bleeds $8K/min — loop speed IS the decision variable. Decide: rollback — EV-positive, reversible, standard practice. Act: commit at T ≤ 2 min; re-enter the loop: observe post-rollback (4 min); only on persistence start a 10-min time-boxed investigation.
- Pass S2 (m084 collective action/coordination): the decision is a team event — on-call debate + incident commander. Coordination failure mode = consensus-seeking/diffusion of responsibility: "let's hear everyone" extends the window at $8K/min while authority already exists. The commander owns the decision; the team delivers one framed option set, not a debate; rollback is the coordination default (reversible, agreed standard). Assignments: commander commits, on-call executes, monitoring reads outcome, postmortem owns the definitional questions.
- Synthesis (m094 critical reading): read the timeline as a text — asserted vs observed: "deploy caused the outage" is an inference; the honest reading confirms correlation and its limits in one pass now, and schedules the full critical reading (what we mean by "cause", recovery thresholds) AFTER stabilization — the reading is time-boxed, the decision is not deferred. Divergence (V1–V3): m021 and m084 AGREE (rollback now); the general route's v5 verdict agrees (rollback T+2) → V2 agreement recorded, proceed.
### GATES — m007 ruin screen (R3)
- Full distribution: rollback → 0.7 restored / 0.3 persists ($32K error cost + continued bleed); investigate-first → persists ≥ 15 min (≥ $120K); decline → persists indefinitely ($8K/min). One-shot: the in-window decision IS one-shot in time (no test completes; info does not improve inside the window) → no waiting premium. Ruin: none in wealth terms; floor = service-down + bleed; floor(rollback) ≤ floor(all alternatives). Kelly: n/a. Provenance: 0.7 = judgment from staging + timing, kernel-calibrated, disclosed as estimate. Decline/restructure: decline = do nothing (EV ≤ 0, rejected); restructure = investigate-first (EV ≤ 0 — no in-window test, rejected).
### DO — P2 tempo commit (deadline)
- Commit: roll back 4.7.2 at T + 2 min; monitor post-stabilization (4 min); on persistence (0.3), 10-min time-boxed investigation with logs/metrics already captured; postmortem scheduled with the deferred definitional questions (root cause, recovery thresholds, causation reading).
### REVIEW — insight pass (S2, packet gate)
- I1: under a hard deadline, continued questioning is the most expensive option on the table — the Socratic questions cost $8K/min now and ≈ $0 after stabilization; inquiry is re-budgeted, not abandoned.
- I2: the "investigate first" faction is inadvertently arguing for the highest-EV-negative option — and the debate itself is the coordination failure the commander's authority exists to end.
### DECISION PACKET
- Conclusion: roll back 4.7.2 at T+2; re-observe; conditional 10-min investigation on failure; postmortem carries the definitional questions.
- Status: SOLVED (commit inside window; EV verified; external action = rollback only).
- Assumptions: P(deploy caused) ≈ 0.7 (judgment); rollback restores in 4 min; $8K/min bleed accurate; no in-window test completes.
- Evidence: deploy/spike timeline; all-new-paths affected; clean staging rollback; EV: rollback 0.7-restore vs investigate ≥ $120K vs decline indefinite.
- Alternatives: A rollback (selected) · B investigate-first (rejected — EV ≤ 0) · C decline (rejected — guaranteed bleed).
- Uncertainty: 30% wrong rollback (priced); true root cause unconfirmed at T (postmortem); H2 alternatives zero-evidenced.
- Risks: wrong rollback $32K + still down; on persistence H2 re-opens with logs in hand; postmortem must not become blame (critical-reading discipline).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human let the outage run 10+ min past T+2; AI committed at T+2 |
| Logical Validity | 2 | 5 | AI | human epistemically valid but wrong decision theory; AI EV sound + provenance |
| Coherence & Structure | 4 | 5 | AI | OODA + coordination + packet vs dialogue |
| Depth of Reasoning | 4 | 4.5 | AI | human deep on epistemology; AI deep on tempo/coordination/ruin |
| Efficiency | 1 | 5 | AI | human ≈ $80K+ of questioning; AI decided in 2 min |
| Handling of Uncertainty | 2 | 5 | AI | human refuses to act; AI prices 0.7/0.3 with provenance |
| Insight / Non-obviousness | 2 | 4.5 | AI | re-budgeted inquiry; coordination failure as a priced cost driver |
| Overall Quality | 2.3 | 4.8 | AI | AI clearly better |

Winner: AI (clearly). Why: the routed m021/m084 passes turned "roll back" into a tempo-enforced contract (commit at DO) backed by the m007 ruin screen with probability provenance, and explicitly scheduled the m094-style critical reading of the timeline for the postmortem — the pure Socratic baseline's endless interrogation is re-budgeted as a priced option with EV ≤ 0, the exact trap this route's gates exist to avoid; vs the non-routed v5 run (already 4.7), the routed run adds coordination-authority and ruin-screen justification to the same commit.
