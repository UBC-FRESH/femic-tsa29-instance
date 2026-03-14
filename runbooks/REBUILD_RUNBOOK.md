# TSA29 Rebuild Runbook

## Portable ASAP checks

1. `femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy`
2. `femic instance validate-spec --spec config/rebuild.spec.yaml`
3. `femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun`

## Full rebuild path (Patchworks-enabled host)

1. Ensure `config/patchworks.runtime.windows.yaml` points at your local Patchworks install.
2. Run:
   `femic instance rebuild --spec config/rebuild.spec.yaml --run-id tsa29_full`
3. Promote latest report:
   `femic instance promote-evidence --output evidence/reference_rebuild_report.latest.json`

## Known current issue

At snapshot publication time, `femic run --run-config config/run_profile.tsa29.yaml`
can fail in 01a on TSA index selection (`KeyError` for `tsa_code='29'`) in this
Linux workspace. Snapshot outputs included in this repo were built from prior
validated TSA29 artifacts and should be used as the immediate student baseline
until that regression is resolved.
