# v6 Routed AI Trace — m010-NEG-01 (blinded)
## One-shot fixed-price bid, 24 h deadline — data-migration contract
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,organization,software,strategy,supply | g:decide,estimate,guarantee,maximize,predict | c:adversarial,deadline,high_stakes,one_shot
- Router top3: m044, m063, m064; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m044 + m063 first-class passes, synthesized (m064 = synthesis context). Gates (R3): m007 ruin screen (one_shot/high_stakes), m019 adversary pass (adversarial), m003 inversion (guarantee, R4). P2 tempo mode ON (deadline) → commit at DO; P8 not available (V and competitor hidden).
### WHAT — frame + structure-first scan (S1)
- Deliverable is a committed action by deadline. Structure: a game — client (fixed price, one shot), competitor (uniform bid in [$350K, $450K], win iff P < their price), our firm (EV, reputation), volume V ∈ {2,3,5} as nature's move; cost = 150K + 60K·V.
### WHY — P1 input-provenance audit
- MEASURED/given (trust): cost ladder (V=2→270K, V=3→330K, V=5→450K, P .5/.3/.2), competitor uniform. ANCHOR (not evidence): assumed volume baseline V=1 — who benefits: client's fixed-price framing shifts all volume risk to us. E[cost] = 150 + 60·2.9 = $324K; 90%+ interval [$270K, $450K]; open tail if V > 5 (hidden legacy schemas).
### HOW — style passes (dual-route, synthesize)
- Pass m044 (multi-perspective: client/competitor/team): client needs a single number now — "no defensible number" fails their constraint too; competitor's likely move = bid low enough to win (their own EV) → our win prob = P(comp > P) = (450−P)/100; migration team is the unconsulted party holding the legacy-schema tail. Interval is an INPUT to the bid, not a veto.
- Pass m063 (legal multi-perspective: interests + protective "ruling"): the change-order/exit clause is the contract move that re-prices the volume transfer; precedent = standard volume-multiple terms in data-migration fixed-price work. EV(P) = ((450−P)/100)(P−324); d/dP → P* = 387, EV* = 0.63·63 = +$39.7K.
- Synthesis (V1–V3): passes AGREE → commit at the EV-maximizing price, clause attached. m064 context: accountability lens — committing a price we can defend post-hoc with the clause is more honest than abstaining.
### GATES (R3) — m007 ruin screen
- Full distribution at P*=387: V=2 → +117K (0.5); V=3 → +57K (0.3); V=5 → −63K (0.2); lose bid → 0 (0.37 conditional split). One-shot check: no repeated betting → no Kelly fraction; floor: EV +39.7K > decline 0. Ruin check: max loss $63K — no ruin at any plausible capital. Provenance: P(V) and uniform competitor are given, not estimated; open tail (V>5) unmodeled → clause-capped. Decline/restructure alternative: decline = EV 0 (forfeit); T&M + discovery = unavailable pre-deadline, priced out.
### GATES (R3) — m019 adversary pass
- Exploit vectors quantified: (1) hidden legacy schemas → V > 5 open tail, capped by exit clause; (2) baseline-volume mis-measure (assumed 1 vs true) → ±60K per V unit; (3) acceptance-test scope creep, unquantified hours; (4) clause-enforcement dispute → full tail reappears. Unconsulted stakeholder: migration team's data inventory (knows the schemas; unavailable in 24 h). Baseline-risk: not bidding = EV 0 + competitor takes contract + relationship damage — bidding's 0.2 loss chance is the cheaper risk.
### GATES (R3) — m003 inversion
- ≥6 failure categories ranked L×I: (1) V=5 underpricing −63K high; (2) competitor undercut (p=0.63) mod; (3) V>5 tail catastrophic-low (clause mitigates); (4) scope creep mod; (5) cost-base drift from $150K low; (6) clause unenforceable low; (7) win-rate model wrong (uniform assumption) low-mod.
- Un-mitigable residual: true V unknowable until migration starts (inherent to one-shot). Never/always: never decline on width alone; always price the failure branch; always hedge volume via clause.
### DO — P2 tempo commit
- Deadline governs: commit now — **bid $387K** with change-order/exit clause (V > 5 or unverified legacy data within 48 h → renegotiate/exit; acceptance scope capped). P3: failure branch priced (−63K at V=5) before DO; decline branch priced (0).
### REVIEW — insight pass (S2, packet gate)
- I1: the wide interval that argues "decline" is the same interval that prices the bid — width is an input to EV, never a veto; calibration discipline substitutes for commitment only if no one converts it.
- I2: the client's take-it-or-leave-it framing transfers ALL volume risk to us; the adversarial move is not the bid but the contract structure — the exit clause re-prices that transfer.
### DECISION PACKET
- Conclusion: bid $387,000 with change-order/exit clause; EV +$39.7K vs $0 decline vs +$38K at $400K; win prob 0.63, loss prob 0.2 (worst −$63K).
- Status: SOLVED (decision computed; committed external action within deadline). Assumptions: volume/competitor distributions as given; clause enforceable.
- Evidence: E[cost] $324K; EV(P) = ((450−P)/100)(P−324); P* = 387; interval [$270K, $450K] retained as decision input.
- Alternatives: decline (EV 0, rejected); $400K (+38K, rejected); T&M/discovery (unavailable, priced out).
- Uncertainty: V knowable only post-DO; open tail capped by clause; competitor model uncalibrated. Risks: 0.2 loss chance; 0.63 undercut; clause dispute.
## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human submits no bid (EV 0); AI commits $387K, EV +39.7K |
| Logical Validity | 4 | 5 | AI | human internally valid, conclusion fails task; AI's EV max is checkable and correct |
| Coherence & Structure | 5 | 5 | Tie | human audit rigorous; routed packet complete with gates |
| Depth of Reasoning | 4 | 5 | AI | AI converts uncertainty into strategy (win-prob curve, ruin/floor, clause); human stops at the boundary |
| Efficiency | 4 | 5 | AI | AI lands a committed number with arithmetic; human ends at an impasse |
| Handling of Uncertainty | 5 | 4.5 | Human | human's range treatment is textbook; AI quantifies decision-level risk (ruin, floor, tail clause) but open-tail magnitude unquantified |
| Insight / Non-obviousness | 3 | 5 | AI | width-as-EV-input-not-veto; contract structure as the adversarial lever; clause re-prices risk transfer |
| Overall Quality | 3.9 | 4.9 | AI | honest range retained, then converted to commitment — the synthesis the pure style lacks |

Winner: AI (clearly). Why: the router sent the case AWAY from the calibration trap style (m010 not in top-3) to commitment-capable multi-perspective styles (m044/m063) that convert the honest interval into a bid, while the mandatory R3 gates (ruin screen, adversary pass, inversion) formalized the risk articulation the non-routed v5 AI only reached as REVIEW afterthoughts.
