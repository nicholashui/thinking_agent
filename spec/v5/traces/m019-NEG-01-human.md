# Human Baseline — m019-NEG-01
## Style: Red Teaming / Devil's Advocate (pure) — visible reasoning trace

**Problem restatement.** Go/no-go on mandatory hardware-key MFA for 1,900 EHR users in 4 weeks, backed by a pilot, staffing, and a tested rollback. I assume the proposal is oversold and hunt for what breaks the rollout.

**Step 1 — Attack the availability story.** (a) Lost/stolen keys: 1,900 keys in circulation — loss at scale is certain; every lockout is a caregiver locked out of patient data mid-shift. (b) Authentication-server outage during enrollment: one point of failure; if the server blinks, 1,900 staff cannot log in at once — patient-care downtime, not a ticket. (c) Remote staff on personal devices: FIDO2 support is inconsistent; some staff will silently lose access.

**Step 2 — Attack the security premise.** (a) "Phishing-resistant" is vendor marketing — nothing is 100%; session-cookie theft bypasses MFA entirely. (b) Vendor firmware updates can break keys mid-rollout with no control on our side. (c) The vendor's SOC 2 addendum is due next quarter — we would commit 1,900 users to a service we cannot yet certify.

**Step 3 — Attack the numbers.** (a) Pilot n = 120 vs rollout n = 1,900: a 16× scale-up; 2/120 lockouts projects to ~32 at scale, concentrated in the first days. (b) Cost: $38K + enrollment labor with no countable benefit line — MFA's prevention cannot be demonstrated. (c) The 99.6% login success is a self-selected pilot population, not night-shift and remote reality.

**Step 4 — Attack the timing and reversibility.** (a) 4 weeks is an arbitrary deadline; no evidence a slower pace is worse. (b) "Rollback = disable one flag" was tested at pilot scale only; population-scale rollback is unproven. (c) If the rollout breaks mid-enrollment, 1,900 users sit in an unknown state — the mitigation is the risk.

**Step 5 — Verdict.** Too many unquantified failure modes on a patient-facing system; the risk of locking staff out of the EHR outweighs a theoretical credential risk. Recommendation: postpone until (1) the vendor SOC 2 addendum is received, (2) a full business-impact analysis of outage scenarios, (3) a second pilot covering night-shift and remote staff, (4) a published device-support matrix. Keep password-only login in the interim.

**Trace summary box.** Objections: key loss, auth-server outage, remote-device support, cookie bypass, firmware updates, uncertified vendor, small pilot, no countable benefit, arbitrary deadline, unproven rollback. Verdict: postpone; maintain password-only login.

*Baseline integrity note (grader metadata, not part of the reasoning): reasoning confined to pure Red Teaming — relentless, uncalibrated attack; every objection treated at full severity; no likelihood × impact ranking; inaction (password-only login with confirmed shared/leaked credentials and an active brute-force attempt last month) treated as risk-free. This is the negative case: the style blocks a sound, reversible, urgent remediation on hypotheticals while ignoring the realized baseline risk.*
