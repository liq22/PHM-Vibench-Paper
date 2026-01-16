#!/usr/bin/env python3
"""
List Vibe Kanban prompt files under paper/state_flow/Agents/.

No external dependencies (does not require PyYAML).
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional


@dataclass(frozen=True)
class AgentMeta:
    path: Path
    name: str
    category: str
    description: str


def _parse_front_matter(text: str) -> Dict[str, str]:
    lines = text.splitlines()
    start = None
    for idx, line in enumerate(lines[:40]):
        if line.strip() == "---":
            start = idx
            break
    if start is None:
        return {}

    meta: Dict[str, str] = {}
    for line in lines[start + 1 :]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip()
    return meta


def _read_agent_meta(file_path: Path) -> AgentMeta:
    text = file_path.read_text(encoding="utf-8", errors="replace")
    meta = _parse_front_matter(text)
    name = meta.get("name", file_path.stem)
    category = meta.get("category", "unknown")
    description = meta.get("description", "").strip()
    return AgentMeta(path=file_path, name=name, category=category, description=description)


def _iter_agent_files(agents_dir: Path) -> Iterable[Path]:
    for file_path in sorted(agents_dir.glob("*.md")):
        if file_path.name.lower() in {"readme.md", "agent_index.md"}:
            continue
        yield file_path


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true", help="Print one prompt path per line")
    parser.add_argument("--category", type=str, default="", help="Filter by category (architect/dev/writer)")
    args = parser.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[3]
    agents_dir = repo_root / "paper" / "state_flow" / "Agents"

    agents = [_read_agent_meta(path) for path in _iter_agent_files(agents_dir)]
    if args.category:
        agents = [a for a in agents if a.category.lower() == args.category.lower()]

    if args.list:
        for agent in agents:
            print(str(agent.path))
        return 0

    by_cat: Dict[str, List[AgentMeta]] = {}
    for agent in agents:
        by_cat.setdefault(agent.category, []).append(agent)

    for category in sorted(by_cat.keys()):
        print(f"[{category}]")
        for agent in by_cat[category]:
            line = f"- {agent.name}: {agent.path}"
            if agent.description:
                line += f" — {agent.description}"
            print(line)
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
