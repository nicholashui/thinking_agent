# Human Baseline — m090-NEG-01
## Style: Minimum Viable Experiment (Build-Measure-Learn) (pure) — visible reasoning trace

**Step 1 — The assumption.** Will clinicians act on Sable's alerts? That is a hypothesis, and I do not commit $2.1M to a hypothesis. So the smallest experiment that validates or kills it: the 2-ICU pilot — side-channel tablet entry, alerts to clinicians, 3 months, pre-committed bar ≥40% alert response.

**Step 2 — The result.** 80% alert response — double the bar. Nurses say it fits the shift workflow. The assumption is validated; no further experimentation is needed on whether clinicians will use it: they will.

**Step 3 — So the decision is made: commit.** "Validated, now commit" — the whole build-measure-learn loop, done properly. Start the $2.1M rollout.

**Step 4 — The constraints surface.** Vendor integration queue 6-9 months; security review ~3 months; HIPAA ~2 months; board gate in 5 weeks; a refundable 25% deposit ($525K) reserves the slot. These are execution logistics, not hypotheses — but before I sink $525K into a deposit, one more honest experiment: a sandbox integration pilot. Cheap, and it validates that the EMR integration actually works before we commit the deposit.

**Step 5 — The trap.** The sandbox pilot takes 8 weeks. It cannot produce certification — no sandbox can; security review and HIPAA sign-off are audits with lead times, not testable behaviors; and the vendor's slot and the 5-week board gate do not wait. The "one more experiment" stalls the unavoidable commitment: the board cycle slips ~10 months, and the pilot's output — whether a sandbox demo works — could not change the go decision anyway: there is no alternative to Sable, and the deposit is refundable.

**Step 6 — What the rigor missed.** The first pilot measured the easiest assumption — will clinicians respond to alerts: the lowest-risk component, answered at 80% — and I treated it as the gate for the whole $2.1M. The gating facts — certification, security, HIPAA, production false-alarm rate — were never testable by any small experiment; they are commitments with lead times. The experiment became the product decision, and the product decision was the experiment.

**Trace summary box.** hypothesis: clinician adoption → pilot: 2 ICUs, 3 mo, ≥40% bar → 80% → "validated, commit" → integration 6-9 mo / security / HIPAA / board in 5 wks / $525K refundable deposit → demands sandbox integration pilot first → cannot certify, blows the window → MVP theater: the test validated a non-gating assumption while the commitment was required all along.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Build-Measure-Learn — which is the point: the style's own machinery (hypothesis → experiment → bar → commit) is executed correctly and still fails, because the pilot gated the wrong assumption and the reflex at the real commitment is another experiment that cannot produce the gating facts. This is the registered weakness: MVP theater — the test is mistaken for the product decision.*
