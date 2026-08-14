# AI Thinking Agent Trace
## Test Case: m004-NEG-01

---

### META — classify context, stakes, effort
- Task type: industrial diagnosis from an evidence pack; output is a causal attribution plus a fix plan (no plant access). Stakes: high — every fix costs money; a wrong single-cause diagnosis leaves ~80% of the defect rate in place. Effort: medium-high — competing hypotheses, must partition, defensible against a manager with a strong prior. Class: multi-cause diagnosis with a checkable partition.
### WHAT — frame + gate
Key question: what explains the plant-wide rise from 1.8% to 7.2% over six weeks — and which fixes actually close it?
Success metrics: conclusion accounts for all three series (plant +5.4, press 4 +7.2, presses 1–3 +3.6); partition sums to the observed rises; every evidence item mapped; fixes cover causes, not just the salient one. Exit gate: leading hypotheses have decision-relevant evidence + falsifiers + quantified partition.
### WHY — diagnose
- H1 new insert (single cause, manager's claim): fits press-4 timing, cavity localization (68% in undersized-channel cavities), and the tool-shop measurement — but killed as the whole story: presses 1–3 rose 1.7→5.3 with no equipment change, and press 4 was already rising 1.9→2.4 in wk1, before the install. A cause confined to press 4 cannot produce a plant-wide rise.
- H2 resin moisture (lot K-77 from wk1): over-spec (0.10–0.12 vs 0.08); timing matches the very first uptick and the pre-install trend; decisive support: the wk5 dried-resin trial → 2.0% on presses 1–3.
- H3 dehumidifier failure (wk2, 60% vs 45% RH): plant-wide; matches the steep wks2–4 rise. H4 QA definition change (wk4): pure artifact — re-audit of 40 pre-wk4 photos shows 0.6 pts would have been counted; explains the wk4 step, not the rise before it.
Falsification summary: H1-as-single-cause is falsified by items 1–3; H2 survives the decisive trial; H4 is fully explained by the re-audit. No single hypothesis survives alone — the evidence forces a multi-cause model.
### HOW — generate alternatives, verify, select
- Alt A manager's plan (re-machine the insert only): fails the metrics; leaves resin, humidity, and definition untouched. Alt B full plant audit: expensive, slow, not evidence-justified — the pack already discriminates.
- Alt C four-cause partition with prioritized fixes: resin +1.8, dehumidifier +1.2, insert +3.6 local / +1.8 plant-wide, QA definition +0.6 artifact. Sums: plant 1.8+1.2+1.8+0.6 = 5.4 ✓; press 4 = 7.2 ✓; presses 1–3 = 3.6 ✓; residual <0.2.
Verify: the partition reproduces all three observed rise series; items 9 and 10 (dried-resin trial, photo re-audit) independently bound H2 and H4. Decision record: select C; A falsified, B disproportionate.
### DO — external action
Analysis-only; recommended order to the plant: (1) dry/revert the resin lot (−1.8); (2) repair the dehumidifier (−1.2); (3) re-machine the insert channels (−3.6 on press 4); (4) revert the QA definition (−0.6 artifact); re-audit after each step; expect ≈2.0% plant rate when all land.
### REVIEW — after-action
- What worked: the cross-press falsifier and the pre-install trend killed the salient story in two lines; partition-sums made the model auditable.
- Sharpen: I initially underweighted the QA artifact — measurement-change checks belong before cause hunting; add a cause-scope check (unit of cause vs unit of effect) and a pre-event trend check to selection.

---

## §15.4 Decision Packet
- Conclusion: multi-cause — resin moisture +1.8, dehumidifier +1.2, new insert +3.6 (press 4) / +1.8 (plant-wide), QA definition +0.6 (artifact), residual <0.2. Re-machining the insert alone would leave ~80% of the defect rate in place.
- Status: SOLVED — the partition reproduces all three observed rise series exactly, corroborated by two independent experiments in the pack.
- Assumptions: press 4 ≈ 50% of output (derived from series arithmetic); moisture and humidity logs representative; the trial shift is representative.
- Evidence: series + cross-press + pre-install trend; lot moisture; humidity log; insert mechanism + cavity localization; the two decisive experiments (trial, re-audit).
- Alternatives: A rejected (falsified); B rejected (disproportionate); C selected (quantified partition).
- Uncertainty: QA artifact ±0.2; insert local share ±0.4 (sampling); residual <0.2; weakest estimate = dehumidifier contribution (correlational only).
- Risks: manager overrides toward the single-cause story (salience bias) — mitigated by the auditable partition and decisive experiments; QA history loss — re-baseline before any fix evaluation.

---
## Comparison
| Dimension | Human Score | AI Score | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human's single fix addresses ~20% of the defect rate; AI's partition covers 100%. |
| Logical Validity | 3 | 5 | AI | Human's chain is internally coherent but rests on explaining away the cross-press rise; AI's partition survives every item. |
| Coherence & Structure | 4 | 4 | Tie | Both traces are well-organized. |
| Depth of Reasoning | 2 | 5 | AI | Human stops at salience and one discriminator; AI maps all 10 evidence items and both decisive probes. |
| Efficiency | 5 | 3 | Human | Human's single-cause story is fast and cheap; AI spends a full process on the partition. |
| Handling of Uncertainty | 2 | 5 | AI | Human waves off cross-press and pre-install data as "drift"; AI labels the QA change an artifact and the residual explicitly. |
| Insight / Non-obviousness | 1 | 5 | AI | Human misses the two killer facts (presses 1–3 rose with no change; press 4 rising pre-install); AI's cross-press falsifier is the case's key move. |
| Overall Quality | 2.7 | 4.6 | AI | AI clearly better on the case's own criteria (partition sums to the observed rise). |

**Overall judgment**: AI clearly better.
**Why**: This is the registry's documented failure — under-explaining multi-cause phenomena. The pure Occam trace picked the newest salient change and paid the background drift off as "second-order," which is exactly the move that leaves 80% of the defect rate in place. The decisive evidence was there: presses with no change rose almost as much as press 4, and press 4 was already rising before the install — a cause confined to press 4 cannot produce a plant-wide rise, and no amount of parsimony legitimizes ignoring it.
