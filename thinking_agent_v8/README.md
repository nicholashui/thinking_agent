# Thinking Agent v8 — Implementation

Governed, stateful, auditable problem-solving system implementing
`thinking_agent.v8.md` per `thinking_agent_impl.v2.md`.

```
META-CONTROL → WHAT → WHY → HOW → DO → REVIEW
continuous VERIFY · state-only classifier · proof-carrying packet
```

## Layered architecture (trust boundaries)

| Plane | Components | Writes |
|---|---|---|
| Task/model | TaskGraph nodes, style passes | state only — proposals |
| Kernel | World-Facts snapshot, SafetyKernel, attestation, PENDING allowlist, authority tokens | policy (operator) |
| Execution | Tool Broker: allowlist, validation, idempotency, receipts | tool receipts |
| Evaluation | verifiers, judge pipeline | verdicts, calibration |
| Persistent | routing KB, competence, ledger, gap map, improvements | judge-pipeline only |

**Invariants enforced:** 11 (KB writes from verdicts only), 12 (design
records never enter KB), 13 (ledger append-only, hash-chained), 14 (draft
plans never execute). `REPLICATE` is denied. Unknown action classes default
to A5. Second-verifier rule is kernel-computed.

## Running

```bash
PYTHONPATH=src python -m pytest tests/ -q        # 121 tests
PYTHONPATH=src python -c "
from thinking_agent.api import ThinkingAgent
agent = ThinkingAgent()
result = agent.invoke({'task_id': 't1', 'input_text': 'decide diagnose engineering'})
print(result.status)  # one of the eight terminal states
"
```

## Validation status

- New suite: 121/121 — eight terminal states, S1–S45 44/44 port, S46–S50 SDL
  scenarios, broker/compensation, interrupt/resume, fault injection, property
  tests, evaluation graph, no-Docker, read-path audit
- Legacy harness: v4 177/177, v5 187/187 (3 runs, deterministic) — unchanged
- Legacy router: recall@3 82.1%, NEG-away 97.2% — unchanged
- Ruff clean · 83% coverage · release manifest generated
- No Docker artifacts (enforced by test)

## Observability

- Graph view: `PYTHONPATH=src python scripts/view_graph.py` — add `--mermaid`, `--png`, or `--evaluation`
- LangSmith (off by default): set `LANGSMITH_TRACING=true` + `LANGSMITH_API_KEY` — traces the structured audit surface only, never hidden reasoning (§1.4)

*No-Docker by design: native Python processes, SQLite/PostgreSQL, system schedulers.*
