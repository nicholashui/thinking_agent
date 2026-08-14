# v6 Routed AI Trace — m001-POS-01 (blinded)
## Deep-sea sphere housing (3000 m) — phone call, pencil and paper
### META (routing — blind router output)
- Signature: d:engineering,finance,medical | g:decide,guarantee,maximize,predict | c:deadline
- Router top3: m001, m020, m023; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m001 + m020 first-class passes, synthesized (m023 = synthesis context). Gate (R3): m003 inversion. Flags: tempo mode ON (P2); closed-scope fast-path candidate (P8).
### WHAT — frame + structure-first scan (S1)
- Guarantee problem: survive 3000 m; deliverables p, t (with model-validity check), mass, float/ballast. The 12 mm figure is experience memory, not a design input. Structure: hydrostatic column → membrane stress in spherical shell; buoyancy = displaced-volume balance.
### WHY — P1 input-provenance audit
- MEASURED/given (trust): ρ_w 1025, g 9.81, r 0.30 m, σ_allow 200 MPa (safety factor applied). ANCHOR (not evidence): 12 mm from steel@2000 m, 250 MPa; colleague benefits from reuse (schedule), not structural truth → convertible only via the same fundamentals. H1 thin-wall valid (falsifier: t/r > 0.1); H2 thick-wall Lamé.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (derive-from-fundamentals: units carried; calibration anchor): p = ρgh = 1025×9.81×3000 = 30.17 MPa [(kg/m³)(m/s²)(m)=Pa ✓]; t = pr/2σ = 30.17e6×0.30/(2×200e6) = 22.6 mm; t/r = 0.075 < 0.1 → thin-wall holds, Lamé excluded by bound; V = 4πr²t = 0.0256 m³ → m = 69.1 kg; displaces 0.113 m³ → 116 kg seawater → FLOATS, ballast ≈ 47 kg.
- Calibration anchor: convert 12 mm memory via same fundamentals — (3000/2000)×(250/200) = 1.875 → 22.5 mm, 0.5% agreement; copied raw it is 47% under-thickness → collapse at depth.
- Pass S2 (pre-mortem: failure assumed, causes RANKED — "lists without ranking" weakness gate-checked): F1 collapse at depth (12 mm copied / σ exceeded) L-high I-catastrophic; F2 floats away unballasted L-mod I-total; F3 weld/penetration leak, wall-thinning L-low-mod; F4 casting porosity L-low (QA, not design).
- Synthesis (V1–V3): passes AGREE with the general route's arithmetic → proceed, agreement recorded. m023 context: steel competence transfers poorly to 3000 m aluminum — reuse economy is the analogy's real cost.
### GATES — m003 inversion (R3)
- ≥6 failure categories ranked L×I: (1) hydrostatic collapse high/catastrophic; (2) buckling low; (3) float-away mod/total; (4) σ_allow misestimate (±10% → t ∈ 20.6–25.0 mm); (5) manufacturing wall-thinning mod; (6) inner-vs-outer radius slip (≈1.4%, use r_inner); (7) ρ drift <1%; (8) corrosion/aging low.
- Un-mitigable residual: unknown material flaw — QA/NDT owns it. Never/always: never ship thinner than the derivation permits; always convert inherited figures before reuse; always float/ballast-check closed air-filled housings.
### DO — P8 fast path + P2 tempo commit
- Deliverable is numbers (internal action). Commit at DO: t = 22.6 mm, manufacture ≥ 23 mm; ballast ≈ 47 kg + margin. P3: failure branch priced — Lamé required only if t/r failed; bound passed, excluded.
### REVIEW — insight pass (S2, packet gate)
- I1: the colleague's memory, CONVERTED, is the strongest independent verification the shop already owns — the shortcut becomes the check (22.5 vs 22.6 mm).
- I2: a closed air-filled shell is self-removing: needs ≈ 70% of its own mass (47/69 kg) as ballast — flotation is a design failure mode, not a launch problem.
### DECISION PACKET
- Conclusion: p = 30.2 MPa; t = 22.6 mm (t/r 0.075, thin-wall valid); m ≈ 69 kg; floats (116 kg) → ballast ≈ 47 kg. Raw 12 mm carryover 47% too thin.
- Status: SOLVED (exact arithmetic, dual-route verified, no external action). Assumptions: uniform ρ_w; σ_allow pre-factored; no penetrations; r = inner radius.
- Evidence: 30.17 MPa; 22.6 mm; t/r 0.075; 69.1 kg; 116 kg; 47 kg; scaled analogy 22.5 mm (0.5%).
- Alternatives: membrane (selected); thick-wall (excluded by bound); raw analogy (rejected, 1.88× under-thickness); steel housing (out of scope).
- Uncertainty: σ ±10% → 20.6–25.0 mm; ρ ±2% → <1%; dominant residual = manufacturing tolerance → ≥ 23 mm. Risks: implosion if analogy copied; float-away if unballasted; future penetrations; material flaw (QA).

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | identical numbers vs reference |
| Logical Validity | 5 | 5 | Tie | both bound-check, both convert the analogy |
| Coherence & Structure | 4 | 5 | AI | routed dual-pass + gate + packet |
| Depth of Reasoning | 5 | 5 | Tie | human σ-sensitivity matched; AI adds ranked pre-mortem + 8-category inversion |
| Efficiency | 3 | 4.5 | AI | human rewrites identities; v6 passes stay lean |
| Handling of Uncertainty | 5 | 5 | Tie | AI prices σ/ρ/tolerance like the human |
| Insight / Non-obviousness | 4 | 5 | AI | float-away pre-mortem; converted-analogy-as-verification; ballast ≈ 70% of own mass |
| Overall Quality | 4.7 | 4.9 | AI | correctness tied; routed pass closed v5's depth/consequence gaps |

Winner: AI (narrow). Why: the routed pre-mortem and inversion gate moved consequence-checking (float/ballast) and calibration depth (σ/tolerance) from REVIEW afterthoughts into first-class completed outputs — the two gaps where the non-routed v5 AI lost to this baseline.
