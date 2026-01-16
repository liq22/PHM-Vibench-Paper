# Global Rules (all tasks)

## Non-negotiables
- Do not fabricate results, metrics, citations, or file contents.
- If unsure, write `TODO:VERIFY` + the exact verification step.
- Keep changes minimal, scoped, and consistent with existing repo conventions.

## Paper knowledge base (explicit SSOT)
- Paper work lives under `paper/**`. Each paper project must explicitly declare its docs SSOT in a local memory file
  (e.g., `paper/**/CLAUDE.md`), including the mandatory checkpoint `STATUS.md` (read first; update on completion).

## Guardrails
- Prefer editing within the requested area only (e.g., paper tasks → `paper/**`).
- When asked to change code, keep the config-first contract and run the maintained validation gates in `AGENTS.md`.
