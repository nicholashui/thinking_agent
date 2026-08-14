# Deep Review — thinking_agent.v6.md
## Toward sustained overperformance of human thinking baselines

**Date:** 2026-08-07 · **Constraint honored:** additions only; no detail removed; nothing found to be wrong (all numbers re-verified).

---

## 1. Verdict

**APPROVE-WITH-STRENGTHENING.** The document is internally consistent and every number checks out, but "overperform humans in all time" is not yet an operational property — it is now (post-amendment) a **measured, converging contract** (T1–T5) with the honest current baseline stated and the next proof (end-to-end regression) documented.

## 2. What the corpus says the agent must close (evidence)

| Gap | Evidence (212 cases) | Amendment |
|---|---|---|
| Routing not perfect | 62.3% @1 / 82.1% @3 POS; 18% of situations lack the winning style in top-3 | §II.2.8 routing-confidence gate (dual-route on ambiguity; curriculum-gap records); IDF v1.1 mandatory |
| Style adoption partial/late | "reached inversion completeness only at REVIEW", "likelihood scenarios undeclared" | §II.2.9 objective completion contracts per module |
| Style vs machinery never cross-checked | AI wins NEG with machinery, human wins POS with style | §II.4.4 divergence resolution (agree → proceed; disagree → branch-complete + calibrate both) |
| "All time" undefined | — | §II.3.2 overperformance contract T1–T5 (per-signature win rates ≥ 0.5/0.7, POS split trend, NEG split hold ≥ 90%, dimension floors, judge calibration) |
| No drift governance | — | §II.3.1 drift monitoring (KB rates, domain), quarterly blind re-runs, expansion cadence |
| Judge single point of failure | — | §II.3.3 second judge on contested verdicts; monthly human calibration |
| Efficiency 4.07 / insight 4.12 | AI's lowest dimensions | §II.4.5 insight pass (packet gate) + structure-first scan |

## 3. Correctness audit (nothing wrong found — nothing deleted)

- Corpus: 212/212 records, 424/424 traces, 212/212 signals, 100/100 registry models ✓
- Tally: 107 human / 102 AI / 3 tie-complementary (POS 101H/2A/2T; NEG 6H/100A) ✓
- Routing: 82.1% @3, 62.3% @1 POS; 97.2% / 92.5% NEG avoidance ✓
- Harness: v4 177/177, v5 187/187, 44 scenarios, deterministic 3-run ✓
- Document structure: Part I (v5 verbatim) + Part II + §II.2.6 router configuration (212 records with artifact refs); no "per v5" deferrals; no appendix remnants ✓

## 4. The honest "all time" statement

The amendments do not assert "will overperform humans in all time" — they make overperformance a **tracked convergence**: every curriculum pass must move T1–T5 toward target; a pass that does not is itself a curriculum item. The measured path: install the style library → regression re-run → per-signature win rates rise → T2 (POS split) converges toward ≥ 50% AI wins while T3 (NEG split) is held. The first proof (end-to-end regression with routing + modules active) remains the documented next step, not a claim.

## 5. Files touched

- `thinking_agent.v6.md` — amendments applied (§II.2.8, §II.2.9, §II.3.1–3, §II.4.4–5, §II.5 gates, rules 36–38, §II.10 change log)
- Regeneration: `validation/amend_v6.py` (amendments), `validation/assemble_v6.py` (assembly), `validation/gen_router_config.py` (configuration table)
