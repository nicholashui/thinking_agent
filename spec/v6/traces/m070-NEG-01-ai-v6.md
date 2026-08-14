# v6 Routed AI Trace — m070-NEG-01 (blinded)
## Westbrook Grid Ops — 2:07 AM dispatch brief, hot-swap vs repair
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,product,science,software,supply | g:decide,estimate,guarantee,maximize,predict | c:high_stakes
- Router top3: m018, m019, m070; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m018 + m019 first-class passes, synthesized (m070 = synthesis context). Gates (R3/R4): m007 ruin screen (high_stakes) + m003 inversion (guarantee). Flags: no deadline in signature → tempo off (60-min brief honored as scenario discipline); facts fully specified → P8 closed-scope fast path.
### WHAT — frame + structure-first scan (S1)
- Frame: one question governs — which path restores power fastest within the 4h hospital-fuel and 8h regulator lines. Deliverable = a verdict with a decision rule, not a description of options.
- Structure: two options, each a (success probability, duration) pair against two binding lines; the 4h line is a mandatory trigger for BOTH, the 8h line is a tail risk of the slower option.
### WHY — P1 input-provenance audit
- GIVEN/trust: SCADA fault class; hospital fuel 4h (documented); 8h rule + ≈ $150k fine (regulatory); parts in stock; costs. ESTIMATED (unanchored): swap reliability 85–90% class-specific — n = 1 (9 prior swaps company-wide, 8/9 successful; only 1 at this class); repair success ≈ 80%; connection 1.5h; ETA 3h. INTERESTED-PARTY: the 85–90% figure is the crew's estimate (the crew that would perform the swap) → wide prior, never precision.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (steel-manning, m018): strongest case for B (repair) — 45-min start vs 3h, $40k vs $120k, parts guaranteed, 80% class record; A's 8/9 is company-wide, not class-specific. Strongest case for A (hot-swap) — 4.5h on success vs 7h; the n = 1 class sample WAS successful; B's tail crosses the fine line. Both cases survive steel-manning → narrative cannot decide; the numbers must.
- Pass S2 (adversary, m019, contract: enumerated vectors + quantified exposure + baseline-risk): attack A — ETA 3h unverified, connection at this class n = 1; quantified: +1h ETA → EV(A) ≈ 6.1h (still beats B); connection failure → ≈ 10h fallback. Attack B — 80% is a class record, parts "guaranteed"; quantified: P(B ≥ 8h) = 0.20 → fine EV ≈ 0.20·$150k = $30k. Baseline risk: company-wide swap failure 1/9 (11%) is consistent with the crew's 10–15% band; no vector breaks the verdict.
- Synthesis context (m070): graded read — S (crews, 8/9) B · W (class-specific n = 1) C · O (unit available 3h) B · T (4h/8h lines) A → all-B/C table, NO verdict: grading is subjective at n = 1 (any B–D defensible) and a 2x2 cannot carry an expected-value decision. True-but-irrelevant filter: the 4h hospital line is TRUE but binds BOTH options — a mandatory trigger, not a differentiator.
- Divergence resolution (V1–V3): passes AGREE the governing quantity is expected restore time; A-vs-hybrid resolved by branch-completeness — the hybrid dominates A (keeps the cancelable repair path) and dominates B (EV). EV(A) = 0.85·4.5 + 0.15·10 ≈ 5.3h; EV(B) = 0.80·7 + 0.20·10 ≈ 7.6h. Sensitivity: A wins the EV comparison even at success 0.75 (5.9h) and at +1h ETA (6.1h).
### GATES — m007 ruin screen (R3) + m003 inversion (R4)
- m007: outcome distributions — A: 4.5h (0.85) / 10h (0.15); B: 7h (0.80) / 10h (0.20). One-shot: yes — single outage, no do-over; consequences bounded (no public hazard; the hospital floor is the hard line). Floor: the 4h hospital protocol is mandatory under BOTH options — it IS the plan's baseline, not a decision input. Provenance: 0.85–0.90 / 0.80 labeled crew/class estimates (n = 1); the verdict holds across their uncertainty bands. Decline/restructure: do not commit fully to A at 2:07 AM — the restructure IS the hybrid (B stays alive, cancelable). Fine EV: ≈ $30k under B, ≈ 0 under the hybrid.
- m003 inversion: "how do we GUARANTEE the outage exceeds 8h?" → ranked: (1) B's 20% tail high; (2) swap failure with no standing repair med; (3) hospital fuel expiry at 4h without trigger med/catastrophic; (4) decision paralysis — a graded table with no verdict med (the gated trap); (5) escalation mishandling low. Un-mitigable residual: n = 1 class-specific reliability (sensitivity-covered). Never/always: never hand a 2 AM board a table without a verdict; always keep a cancelable path alive; always trigger hospital protocols at the documented line.
### DO — P8 fast path + P3 branch completeness
- Advisory brief; no execution. Branches priced: swap arrives early → commit A at t ≈ 3h; swap late → repair continues; repair > 60% complete at t ≈ 3h → commit B, cancel the rental. Commit at DO: hybrid verdict + 4h trigger + 8h escalation pre-brief.
### REVIEW — insight pass (S2, packet gate)
- I1: the decision-relevant number (EV restore time) lives in no quadrant of the graded table — the instrument swap IS the insight; an all-moderate graded table is the tell that the instrument is wrong for the decision.
- I2: the 4h hospital line is a floor, not a differentiator — a graded table files it under Threats (grade A) and still decides nothing; true-but-irrelevant applies to constraint lines that bind every option.
### DECISION PACKET
- Conclusion: hot-swap (A) with parallel-start: dispatch the repair crew now (45-min start, ≈ $15k, cancelable), commit to A at t ≈ 3h when the mobile unit arrives unless repair is > 60% complete; hospital fuel-rotation / patient-transfer protocols at the 4h mark regardless of option.
- Status: SOLVED (decision brief; no external execution). Assumptions: 0.85 swap reliability as a wide prior; connection 1.5h ± 0.5h; 0.80 repair success; parts in stock; costs as stated.
- Evidence: EV(A) ≈ 5.3h vs EV(B) ≈ 7.6h; P(B ≥ 8h) = 0.20 vs P(A ≥ 8h) = 0.15; fine EV $30k (B) vs ≈ 0 (hybrid); documented 4h line; sensitivity at 0.75 / +1h ETA.
- Alternatives: B repair-only (rejected — EV 7.6h, 20% fine tail) · A alone (subsumed — discards the cancelable repair path) · C hybrid (selected).
- Uncertainty: class-specific swap reliability (n = 1) — sensitivity-covered; ETA/connection variance ± 0.5h; fine risk bounded. Risks: swap connection failure (standing repair path); late mobile unit; hospital fuel expiry (4h trigger); fine if > 8h (EV ≈ $30k under B, ≈ 0 under hybrid).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human: balanced table, no verdict; AI: verdict + decision rule in the brief |
| Logical Validity | 3 | 5 | AI | human consistent but reasons to "risk preference"; AI computes EVs with tails vs the lines |
| Coherence & Structure | 4 | 5 | AI | human trace clean; AI dual-pass + gates + packet |
| Depth of Reasoning | 2 | 5 | AI | human stops at "grading is subjective (n = 1)"; AI turns n = 1 into a wide prior + sensitivity |
| Efficiency | 3 | 4.5 | AI | human is faster and produces nothing decision-relevant; AI's stages buy the verdict |
| Handling of Uncertainty | 2 | 5 | AI | human flags the unanchored grade and stops; AI quantifies and bounds the fine tail |
| Insight / Non-obviousness | 2 | 5 | AI | human's epilogue is the one good beat; AI finds parallel-start and the non-differentiator line |
| Overall Quality | 2.6 | 4.9 | AI | the pure style's structural limit — a 2x2 cannot carry an EV decision — is decisive |

Winner: AI (clearly). Why: the dual-route steel-man + adversary passes and the m007 ruin gate made the instrument swap (EV restore time with provenance, floor and decline-restructure) and the parallel-start rule guaranteed first-class outputs instead of general-route recovery; the m070 context's true-but-irrelevant filter names the hospital line as a non-differentiator the baseline's table would mis-file as a threat.
