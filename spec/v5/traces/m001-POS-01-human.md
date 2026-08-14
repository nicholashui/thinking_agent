# Human Baseline Trace — First Principles Thinking
## Test Case: m001-POS-01

I will not start from "we always use 12 mm." I will start from what cannot be doubted.

### Step 1 — Fundamental facts
1. Pressure in a fluid at depth is the weight of the column above per unit area: p = ρgh. That is a definition, not a rule of thumb.
2. A pressurized sphere carries load as membrane stress: σ = pr/2t — but only while t ≪ r. I must check the limit, not assume it.
3. Mass = density × volume. Buoyancy: the shell displaces its volume of water; it floats iff displaced water mass > shell mass.

### Step 2 — Pressure, with units
p = ρgh = 1025 kg/m³ × 9.81 m/s² × 3000 m = 30,165,750 Pa ≈ 30.2 MPa.
Unit check: (kg/m³)(m/s²)(m) = kg/(m·s²) = Pa. ✓

### Step 3 — Wall thickness
Membrane: σ = pr/2t → t = pr/(2σ) = 30.17×10⁶ Pa × 0.30 m / (2 × 200×10⁶ Pa) = 0.0226 m ≈ 22.6 mm.
Validity check: t/r = 22.6 mm / 300 mm = 0.075 < 0.1 → the thin-wall model is legitimate here. If it had failed, I would have to solve the Lamé thick-wall problem; it does not.

### Step 4 — Shell mass
Volume of shell ≈ surface area × thickness = 4π(0.30 m)² × 0.0226 m = 1.131 m² × 0.0226 m = 0.0256 m³.
Mass = 0.0256 m³ × 2700 kg/m³ = 69.1 kg ≈ 69 kg.

### Step 5 — Float or sink
A closed shell displaces its outer volume ≈ (4/3)πr³ = 4.189 × 0.027 m³ = 0.113 m³.
Displaced water mass = 0.113 m³ × 1025 kg/m³ = 116 kg. Shell weighs 69 kg < 116 kg → it FLOATS.
Ballast to sink it: 116 − 69 ≈ 47 kg, plus margin for cables and sensors. This is not decoration: at 3000 m, a positively buoyant instrument floats up and is lost.

### Step 6 — The colleague's 12 mm: convert, don't copy
The 12 mm comes from steel at 2000 m. Scale it from the same fundamentals — same radius, seawater cancels: t ∝ ρgh/σ_allow.
Factor = (3000 m / 2000 m) × (250 MPa / 200 MPa) = 1.5 × 1.25 = 1.875.
Predicted aluminum thickness = 12 mm × 1.875 = 22.5 mm — my derived 22.6 mm within 0.5%. The analogy, correctly converted, CONFIRMS the derivation; copied raw, it is 47% too thin and would collapse at depth.

### Step 7 — Uncertainty
Geometry and density are exact inputs. σ_allow is a design decision: ±10% → t between 20.6 and 25.0 mm. ρ_w varies ±2% with depth/temperature → t moves < 1%. The dominant practical risk is manufacturing tolerance — specify a manufactured wall ≥ 23 mm.

### Conclusion
p = 30.2 MPa; t = 22.6 mm (t/r = 0.075, thin-wall valid); shell mass ≈ 69 kg; the housing floats (116 kg displacement) and needs ≈ 47 kg of ballast. Every number derives from ρgh, pr/2t, ρV, and water density — nothing inherited from "how we always do it"; and the inherited number, once converted rather than copied, agrees with the derivation.
