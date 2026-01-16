# paper/state_flow/ Guidelines (AGENTS)

## Scope
- You are working inside the replication package: `paper/state_flow/`.
- Default policy: only change files under `paper/state_flow/**`.

## Absolute directory rules (paper special zone)
- Experiment YAMLs: `paper/state_flow/configs/` (do not touch repo-root `configs/`)
- Run/plot scripts: `paper/state_flow/scripts/` (do not touch repo-root `scripts/`)
- Outputs: `paper/state_flow/results/` (commit only lightweight artifacts if requested)

## Start / Finish checklist
- Start: read `paper/state_flow/core/STATUS.md` and restate current phase + next TODOs.
- Finish: update `paper/state_flow/core/STATUS.md` and append a short entry to
  `paper/state_flow/core/ITERATION_LOG.md`.

## If code changes are needed
- Stop and write a handoff request in `paper/state_flow/core/STATUS.md` (exact `src/**` targets + validation commands).

