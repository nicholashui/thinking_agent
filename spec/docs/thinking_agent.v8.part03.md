<!-- ============================================================
  LP03 — Design Principles, Architectural Overview, Four Nested Timescales
  Source file: thinking_agent.v8.md  (split part 03/12)
  ============================================================ -->
## 6. Design Principles

*(P1–P12 unchanged. The mechanism matrix's v5 additions: P4's enforcing point includes the identity-registry second-verifier rule and the pre-DO bar check on the selected decision; P8's authority-token path has no task-gated minting (V1/V3); P11's plateau stop is RESOURCE\_LIMITED-mapped; P12's packet is produced on every path with gated reviews.)*

***

## 7. Architectural Overview

```text
┌──────────────────────────────────────────────────────────────┐
│                  HUMAN / ENVIRONMENT                         │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ GOVERNANCE AND SAFETY KERNEL                                │
│ Goals • permissions • policy • risk gates • interrupts      │
│ WORLD-FACTS STORE (all security knobs) • static allowlist   │
│ identity registry • token minting • no-replication          │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ META-CONTROLLER (competence-aware; method composer)         │
│ BUDGET ENVELOPE • ROUTE FLAGS • E5 stabilize-then-diagnose  │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ STRUCTURED COGNITIVE WORKSPACE                              │
│ WHAT → WHY → HOW → DO → REVIEW                              │
│ STATE-ONLY CLASSIFIER • pre-DO bar+identity check           │
│ delta-cached outcomes • gated reviews • planner-once        │
│ early classifier entry • checkpoint at every stage          │
└───────────────┬──────────────────────┬───────────────────────┘
                │                      │
┌───────────────▼────────────┐  ┌──────▼──────────────────────┐
│ REASONING AND COUNCIL      │  │ MEMORY AND WORLD MODEL     │
│ search • generate          │  │ RETRIEVE-IN-DIAGNOSE        │
│ council (debate round)     │  │ (priced hits, real fill)    │
│ critique • synthesize      │  │ competence (kernel feed)    │
└───────────────┬────────────┘  └──────┬──────────────────────┘
                │                      │
┌───────────────▼──────────────────────▼───────────────────────┐
│ TOOL BROKER AND EXECUTION SANDBOX                           │
│ timeouts • retries • idempotency • compensation             │
│ pending kernel-allowlist subset (no fallback) • checkpoint  │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│ TELEMETRY, EVALUATION, AND SELF-EVOLUTION                   │
│ per-stage audit • frozen baseline (kernel state)            │
│ verifier history registry • EvaluationPlane (Phase 2)       │
└──────────────────────────────────────────────────────────────┘
```

***

## 8. Four Nested Timescales

*(Action loop §8.1; task loop §8.2 with per-stage checkpoints; learning loop §8.3 — competence fed from the kernel calibration registry with a provenance gate (V2), memory retrieval genuinely read back (V6); architecture-evolution loop §8.4; session layer §8.5 per v4, with the LearningScheduler triggers still design-level (disclosed).)*

***

