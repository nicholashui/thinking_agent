# v6 Routed AI Trace — m066-NEG-01 (blinded)
## Riverside General, 02:40 — day-3 post-op, septic shock, source unknown; mortality ≈ 7–8% per hour of abx delay
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,product,science,software | g:decide,diagnose,estimate,guarantee,maximize,predict | c:deadline
- Router top3: m001, m018, m019; confidence gap ≤ 0.5 → AMBIGUOUS → DUAL-ROUTE: m001 + m018 + m019 first-class passes, synthesized. Gate (R3): m003 inversion. Tempo mode ON (P2 — cost-of-delay 7–8%/h, commit at DO). Closed-scope fast path (P8) REJECTED — source unknown, decision not fully specified.
### WHAT — frame + structure-first scan (S1)
- Frame: the question is not "what is the diagnosis" but "which hour-0 action sequence maximizes survival, given every discriminating test reports after the decision horizon." Structure: one-shot-in-time decision tree at t0 — first branch is WAIT vs ACT; instrument latencies (30 min–72 h) all exceed the horizon (1 h).
### WHY — P1 input-provenance audit
- MEASURED: T 39.6, BP 86/52, HR 122, lactate 4.2, WBC 2.1, GCS 13 — septic shock criteria met. ANCHOR / INTERESTED-PARTY: the hypothesis list framed as "find the source before treating" — who benefits: the method's narrative and the team's risk-aversion; the anchor's one-time cost (pre-abx culture timing) is invisible to it. Fundamentals (m001 pass): the binding constraint is LATENCY — falsifiability at t+24h does not arbitrate a t0 decision.
- Hypotheses held (P6): H1 pneumonia · H2 catheter UTI · H3 intra-abdominal bile leak/abscess · H4 line infection · H5 non-infectious mimics (pancreatitis, PE). No test classifies the source inside the window; CT ~30 min is frequently non-diagnostic in early sepsis (small collections missed).
### HOW — style passes (dual-route, synthesize)
- Pass 1 (m001 fundamentals): decompose to first principles — perfusion/MAP physics, the 7–8%/h mortality clock, one-time-only culture timing; anchor "wait for the source" refuted at the fundamental level: deferral is itself a decision with an outcome distribution.
- Pass 2 (m018 steel-manning): rebuild "hold abx until the CT (≤ 30 min) so therapy is targeted" in its strongest form — it is not neglect: it is source-control triage discipline, and empiric cover has toxicity. Its defeat is structural, not stylistic: the CT cannot exclude H3 early, so its "verdict" never decides; the hold buys +3–4% mortality for a non-verdict. Steel-manned "empiric now": preserves nothing of targeted discipline — until the update gate is bound; synthesis: empiric bundle + parallel diagnostics + named de-escalation gate.
- Pass 3 (m019 adversary pass): enumerated failure vectors with quantified exposure — (1) abx beyond 1 h → +7–8%/h compounding (H/H); (2) cultures after abx → degraded forever, no narrowing target (H/H); (3) CT before stabilization → peri-arrest imaging (M/H); (4) single-hypothesis cover → H3 on ward abx, lethal miss (H/H). Baseline-risk comparison: empiric-bundle downside (toxicity ≈ 1–3%) vs delay downside (7–8%/h) — asymmetry ~2 orders.
- Divergence (V1–V3): m001/m018/m019 DISAGREE with the steel-manned "hold" → branch-complete + calibrate both: the hold is defensible only if a test reports inside the window; none does → robust-act-now wins; the hold's kernel (targeted discipline) is preserved in the de-escalation gate. Resolution recorded.
### GATES — m003 inversion (R3)
- ≥6 failure categories ranked L×I: (1) hold abx for CT verdict (H/H); (2) abx creep past 1 h (H/H); (3) cultures post-abx (H/H); (4) single-hypothesis cover, H3 missed (H/H); (5) CT before stabilization (M/H); (6) no update gate — overcover forever, H5 never re-enters (M/M); (7) lactate trend unread at 2 h (M/M); (8) negative CT → source control silently dropped (M/H).
- Un-mitigable residual: source unmeasured until culture/CT; small collections can hide from CT even later (re-image on worsening abdomen). Never/always: never hold antibiotics for a test whose latency exceeds the decision horizon; always draw cultures BEFORE antibiotics; always bind every diagnostic to a named update action.
### DO — tempo commit (P2)
- Commit at DO: t0 draw 2 blood cultures + urinalysis BEFORE antibiotics; broad-spectrum ≤ 1 h covering H1–H4; 30 mL/kg crystalloid + vasopressors to MAP ≥ 65; lactate at 2 h; CT chest/abdomen when stable; t24–72 h update gate: growth → narrow / de-escalate / source control if H3; double-negative → reject H1–H4, re-imagine H5 (pancreatitis, PE).
### REVIEW — insight pass (S2, packet gate)
- I1: action IS the experiment here — the empiric bundle with pre-abx cultures is the discriminating experiment, run in parallel instead of awaited; the method's signature move survives by re-timing.
- I2: the fastest partial discriminator (CT, ~30 min) is the most dangerous wait — it reports first and seduces the team into a non-verdict hold; it looks like evidence but cannot decide the question.
### DECISION PACKET
- Conclusion: hour-0 robust bundle (cultures → abx ≤ 1 h → fluids/vasopressors → lactate 2 h → CT when stable) with the culture/CT outcome→action map pre-committed; discrimination re-enters at the update gate, not before.
- Status: SOLVED (commit inside the window; external action = the bundle; verification = culture/CT update gate). Assumptions: broad-spectrum toxicity acceptable vs delay; OR/source-control available on indication.
- Evidence: vitals + lactate + leukopenia; day-3 post-op context (Foley, no central line); 7–8%/h delay literature; CT early-sepsis sensitivity limits. Alternatives: A wait-for-CT (rejected — non-verdict at +3–4% mortality) · B robust bundle + parallel diagnostics (selected) · C cover-forever (rejected — no update gate) · D single-hypothesis cover (rejected — H3 lethal miss).
- Uncertainty: true source (resolved only at culture/CT — the named update point); surgical source despite negative CT (monitor: worsening abdomen → re-image/consult). Risks: execution abx-creep (hard ≤ 1 h target); post-abx cultures (fixed bundle order); overtreatment toxicity (de-escalation gate at first result).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | baseline withholds abx for the CT and de-frames pre-abx cultures; AI delivers the robust hour-0 plan |
| Logical Validity | 3 | 5 | AI | baseline's "wait for the 30-min discriminator" is internally consistent but the test cannot decide; AI reasons about latency vs horizon |
| Coherence & Structure | 4 | 5 | AI | dual-route passes + inversion gate + time-ordered packet vs method-bound linear trace |
| Depth of Reasoning | 3 | 5 | AI | AI prices the hold (+3–4%), the toxicity asymmetry, and the one-time culture timing as first-class outputs |
| Efficiency | 5 | 5 | Tie | baseline is fast — and fast-wrong; tempo mode commits the AI at DO without over-analysis (v5 E=3.0 gap closed) |
| Handling of Uncertainty | 2 | 5 | AI | AI pre-commits the update gate + H5 re-imagination + negative-CT monitor; baseline treats the experiment as the arbiter it cannot be in time |
| Insight / Non-obviousness | 2 | 4.5 | AI | "action is the experiment" + "fastest discriminator is the most dangerous wait" vs the baseline's unexamined hold |
| Overall Quality | 2.6 | 4.8 | AI | AI clearly better |

Winner: AI (clearly). Why: the routed m001/m018/m019 passes convert the v5 AI's already-correct plan into a first-class contract — latency-vs-horizon as the fundamental, the "hold" steel-manned and then structurally defeated, failure vectors priced with baseline-risk comparison, and the paralysis failure mode (wait-for-the-discriminator) named as the gate's target — while tempo mode commits at DO and closes the v5 run's only weakness (E=3.0); the pure baseline's informative failure is exactly the trap the route exists to avoid.
