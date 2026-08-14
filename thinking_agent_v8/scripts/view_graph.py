#!/usr/bin/env python3
"""View the LangGraph graph of the Thinking Agent.

Usage (from thinking_agent_v8/):
  PYTHONPATH=src python scripts/view_graph.py               # ASCII in terminal
  PYTHONPATH=src python scripts/view_graph.py --mermaid     # Mermaid markup
  PYTHONPATH=src python scripts/view_graph.py --mermaid --out docs/svg/task_graph.mmd
  PYTHONPATH=src python scripts/view_graph.py --png docs/svg/task_graph.png   # needs mmdc (npm i -g @mermaid-js/mermaid-cli)
  PYTHONPATH=src python scripts/view_graph.py --evaluation  # the SDL evaluation graph
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the Thinking Agent LangGraph graph")
    parser.add_argument("--mermaid", action="store_true",
                        help="print Mermaid markup (paste into mermaid.live / GitHub)")
    parser.add_argument("--png", nargs="?", const=None, default=None,
                        help="render PNG via mermaid-cli (mmdc); optional output path")
    parser.add_argument("--out", default=None,
                        help="write the Mermaid markup to this file")
    parser.add_argument("--evaluation", action="store_true",
                        help="render the SDL EvaluationEpisodeGraph instead")
    args = parser.parse_args()

    if args.evaluation:
        from thinking_agent.graphs.evaluation_episode_graph import compile_evaluation_graph
        graph = compile_evaluation_graph().compile().get_graph()
        title = "evaluation_episode"
    else:
        from thinking_agent.graphs.task_graph import compile_task_graph
        graph = compile_task_graph().compile().get_graph()
        title = "task_graph"

    if args.png is not None or args.mermaid or args.out:
        mermaid = graph.draw_mermaid()
        if args.out:
            Path(args.out).write_text(mermaid, encoding="utf-8")
            print(f"mermaid written to {args.out}")
        if args.png is not None:
            import subprocess
            import tempfile
            import os
            out = args.png or f"{title}.png"
            mmd = tempfile.mktemp(suffix=".mmd")
            Path(mmd).write_text(mermaid, encoding="utf-8")
            subprocess.run(["mmdc", "-i", mmd, "-o", out], check=True)
            os.unlink(mmd)
            print(f"PNG written to {out} (open it in any image viewer)")
        if args.mermaid and not args.out and args.png is None:
            print(mermaid)
        return 0

    print(graph.draw_ascii())
    print("\n# terminal view; use --mermaid for markup, --png for an image, "
          "--evaluation for the SDL graph")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
