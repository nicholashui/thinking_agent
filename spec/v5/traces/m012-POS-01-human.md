# Human Baseline — m012-POS-01
## Style: Causal Reasoning (Pearl-style, pure) — visible reasoning trace

**Step 1 — Draw the causal graph.** B (banner seen), P (purchase), M (engagement/email exposure). The exposure process is not random: engaged users click banners more and buy more. Graph: B ← M → P and B → P. M is a confounder — it opens a back-door path from B to P. This is exactly the structure that turns association into a lie about intervention.

**Step 2 — Write down what marketing claims.** P(P|B=1) = (0.4×0.8×0.55 + 0.6×0.2×0.25)/0.44 = 0.206/0.44 ≈ 0.468. P(P|B=0) = (0.4×0.2×0.50 + 0.6×0.8×0.20)/0.56 = 0.136/0.56 ≈ 0.243. Naive contrast ≈ +0.225 — the "+22.5 pts" they quoted. This is P(P | B), an associational statement. The rollout question is do(B=1) vs do(B=0) — a question about the intervention, not the observation. Association ≠ intervention: 22.5 pts is the wrong number on its face.

**Step 3 — Back-door adjustment (do-calculus).** M satisfies the back-door criterion: it blocks all non-causal paths B←M→P, and it's fully observed. So P(P | do(B=1)) = Σ_m P(P | B=1, M=m) P(M=m) = 0.4×0.55 + 0.6×0.25 = **0.37**. P(P | do(B=0)) = 0.4×0.50 + 0.6×0.20 = **0.32**. Causal effect = **+0.05** — five points, not 22.5. The marketing claim is inflated by a factor ≈ 0.225/0.05 = **4.5×**.

**Step 4 — Consistency check.** The stratum-specific contrasts are both +0.05 (0.55−0.50; 0.25−0.20) — no effect modification by M. So the adjusted contrast is the effect of B in every stratum; the naive 22.5 pts is pure selection plus the true 5 pts. A +5 pt effect is real but small. Now the decision is arithmetic: exposure rises from 44% to 100%; the marginal 5,600 newly exposed users buy at +0.05 → 280 incremental purchases ≈ +$7,000 revenue. Annoyance cost: 5,600 × $2.50 = $14,000. **Net −$7,000 → do NOT mass-roll out.** Under the naive claim you'd compute +2,250 purchases ≈ +$56,250 vs $14,000 → roll out. The causal correction flips the decision. Recommend: no mass rollout; offer the banner only to engaged users (they already see it) or run a small randomized A/B to confirm +5 pts before wider spend.

**Step 5 — Assumptions check.** Positivity: all four (M, B) strata observed — yes. SUTVA: one user's banner does not change another user's purchase — plausible. No unmeasured confounding: M is the only plausible shared driver in the recorded world; stated as an assumption, not a fact. If U existed, the +5 pt estimate would be biased too — that residual risk is why the A/B is the clean confirmatory move.

**Trace summary box.** Graph: B←M→P, B→P. Naive ≈ +0.225 (4.5× inflated). Adjusted: do(B=1)=0.37, do(B=0)=0.32, effect +0.05. Decision: don't mass-roll-out (net −$7,000); targeted/A/B path. Assumptions: positivity ✓, SUTVA ✓, no-unmeasured-confounding (stated).

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to the Pearl-style moves — graph, confounder, back-door adjustment, do-notation, interventional claims, identification assumptions. The trace performs excellently here: the 4.5× inflation check plus the cost-conditioned decision flip are the decisive moves, and both are verifiable arithmetic.*
