# femic-tsa29-instance

Canonical standalone **TSA29 FEMIC instance** for student use, reproducibility
work, and issue `#10` closeout.

## Purpose

This repository now carries two related stories:

1. A published TSA29 snapshot baseline that remains useful for inspection and
   teaching.
2. A current rebuild contract that has been rebased onto FEMIC's BTC-first
   TIPSY seam.

The active supported rebuild path is now:

- `data/03_input-tsa29.csv`
- unattended BTC (`TIPSYbtc.exe /TSR`)
- `data/04_output-tsa29.csv`
- `data/04_error-tsa29.csv`
- `femic tsa btc-post-tipsy --run-config config/run_profile.tsa29.yaml --tsa 29 --run-id <id>`

Legacy `02_input-tsa29*.dat` and `04_output-tsa29.out` artifacts remain in the
repo as historical snapshot evidence and compatibility context only. They are
no longer the primary operator contract.

## Source Provenance

- FEMIC source repo: `https://github.com/UBC-FRESH/femic`
- Published snapshot source commit: `b072025`
- Published snapshot date (UTC): `2026-04-03`

Those provenance fields describe the current published TSA29 PoC package in
this repo. Use the docs, runbook, and rebuild spec here as the source of truth
for what this published snapshot includes and how it should be materialized.

## DataLad Dataset Policy

This repository is now a **DataLad/git-annex-managed standalone instance**.

Publication policy:

- keep docs, config, small canonical text artifacts, and launch wrappers in Git
- annex bulky instance payloads and oversized rebuild/runtime artifacts
- do **not** publish transient local runtime spill such as saved-stage dumps,
  scratch logs, or temporary launcher traces

The published standalone Patchworks package is intentionally split into two
complementary surfaces:

- **launch-critical runtime assets**
  `models/tsa29_patchworks_model/blocks/`, `models/tsa29_patchworks_model/tracks/`,
  and the analysis/PIN launch surfaces
- **editable anti-lock-in rebuild assets**
  `output/patchworks_tsa29_validated/forestmodel.xml` plus
  `output/patchworks_tsa29_validated/fragments/`

That split is deliberate: users should be able to open the model directly in
Patchworks *and* still fly outside FEMIC for manual overlays / local rebuild
variants if they choose.

## Included Snapshot Assets

- Runtime configs: `config/run_profile.tsa29.yaml`, `config/tipsy/tsa29.yaml`
- Rebuild contract: `config/rebuild.spec.yaml`, `config/rebuild.allowlist.yaml`
- TSA29 model-input bundle: `data/model_input_bundle/*.csv`
- Historical TIPSY seam artifacts:
  - `data/02_input-tsa29_si_plus2.dat`
  - `data/04_output-tsa29.out`
- Curve/intermediate artifacts: `data/tipsy_*tsa29*`, `data/vdyp_*tsa29*`
- Validated Patchworks outputs: `output/patchworks_tsa29_validated/`
- Validation bundle/checkpoint: `output/patchworks_tsa29_validation/`
- Canonical docs + figure appendix: `docs/`

## Excluded

- Secrets, credentials, and local environment scripts.
- Non-TSA29 bulky base datasets (use the shared public-data mirror workflow in
  the parent FEMIC project).
- Fresh BTC-generated `03_input-tsa29.csv`, `04_output-tsa29.csv`, and
  `04_error-tsa29.csv` until a current rebuild/evidence pass republishes them.

## Quickstart

0. Materialize required payloads if this checkout was cloned as a DataLad
   dataset with annexed content unavailable locally:

   ```bash
   git annex version
   datalad --version
   git annex info --fast
   datalad get models/tsa29_patchworks_model/blocks
   datalad get models/tsa29_patchworks_model/tracks
   datalad get output/patchworks_tsa29_validated
   ```

   If the published snapshot names a specific special remote, enable that
   remote before the `datalad get` calls above.

   On Windows inside a parent FEMIC checkout, prefer the active virtual
   environment explicitly:

   ```powershell
   .\.venv\Scripts\python.exe -m datalad get models/tsa29_patchworks_model/blocks
   .\.venv\Scripts\python.exe -m datalad get models/tsa29_patchworks_model/tracks
   .\.venv\Scripts\python.exe -m datalad get output/patchworks_tsa29_validated
   ```

1. Validate the case wiring:

   ```bash
   femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
   ```

2. Inspect the current published baseline:

   - `output/patchworks_tsa29_validated/forestmodel.xml`
   - `output/patchworks_tsa29_validated/fragments/`
   - `models/tsa29_patchworks_model/blocks/`
   - `models/tsa29_patchworks_model/tracks/`

   For the known-good Windows Patchworks path, use a workstation with
   Patchworks already installed and licensed. FEMIC should normally inherit the
   real system-level `SPS_LICENSE_SERVER` value on that host rather than
   overriding it in runtime config.

   Thin-checkout note: if any annex-backed validated fragments or runtime model
   files are absent locally, materialize them with `datalad get` before
   Patchworks preflight rather than treating the published instance as
   incomplete.

3. Validate the rebuild contract without mutating the instance:

   ```bash
   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun
   ```

4. For the active BTC-first rebuild path, use the sequence documented in
   `docs/rebuild-and-qa.rst` and `runbooks/REBUILD_RUNBOOK.md`.

## Current Rebuild Contract

The approved current contract for issue `#10` is:

1. `femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy`
2. `femic prep geospatial-preflight`
3. `femic run --run-config config/run_profile.tsa29.yaml --run-id <id>`
4. confirm FEMIC stops at the BTC boundary with:
   - `data/03_input-tsa29.csv`
   - `data/tipsy_params_tsa29.xlsx`
   - optional legacy mirror: `data/02_input-tsa29_si_plus2.dat`
5. run unattended BTC and resume:

   ```bash
   femic tsa btc-post-tipsy --run-config config/run_profile.tsa29.yaml --tsa 29 --run-id <id>
   ```

6. confirm returned BTC artifacts:
   - `data/04_output-tsa29.csv`
   - `data/04_error-tsa29.csv`
7. continue Patchworks validation/evidence steps:
   - regenerate `output/patchworks_tsa29_validated/fragments/` if the thin
     checkout does not already carry the shapefile set
   - use `output/patchworks_tsa29_validated/forestmodel.xml` together with the
     matching validated fragments set as the canonical Matrix Builder input pair
   - use `--topology-backend patchworks-raster` for
     `femic patchworks build-blocks` on the full TSA29 validated surface
   - expect `femic patchworks matrix-build` to require an available Patchworks
     license seat on the current host

See full docs in `docs/`.
