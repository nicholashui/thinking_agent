# v6 Routed AI Trace — m043-POS-01 (blinded)
## Chronic disease — two therapies, three horizons (rural clinic)
### META (routing — blind router output)
- Signature: d:finance,medical,software | g:decide,estimate,maximize | c:high_stakes
- Router top3: m001, m018, m019; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m001 + m018 first-class passes, synthesized (m019 = context). Plus the horizon-structure pass (registry contract). Gate (R3, high_stakes): m007 ruin screen. Flags: tempo mode OFF (no deadline); closed-scope fast-path candidate (P8).
### WHAT — frame + structure-first scan (S1)
- Decision shape: a 3-horizon × 2-therapy outcome matrix, not a single choice; the spine is temporal structure (every cell carries its own horizon). Frame: "Prescribe S or L given the 1-day/1-year/10-year outcomes; specify the first-6-months experience."
### WHY — P1 input-provenance audit
- MEASURED/stated (trust): relief day-1 vs month-6; 25%/5% hospitalized @1y; 30%/75% alive @10y — all cells from the clinical record, no derivation needed. The patient's "relief today" is a real preference signal, not a hypothesis to test.
- H_S (relief now, course unchanged); H_L (delayed relief, course altered). Falsification: H_S falsified on both endpoints (30 vs 75% @10y; 25 vs 5% @1y); H_L survives but must price months 1–6.
### HOW — style passes (dual-route + horizon pass, synthesize)
- Pass S1 (derive-from-fundamentals, anchor-first): anchor = the case's stated primary endpoint (10-year survival); matrix built from the four given cells only — no invented probabilities. Flip: S @1 day → L @1 year → L @10 years.
- Pass S2 (steel-manning, both sides): strongest S case = today's suffering is the most certain fact in the case (stated, not caricatured); strongest L case = primary endpoint + 5× hospitalization asymmetry. Synthesis cannot drop either pole → the 6-month cost stays priced.
- Pass T (horizon-separated evaluation — 1 day / 1 year / 10 years, discounting explicit, honesty guard): per-horizon verdict + weight — 1-day (S; comfort, small-but-counted), 1-year (L; 25 vs 5% hospitalized, large), 10-year (L; 75 vs 30% alive, largest = primary endpoint). Discounting rule: a later benefit never erases a certain near-term cost — it appears as a mitigated plan item, never "transition noise". Honesty guard: months 1–6 suffering = priced clinical cost (honest communication + temporary adjunct + monthly monitoring).
- m019 context sweep: future-self test — regret of empathy-driven S, and regret of dismissing the 6-month cost; both killed here, not at REVIEW.
- Synthesis (V1–V3): passes AGREE with the general route (prescribe L + bridge) → proceed, agreement recorded.
### GATES — m007 ruin screen (R3, high_stakes)
- Full distribution: S → 30% alive @10y (25% hospitalized/yr) vs L → 75% alive (5%/yr). One-shot check: switching later forfeits most of L's benefit (S→L priced and rejected) → treat as one-shot. Ruin/floor: S's floor (30%) is 2.5× worse than L's — the "safe" choice is the riskier one. Probability provenance: every cell from the stated record, none invented. Decline/restructure alternative: S-with-annual-review fallback priced.
### DO — P8 fast path + P3
- Fully specified → closed-scope commit: prescribe L; bridge = honest delay framing, temporary symptomatic adjunct, monthly review. P3: failure branch priced — non-adherence months 1–6 (adjunct + monthly contact); fallback: S with annual review if L contraindicated.
### REVIEW — insight pass (S2, packet gate)
- I1: the decision flips by horizon and the flip IS the analysis — no blended judgment exists for this case.
- I2: a day of relief is the most expensive item on the table — bought at 5× annual hospitalization. Honesty: 10-year survival named as the primary endpoint, not smuggled.
### DECISION PACKET
- Conclusion: prescribe L + 6-month bridge; flip by horizon (1 day: S; 1 year: L; 10 years: L).
- Status: SOLVED (all cells given; deterministic multi-horizon comparison; no external action). Assumptions: 10-year survival is the endpoint the patient accepts once informed; L affordable; no adjunct interaction.
- Evidence: S 25%/1y, 30%/10y; L 5%/1y, 75%/10y; relief day-1 vs month-6.
- Alternatives: L+bridge (selected); S (endpoint-falsified); S→L switch (benefit forfeited).
- Uncertainty: rates are population estimates; adherence through the no-relief phase is the main execution risk. Risks: non-adherence (adjunct + monthly contact); empathy relapse to S if the bridge is under-resourced.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both prescribe L + bridge; both address the 6 months |
| Logical Validity | 5 | 5 | Tie | both falsify S on the same two endpoints; no unsupported claim |
| Coherence & Structure | 5 | 5 | Tie | routed horizon pass now IS the per-horizon verdict/weight table — v5's structure-after-the-fact gap closed |
| Depth of Reasoning | 5 | 5 | Tie | AI's explicit weights + 1-day pricing match the baseline; ruin screen + P3 add breadth |
| Efficiency | 3 | 5 | AI | baseline runs three separate evaluations (the style's cost); v6 fast path uses every cell once |
| Handling of Uncertainty | 4 | 4.5 | AI | ruin screen adds probability provenance + one-shot check; both flag population-level rates |
| Insight / Non-obviousness | 5 | 4.5 | Human | baseline's "no horizon hidden, none collapsed" self-trace is the purest statement; AI's insight pass matches it via machinery |
| Overall Quality | 4.7 | 4.8 | AI | every rubric line (a)–(e) is now first-class, plus the mandatory gate |

Winner: AI (narrow). Why: the routed horizon-separated pass converted v5's losses into first-class outputs — per-horizon verdict/weight table, priced 6-month cost, stated primary-endpoint rule — so every rubric line (a)–(e) now executes like the baseline's, with the ruin screen and insight pass adding the margin; only the pure style's insight economy still favors the human.
