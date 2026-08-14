# AI Thinking Agent Trace
## Test Case: first-principles-NEG-01

---

### META — classify context, stakes, effort

- **Task type**: time-bounded field diagnosis with a physical action (restore a pump).
- **Stakes**: moderate — customer downtime; a wrong re-energization can damage equipment, so safety is in scope; but no life-safety.
- **Environment**: on-site, 20-minute window, multimeter + tools, next job booked.
- **Effort level**: fast-path eligible? No — this is an action task requiring an explicit decision record, but the *reasoning* budget should be minutes, not iterations: the dominant fact is handed to me in the base rates.
- **Class**: diagnosis with known base rates and known step costs — an expected-value sequencing problem, not an open investigation.

### WHAT — frame + gate

**Key question**: Get the pump running (or isolate the fault with certainty) within the 20-minute window, without unsafe steps.

**Success metrics**:
1. Pump running or fault definitively isolated at ≤20 minutes.
2. Check order consistent with expected-value ranking given the base rates and step costs.
3. No unsafe step (never reset a protective device into a known live fault; never leave a protective device disabled).

**Exit gate**: pass when the pump runs and stays running, or the fault is isolated, inside the window. This task requires DO (external action).

### WHY — diagnose

Hypotheses, from most to least probable (fleet data is direct evidence on this exact model, n=200):

- **H1: thermal overload relay tripped (70%)** — consistent with controller showing "trip"; no noises/smells reported (a motor winding fault usually presents with smell, heat, or current asymmetry by the time it trips an overload).
- **H2: motor winding failure (15%)** — would explain a *hard* trip; but the reported symptoms (quiet, no smell, trip shown on the relay) fit H1 better.
- **H3: supply/contactor fault (10%)** — would usually show on panel indication or prevent the relay from even reading; controller shows a trip, which implies the protection chain is alive and did its job — weakens H3.
- **H4: other (5%)** — residual; can't be sequenced against.

**Evidence**: the controller's "trip" indication is itself evidence FOR H1's mechanism: the relay tripped, i.e., the protection link functioned. The absence of smell/heat/odd noise is weak evidence against H2 (motor faults are usually audible/smelly when they trip an overload). The base rate and the symptom evidence point the same way.

**Falsification**: H1 is falsified by the relay refusing to latch (mechanical failure) or by the pump re-tripping immediately after reset (→ H2/H3, motor test next). Note: a re-trip *after* reset is the clean, low-cost discriminator between H1 and H2 — the reset is not only a candidate fix, it is also a diagnostic probe. That property is what makes it the right first step even if it were only 30% probable.

### HOW — generate alternatives, verify, select

- **Alt A — physical chain trace (systematic)**: verify supply → contactor → motor → load in dependency order before touching the relay. Cost: ≥20 min (5+5+10), likely exceeds window even if it lands on the relay late. Never unsafe, but cannot meet success metric 1 for the common case.
- **Alt B — expected-value ordering**: relay reset first (70%, 2 min) → if re-trips, supply check (5 min) → if clean, motor test (10 min). E[time to resolve] = 0.70×2 + 0.10×7 + 0.15×12 ≈ 4.7 min; 95% coverage (5% other unresolvable). Fully inside window; reset is safe *because* the controller shows a trip on a protective device (the protection function worked), and because we stay present to observe the outcome.
- **Alt C — replace the starter/relay outright**: parts cost + wait time; unjustified before a 2-min check.

**Verify**: compute EV for A's order: 0.70×15 + 0.10×20 + 0.15×22 ≈ 15.8 min before likely resolution — marginal at best; if motor test runs first, worse. B's 4.7 min dominates. Safety check for B: resetting a relay that has *already* tripped is not "defeating a protection device" — the protection did its job; we are merely resetting it to observe the system, with the motor protection still in circuit. This is standard, safe practice.

**Decision record**: select **B**. A is sound physics but fails the stated success metrics on expected cost; C is wasteful. B also has the best information structure: it costs 2 minutes and partitions the hypothesis space (runs → H1 confirmed; immediate re-trip → H2 likely → motor test, 10 min, still inside window).

### DO — execute

1. T+0–2: Locate relay on the contactor. Reset it (press and hold until latch). No meter needed.
2. T+2: Energize via the controller start button. Pump starts, holds, builds normal pressure.
3. T+3: Observe 1 minute — no re-trip, steady current on the display, no abnormal noise.
4. T+4: **Done. Pump running.** Job complete at ~T+4, well inside the 20-minute window.
5. Note for the customer: if it trips again within the next shifts, call back — that pattern indicates the motor test (H2), and I log that the winding insulation reading on a cold, just-tripped motor is not a reliable pass/fail without a load run; the running behavior is the test.

### REVIEW — after-action

- What worked: treating the reset as a probe rather than a "fix" — the 2-minute action resolved the 70% case and cleanly partitions the remaining hypotheses.
- What I must not lose: when base rates are given, use them as the primary sequencing input; a physical-chain analysis is the tie-breaker, not the default.
- What was avoided: the systematic trace (Alt A) would have consumed the window on a 70% case; the EV pass is what kept the customer's deadline.
- Improvement queued: in diagnosis tasks, always make a one-line EV table before touching hardware when base rates are available.

---

## §15.4 Decision Packet

- **Conclusion**: The thermal overload relay had tripped. Reset + observe restored the pump in ~4 minutes. If a re-trip occurs within the next shifts, the follow-up is a motor winding test (H2 path). Job closed.
- **Status**: SOLVED — outcome verified by direct observation (pump running, no re-trip, normal current on display) inside the time budget.
- **Assumptions**: fleet base rates (n=200, same model) are accurate; controller "trip" indication is trustworthy; no visual evidence of burning/smell that would contraindicate reset; protection remained in circuit throughout (no defeat devices).
- **Evidence**: controller state at arrival ("trip" on overload relay); relay found in tripped state; successful reset → normal start → 1-minute steady run; current display stable.
- **Alternatives**: A (full physical chain trace, E≈15.8+ min) rejected on expected cost; C (pre-emptive starter replacement) rejected on cost/need. Selected: B (EV-ordered, reset-as-probe), E[time-to-resolve] ≈ 4.7 min, 95% coverage.
- **Uncertainty**: 5% "other" residual (not resolved by this sequence — if it recurs without re-trip, escalate to specialist); H2 remains possible but is now evidenced-against (running clean for 1 min under start current); the 70/15/10/5 split has sampling error (±6–7% at n=200).
- **Risks**: re-trip during run (motor fault) — mitigated by staying present and logging follow-up; customer equipment damage — none incurred (protection never disabled); time overrun — none (4 min used of 20).

---
## Comparison

| Dimension | Human Score | AI Score | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human leaves the pump off at T+27; AI restores it at ~T+4. |
| Logical Validity | 5 | 5 | Tie | Human's chain logic is physically sound (never unsafe); AI's probe logic is equally sound. |
| Coherence & Structure | 4 | 5 | AI | Human's trace is coherent but action-sequenced around rigor; AI's is sequenced around outcome. |
| Depth of Reasoning | 4 | 4 | Tie | Human decomposes the full energy chain; AI reasons through EV plus the reset-as-probe insight. |
| Efficiency | 1 | 5 | AI | Human consumes 27 min to reach "not certified to run"; AI resolves in ~4 min. |
| Handling of Uncertainty | 3 | 4 | AI | Human over-resolves a borderline reading as a blocker; AI treats the same reading correctly as a cold-winding artifact to check under load. |
| Insight / Non-obviousness | 2 | 4 | AI | Human's protective-device principle is sound but unhelpful here; AI's "the reset is a probe, not the fix" reframing is the decisive move. |
| Overall Quality | 3.0 | 4.6 | AI | AI clearly better on the case's own success criteria (time-bounded resolution, base-rate-consistent ordering). |

**Overall judgment**: AI clearly better.

**Why**: The case's success criteria are time-bounded resolution and base-rate-consistent check ordering — exactly the dimension where a pure first-principles decomposition is weakest. The human trace is correct physics and wrong resource allocation: it treats the 70% base rate as epistemically second-class and re-derives the fault from the chain, spending 25 of 27 minutes establishing that the motor is *probably* fine. The AI used the base rate as the primary fact, treated the relay reset as a cheap, safe, informative probe (fix if 70% case, signal if not), and resolved the job inside 4 minutes — with the correct caveat that a re-trip would immediately trigger the motor test the human was doing pre-emptively.
