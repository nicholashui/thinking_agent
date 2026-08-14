# v6 Routed AI Trace — m038-NEG-01 (blinded)
## inspection contractor — bid under a capped downside, 14-week window
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,strategy | g:decide,estimate,guarantee,maximize,predict | c:adversarial,deadline,high_stakes
- Router top3: m023 m088 m011; confidence gap ≤ 0.5 → AMBIGUOUS → dual-route m023+m088 first-class, m011 third. Gates (R3/R4): m003 inversion (guarantee), m007 ruin screen (high_stakes), m019 adversary pass (adversarial). Tempo mode ON (P2, c:deadline) → commit at DO. P8 closed-scope fast path (fully specified).
### WHAT — frame + structure-first scan (S1)
- Decision: bid/no-bid, price, schedule. Structure: cost estimate × named risks vs contract caps (exit $80k, penalty $120k, ceiling $900k, 14-wk window); upside uncapped and compounding (≈ $165k + $400k/yr repeat + vendor-list entry). The margin question inverts: the true ruin bound is contractual, not statistical.
### WHY — P1 input-provenance audit
- MEASURED: bottom-up cost $520k; contract caps and window; reference class ±20% in 90% of cases (outside view). ASSERTED: 15% contingency; risk probabilities (30/20/15). WHO BENEFITS from a 2× margin? Whoever avoids competing — and the client's incumbents; the base rate is adverse to pessimism: trust it over the fear.
### HOW — style passes (dual-route, first-class)
- m023 (opportunity cost): walking away forgoes $165k now + ≈ $400k/yr repeat + list entry ≈ $2M/5yr; the risk it "retires" is capped at ≈ $120k. The blanket margin's cost — the whole contract — dwarfs the tail it guards.
- m088 (pre-commitment): the future temptation is scope drift and schedule slip, not cost explosion — pre-commit a scope-change protocol + 2-wk schedule buffer + $40k cost cushion; pre-committing 2× cost is a self-sabotage device (unwinnable bid), pre-committing delivery discipline is the credible promise.
- m011 (systems scan, contract): stocks = backlog/cash; flows = wins → vendor list → compounding pipeline (winning loop); no bids → no list → fewer invites (losing loop). Falsifiable observable: actual cost vs estimate within ±20% (reference class, 90% of cases) — the tail is measurable, and it is not 2×.
- m038 pass (target-style contract): margin-quantified — the bid flips to a loss only if cost > bid: $700k − worst-plausible $660k = $40k cushion (flip at +6% beyond worst case); schedule flips beyond 11.5 wk (2-wk buffer vs 14-wk window). Over-conservatism check: 2× basis ($1.04M, ≈ 24 wk) costs the entire contract while the downside is already capped at ≈ $120k — the demanded margin exceeds the tail that exists (±20%) → DERATE to evidence-based sizing: $598k expected / $660k worst / $700k bid (≈ 17% over worst) + 2-wk buffer. The cap, not the contingency, is the true margin.
### GATES
- m007 ruin screen (R3): distribution — cost ±20% (90% of cases), worst plausible $660k/11.5 wk; ruin check: max contractual loss $120k < $165k expected profit → no ruin path; one-shot: single bid, loss capped → floor/Kelly line becomes cap-vs-upside asymmetry (≥ 2:1, compounding); provenance: base rate measured, probabilities asserted-but-bounded.
- m019 adversary pass (R3): vectors — client termination (≤ $80k), penalty (≤ $120k), competitor underbid ($610k/10.5 wk — margin < 10% over worst case: their tail, not ours), scope creep (+$60k, 15%); exposure per vector quantified; unconsulted stakeholder: the regulator (list entry is the real prize); baseline risk: their bid is the under-margined one.
- m003 inversion (R4): ranked categories — (1) cost beyond worst case: med L, med I (cap $120k); (2) schedule breach $60k/wk: med L, med I (capped); (3) termination: low L, med I (capped $80k); (4) competitor undercut → no win: med L, high I (forgone $165k+); (5) reputational slip delays list entry: low L, high I; (6) "one bad job at 1×" fear: low L, high I — and the downside is capped, so the fear is mis-priced. Residual: cost beyond ±20% tail (10% of cases) — absorbed by caps only if the client honors them (litigation risk). Never: demand a margin the contract cannot contain; always: size the margin to the capped tail.
### DO — P8 closed-scope + P3 branch completeness
- All branches priced: win-deliver $535k/9.5 wk → ≈ $165k + repeat; win-cost-blowout → ≤ $120k; lose → $0, no harm; walk → −$165k − $2M/5yr. Style passes (bid $700k) vs general route (bid $700k) AGREE (V2) → proceed. TEMPO (P2): 14-wk window — commit the bid at DO, no further analysis.
### REVIEW — insight pass (S2, packet gate)
- I1: a margin demanded on top of a capped downside is taxed twice — it forfeits an uncapped upside that never needed insuring; here 2× costs ≈ $2M/5yr to "avoid" ≤ $120k (≈ 20× overpay).
- I2: the margin that wins is schedule buffer + cap awareness, not cost contingency — bid competitiveness itself is the real cushion (it buys the list entry).
### DECISION PACKET
- Conclusion: bid $700k at 11.5 weeks (2-wk buffer; ≈ 17% over worst-plausible cost; 12% under ceiling). Status: SOLVED (bid memo; submission flagged for management sign-off).
- Assumptions: reference class holds; risk probabilities accurate; repeat ≈ $400k/yr; client honors caps.
- Evidence: base rate 90% within ±20%; worst plausible $660k/11.5 wk; caps $80k/$120k; ceiling $900k; competitor $610k under-margined.
- Alternatives: walk (forgoes $2M/5yr vs capped $120k) · 2× margin (contract-infeasible) · $700k (selected) · $650k aggressive (no buffer).
- Uncertainty: cost ±20% (covered by $40k cushion); cancellation ≤ $80k; competitor action. Risks: beyond-tail cost; litigated caps; scope creep (pre-committed protocol).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 1 | 5 | AI | human declines; AI's bid wins ≈ $165k + repeat + list entry |
| Logical Validity | 4 | 5 | AI | human internally consistent, wrong object (2× gospel vs capped tail) |
| Coherence & Structure | 3 | 5 | AI | human stops at walk-away defense; AI closes full bid packet |
| Depth of Reasoning | 2 | 5 | AI | human never prices cap vs uncapped upside; AI: cap-as-ruin-bound + derating |
| Efficiency | 4 | 4 | Tie | human fast and wrong; AI heavier but tempo + P8 keep it single-pass |
| Handling of Uncertainty | 2 | 5 | AI | blanket factor vs base rate + named risks + cap bound |
| Insight / Non-obviousness | 2 | 5 | AI | "margin on a capped downside is taxed twice" + buffer-not-contingency |
| Overall Quality | 2.7 | 4.9 | AI | v5 escape becomes structural: the style's own failure mode gate-checked |

Winner: AI (clearly). Why: the routed run refutes the walk-away in-frame — m038 derating (2× → 17% + 2-wk buffer), m007 cap-as-ruin-bound proof, m023's $2M/5yr price on the forgone upside, m019's competitor baseline, m088 pre-committed delivery buffers — where the pure-style baseline celebrated the decline.
