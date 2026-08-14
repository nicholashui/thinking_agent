#!/usr/bin/env python3
"""Install all skills found in external/sources/* into the user skills
directory (~/.claude/skills/).

Policy:
- Install order: official Anthropic repos first, dedicated collections next,
  aggregators after, foreign-CLI skill sets last (first occurrence of a name
  wins — official beats aggregator copies).
- Never overwrite: a skill name already installed in this run, or a
  pre-existing user skill, is skipped and reported.
- A SKILL.md without a valid Claude frontmatter (name + description) is
  skipped and reported (foreign formats are not forced).
- The whole skill directory is copied (SKILL.md + any bundled files).
"""
import io
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(r"C:\Project\thinking_agent")
SOURCES = ROOT / "external" / "sources"
USER_SKILLS = Path.home() / ".claude" / "skills"

PRIORITY = [
    "anthropic-claude-code",
    "anthropic-claude-plugins-official",
    "anthropic-skills",
    "claude-mem",
    "superpowers",
    "vercel-agent-skills",
    "claude-code-best-practice",
    "andrej-karpathy-skills",
    "andrej-karpathy-skills-cursor-vscode",
    "agents-md",
    "wshobson-agents",
    "ecc",
    "google-gemini-cli",
    "openai-codex",
    "opencode",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.S)


def frontmatter(path: Path):
    text = io.open(path, encoding="utf-8", errors="replace").read(8192)
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, False
    fm = m.group(1)
    name_m = re.search(r"^name:\s*(\S+)", fm, re.M)
    desc_m = re.search(r"^description:\s*\S", fm, re.M)
    return (name_m.group(1) if name_m else None), bool(desc_m)


def safe_folder(name: str) -> str:
    s = re.sub(r"[^A-Za-z0-9._-]+", "-", name).strip("-")
    return s or None


def main():
    USER_SKILLS.mkdir(parents=True, exist_ok=True)

    repos = {d.name for d in SOURCES.iterdir() if d.is_dir()}
    order = [r for r in PRIORITY if r in repos] + \
            sorted(repos - set(PRIORITY))

    installed = {}          # name -> source repo
    skipped_existing = []   # (name, source, reason)
    skipped_invalid = []    # relative path
    collisions = []         # (name, source, kept_from)

    for repo in order:
        rdir = SOURCES / repo
        for sk in sorted(rdir.rglob("SKILL.md")):
            if ".git" in sk.parts:
                continue
            name, has_desc = frontmatter(sk)
            if not name or not has_desc:
                skipped_invalid.append(str(sk.relative_to(SOURCES)))
                continue
            if name in installed:
                collisions.append((name, repo, installed[name]))
                continue
            dst = USER_SKILLS / (safe_folder(name) or name)
            if dst.exists():
                skipped_existing.append((name, repo, "already present in user skills"))
                continue
            shutil.copytree(sk.parent, dst)
            installed[name] = repo

    print(f"Installed: {len(installed)}")
    print(f"Skipped (name already taken): {len(collisions)}")
    print(f"Skipped (pre-existing user skill): {len(skipped_existing)}")
    print(f"Skipped (invalid/missing frontmatter): {len(skipped_invalid)}")
    print()
    by_repo = {}
    for name, repo in installed.items():
        by_repo.setdefault(repo, []).append(name)
    print("=== Installed by source repo ===")
    for repo, names in sorted(by_repo.items(), key=lambda kv: -len(kv[1])):
        print(f"  {repo}: {len(names)}")
    if skipped_existing:
        print("\n=== Pre-existing user skills NOT overwritten ===")
        for name, repo, reason in skipped_existing:
            print(f"  {name} (from {repo})")
    if skipped_invalid:
        print(f"\n=== Invalid frontmatter samples (first 10 of {len(skipped_invalid)}) ===")
        for p in skipped_invalid[:10]:
            print(f"  {p}")


if __name__ == "__main__":
    main()
