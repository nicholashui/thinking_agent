"""Native CLI entry point (impl §29): single-process task invocation.

Usage:
  thinking-agent run task.json --policy configs/kernel/world_facts.development.yaml
  thinking-agent inspect --thread th-x --sqlite agent.db
"""

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="thinking-agent",
                                     description="Thinking Agent v8 — governed worker CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_run = sub.add_parser("run", help="invoke one task")
    p_run.add_argument("task_file", help="JSON task request file")
    p_run.add_argument("--policy", default=str(REPO / "configs" / "kernel"
                                               / "world_facts.development.yaml"))
    p_run.add_argument("--sqlite", default=None, help="durable checkpointer DB")

    p_inspect = sub.add_parser("inspect", help="inspect a checkpointed thread")
    p_inspect.add_argument("--thread", required=True)
    p_inspect.add_argument("--sqlite", required=True)
    p_inspect.add_argument("--policy", default=str(REPO / "configs" / "kernel"
                                                   / "world_facts.development.yaml"))

    args = parser.parse_args(argv)

    sys.path.insert(0, str(REPO / "src"))
    from thinking_agent.api import ThinkingAgent

    if args.command == "run":
        request = json.loads(Path(args.task_file).read_text(encoding="utf-8"))
        agent = ThinkingAgent(policy_path=args.policy, sqlite_db=args.sqlite)
        result = agent.invoke(request)
        packet = result.decision_packet.model_dump() if hasattr(
            result.decision_packet, "model_dump") else result.decision_packet
        print(json.dumps({"status": result.status, "packet": packet},
                         ensure_ascii=False, indent=2, default=str))
        return 0

    if args.command == "inspect":
        agent = ThinkingAgent(policy_path=args.policy, sqlite_db=args.sqlite)
        state = agent.get_state(args.thread)
        packet = state.values.get("decision_packet", {}) if state else {}
        print(json.dumps({"thread": args.thread,
                          "terminal_status": packet.get("terminal_status"),
                          "packet_id": packet.get("packet_id")},
                         ensure_ascii=False, indent=2, default=str))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
