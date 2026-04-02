# TSA29 Rebuild Runbook

## Portable checks

1. `femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy`
2. `femic instance validate-spec --spec config/rebuild.spec.yaml`
3. `femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun`

## Active BTC-first rebuild path

1. Ensure `config/patchworks.runtime.windows.yaml` points at your local
   Patchworks install. The runtime expects:
   - fragments under `output/patchworks_tsa29_validated/fragments/`
   - ForestModel XML under `models/tsa29_patchworks_model/yield/`
   - tracks under `models/tsa29_patchworks_model/tracks/`
   - if the thin checkout only contains `output/patchworks_tsa29_validated/fragments/README.md`,
     regenerate the validated fragments bundle before Patchworks preflight:
     `femic export patchworks --tsa 29 --bundle-dir data/model_input_bundle --checkpoint data/ria_vri_vclr1p_checkpoint7.feather --output-dir output/patchworks_tsa29_validated`
2. Ensure `FEMIC_EXTERNAL_DATA_ROOT` points at the materialized public-data
   mirror before running rebuild commands.
3. If you need deterministic bootstrap sampling during investigation, set
   `FEMIC_SAMPLING_SEED=29` in the shell.
4. Run the upstream compile to the BTC boundary:
   `femic run --run-config config/run_profile.tsa29.yaml --run-id tsa29_full`
5. Confirm FEMIC stopped at the intended handoff seam:
   - `data/03_input-tsa29.csv`
   - `data/tipsy_params_tsa29.xlsx`
   - optional legacy mirror: `data/02_input-tsa29_si_plus2.dat`
6. Resume with unattended BTC and downstream bundle assembly:
   `femic tsa btc-post-tipsy --run-config config/run_profile.tsa29.yaml --tsa 29 --run-id tsa29_full`
7. Confirm returned BTC artifacts:
   - `data/04_output-tsa29.csv`
   - `data/04_error-tsa29.csv`
8. Continue Patchworks validation:
   - `femic patchworks preflight --config config/patchworks.runtime.windows.yaml`
   - `femic patchworks build-blocks --config config/patchworks.runtime.windows.yaml --with-topology --topology-backend patchworks-raster`
   - `femic patchworks matrix-build --config config/patchworks.runtime.windows.yaml --run-id tsa29_full`
   - Matrix Builder also requires a currently available Patchworks license seat;
     if stderr reports `No license available`, stop there and rerun once the
     license server can grant a seat.
9. Promote latest report if needed:
   `femic instance promote-evidence --output evidence/reference_rebuild_report.latest.json`

## Legacy note

The older `data/02_input-tsa29*.dat` and `data/04_output-tsa29.out` artifacts
remain useful as historical snapshot evidence, but they are no longer the
primary operator contract for issue `#10`.
