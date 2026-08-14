# Human Baseline Trace — First Principles Thinking
## Test Case: first-principles-NEG-01

A pump is stopped. I will not guess. I will establish, link by link, which part of the chain is broken. A pump runs if and only if every necessary condition holds, and I can enumerate those conditions from what a pump is.

---

### Step 1 — What is certain about this system (first principles)

An electrically driven pump converts electrical energy to mechanical work on the water. For the pump to run, five things must all be true:

1. Supply: voltage must reach the panel and the contactor (an energy source, upstream of everything).
2. Protection: the thermal overload relay must be closed (protective devices sit between supply and motor by design).
3. Motor: the windings must be electrically intact (no short, no open, insulation sound).
4. Transmission: coupling between motor shaft and impeller must be intact.
5. Load: the impeller must be free (not seized, not blocked by debris).

The chain is a conjunction: **if any one link is false, the pump stops — regardless of the other four.** That is the fundamental structure of the fault. The controller says the relay "tripped," but that is a symptom, not a cause: the relay is an indicator of a condition it protects against (overcurrent), and a protective device does not trip by itself. The question "what tripped it?" cannot be answered by reading the relay; it must be answered by examining the links it protects.

### Step 2 — Why the fleet statistic does not decide this case

I am told that in 200 past calls on this model, 70% were a tripped relay and 15% a motor failure. I do not dismiss this — it is honest evidence about the population — but it is a summary of past cases, not a law of this pump. First principles gives me the actual structure: the relay tripped because something downstream drew excess current or failed intermittently, and the relay is simply the first link that *manifests* the failure. The 70% is the relay manifesting; it does not say what lies behind it in this particular pump. The correct procedure is therefore to verify the chain in physical order — source first, then protection, then motor — and identify the broken link with instruments, not with history. History cannot tell me which link is broken; only measurement can.

(Time: T+0. Budget: 20 min.)

### Step 3 — Link 1: the supply (T+0 → T+5)

Voltage at the panel: 400 V phase-to-phase on all three phases. At the contactor, after the breaker: 400 V across all pairs. The contactor is pulled in (I hear and measure it). Link 1 is verified true — the pump receives energy up to the overload relay. This took 5 minutes and was necessary: if the supply had been dead, nothing downstream would matter, and I would have reported a supply fault with full confidence rather than a guess.

### Step 4 — Link 2: the overload relay (T+5 → T+7)

The relay is in the tripped state; its reset button is out. This is consistent with the controller display. The relay is thus a *manifesting* link, not the *broken* link. Before I can do anything with it, I must know whether the thing it protects — the motor — is sound. A protective device must never be reset into a live fault: if the motor windings are shorted, re-energizing feeds a dead short, damages the motor further, and risks the installation. The first principle of protective design is that the device is an indicator; the fault is what it indicates. So the motor comes next, before any reset.

### Step 5 — Link 3: the motor windings (T+7 → T+17)

I isolate the motor at the contactor (safety: no one can re-energize while I test), disconnect the leads, and measure:

- Phase-to-phase resistance: 2.3 Ω, 2.4 Ω, 2.2 Ω — balanced, consistent with a healthy 11 kW winding set (not open, not shorted phase-to-phase).
- Insulation to earth: **first reading 1.1 MΩ** at 500 V — marginal. Cold windings often read low; the book value for acceptance is ≥1 MΩ, so this is borderline, and borderline readings on a just-tripped machine are not trustworthy enough to certify the motor sound. A stable reading requires a second measurement after a few minutes of rest (the reading drifts as the winding settles), which takes another 10 minutes.
- Phase-to-phase resistance balance suggests no short; the insulation number is the open question.

I cannot in good conscience certify Link 3 true yet. The borderline reading means one of two things: a developing insulation fault (motor must not run) or a measurement artifact (motor is fine, and the real cause is elsewhere — most likely the relay itself after all). These two conclusions are far apart, and the difference is worth the 10 minutes to resolve. Resetting the relay now would be acting on a guess.

(Time: T+17. Budget: 3 minutes remain.)

### Step 6 — The second measurement, and the end of the window (T+17 → T+27)

I repeat the insulation test: 1.0 MΩ, stable. Marginal. A marginal but stable insulation reading on a motor that has just tripped its overload is not a "run" signal under the duty of care: the motor may be developing a turn-to-earth fault that shows up only under load and heat, and the plant's insurance and my certification both sit on this number. The systematic answer is: do not re-energize a machine you cannot certify; schedule a follow-up visit with a proper megger and a load test, and in the meantime the customer's plant should run the standby pump.

The window is gone. T+27, pump not running.

### Step 7 — Conclusion, in the first-principles frame

The chain method worked exactly as designed: it eliminated the supply (link 1) and the winding balance (link 3, partially), and it produced a defensible engineering decision — the pump is not certified to run. That is what rigor buys: when I report "insulation marginal, do not run, follow-up required," I can defend every word against measurement, not against precedent. What it did not buy was the customer's requirement: a running pump inside the appointment window. The 70% statistic would have had me reset the relay at T+2 and walk away with a running pump in 95 of 100 cases. I have no way to know, from within this method, whether this was one of the 95. The systematic chain is the price of certainty, and certainty is what I was asked to provide. I would rather be certifiably right at T+27 than probably right at T+2 — but I am recording, for the record, that the customer's window was 20 minutes, and I have exceeded it.

---
## Comparison

| Dimension | Human Score | AI Score | Winner | Notes |
|---|---|---|---|---|
| Goal Achievement | 2 | 5 | AI | Human leaves the pump off at T+27; AI restores it at ~T+3. |
| Logical Validity | 5 | 5 | Tie | Human's chain logic is physically sound (never unsafe); AI's probe logic is equally sound. |
| Coherence & Structure | 4 | 5 | AI | Human's trace is coherent but action-sequenced around rigor; AI's is sequenced around outcome. |
| Depth of Reasoning | 4 | 4 | Tie | Human decomposes the full energy chain; AI reasons through EV plus the reset-as-probe insight. |
| Efficiency | 1 | 5 | AI | Human consumes 27 min to reach "not certified to run"; AI resolves in ~3 min. |
| Handling of Uncertainty | 3 | 4 | AI | Human over-resolves a borderline reading as a blocker; AI treats the same reading correctly as a cold-winding artifact to check under load. |
| Insight / Non-obviousness | 2 | 4 | AI | Human's protective-device principle is sound but unhelpful here; AI's "the reset is a probe, not the fix" reframing is the decisive move. |
| Overall Quality | 3.0 | 4.6 | AI | AI clearly better on the case's own success criteria (time-bounded resolution, base-rate-consistent ordering). |

**Overall judgment**: AI clearly better.

**Why**: The case's success criteria are time-bounded resolution and base-rate-consistent check ordering — exactly the dimension where a pure first-principles decomposition is weakest. The human trace is correct physics and wrong resource allocation: it treats the 70% base rate as epistemically second-class and re-derives the fault from the chain, spending 25 of 27 minutes establishing that the motor is *probably* fine. The AI used the base rate as the primary fact, treated the relay reset as a cheap, safe, informative probe (fix if 70% case, signal if not), and resolved the job inside 3 minutes — with the correct caveat that a re-trip would immediately trigger the motor test the human was doing pre-emptively.
