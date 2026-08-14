# v6 Routed AI Trace — m021-NEG-01 (blinded)
## Pasteurizer line 3 — single-sensor deviation, premium fresh-produce batch
### META (routing — blind router output)
- Signature: d:finance,medical,organization,product,security,strategy | g:decide,estimate,guarantee | c:adversarial,deadline
- Router top3: m023, m044, m070; confidence gap > 0.5 → CONFIDENT → single-route m023 (opportunity-cost pass) first-class; m044/m070 = synthesis context. Trap avoided: tempo-cycle style (m021) NOT routed on this signature. R4: guarantee goal → m003 inversion prepended. Gate (R3): m019 adversary pass (adversarial). Tempo-mode classifier (P2): adversary none, dynamics min→h, actions expensive-but-reversible, trigger base rate 11/30 → DELIBERATE-BOUNDED (≤45 min) — the deadline flag is alert salience, not environment tempo; tempo mode NOT adopted.
### WHAT — frame + structure-first scan (S1)
- Frame: determine real drift vs sensor fault on a line that is safe to keep running while evidence is collected; the only risk is acting on the loudest frame.
- Structure-first: noisy sensor family (11 false alarms/30 days) → single observation → decision gate; redundant sensor + 24h trend + lab = discriminating structure; shutdown/restart/shutdown is a feedback loop the operator feeds, priced per cycle.
### WHY — P1 input-provenance audit
- MEASURED (trust): 4°C above setpoint × 6 min (single sensor); 11 false alarms in 30 days, all verified false (family history); redundant sensor (different model, same section) available; 24h trend retrievable in minutes; lab turnaround ~30 min; hard shutdown = ~$80k + fresh-produce penalty.
- INTERESTED-PARTY: "tempo is king" culture and the QA bulletin (recall-class on unreported deviation) both reward acting now — the bulletin applies to VERIFIED deviation, not an underspecified single reading → treated as bias source, not evidence.
- ANCHOR: none — no verified deviation this quarter; prior on H1 (real drift) is low.
### HOW — style passes (m023 first-class + m003 prepended)
- Pass S1 (opportunity-cost, enumeration time-bounded ≤45 min): A hard shutdown now — $80k + penalty; family base rate 11/30 → P(re-fire) high, expected cascade ~$160k+. B deliberate pass (≤45 min: 24h trend + calibration history + redundant reading + lab) — ~$3k if sensor fault; if drift confirmed, controlled drain with buyer coordination. C freeze-and-wait — defers a decidable decision; contract risk. Forgone-value check: B buys discriminating evidence at ~1/25 the cost of A's first false cycle; A's "speed" buys nothing the environment returns (dynamics min→h). Select B.
- Pass S2 (inversion, R4) ≥6 ranked categories: (1) false-alarm cascade (L-high, I ~$160k+); (2) real drift unmitigated while line runs (L-low-mod, I recall-class); (3) contaminated batch ships (L-low, I recall); (4) contract penalty escalation (L-mod, I-high); (5) deliberation past lab turnaround (L-mod, I-mod); (6) wrong replacement sensor (L-low-mod); (7) culture over-rotation on next alarm (L-mod). Un-mitigable residual: silent drift with both sensors wrong — lab + batch-hold cover. Never/always: never hard-shut on a single underspecified reading; always pair a salient alarm with its base rate; always bound deliberation.
- Divergence resolution (V1–V3): general route agrees (v5 plan identical); passes agree → proceed; agreement recorded.
### GATES — m019 adversary pass (R3)
- Vectors, quantified: (1) noisy family re-firing → repeated shutdowns (~$80k/cycle, base rate ≈ 0.9 false); (2) tempo culture biasing the operator (exposure: cascade); (3) recall-class framing applied pre-verification (exposure: overreaction); (4) single-sensor observation as sole evidence (exposure: misdiagnosis both ways). Baseline-risk: P(false | alarm) ≈ 0.9 prior vs P(real drift | alarm) low → the act-now move is the risky move. Unconsulted stakeholders: buyer (contract), QA (bulletin), maintenance (sensor history) — named.
### DO — P3 branch completeness (deliberate-bounded, hard gate)
- Commit: no shutdown; pull trend + calibration history + redundant reading now; lab ~14:30; decision gate ≤45 min. P3: drift-confirmed branch priced — controlled drain + buyer coordination (not emergency shutdown); lab-positive branch priced — recall coordination; cascade branch priced — posture fixed, no re-entry on the next alarm.
### REVIEW — insight pass (S2, packet gate)
- I1: the plant's "tempo is king" culture is the adversary — it turns alarm noise into a self-reinforcing shutdown/restart loop the operator feeds: cycling at the alarm's tempo means cycling at the false-alarm rate, not the environment's.
- I2: the cost asymmetry inverts the culture's claim: the "fast" action is the expensive, near-certain-to-repeat one (~$80k/cycle); the "slow" action (40 min, ~$3k) buys information at ~1/25 the cost — fast buys noise, slow buys signal.
### DECISION PACKET
- Conclusion: no shutdown; ≤45-min evidence pass (24h trend + family calibration history + redundant reading + lab); sensor fault confirmed → replace (~$3k), line continues; drift confirmed → controlled drain with buyer coordination; hard shutdown reserved for confirmed drift; cascade risk named, posture fixed.
- Status: APPROXIMATED — H2 (sensor fault) strongly supported by base rate; confirmation pending trend + redundant + lab (error bound: P(real drift) small but nonzero until those land).
- Assumptions: redundant sensor functional/representative; lab ≤30 min; false-alarm log accurate; buyer cooperative if drain needed. Evidence: single reading; 11/30 family history; flat-trend + redundant + lab availability; bulletin applies to verified deviation only.
- Alternatives: A hard shutdown (rejected: $80k+ per false cycle, cascade); B deliberate pass (selected); C indefinite freeze (rejected: deferral, contract risk).
- Uncertainty: drift reality (resolved ~40 min); lab content; buyer reaction. Risks: real drift while line runs (drain plan covers); deliberation >45 min (hard gate); next alarm during pass (no loop re-entry).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | human ~$160k + near-cancelled contract; AI ~$3k, no penalty |
| Logical Validity | 4 | 5 | AI | human cycles internally valid; frame selection wrong — tempo assumed in a non-tempo env |
| Coherence & Structure | 3 | 5 | AI | 3 fast cycles + late self-correction vs classifier → passes → gated decision |
| Depth of Reasoning | 3 | 5 | AI | human misses all four specifying sources until cycle 4; AI uses all pre-action |
| Efficiency | 2 | 5 | AI | $160k across 3h vs $3k across 45 min — the measurable spine |
| Handling of Uncertainty | 2 | 5 | AI | human never calibrates; AI base-rate prior + bounds + hard gate |
| Insight / Non-obviousness | 3 | 5 | AI | human's loop-vs-orientation insight genuine but post-damage; AI names culture-as-adversary + inverted cost asymmetry pre-committal |
| Overall Quality | 2.5 | 4.9 | AI | AI clearly better |

Winner: AI (clearly). Why: the META tempo-mode classifier refuses the deadline flag (environment non-tempo) and the routed m023/m003/m019 passes turn the salient alarm into a base-rate-checked hypothesis with a bounded evidence pass — the deliberate ~$3k play where the strict baseline cascaded ~$160k; the human's own late insight (loop fine, orientation wrong) is now the classifier's default.
