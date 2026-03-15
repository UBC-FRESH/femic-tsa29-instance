# TSA29 Curve Stability Evidence (2026-03-15)

This note records the Phase 19.15 curve-QA rerun after plotting/fitting updates.

## Inputs and run records

- Curve event log: `../vdyp_io/logs/vdyp_curve_events-tsa29-20260315T184955Z.jsonl`
- Run event log: `../vdyp_io/logs/vdyp_runs-tsa29-tsa29_warm_cov80b_20260315T073353Z.jsonl`
- Post-TIPSY manifest: `../vdyp_io/logs/run_manifest-post_tipsy_20260315T190051Z.json`
- Selection summary CSV: `curve_selection_summary-tsa29-20260315T184955Z.csv`

## QA summary

- Stratum coverage target run: `top_area_coverage=0.80`
- Selected strata: `18` (`coverage=0.8061826878755755`)
- TSA29 AU-level overlay plots regenerated: `54` (`plots/tipsy_vdyp_tsa29-*.png`)
- Stratum SI violin diagnostic regenerated: `plots/strata-tsa29.png`

## Curve-selection outcomes (54 rows)

- `primary_nlls`: 12
- `tail_blend`: 19
- `merchantable_floor`: 22
- `censored_refit`: 1

## Acceptance notes

- First-point anchor checks passed (`167/167`, mismatches `0`).
- Curve-warning events were reviewed (`34` warning events in curve log).
- Post-TIPSY bundle assembly completed and refreshed:
  - `data/model_input_bundle/au_table.csv`
  - `data/model_input_bundle/curve_table.csv`
  - `data/model_input_bundle/curve_points_table.csv`

## Caveat

The final post-TIPSY finalize step for this run used
`FEMIC_ALLOW_STALE_TIPSY_OUTPUT=1` to bypass timestamp freshness enforcement,
because `data/04_output-tsa29.out` mtime lagged the regenerated
`data/02_input-tsa29.dat` handoff file.
