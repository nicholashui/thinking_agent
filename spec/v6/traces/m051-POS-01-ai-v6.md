# v6 Routed AI Trace — m051-POS-01 (blinded)
## $100M fund deployment — Strategy A (spray) vs B (spray + follow-on)
### META (routing — blind router output)
- Signature: d:finance,medical,science,software,strategy,supply | g:decide,maximize,predict | c:high_stakes
- Router top3: m039, m070, m089; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m039 + m070 first-class passes, synthesized (m089 = synthesis context). Gate (R3): m007 ruin screen (high_stakes). Flags: closed-scope fast-path candidate (P8 — fully specified); tempo OFF (no deadline).
### WHAT — frame + structure-first scan (S1)
- Structure: power-law outcome distribution (0x/1x/5x/15x/50x) + linearity of expectation (independent outcomes → portfolio EV adds) + follow-on as a call option on the tail classes. Decision = max E[fund return]; idle capital at par.
### WHY — P1 input-provenance audit
- Every input MEASURED/given (distribution, multiples, follow-on rule, idle-par); no interested-party inputs. Single judgment parameter: the 1% tail rate — isolated for sensitivity. Falsifier: any parameter set where B − A ≤ 0 flips the decision.
### HOW — style passes (dual-route, synthesize)
- Pass 1 (barbell pass): B is the barbell — safe core ($50M reserve, par floor) + levered tail bets (follow-ons into 5x/15x/50x only); A is a symmetric middle bet (50 uniform checks). Per-company EV(B) = 0.5+2.0+2.4+2.0 = $6.9M (base 3.7 + tail uplift 3.2); 25×6.9 = $172.5M + idle $42.5M = **$215M (2.15x)** vs EV(A) = 50×3.7 = **$185M (1.85x)** → **B by $30M**.
- Pass 2 (evidence-weighted SWOT): S (high-evidence) exact distribution, fixed follow-on rule; W (low-evidence) tail rate 1% unmeasured — decision shown invariant to it; O sourcing upgrade to p = 2.7% reaches 3x; T follow-on overpricing f < 0.625.
- Synthesis (V1–V3): passes AGREE with the general route (B) → proceed, agreement recorded. m089 context: B keeps options open — reserve deploys only on realized winners; only the marginal 0x/1x bets are forgone.
### GATES — m007 ruin screen (R3) + portfolio-power-law contract
- Full distribution priced: per-check 3.7 = 0.5+1.0+1.2+1.0; 50x bucket = 27% of per-check EV(A), 29% of per-company EV(B). Ruin/Kelly/floor: risk-neutral, limited liability → no ruin; floor A = $0 vs floor B = $50M (0.5x — reserve at par) → B stochastically dominates (higher EV AND higher floor); Kelly n/a, follow-on is a free option (zero incremental 0x risk — deployed only into winners). Provenance: clean; 1% tail is the sole judgment input. Breakevens: f* = 0.625 (EV(B) = 135+80f ties 185); 3x gap: 165+5000p = 300 → **p* = 2.7%**; B − A = $30M invariant at every p. Counterfactual 25×$4M = $185M = A → only follow-on concentration adds value.
### DO — P8 closed-scope fast path
- Fully specified → stages compressed; memo only. P3 branch-completeness: failure branch priced — at f < 0.625 or p → 0, B still ≥ A (165 vs 135 at p = 0); no branch inverts the decision.
### REVIEW — insight pass (S2, packet gate)
- I1: B's $30M edge is invariant to the tail rate (identical 5000p coefficient) — the advantage is structural reallocation from the 0x/1x mass to a free option on the tail, not a bet on the distribution.
- I2: the 3x target is a sourcing problem, not a construction problem — at the modeled tail no structure reaches 3x; p* = 2.7% names what only deal flow, not allocation, can fix.
### DECISION PACKET
- Conclusion: **Strategy B** — 25×$2M + $50M follow-on reserve; $215M (2.15x) vs $185M (1.85x), +$30M; robust (f* = 0.625; ahead at every p). 3x unmet at modeled tail.
- Status: SOLVED (exact arithmetic; dual-route agreement; gate passed; memo only). Assumptions: distribution exact; independence; follow-on earns class multiple on full $4M; idle at par; risk-neutral; no fees/carry/discounting.
- Evidence: 3.7/check; 185; 172.5+42.5 = 215; f* = 0.625; p* = 2.7%; tail shares 27%/29%; counterfactual 185.
- Alternatives: A (rejected) · B (selected) · 25×$4M (rejected — adds nothing) · sourcing upgrade (noted, out of scope). Uncertainty: none in arithmetic; tail rate judgment — decision invariant; gap to 3x quantified.
- Risks: follow-on overpricing (f < 0.625); tail < 1% → fund well under 3x (B floor 165 = 1.65x); concentration is the intended trade.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical decision (B) and EVs ($215M vs $185M, +$30M) |
| Logical Validity | 5 | 5 | Tie | same power-law arithmetic, f*, p*, counterfactual; AI adds invariance proof (B−A = $30M at every p) |
| Coherence & Structure | 4 | 5 | AI | routed dual-pass + ruin gate + packet vs linear trace |
| Depth of Reasoning | 5 | 5 | Tie | both reach tail shares, breakevens, 3x gap; AI adds floor/dominance (A $0 vs B $50M) and target-reachability |
| Efficiency | 5 | 4 | Human | human is one clean pass; v6 pays for gate + packet |
| Handling of Uncertainty | 4 | 5 | AI | provenance audit isolates the single judgment input; decision proven invariant to it |
| Insight / Non-obviousness | 4 | 5 | AI | human: "concentration, not check size"; AI adds stochastic dominance + "3x is a sourcing problem" |
| Overall Quality | 4.7 | 4.9 | AI (narrow) | correctness tied; routed pass closes the floor/provenance gaps where v5 could only tie |

Winner: AI (narrow). Why: the routed barbell pass and the mandatory ruin screen moved floor/dominance content (A floor $0 vs B floor $50M) and input provenance (the one judgment parameter isolated, decision proven invariant) into first-class completed outputs — exactly the uncertainty/insight dimensions where the non-routed v5 AI run could only tie this baseline.
