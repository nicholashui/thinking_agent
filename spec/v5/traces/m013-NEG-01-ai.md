# AI Thinking Agent — Trace — m013-NEG-01
**Run metadata:** single deterministic run; blinded; task = data-loss incident with 2 h deadline; external action = implement boundary fix + raise vendor ticket.

## Stage 0 — META-CONTROL
- **Context:** silent 0.4% nightly loss for 6 days; next run in 2 h; BI stale. **Stakes:** medium (data integrity). **Effort:** E3, time-bound. **Route:** incident triage (Cynefin: complicated — stabilize-before-diagnose). **Safety:** proceed.

## Stage 1 — WHAT
- **Frame:** stop the loss tonight and prevent recurrence within 2 h; explanation is secondary. **Scope:** evidence 1–6; deliverable = action plan, not just diagnosis. **Gate:** enough evidence to act — yes.

## Stage 2 — WHY
- **Chain (evidence per link):** rows dropped ← transform skips nulls (E2) ← `region` null since vendor v2.1 made it optional (E3) ← no ingest validation, so nulls are silent (E5) ← vendor shipped without notification; v2.2 in 6–8 weeks (E4).
- **Depth control:** the chain continues into the vendor's release process (E4) — outside our authority, budget, and timeline. Stop drilling there; record as escalation context. The harm (silent loss) is produced at OUR ingest boundary, which we control.
- **Falsification:** had validation existed, the job would fail loudly (E5) — the boundary is the lever. Gate passed.

## Stage 3 — HOW
- **Alternatives:** A. Root fix via vendor (process change / wait for v2.2) — 6–8 weeks, loss continues silently, no control; rejected as primary. B. Boundary fix now: validation + dead-letter + alert (~30 min, covers tonight), replay 6-day backlog idempotently, one scoped vendor ticket. C. Status quo — rejected (same loss, no visibility).
- **Verification:** validation blocks nulls from tonight; alert fires on any skip; replay checked against reconciliation. **Selection: B.**

## Stage 4 — DO
- **External:** implement validation + dead-letter + alert; replay backlog; raise vendor ticket (severity + timeline ask).

## Stage 5 — REVIEW
- **AAR:** control-boundary stop was the key move — dug to the vendor, stopped there, acted at our boundary. Residual: unknown null classes beyond `region`; dead-letter needs an owner; v2.2 may not fix — covered by the alert, not trust.

## Decision Packet
- **Conclusion:** act at the ingest boundary (validation + dead-letter + alert) as the primary fix; escalate the vendor root in one scoped ticket; replay the 6-day backlog. **Status:** SOLVED (loss mechanism closed at our boundary; escalation recorded).
- **Assumptions:** validation rules cover current schema (region + unknown); replay is idempotent; vendor timeline not trusted for containment. **Evidence:** E2, E3, E4, E5. **Alternatives:** A rejected · B selected · C rejected. **Uncertainty:** other silent-drop classes unknown; alert coverage = validation-rule coverage. **Risks:** vendor ships new breaking schema before rules mature; backlog replay races tonight's run — schedule replay after.

## Comparison
*Evaluator section (provisional, appended after both runs).*

| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human targets the vendor root (6–8 wks) while loss continues; AI's boundary fix contains tonight and closes the silent-loss mechanism |
| Logical Validity | 5 | 5 | Tie | Both verify the chain link by link, including the leap into the vendor |
| Coherence & Structure | 4 | 5 | AI | Staged trace + packet; human linear but disciplined |
| Depth of Reasoning | 4 | 5 | AI | Human digs one link deeper (unactionable); AI reaches the deepest *actionable* cause — the correct depth here |
| Efficiency | 2 | 5 | AI | Human's effort flows to an unactionable root; AI time-boxes (30 min vs 6–8 wks) |
| Handling of Uncertainty | 3 | 5 | AI | Human stakes the fix on unobservable vendor internals; AI converts uncertainty into monitoring + scoped escalation |
| Insight / Non-obviousness | 2 | 5 | AI | AI's "deepest cause ≠ actionable cause" move is the non-obvious one the case rewards |
| **Overall Quality** | **3.4** | **4.9** | **AI (clearly)** | Negative case: stopping depth beats digging depth |

**Overall judgment:** AI clearly better (4.9 vs 3.4). The pure-RCA baseline verified the full chain but fixated on the deepest cause — the vendor's release process, outside its control — demoting the 30-minute boundary fix that fully contains the harm to "interim". The AI dug just as far, recognized the control boundary, and made containment the primary fix with a scoped escalation for the unactionable root.
