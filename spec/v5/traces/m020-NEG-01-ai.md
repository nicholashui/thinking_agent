# AI Thinking Agent Run — m020-NEG-01
**Agent process**: META-CONTROL → WHAT → WHY → HOW → DO → REVIEW (with VERIFY layer). Blinded run: no thinking-model name or style information provided.
## META — Context, stakes, effort
- Operational vendor choice on top of a mature, repeatedly successful operation. Low-moderate stakes (12,000 registrants, 6 weeks to ticket sales), hard deadline (decision this week). Complicated-with-narrow-unknowns — the conference plan is well-trodden; only the ticketing delta carries genuine uncertainty. Balanced-analytical, advisory.

## WHAT — Frame
- "Decide whether to replace the incumbent ticketing platform with the new vendor, 6 weeks before ticket sales." Key question: "Which parts carry genuine new risk, and which are established and taken as given?" Metrics: base-rate statement for the unchanged plan; ranked risk pass on the delta only; decision with a defined rollback rule. Gate check: pass — the conference plan is the baseline, not a risk surface.

## WHY — Hypotheses, evidence, falsification
- H1: the unchanged plan will succeed — base rate 11/11 runs, same venue/team/vendors, rising feedback; runbook + insurance cover standard event risks. H2: ticketing migration is the only material new risk — 12,000-record migration, 3-week window, unknown support profile vs. 8-year-uneventful incumbent.
- Evidence: feedback trend; venue contract continuity; insurance schedule; incumbent uptime; vendor fee/feature comparison; migration window vs. sale opening. Falsification: H1 challenged only by a runbook change (none); H2 testable by dress rehearsal (staging migration, hash-verified, load test) — fail or window overshoot converts adopt-with-rollback to keep-incumbent. G-WHY: pass — H1 is base rate, not an effort sink; H2 is the decision-relevant hypothesis with a defined test.

## WHY-adjacent — bounded risk pass (capped at 3, ranked, delta-only)
1. Migration data integrity (High L, High I) → staging dry-run with hash verification at T-3 weeks. 2. Support-load spike on new vendor (Med L, Med-High I) → SLA clause (4-hr response); incumbent keeps read-only DB as rollback source. 3. Vendor stability post-migration (Low L, High I) → data escrow; pre-specified rollback trigger. Excluded: venue fire, wifi, speaker illness, food poisoning — runbook/insurance covered, unchanged in 11 runs; listing them changes nothing.

## HOW — Generate, test, select
- A — Full cutover now: best fees/analytics; no detection point before sale day. B — Keep incumbent: zero new risk; forego measured savings; a default, not a choice. C — Adopt with gated rollout: sign vendor with SLA; full dress rehearsal at T-3 (staging migration, hash-verified, load test, numeric criteria); incumbent DB retained warm; rule — rehearsal fail or SLA unmet by sale day → roll back within 48h.
- Verify: A's first signal is a crashed sale day. B ignores a measured cost advantage for an unmeasured risk; the rehearsal is cheap relative to the fee difference. C bounds A's risk with the evidence H2 requires and preserves the escape. Feasibility: 3-week window fits the rehearsal; SLA negotiable this week. Selection (record): C — converts the only genuine uncertainty into a testable checkpoint before the irreversible event, keeps the upside, pre-specifies the failure response.

## DO
- Attestation: advisory recommendation, class A2; no live execution.## REVIEW — After-action review
- What went well: base-rate routing kept effort off the proven plan; risk pass explicitly delta-only and capped; rollback rule makes the decision checkable.
- To record: (1) Refusing to manufacture risk was deliberate and must be logged as a decision, not an omission — re-listing insured runbook items would dilute the migration focus. (2) The 48h rollback depends on the incumbent's read-only copy being refreshed to cutover — that refresh is a task, not a wish. (3) Rehearsal-failure criteria must be numeric (e.g., >0.5% record mismatch) to prevent judgment debates at T-3. Folded back as risks.

## Decision Packet
- **Conclusion**: Adopt the new platform under C (gated rollout): sign with SLA (4-hr response); full dress rehearsal at T-3 (staging migration, hash-verified, load test, numeric criteria); incumbent read-only DB retained warm, refreshed to cutover; rule — rehearsal fail or SLA unmet by sale day → roll back to incumbent within 48h.
- **Status**: `APPROXIMATED` — decision made with a defined checkpoint; migration success unproven until rehearsal (error bound: vendor support behavior unknown until first sale wave).
- **Assumptions**: incumbent rollback copy viable and refreshable; rehearsal fits the 3-week window; SLA negotiable this week; unchanged plan continues its base rate. **Evidence**: 11-run record; venue continuity; insurance; incumbent uptime; vendor comparison; window timing.
- **Alternatives**: A (rejected: no detection point), B (rejected as default: measured savings foregone for unmeasured risk), C (selected). **Uncertainty**: vendor responsiveness (SLA + rehearsal); migration data quality (hash-verified rehearsal); fee-savings accuracy.
- **Risks**: rehearsal failure → pre-specified 48h rollback; migration corruption → hash check; support overload → SLA + monitored queue; excluded event risks unchanged, covered.

## Comparison — m020-NEG-01

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human asks "what if the conference fails?" and never decides the ticketing question; AI decides with a gate. |
| Logical Validity | 4 | 5 | AI | Human internally valid but commits goal displacement (analyzes the wrong decision); AI's base-rate → delta → gate chain stays on-goal. |
| Coherence & Structure | 3 | 5 | AI | Human: 15 equal-weight causes, no spine; AI: base-rate routing → 3 ranked delta risks → selected alternative with rollback. |
| Depth of Reasoning | 4 | 4 | Tie | Human's 15-item enumeration is thorough and its Step-5 self-observation self-aware; AI's delta pass is narrower but decision-relevant, and its AAR catches rollback-copy refresh scheduling. |
| Efficiency | 2 | 5 | AI | Human spends a 15-cause pass re-deriving what runbook and insurance already encode; AI caps the pass at 3 delta risks. |
| Handling of Uncertainty | 2 | 5 | AI | Human: no ranking, no checkpoint, deferral by implication; AI: rehearsal gate, numeric criteria, 48h rollback. |
| Insight / Non-obviousness | 3 | 4 | AI | Human's one genuine insight (migration integrity as the real risk, item 8) is buried at equal weight among 15; AI builds the decision around exactly that item. |
| Overall Quality | 2 | 5 | AI | AI clearly better on the negative case. |

**Overall judgment**: AI clearly better. Strict pre-mortem converted a healthy plan with one narrow decision into a 15-item unranked catastrophe list whose mitigations either duplicate the runbook (no change) or demand escalation (paralysis); the actual decision was never analyzed. The AI's mixed-method run routed effort by base rate — took the proven plan as given, concentrated on the genuine delta, and produced a decision with a rehearsal gate and a pre-specified rollback. The human's surviving insight (migration integrity) is real and is exactly the AI's top-ranked delta risk; the difference is structural: the human buried it at equal weight among fifteen, the AI built the decision around it.
