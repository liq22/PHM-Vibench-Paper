# Code Area Rules (`src/**`, `configs/**`, tooling)

## Config-first contract (do not break)
- The supported entrypoint is `python main.py --config <yaml> [--override key=value ...]`.
- Keep the 5-block model: `environment/data/model/task/trainer`.
- Do not hardcode experiment parameters in Python; commit them into `configs/**`.

## Traceability gates
- If you add/modify maintained demos, update `configs/config_registry.csv`.
- Regenerate atlas when registry changes: `python -m scripts.gen_config_atlas`.
- Validate configs: `python -m scripts.validate_configs`.

## Testing expectations
- Prefer running maintained tests: `python -m pytest test/`.
- Avoid unrelated refactors; keep PRs reviewable.

