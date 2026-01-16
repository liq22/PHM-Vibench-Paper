# Vibe Kanban v2.0 — Agent Prompts (paper/state_flow/)

This folder contains the **copy-paste prompt templates** for Vibe Kanban profiles used by the DSSF state-flow paper.

## Non-negotiables (Replication Package Boundary)
- `paper/state_flow/` is the **only** workspace for paper experiments.
- All experiment YAMLs go to `paper/state_flow/configs/`.
- All run/plot scripts (Python/Shell) go to `paper/state_flow/scripts/`.
- Outputs go to `paper/state_flow/results/`.
- Do not create/modify repo-root `configs/` or `scripts/` for paper work.
- Treat `src/` as read-only unless explicitly fixing a bug.

## Profiles
- Architect: `paper/state_flow/Agents/Architect.md`
- Repo-Engineer: `paper/state_flow/Agents/Repo-Engineer.md`
- Paper-Author: `paper/state_flow/Agents/Paper-Author.md`
- Index: `paper/state_flow/Agents/agent_index.md`

## Local helper (optional)
```bash
python paper/state_flow/scripts/show_agents.py
```

## Guardrail (recommended)
- Use Vibe Kanban cleanup script: `dev/vibekanban/cleanup_state_flow_only.sh`
