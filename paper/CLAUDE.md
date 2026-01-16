# paper/: Local Memory (Research / Writing)

## vibe research guide and rule
- Paper docs SSOT (ground truth): `paper/state_flow/core/`
- Always read first: `paper/state_flow/core/STATUS.md`
- On completion: update `paper/state_flow/core/STATUS.md` and append to
  `paper/state_flow/core/ITERATION_LOG.md`

## Scope guard (paper-only by default)
- For paper-writing / research-doc tasks: only change files under `paper/**` unless explicitly requested otherwise.
- If code changes are required, write a concrete handoff request in `paper/state_flow/core/STATUS.md` (what/where/how to
  validate), instead of changing `src/**` directly.

## Where to write
- Core doc map: `paper/state_flow/core/README.md`
- Backlog: `paper/state_flow/core/09_TODO_and_Backlog.md`

## Optional validation
- Docs links: `python -m scripts.validate_docs` (run from repo root)

