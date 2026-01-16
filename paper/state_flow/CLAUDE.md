# paper/state_flow/: Local Memory (Replication Package v2.0)

## vibe research guide and rule
- This paper project is **self-contained under `paper/state_flow/`** (replication package boundary).
- Docs SSOT (read first): `paper/state_flow/core/`
  - Mandatory checkpoint: `paper/state_flow/core/STATUS.md`
- On completion: update `paper/state_flow/core/STATUS.md` and append to `paper/state_flow/core/ITERATION_LOG.md`.

## “Paper Special Zone” principle (hard boundary)
- All paper experiments must live in:
  - YAML configs: `paper/state_flow/configs/`
  - Python scripts (run/plot): `paper/state_flow/scripts/`
  - Shell scripts: `paper/state_flow/scripts/`
  - LaTeX: `paper/state_flow/tex/`
  - Outputs: `paper/state_flow/results/`
- Do **not** add/modify repo-root `configs/` or `scripts/` for paper work.
- Treat `src/` as read-only unless the task is an explicit bug fix.

