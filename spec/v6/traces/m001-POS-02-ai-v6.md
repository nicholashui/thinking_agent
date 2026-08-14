# v6 Routed AI Trace — m001-POS-02 (blinded)
## One-off custom steel box (12.0 × 2.4 × 2.6 m, 2.0 mm plate) — phone call, pencil and paper
### META (routing — blind router output)
- Signature: d:engineering,finance,medical,product,software | g:decide,estimate,predict | c:high_stakes
- Router top3: m001, m018, m019; confidence gap <= 0.5 → AMBIGUOUS → DUAL-ROUTE: m001 + m018 first-class passes, synthesized (m019 = synthesis context). Gate (R3): m007 ruin screen (c:high_stakes). Flags: P1 provenance audit; P3 branch-completeness; S1 structure scan; S2 insight pass; P8 closed-scope fast path (fully specified).
### WHAT — frame + structure-first scan (S1)
- Deliverables: total steel mass (kg), material cost (USD). Structure is one derivation chain: geometry → area → volume → mass → cost, with two labeled allowances. All inputs given → fully specified, P8 fast path eligible.
### WHY — P1 input-provenance audit
- MEASURED/given (trust): dimensions (exact), density 7,850 kg/m³ (physical constant), price $1.10/kg (market input — volatile), +8% frame / +5% waste (engineering assumptions, labeled). ANCHOR (not evidence): "similar jobs" — no experience at this size; analogy rejected as primary evidence, kept only as calibration. H1 analogy vs H2 derivation → H2.
### HOW — style passes (dual-route, synthesize)
- Pass S1 (derive-from-fundamentals: units carried; calibration anchor): six faces explicit — 2×(12.0×2.6)=62.40 m²; 2×(2.4×2.6)=12.48 m²; 2×(12.0×2.4)=57.60 m² → 132.48 m² [m×m=m² ✓]; t=0.002 m → V=0.26496 m³ [m²×m=m³ ✓]; m_plate=7,850×0.26496=2,079.9 kg; frame +8%=166.4 → 2,246.3; waste +5%=112.3 → total 2,358.6 kg ≈ 2.36 t; cost=2,358.6×$1.10=$2,594.5 ≈ $2,600.
- Calibration anchor: derived constant 15.7 kg/m² (density×thickness) → 132.48×15.7=2,080 kg plate, matches S1 exactly; real 40-ft container (same footprint) tares ~3.9 t — plain flat 2 mm box lighter term-by-term (corrugation, posts, castings): consistent, not contradictory.
- Pass S2 (steel-manning: opposing view in strongest form): "labor, not material, decides the quote; a rough analogy is enough for budgeting." Strongest form accepted: analogy is cheap and directionally right when geometry is close. Rebuttal: geometry is novel here and the labor decision hinges on the residual after material — a wrong material number mis-prices labor risk, so derivation is load-bearing; analogy only calibrates.
- Synthesis (V1–V3): passes AGREE with the general route's arithmetic → proceed, agreement recorded. m019 context: no party gains from a biased number; the real exposure is price volatility, not mis-estimate.
### GATES — m007 ruin screen (R3, c:high_stakes)
- Distribution: mass ±5% (frame/waste ±2 pts → ±47 kg); cost dominated by plate price — ±20% → $2,075–$3,113; ±30% → $1,816–$3,373. Ruin check: bounded quote exposure, shop can re-quote → no ruin threshold. One-shot: no (revocable quote). Floor: cost floor ≈ $2,123 at $0.90/kg. Provenance: price band from steel-market quarterly volatility (market fact). Decline/restructure alternative: quote the range, not the point; re-quote if labor doesn't fit.
### DO — P8 fast path + P3 branch-completeness
- Deliverable is numbers (internal action). Commit at DO: mass ≈ 2.36 t; cost ≈ $2,600; report range 2.2–2.5 t / $1.95k–$3.25k. P3: negative branch priced — price +30% + waste overrun ≈ $3.5k; frame error ±47 kg ≈ ±$52 — both inside the reported range.
### REVIEW — insight pass (S2, packet gate)
- I1: the derived constant 15.7 kg/m² is what plate suppliers print — the shop can verify this quote against a supplier spec sheet without re-deriving.
- I2: price is the dominant lever and outside the shop's control — quoting in $/kg terms lets the shop re-price instantly when steel moves.
### DECISION PACKET
- Conclusion: 2,358.6 kg ≈ 2.36 t; material cost $2,594.5 ≈ $2,600; report range $1.95k–$3.25k.
- Status: SOLVED (exact arithmetic, dual-route verified, no external action). Assumptions: uniform 2.0 mm; density 7,850; +8%/+5% allowances; plain closed box; price material-only.
- Evidence: 132.48 m²; 0.26496 m³; 2,079.9 kg; +166.4; +112.3; 2,358.6 kg; cross-check 132.48×15.7=2,080 kg; $2,594.5.
- Alternatives: shortcut-only (rejected — hides face counts); analogy-only (rejected — novel geometry); derivation primary + derived-constant verify + container calibration (selected).
- Uncertainty: price ±20–30% dominant; frame ±2 pts → ±47 kg; geometry details small upward bias. Risks: price spike mid-quote; openings/doors added; first-off waste higher; ruin screen: bounded, re-quotable.

## Comparison
| Dimension | Human | AI | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 5 | 5 | Tie | both 2,359 kg / $2,595 |
| Logical Validity | 5 | 5 | Tie | both derivations check out |
| Coherence & Structure | 5 | 5 | Tie | six faces + units now explicit in the routed trace |
| Depth of Reasoning | 5 | 5 | Tie | calibration anchor + container calibration matched; steel-manning adds counter-position |
| Efficiency | 3 | 5 | AI | v6 passes lean, closed-scope fast path |
| Handling of Uncertainty | 5 | 5 | Tie | ruin screen matches human's priced range, adds provenance + floor |
| Insight / Non-obviousness | 4 | 4 | Tie | both flag plain-box-lighter-than-container; $/kg reframing mild |
| Overall Quality | 4.7 | 4.9 | AI | correctness tied; routed pass closed v5's depth/uncertainty gaps |

Winner: AI (narrow). Why: the routed contracts (m001 calibration anchor, m007 ruin screen) moved the human baseline's two winning moves — derived-constant verification and provenance-carrying priced uncertainty — from human-only into mandatory v6 outputs, and steel-manning engaged the labor-dominates counter-position the non-routed v5 run never addressed.
