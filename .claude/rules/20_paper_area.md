# Paper Area Rules (`paper/**`)

## Paper docs SSOT (explicit)
- Ground truth directory is declared by the active paper project under `paper/**` (e.g., in `paper/**/CLAUDE.md`).
- Always read first: that project's `STATUS.md`.
- On completion: update that project's `STATUS.md` and append to its `ITERATION_LOG.md`.

## Scope guard (paper-only by default)
- For paper-writing / research-doc tasks: only change files under `paper/**` unless the task explicitly requests code.
- If code changes are needed, write them as a concrete handoff request in the project's `STATUS.md`.

## Replication package hygiene (avoid root pollution)
- For paper experiments: keep YAMLs and scripts inside the active paper project (e.g., `paper/<project>/configs/` and
  `paper/<project>/scripts/`), not in repo-root `configs/` or `scripts/`.
