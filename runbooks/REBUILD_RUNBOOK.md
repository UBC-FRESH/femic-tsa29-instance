# TSA29 Rebuild Runbook

## Portable checks

1. `femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy`
2. `femic instance validate-spec --spec config/rebuild.spec.yaml`
3. `femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun`

## Active BTC-first rebuild path

1. Ensure `config/patchworks.runtime.windows.yaml` points at your local
   Patchworks install. The runtime expects:
   - fragments under `output/patchworks_tsa29_validated/fragments/`
   - ForestModel XML under `output/patchworks_tsa29_validated/`
   - tracks under `models/tsa29_patchworks_model/tracks/`
   - on known-good Windows workstations, inherit the real system-level
     `SPS_LICENSE_SERVER` value instead of injecting a replacement runtime
     license value through FEMIC config
   - if a thin checkout is missing annex-backed validated fragments or other
     shipped runtime payloads, materialize them with `datalad get` before
     Patchworks preflight rather than regenerating them blindly
2. Ensure `FEMIC_EXTERNAL_DATA_ROOT` points at the materialized public-data
   mirror before running rebuild commands.
3. If you need deterministic bootstrap sampling during investigation, set
   `FEMIC_SAMPLING_SEED=29` in the shell.
4. Run the upstream compile to the BTC boundary:
   `femic run --run-config config/run_profile.tsa29.yaml --run-id tsa29_full`
5. Confirm FEMIC stopped at the intended handoff seam:
   - `data/03_input-tsa29.csv`
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

## Comparison note

Treat `plots/tipsy_vdyp_tsa29-*.png` as the current accepted comparison
surface. The active TSA29 library is the refreshed `54`-plot family aligned to
the current managed-AU lane.
