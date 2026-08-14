# v6 Routed AI Trace — m077-POS-01 (blinded)
## Meridian Software — Atlas continuation decision (board brief, 7 days)
### META (routing — blind router output)
- Signature: d:finance,medical,organization,product,software,strategy | g:decide,estimate,maximize,predict | c:adversarial
- Router top3: m044, m070, m077; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m044 + m070 first-class passes, m077 contract pass, synthesized. Gate (R3): m019 adversary pass (adversarial). Flags: P8 closed-scope fast-path candidate (closed ledger); no deadline → tempo off.
### WHAT — frame + structure-first scan (S1)
- Decision-tree shape: A continue / B kill+redeploy / C hold, forward cash flows only. Frame rule before arithmetic: the $8.4M is identical under every option — excluded from all comparisons by frame, not by later edit. Two-stage tree (sign contract? → margin/wind-down) with a break-even line.
### WHY — P1 input-provenance audit
- MEASURED (closed ledger, trust): p 0.25 (segment report), +$3.6M / −$1.9M forward values, $1.0M resale offer (verified, lapses on continue), +$2.8M @ 0.85 redeploy (internal ops plan). ANCHOR (not evidence): "we're $8.4M in" (CEO), cumulative book value (CFO) — interested-party framings; both benefit from continuation; neither survives forward EV. Pipeline 0 POCs, no LOI → nothing contradicts the analyst p.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (stakeholder sweep, m044): CEO/CFO/Atlas team all gain only non-forward value from continuing; board loses −0.525M under A; pilots hold maintenance obligations, not equity; reseller is the exit buyer. No stakeholder's forward position improves under A.
- Pass S2 (evidence-graded SWOT, m070): S = core SaaS, 400 accounts (A-grade); W = Atlas 3 yrs, 0 committed customers, 0 POCs, 2 competitors at 60% price (A-grade); O = $1.0M sale + redeploy +2.38 (A-grade); T = hold decays (B-grade). DROPPED: "cumulative book value is the board's largest asset" (accounting residue, C-grade — not forward evidence).
- Pass S3 (forward-value contract, m077): (1) $8.4M stripped as the FIRST move — unrecoverable, excluded from every number; (2) forward-only EV: A = 0.25·3.6 + 0.75·(−1.9) = **−$0.525M**; B = 1.0 + 0.85·2.8 = **+$3.38M**; C = 0.15·2.0 − 1.1 = **−$0.80M**; (3) anchors named and refuted: proportion ("only $6.5M vs $8.4M in" — the next dollar buys −0.525M), waste ("pilots wasted" — gone either way), book value (residue; the real asset is the $1.0M offer that lapses); (4) commitment-effects CHECKED, not blindly ignored: no forward value is contingent on Atlas continuing — pilot obligations are priced as wind-down (−1.9M), no window/reputation channel exists here; the resale offer is forward value on the B side.
- Synthesis (V1–V3): all three passes AGREE with the general route → proceed; agreement recorded.
### GATES — m019 adversary pass (R3, adversarial)
- Attack the recommendation: (1) p 0.25 overestimated → A worsens, B unchanged; (2) redeploy 0.85 too confident → B still wins at 0.5 (1.0+1.4 = +2.4); (3) the resale offer lapses if we continue — holding "the asset" forfeits it; (4) baseline comparison: C = −0.80M → inaction is not neutral. No vector survives; exposure quantified per vector.
### DO — P8 closed-scope fast path
- Fully specified (closed ledger) → stages compressed; commit at DO: recommend B — sell IP $1.0M, redeploy team (+2.38M EV), refuse all three anchors in the boardroom. P3: B's failure branch priced (redeploy underdelivers → floor = $1.0M sale + partial redeploy, still positive; A's failure = wind-down −1.9M).
### REVIEW — insight pass (S2, packet gate)
- I1: the CFO's "largest asset" is, in EV terms, a liability — holding it costs +$3.38M of redeployment value.
- I2: the analyst would have to be ~40% wrong (25% vs break-even 34.5%) for continuation to win — with an empty pipeline, that is the argument.
### DECISION PACKET
- Conclusion: kill Atlas; take the $1.0M resale offer; redeploy the 24-person team to route-planning SaaS. Status: SOLVED (decision brief; no external action).
- Assumptions: p 0.25 and redeploy 0.85 are best estimates; resale offer lapses on continue; no hidden signed commitments. Evidence: $8.4M excluded; EVs A −0.525 / B +3.38 / C −0.80; break-even p 34.5%; 2 competitors @ 60% price; 0 POCs / no LOI.
- Alternatives: A continue (−0.525, rejected) · C hold (−0.80, rejected) · B kill+sell+redeploy (+3.38, selected).
- Uncertainty: p width (34.5% break-even vs 25% → 40% margin); redeploy confidence (wins even at 0.5). Risks: redeploy underdelivers (floor positive); board inertia from CEO anchoring (brief names the anchors); analyst bias upward (verdict unchanged).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical EVs, verdict, break-even |
| Logical Validity | 5 | 5 | Tie | same forward-only structure |
| Coherence & Structure | 4 | 5 | AI | routed passes + packet |
| Depth of Reasoning | 5 | 5 | Tie | human owns the one-sweep exclusion; AI matches by contract + provenance/stakeholder audit |
| Efficiency | 5 | 4 | Human | human one linear pass; routed passes lean (P8) but multi-pass |
| Handling of Uncertainty | 5 | 5 | Tie | both carry break-even + halving robustness |
| Insight / Non-obviousness | 4 | 5 | AI | "largest asset is a liability"; who-benefits audit; hold-not-neutral |
| Overall Quality | 4.7 | 4.8 | AI | correctness tied; routed contract makes the exclusion first-move and adds audit depth |

Winner: AI (narrow). Why: the routed forward-value contract executes the $8.4M exclusion as move 1 (fixing v5's "re-derived inside WHAT/WHY" gap and the "preserves the pilots" draft slip) and the stakeholder/evidence/baseline passes add depth the baseline lacks; the human keeps the cleaner single-pass efficiency.
