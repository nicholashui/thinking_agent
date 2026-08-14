# Thinking Agent v8 – Extremely Detailed Implementation Plan (LangGraph)

**Document Version:** 1.0  
**Date:** 2026-08-13  
**Status:** Implementation Specification (Plan Only)  
**Target Framework:** LangGraph (latest stable as of mid-2026) + LangChain Core  
**Primary Language:** Python 3.12+  
**Author Context:** Designed for integration with existing N1ch01as multi-agent infrastructure (generic-swarm-ops / common-agent-swarm-ops), DeepSeek / xAI model routing, and local-first deployment preferences.

This document is the single source of truth for implementing Thinking Agent v8. It contains complete technical specifications, schemas, node contracts, control-flow logic, prompt structures, testing requirements, and phased delivery plan. No code is included — only precise implementation instructions.

---

## 1. Executive Summary & Design Goals

### 1.1 Core Objective
Build a production-grade, stateful, graph-based cognitive agent that performs deep, auditable multi-step reasoning. The agent must expose an explicit thinking process (inner monologue + structured reasoning steps), support hierarchical problem decomposition, parallel hypothesis exploration, rigorous self-critique, tool-augmented execution, and continuous quality gating before producing a final answer.

### 1.2 Key Design Principles
- **Explicit Cognition**: Every reasoning step must be recorded in an append-only `thinking_trace`.
- **Quality Gates First**: No progression without passing configurable evaluation thresholds.
- **Controlled Parallelism**: Limited fan-out of reasoning branches with mandatory synthesis.
- **Auditability**: Full trace + metrics always available in the final output.
- **Budget Awareness**: Hard limits on iterations, tokens, and wall-clock time.
- **Model Heterogeneity**: Different models can be assigned to Planner / Thinker / Critic roles.
- **Local-First & Self-Hosted Friendly**: Prefer in-process or self-hosted components; minimal mandatory cloud dependency.
- **Spec-Driven**: All schemas, contracts, and quality gates defined before coding begins.

### 1.3 Non-Goals (v8)
- Multi-agent swarm coordination (belongs to generic-swarm-ops layer).
- Real-time collaborative UI / dashboard.
- Online learning / fine-tuning loops.
- Native multi-modal input (text-only in v8).
- Automatic prompt optimization (manual + evaluation-driven only).

### 1.4 Success Definition for v8
A successful v8 implementation can:
1. Accept a complex reasoning query.
2. Produce a hierarchical plan.
3. Explore multiple reasoning branches in parallel.
4. Critically evaluate each branch with structured scores and actionable feedback.
5. Loop for revision when quality gates fail.
6. Call tools when evidence is required.
7. Synthesize a final answer with full thinking trace, confidence score, and evaluation metrics.
8. Remain stable under stress (10+ iterations, contradictory information, tool failures).
9. Export a complete audit package.

---

## 2. High-Level Architecture

### 2.1 Logical Layers
```
┌─────────────────────────────────────────────────────────────┐
│                      Public API Layer                       │
│  agent.invoke() / agent.stream() / agent.ainvoke()          │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│                    LangGraph StateGraph                     │
│  MetaController → MemoryRetriever → Planner → ParallelThink │
│  → Critic → Evaluator → (Executor) → Reflector → Finalizer  │
└────────────────────────────┬────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────┐
│              Supporting Services                            │
│  • Model Router (DeepSeek / xAI / local)                    │
│  • Tool Registry + Executor                                 │
│  • Memory (Vector + optional Graph / LightRAG)              │
│  • Checkpointer (Postgres / Redis / Memory)                 │
│  • Observability (LangSmith / OpenTelemetry / custom)       │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Cognitive Loop (Simplified)
1. Retrieve relevant long-term memory.
2. Meta-decide strategy and depth.
3. Plan hierarchical decomposition.
4. Think (single or parallel branches).
5. Critique every reasoning step.
6. Evaluate against quality gates.
7. Execute tools if required.
8. Reflect, synthesize, decide continue / revise / finish.
9. Finalize with full audit trail.

The graph is cyclic with strict guards against infinite loops.

---

## 3. Project Structure (Recommended)

```
thinking_agent_v8/
├── pyproject.toml
├── README.md
├── .env.example
├── configs/
│   ├── default.yaml
│   ├── fast.yaml
│   ├── deep.yaml
│   └── research.yaml
├── src/
│   └── thinking_agent/
│       ├── __init__.py
│       ├── main.py                 # Public API entry
│       ├── graph.py                # StateGraph construction
│       ├── state.py                # All TypedDict / Pydantic models
│       ├── config.py               # Configuration loading & validation
│       ├── nodes/
│       │   ├── __init__.py
│       │   ├── meta.py
│       │   ├── memory.py
│       │   ├── planner.py
│       │   ├── thinker.py
│       │   ├── parallel.py
│       │   ├── critic.py
│       │   ├── evaluator.py
│       │   ├── executor.py
│       │   ├── reflector.py
│       │   └── finalizer.py
│       ├── prompts/
│       │   ├── __init__.py
│       │   ├── meta.py
│       │   ├── planner.py
│       │   ├── thinker.py
│       │   ├── critic.py
│       │   ├── reflector.py
│       │   └── templates/          # Jinja2 or pure string templates
│       ├── tools/
│       │   ├── __init__.py
│       │   ├── registry.py
│       │   └── base.py
│       ├── memory/
│       │   ├── __init__.py
│       │   ├── retriever.py
│       │   └── store.py
│       ├── evaluation/
│       │   ├── metrics.py
│       │   ├── gates.py
│       │   └── harness.py
│       ├── utils/
│       │   ├── logging.py
│       │   ├── tracing.py
│       │   ├── model_router.py
│       │   └── helpers.py
│       └── exceptions.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── fixtures/
│   └── evaluation/
├── notebooks/
│   └── exploration.ipynb
└── scripts/
    ├── run_eval.py
    └── stress_test.py
```

---

## 4. Dependencies & Environment

### 4.1 Core Dependencies (pyproject.toml)
```toml
[project]
name = "thinking-agent-v8"
version = "0.8.0"
requires-python = ">=3.12"
dependencies = [
    "langgraph>=0.2.0",
    "langchain-core>=0.3.0",
    "langchain-openai>=0.2.0",          # for compatible OpenAI-style endpoints
    "langchain-community>=0.3.0",
    "pydantic>=2.8.0",
    "pydantic-settings>=2.4.0",
    "httpx>=0.27.0",
    "tenacity>=8.5.0",
    "structlog>=24.4.0",
    "orjson>=3.10.0",
    "jinja2>=3.1.0",
    "numpy>=2.0.0",
    "tiktoken>=0.7.0",
    # Optional but recommended
    "langsmith>=0.1.0",
    "redis>=5.0.0",
    "psycopg[binary]>=3.2.0",
    "chromadb>=0.5.0",                  # or qdrant-client / lancedb
]
```

### 4.2 Model Providers
- Primary: DeepSeek (V3 / V4 Flash / R1-style reasoning models)
- Secondary: xAI Grok family
- Local: Ollama / vLLM / llama.cpp compatible endpoints
- Model router must support per-node model override via config.

### 4.3 Environment Variables
```
THINKING_AGENT_ENV=dev|staging|prod
DEFAULT_MODEL=deepseek-chat
CRITIC_MODEL=deepseek-reasoner          # stronger model preferred
PLANNER_MODEL=deepseek-chat
OPENAI_API_BASE=...                     # for compatible endpoints
OPENAI_API_KEY=...
DEEPSEEK_API_KEY=...
XAI_API_KEY=...
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=...
LANGCHAIN_PROJECT=thinking-agent-v8
CHECKPOINT_BACKEND=memory|postgres|redis
DATABASE_URL=...
REDIS_URL=...
VECTOR_STORE_PATH=...
MAX_ITERATIONS=12
DEFAULT_TEMPERATURE=0.3
```

---

## 5. Core State Schema (Complete Technical Specification)

All state must be defined using Pydantic v2 models for validation + TypedDict for LangGraph compatibility where required.

### 5.1 Primary State Model

```python
from typing import Annotated, Literal, Optional, Any
from typing_extensions import TypedDict
from pydantic import BaseModel, Field
from langgraph.graph.message import add_messages
import operator

class ThinkingStep(BaseModel):
    step_id: str
    branch_id: str
    role: Literal["meta", "planner", "thinker", "critic", "executor", "reflector", "system"]
    content: str
    timestamp: str
    model: Optional[str] = None
    token_count: Optional[int] = None
    parent_step_id: Optional[str] = None
    metadata: dict[str, Any] = Field(default_factory=dict)

class CritiqueItem(BaseModel):
    aspect: str                          # e.g. "logical_consistency", "evidence_strength"
    score: float                         # 0.0 – 1.0
    severity: Literal["critical", "major", "minor", "suggestion"]
    description: str
    suggested_fix: Optional[str] = None
    related_step_ids: list[str] = Field(default_factory=list)

class Critique(BaseModel):
    overall_score: float
    items: list[CritiqueItem]
    must_revise: bool
    revision_instructions: list[str]
    confidence_in_critique: float

class EvaluationMetrics(BaseModel):
    correctness: float = 0.0
    completeness: float = 0.0
    coherence: float = 0.0
    confidence: float = 0.0
    novelty: float = 0.0
    efficiency: float = 0.0
    evidence_strength: float = 0.0
    overall: float = 0.0
    passed_gates: bool = False
    gate_failures: list[str] = Field(default_factory=list)

class PlanStep(BaseModel):
    step_id: str
    description: str
    status: Literal["pending", "in_progress", "completed", "failed", "skipped"]
    depends_on: list[str] = Field(default_factory=list)
    assigned_branch: Optional[str] = None
    result_summary: Optional[str] = None

class Plan(BaseModel):
    goal: str
    steps: list[PlanStep]
    strategy: str
    estimated_complexity: Literal["low", "medium", "high", "extreme"]
    max_depth: int

class ToolCallRecord(BaseModel):
    tool_name: str
    tool_input: dict[str, Any]
    tool_output: Any
    success: bool
    error: Optional[str] = None
    latency_ms: Optional[float] = None

class AgentState(TypedDict):
    # Core conversation
    messages: Annotated[list, add_messages]
    
    # Original input
    input: str
    input_metadata: dict[str, Any]
    
    # Cognitive artifacts
    plan: Optional[Plan]
    thinking_trace: Annotated[list[ThinkingStep], operator.add]
    active_branches: list[str]
    current_hypothesis: Optional[str]
    
    # Critique & Evaluation
    latest_critique: Optional[Critique]
    evaluation_metrics: Optional[EvaluationMetrics]
    
    # Tooling
    pending_tool_calls: list[dict]
    tool_history: Annotated[list[ToolCallRecord], operator.add]
    
    # Memory
    memory_context: list[dict]
    
    # Control
    iteration_count: int
    max_iterations: int
    status: Literal[
        "initialized", "retrieving", "meta", "planning", 
        "thinking", "critiquing", "evaluating", "executing", 
        "reflecting", "finalizing", "done", "error", "interrupted"
    ]
    error: Optional[str]
    
    # Output
    final_answer: Optional[str]
    confidence: Optional[float]
    audit_package: Optional[dict]
    
    # Runtime config snapshot
    runtime_config: dict[str, Any]
```

### 5.2 Reducer Rules
- `messages`: use LangGraph `add_messages`
- `thinking_trace`: append-only (`operator.add`)
- `tool_history`: append-only
- All other fields: overwrite (last writer wins) unless explicitly documented otherwise.

### 5.3 Validation Rules
- `iteration_count` must never exceed `max_iterations`.
- `thinking_trace` entries must have unique `step_id` within a run.
- `Critique.must_revise == True` forces a revision path.
- `EvaluationMetrics.passed_gates == False` prevents progression to Finalizer unless hard timeout.

---

## 6. Configuration Schema

```yaml
# configs/default.yaml
agent:
  name: "thinking-agent-v8"
  version: "0.8.0"
  max_iterations: 12
  max_parallel_branches: 4
  default_temperature: 0.3
  critic_temperature: 0.1
  enable_parallel: true
  enable_memory: true
  enable_tools: true
  early_exit_on_high_confidence: true
  high_confidence_threshold: 0.92

models:
  default: "deepseek-chat"
  meta: "deepseek-chat"
  planner: "deepseek-chat"
  thinker: "deepseek-chat"
  critic: "deepseek-reasoner"          # stronger model
  reflector: "deepseek-chat"
  finalizer: "deepseek-chat"

quality_gates:
  min_overall_score: 0.75
  min_correctness: 0.70
  min_coherence: 0.80
  min_evidence_strength: 0.65
  critical_flaw_blocks: true

memory:
  top_k: 8
  score_threshold: 0.72
  use_graph: false                    # set true when LightRAG ready

tools:
  allowed:
    - web_search
    - calculator
    - code_interpreter
    - knowledge_lookup
  timeout_seconds: 30

tracing:
  enabled: true
  project: "thinking-agent-v8"
```

Configuration must be loaded via Pydantic Settings and frozen at graph compilation time (snapshot into `runtime_config`).

---

## 7. Node Specifications (Complete Contracts)

Every node is a pure function: `(state: AgentState) -> dict` (partial state update).

### 7.1 MemoryRetriever Node
**File:** `nodes/memory.py`  
**Responsibility:** Retrieve relevant long-term context before any cognitive work.  
**Inputs:** `input`, `plan` (if exists), `runtime_config`  
**Outputs:** `memory_context`, `status="retrieving"`  
**Technical Details:**
- Query construction: original input + current plan goal + key entities extracted via lightweight NER or LLM.
- Backend: Chroma / Qdrant / LanceDB (local preferred) or remote.
- Optional LightRAG / graph retrieval path when `memory.use_graph = true`.
- Deduplicate and rank results.
- Truncate to token budget (configurable).
- On failure: return empty list + warning in thinking_trace (do not crash).

### 7.2 MetaController Node
**File:** `nodes/meta.py`  
**Responsibility:** Decide overall strategy, complexity estimate, depth limit, and whether tools are likely needed.  
**Inputs:** `input`, `memory_context`, `runtime_config`  
**Outputs:** `runtime_config` updates, initial `status="meta"`, first thinking_trace entry  
**Prompt Requirements:**
- Force structured output: strategy, complexity, max_depth, tool_likelihood, early_exit_possible.
- Must justify decision in one short paragraph (recorded in thinking_trace).

### 7.3 Planner Node
**File:** `nodes/planner.py`  
**Responsibility:** Produce hierarchical Plan object.  
**Inputs:** `input`, `memory_context`, `runtime_config`  
**Outputs:** `plan`, `status="planning"`  
**Technical Requirements:**
- Output must validate against `Plan` Pydantic model.
- Steps must form a valid dependency DAG (no cycles).
- Each step receives a unique `step_id` (UUID4 or nanoid).
- Complexity classification drives later parallel limits.

### 7.4 Thinker Node (Single)
**File:** `nodes/thinker.py`  
**Responsibility:** Generate one coherent reasoning chain for a given plan step or hypothesis.  
**Inputs:** current plan step, memory_context, previous critique (if revision)  
**Outputs:** new `ThinkingStep` entries, updated `current_hypothesis`  
**Technical Requirements:**
- Must emit intermediate “inner monologue” style reasoning.
- Prefer structured intermediate conclusions.
- Token budget awareness (summarize if approaching limit).
- On revision: must explicitly address every `revision_instructions` item.

### 7.5 ParallelThinker Node
**File:** `nodes/parallel.py`  
**Responsibility:** Fan-out multiple Thinker instances using LangGraph `Send` API.  
**Technical Implementation Notes:**
- Create up to `max_parallel_branches` Send objects.
- Each branch receives unique `branch_id`.
- After all branches complete, results are collected and passed to Critic.
- Must handle partial failures (one branch error should not kill entire graph).

### 7.6 Critic Node
**File:** `nodes/critic.py`  
**Responsibility:** Perform rigorous, structured critique of all current thinking.  
**Inputs:** full `thinking_trace`, `plan`, `tool_history`  
**Outputs:** `latest_critique`  
**Critical Requirements:**
- Must use stronger model when configured.
- Output must validate against `Critique` model.
- Every `CritiqueItem` must contain concrete `suggested_fix` when severity ≥ major.
- `must_revise` flag is authoritative for downstream routing.
- Critic is forbidden from generating the final answer.

### 7.7 Evaluator Node
**File:** `nodes/evaluator.py`  
**Responsibility:** Apply deterministic quality gates on top of Critic output.  
**Inputs:** `latest_critique`, `evaluation_metrics` (previous), `runtime_config.quality_gates`  
**Outputs:** updated `evaluation_metrics`, decision flags  
**Logic (must be deterministic):**
```
overall = weighted_average of metrics
passed = (
    overall >= min_overall_score AND
    correctness >= min_correctness AND
    coherence >= min_coherence AND
    evidence_strength >= min_evidence_strength AND
    not (critical_flaw_blocks and any critical items)
)
```
- Record exact gate failures.
- This node contains almost no LLM calls (pure logic preferred).

### 7.8 Executor Node
**File:** `nodes/executor.py`  
**Responsibility:** Execute pending tool calls and pack observations.  
**Inputs:** `pending_tool_calls`  
**Outputs:** `tool_history` entries, clear `pending_tool_calls`  
**Technical Requirements:**
- Strict allow-list from config.
- Timeout + retry with tenacity.
- Sanitize tool outputs before inserting into state (length limits, PII redaction optional).
- On tool failure: record error, do not crash graph.

### 7.9 Reflector Node
**File:** `nodes/reflector.py`  
**Responsibility:** Synthesize all branches, update plan status, decide next action.  
**Inputs:** everything  
**Outputs:** updated plan, possibly new pending_tool_calls, status decision  
**Decision Outcomes:**
- `"continue_thinking"`
- `"revise_plan"`
- `"call_tools"`
- `"finalize"`
- `"error"`

### 7.10 Finalizer Node
**File:** `nodes/finalizer.py`  
**Responsibility:** Produce clean final answer + complete audit package.  
**Outputs:** `final_answer`, `confidence`, `audit_package`, `status="done"`  
**Audit Package Contents (mandatory):**
- Full thinking_trace
- Final plan
- All critiques
- Evaluation metrics history
- Tool history
- Iteration count
- Model versions used
- Token usage summary
- Runtime config snapshot

---

## 8. Graph Construction Specification

### 8.1 Graph Topology (Pseudocode)

```python
workflow = StateGraph(AgentState)

# Nodes
workflow.add_node("memory_retriever", memory_retriever_node)
workflow.add_node("meta_controller", meta_controller_node)
workflow.add_node("planner", planner_node)
workflow.add_node("thinker", thinker_node)
workflow.add_node("parallel_thinker", parallel_thinker_node)
workflow.add_node("critic", critic_node)
workflow.add_node("evaluator", evaluator_node)
workflow.add_node("executor", executor_node)
workflow.add_node("reflector", reflector_node)
workflow.add_node("finalizer", finalizer_node)

# Entry
workflow.set_entry_point("memory_retriever")

# Linear + Conditional
workflow.add_edge("memory_retriever", "meta_controller")
workflow.add_edge("meta_controller", "planner")
workflow.add_conditional_edges("planner", route_after_planner, {
    "parallel": "parallel_thinker",
    "single": "thinker",
    "finalize": "finalizer"
})
workflow.add_edge("thinker", "critic")
workflow.add_edge("parallel_thinker", "critic")
workflow.add_edge("critic", "evaluator")
workflow.add_conditional_edges("evaluator", route_after_evaluator, {
    "revise": "thinker",
    "replan": "planner",
    "tools": "executor",
    "reflect": "reflector",
    "finalize": "finalizer"
})
workflow.add_edge("executor", "reflector")
workflow.add_conditional_edges("reflector", route_after_reflector, {
    "think": "thinker",
    "plan": "planner",
    "tools": "executor",
    "finalize": "finalizer",
    "error": "finalizer"
})
workflow.add_edge("finalizer", END)
```

### 8.2 Routing Functions (Must Be Pure)
All routing functions receive full state and return a string key. They must be deterministic given the same state.

Key routing logic points:
- After Planner: decide parallel vs single based on complexity + config.
- After Evaluator: highest priority is critical flaws → revise; then tools needed → executor; then pass → reflector.
- After Reflector: respect max_iterations hard stop.

### 8.3 Parallel Execution
Use LangGraph `Send` API inside `parallel_thinker_node`:
```python
from langgraph.types import Send

def parallel_thinker_node(state):
    branches = create_branch_payloads(state)
    return [Send("thinker", branch_state) for branch_state in branches]
```

---

## 9. Prompt Engineering Requirements

All prompts must be stored as versioned templates (Jinja2 or pure Python f-strings with clear placeholders).

### 9.1 Mandatory Prompt Sections
Every cognitive node prompt must contain:
1. Role definition
2. Current goal / plan context
3. Relevant memory
4. Full or summarized thinking_trace (with length control)
5. Explicit output schema / format instructions
6. Constraints (token budget, forbidden behaviors)
7. Examples of good / bad output (few-shot where beneficial)

### 9.2 Critic Prompt Special Rules
- Critic must never invent new facts.
- Critic must reference specific step_ids when criticizing.
- Critic must output valid JSON matching `Critique` model.
- Temperature ≤ 0.2 recommended.

### 9.3 Revision Prompt Injection
When `must_revise == True`, the Thinker prompt must begin with:
```
PREVIOUS CRITIQUE (YOU MUST ADDRESS EVERY ITEM):
{formatted_critique}
```

---

## 10. Tool System Specification

### 10.1 Tool Interface
Every tool must implement:
```python
class BaseTool(BaseModel):
    name: str
    description: str
    args_schema: type[BaseModel]
    
    def invoke(self, **kwargs) -> Any: ...
    async def ainvoke(self, **kwargs) -> Any: ...
```

### 10.2 Built-in Tools (v8 Minimum)
- `web_search` (Tavily / Serper / local SearxNG)
- `calculator` (safe math expression evaluator)
- `code_interpreter` (restricted Python REPL or e2b / modal style)
- `knowledge_lookup` (internal vector / graph query)

### 10.3 Safety
- Hard allow-list
- Input validation via Pydantic
- Output length truncation
- Timeout + circuit breaker
- No arbitrary code execution without sandbox

---

## 11. Memory System Specification

### 11.1 Short-term
Handled entirely by LangGraph state + messages.

### 11.2 Long-term
- Vector store for semantic retrieval.
- Optional LightRAG / knowledge graph path for multi-hop memory.
- Write path (v8): only explicit “commit important insight” actions from Reflector (not automatic).
- Metadata: source, timestamp, importance score, related entities.

### 11.3 Retrieval Pipeline
1. Query rewriting (optional LLM)
2. Hybrid search (vector + keyword)
3. Reranking (optional)
4. Context packing with citation IDs

---

## 12. Checkpointing & Persistence

- Use LangGraph native checkpointer.
- Supported backends: MemorySaver (dev), PostgresSaver, RedisSaver.
- Thread ID = conversation / session ID.
- Support `interrupt_before` / `interrupt_after` on Critic and Reflector for human-in-the-loop.
- On resume: full state restoration including thinking_trace.

---

## 13. Evaluation & Quality Gates (Technical)

### 13.1 Metric Definitions
All scores normalized to [0.0, 1.0].

- **Correctness**: factual accuracy + logical validity of conclusions.
- **Completeness**: coverage of original query requirements.
- **Coherence**: internal consistency across thinking steps.
- **Confidence**: calibrated self-assessed certainty.
- **Evidence Strength**: quality and relevance of supporting observations / memory.
- **Novelty**: non-obvious insights (optional, lower weight).
- **Efficiency**: reasoning steps vs complexity (penalize unnecessary loops).

### 13.2 Gate Evaluation Code Path
Must be pure Python (no LLM) inside Evaluator node for determinism and speed.

### 13.3 Offline Evaluation Harness
- Curated set of 30–50 hard reasoning problems with gold traces.
- Automated scoring of final answer + process metrics.
- Ablation support (disable Critic, disable parallel, etc.).
- Regression detection on every PR.

---

## 14. Observability

- Structured logging with structlog (JSON).
- LangSmith tracing enabled by default in non-prod.
- Custom spans for each node.
- Token usage and latency recorded per node.
- Final audit_package always contains complete run metadata.

---

## 15. Error Handling & Resilience

- Every node wrapped with try/except that writes to `state["error"]` and routes to Finalizer.
- Tool failures are non-fatal.
- LLM structured output parsing failures trigger one automatic retry with repair prompt, then fail gracefully.
- Max iteration hard stop always produces best-effort answer + warning.

---

## 16. Testing Strategy (Exhaustive)

### 16.1 Unit Tests
- Each node with mocked LLM responses (using respx or pytest-httpx).
- State update correctness.
- Routing function pure logic.

### 16.2 Integration Tests
- Full graph runs with recorded fixtures.
- Parallel branch collection.
- Revision loops.
- Tool calling happy path + failure path.
- Checkpoint save/load/resume.

### 16.3 Evaluation Tests
- Golden problem set.
- Score thresholds must not regress.

### 16.4 Stress Tests
- 15+ iteration forced loops.
- Contradictory memory injection.
- Tool timeout storms.
- Extremely long thinking_trace handling (summarization trigger).

---

## 17. Phased Delivery Plan (Detailed Tasks)

### Phase 0 – Project Skeleton (0.5–1 day)
- [ ] Initialize repository + pyproject.toml
- [ ] Create full directory structure
- [ ] Implement config loading + validation
- [ ] Implement base state models + validators
- [ ] Basic logging + tracing setup
- [ ] Empty graph that compiles

### Phase 1 – Linear Cognitive Path (2–3 days)
- [ ] MemoryRetriever (stub or simple vector)
- [ ] MetaController
- [ ] Planner
- [ ] Thinker (single)
- [ ] Critic
- [ ] Evaluator
- [ ] Reflector
- [ ] Finalizer
- [ ] Linear edges + basic routing
- [ ] Unit tests for every node
- [ ] First end-to-end successful run on simple query

### Phase 2 – Quality Gates & Revision Loops (1–2 days)
- [ ] Full quality gate logic
- [ ] Revision injection into Thinker
- [ ] Max iteration guard
- [ ] Integration tests for revision cycles

### Phase 3 – Parallelism (1–2 days)
- [ ] ParallelThinker with Send API
- [ ] Branch ID tracking
- [ ] Synthesis logic in Reflector
- [ ] Parallel limit enforcement
- [ ] Tests for partial branch failure

### Phase 4 – Tools (1–2 days)
- [ ] Tool registry
- [ ] Executor node
- [ ] At least two real tools (calculator + one search)
- [ ] Observation feedback into thinking_trace
- [ ] Safety / timeout tests

### Phase 5 – Memory Hardening (1 day)
- [ ] Production vector store integration
- [ ] Optional LightRAG path
- [ ] Memory write policy from Reflector

### Phase 6 – Observability, Checkpointing, HITL (1–2 days)
- [ ] Postgres / Redis checkpointer
- [ ] interrupt_before on Critic
- [ ] Complete audit_package
- [ ] LangSmith dashboard validation

### Phase 7 – Evaluation Harness & Polish (2 days)
- [ ] Golden dataset
- [ ] Automated scoring scripts
- [ ] Ablation runner
- [ ] Performance profiling
- [ ] Documentation + example notebooks
- [ ] Config presets (fast / deep / research)

### Phase 8 – Integration Readiness
- [ ] Clean public API surface
- [ ] Compatibility layer for generic-swarm-ops embedding
- [ ] Version pinning + release notes

---

## 18. Risk Register

| ID  | Risk                              | Likelihood | Impact | Mitigation                                      |
|-----|-----------------------------------|------------|--------|-------------------------------------------------|
| R1  | Infinite reasoning loops          | Medium     | High   | Hard max_iterations + quality gate + timeout    |
| R2  | Context window explosion          | High       | High   | Trace summarization + selective memory          |
| R3  | Weak or hallucinated critique     | Medium     | High   | Stronger model + forced schema + few-shot       |
| R4  | Parallel branch cost explosion    | Medium     | Medium | Hard max_parallel_branches                      |
| R5  | Non-deterministic routing         | Low        | High   | Pure routing functions + unit tests             |
| R6  | Tool sandbox escape               | Low        | Critical | Allow-list + sandbox + output sanitization    |
| R7  | State serialization failures      | Medium     | Medium | Strict Pydantic models + orjson                 |
| R8  | Model provider rate limits        | High       | Medium | Tenacity retries + model fallback router        |

---

## 19. Acceptance Criteria (Definition of Done)

v8 is considered complete when:

1. All phases 0–7 are finished and merged.
2. Full graph compiles and runs without error on the golden evaluation set.
3. Average overall evaluation score ≥ 0.78 on the held-out set.
4. Revision loops correctly trigger and terminate.
5. Parallel branches produce measurable lift on open-ended problems.
6. Complete audit_package is present in every successful run.
7. Checkpoint resume works across process restarts.
8. Documentation is sufficient for another engineer to extend a new node.
9. Integration smoke test with generic-swarm-ops passes (or documented interface).
10. No critical items remain in the risk register without mitigation.

---

## 20. Extension Points for Future Versions

- v9: Multi-agent debate inside the Thinker layer
- Native multi-modal (image / diagram) reasoning
- Automatic prompt optimization loop
- Persistent self-improvement via reflection memory
- Direct embedding as a specialized worker inside generic-swarm-ops
- Formal verification of selected reasoning steps

---

**End of Specification**

This document is intentionally exhaustive. Every schema, contract, routing decision, and quality gate is defined so that implementation can proceed with minimal ambiguity. Begin with Phase 0 and treat each phase as a gated milestone with its own review. 

Ready for task decomposition into executable `task.md` items when implementation starts.