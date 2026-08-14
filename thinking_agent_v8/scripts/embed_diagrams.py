#!/usr/bin/env python3
"""Embed the docs/svg diagrams into each docs markdown file (idempotent —
removes a previous embed of the same image first)."""
import io
from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"

EMBEDS = [
    ("architecture.md", "# Architecture (impl §5)",
     "architecture_planes.svg",
     "Figure — the logical planes: public API over the governed task graph, "
     "with the kernel, cognitive, tool, evaluation, and memory/learning "
     "planes at distinct authority boundaries."),
    ("database_schema.md", "# Database Schema (impl §19)",
     "database_stores.svg",
     "Figure — three separated stores (checkpointer, kernel policy, "
     "application DB) and the append-only ledger hash chain; production "
     "roles on separate credentials."),
    ("installation.md", "# Installation Guide",
     "installation_steps.svg",
     "Figure — the five installation steps, optional durable checkpoints, "
     "and the platform scheduling map."),
    ("integration.md", "# Integration (impl §21.4)",
     "integration_swarm.svg",
     "Figure — the swarm worker contract: one governed worker, one "
     "TaskResult, with the hard limits the external layer cannot cross."),
    ("native_installation.md", "# Native Installation (impl §29.1)",
     "native_install_flow.svg",
     "Figure — the native install flow: requirements, venv, install, verify "
     "— no Docker anywhere."),
    ("operations.md", "# Operations Runbook (native, no Docker — impl §29)",
     "operations_services.svg",
     "Figure — production service processes, the scheduled-operations "
     "cadence, and the backup/restore requirement."),
    ("prompts.md", "# Prompt Architecture (impl §20.4)",
     "prompts_contract.svg",
     "Figure — the 13-element prompt contract, structured-output repair "
     "path, untrusted-evidence wrapping, and role separation."),
    ("requirements_traceability.md", "# Requirements Traceability Matrix",
     "traceability_map.svg",
     "Figure — the traceability map: spec requirement → implementation "
     "component → primary tests (all rows TESTED)."),
    ("security_model.md", "# Security Model (impl §5.2/§9/§16)",
     "security_model_defenses.svg",
     "Figure — attack vectors mapped to their code-enforced defenses, the "
     "kernel trust boundary, and the verdict-derived write path."),
    ("testing.md", "# Testing (impl §25)",
     "testing_layers.svg",
     "Figure — the test-layer pyramid: 120 tests across unit, routing/SDL, "
     "evaluation/integration, security/fault-injection, and property layers, "
     "with the frozen legacy harness underneath."),
    ("user_guide.md", "# User Guide",
     "user_guide_loop.svg",
     "Figure — the governed loop (META→WHAT→WHY→HOW→DO→REVIEW), the "
     "continuous verify band, and the eight terminal states with the "
     "proof-carrying packet."),
]


def embed(md: str, heading: str, svg: str, caption: str) -> None:
    path = DOCS / md
    src = io.open(path, encoding="utf-8").read()
    assert heading in src, f"anchor missing in {md}: {heading}"
    block = (f"{heading}\n\n"
             f"![{caption.split(' — ')[0]}](svg/{svg})\n\n"
             f"*{caption}*\n")
    # idempotent: remove any previous embed of the same image
    old_marker = f"](svg/{svg})"
    if old_marker in src:
        lines = src.splitlines(keepends=True)
        keep = []
        skip = 0
        for i, line in enumerate(lines):
            if old_marker in line:
                # drop the image line and the following caption line
                skip = 2
                continue
            if skip > 0:
                skip -= 1
                continue
            keep.append(line)
        src = "".join(keep)
    src = src.replace(heading, block, 1)
    io.open(path, "w", encoding="utf-8").write(src)
    print(f"embedded {svg} -> {md}")


if __name__ == "__main__":
    for md, heading, svg, caption in EMBEDS:
        embed(md, heading, svg, caption)
    # user_guide gets a second diagram (SDL cycle) after the first one
    ug = DOCS / "user_guide.md"
    src = io.open(ug, encoding="utf-8").read()
    anchor = "## 5. Self-Directed Learning (SDL)"
    assert anchor in src
    sdl_block = (anchor + "\n\n"
                 "![SDL cycle](svg/user_guide_sdl.svg)\n\n"
                 "*Figure — the Self-Directed Learning cycle: discovery, gap "
                 "map, plan, human gate, trial, external judge, ledger, and "
                 "review — closing the loop into the next round.*\n")
    src = src.replace(anchor, sdl_block, 1)
    io.open(ug, "w", encoding="utf-8").write(src)
    print("embedded user_guide_sdl.svg -> user_guide.md")
