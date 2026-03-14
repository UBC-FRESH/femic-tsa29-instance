# femic-tsa29-instance

Canonical standalone **TSA29 FEMIC instance** for immediate student use and
pipeline reproducibility testing.

## Purpose

This repository provides a hybrid deliverable:

1. A ready-to-use TSA29 snapshot baseline (usable now).
2. A rebuild contract and evidence path to validate pipeline reproducibility.

## Source Provenance

- FEMIC source repo: `https://github.com/UBC-FRESH/femic`
- FEMIC source commit: `5caa72c`
- Snapshot date (UTC): `2026-03-14`

## Included Snapshot Assets

- Runtime configs: `config/run_profile.tsa29.yaml`, `config/tipsy/tsa29.yaml`
- Rebuild contract: `config/rebuild.spec.yaml`, `config/rebuild.allowlist.yaml`
- TSA29 model-input bundle: `data/model_input_bundle/*.csv`
- BatchTIPSY artifacts: `data/02_input-tsa29_si_plus2.dat`, `data/04_output-tsa29.out`
- Curve/intermediate artifacts: `data/tipsy_*tsa29*`, `data/vdyp_*tsa29*`
- Validated Patchworks outputs: `output/patchworks_tsa29_validated/`
- Validation bundle/checkpoint: `output/patchworks_tsa29_validation/`
- Canonical docs + figure appendix: `docs/`

## Excluded

- Secrets, credentials, local env scripts.
- Non-TSA29 bulky base datasets (use shared mirror workflow in the FEMIC parent
  project and data-access runbooks).

## Quickstart (Snapshot-first)

1. Validate case wiring:

   ```bash
   femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
   ```

2. Inspect baseline outputs:

   - `output/patchworks_tsa29_validated/forestmodel.xml`
   - `output/patchworks_tsa29_validated/fragments/`

3. Rebuild-plan smoke (no mutation):

   ```bash
   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun
   ```

See full docs in `docs/`.
