# Change Log

Newest entries are appended last.

## 2026-06-27

- Started the TSA29 documentation expansion lane under
  `UBC-FRESH/femic-tsa29-instance#9`.
- Added instance-local roadmap and changelog tracking because the TSA29 repo
  did not previously carry `ROADMAP.md`, `CHANGE_LOG.md`, or a `planning/`
  directory.
- Initial audit found an existing Sphinx docs tree and GitHub Pages workflow,
  so the docs lane is an expansion and publication-hardening pass rather than
  a blank-docs bootstrap.
- Expanded the Sphinx docs with TSA29-specific project overview, THLB
  reconstruction guidance, Patchworks runtime status, teaching workflows,
  advanced student challenges, and known limitations pages.
- Aligned the GitHub Pages workflow with the current TFL 6 pattern, including
  pull-request builds, Pages configuration, Node 24 compatibility env, and
  deploy-only-on-main/workflow-dispatch behavior.
- GitHub Pages was enabled for the repository with workflow deployment after
  the first PR run showed the Pages site had not been created yet.
- Validation: `sphinx-build -b html docs docs/_build/html -W` passed.

## 2026-06-27

- Started issue `#11` after finding the published yield-curve gallery served
  git-annex pointer payloads instead of real PNG images. The local maintainer
  checkout had materialized plot files, but GitHub Pages built from a plain Git
  checkout where `plots/tipsy_vdyp_tsa29-*.png` resolved to annex pointers.
- Added plain-Git copies of the accepted 54 TIPSY-vs-VDYP plot PNGs under
  `docs/_static/yield-curves/`, repointed `docs/yield-curve-comparisons.rst`
  to those docs-static assets, and kept the original annex-backed `plots/`
  evidence surface unchanged.
- Validation: `sphinx-build -b html docs docs/_build/html -W` passed.
- Deployed the D1.1 repair to GitHub Pages from `main` and verified the public yield-curve page plus representative image URL. `https://ubc-fresh.github.io/femic-tsa29-instance/_images/tipsy_vdyp_tsa29-21000.png` returned HTTP 200, `24485` bytes, and the PNG signature `89 50 4E 47`.

## 2026-06-30

- Started runtime tracking hygiene under issue `#13` after fresh Windows
  materialization exposed checkout fragility from deep tracked
  `runtime/logs/**` paths.
- Added a broad `runtime/` ignore rule and removed 1,276 tracked
  `runtime/**` artifacts from the Git index while leaving local working-tree
  runtime files generated and ignored.
- Verification before commit: `git ls-files runtime` returned no tracked
  paths, and the `arbutus-s3` block-payload annex audit returned no missing
  keys for `models/tsa29_patchworks_model/blocks`.
- Fresh short-path Windows clone verification passed: the branch checked out
  without tracked `runtime/**` long-path failures, DataLad fetched
  `blocks.dbf`, `blocks.shp`, and `blocks.shx` from `arbutus-s3`, no block
  keys remained missing locally, and `blocks.shp` read as ESRI shapefile file
  code `9994` with polygon shape type `5`.

## 2026-07-01

- Started the TSA29 strict locked-chain package extraction under issue `#15`.
- Created branch `feature/tsa29-femic-strict-chain` as the instance side of
  parent FEMIC P90.
- Recorded the active plan in `ROADMAP.md`: this repository will own the
  `tsa29_locked_chain_strict` named-pipeline contract through an installable
  `tsa29_femic` package and a `femic.named_pipeline_contracts` entry point.
- Scope is intentionally narrow: TSR adjudication overlays, Patchworks variant
  registries, and instance catalogs remain later parent roadmap phases.

## 2026-07-01

- Added installable package `tsa29_femic` with entry point
  `femic.named_pipeline_contracts = tsa29_locked_chain_strict`.
- Moved TSA29 strict locked-chain row-order policy, ledger interpretation,
  restart-seam preflight, GLB checkpoint materialization, strict parent-step
  sequencing, and locked-ledger validation into `tsa29_femic.locked_chain`.
- Added TSA29-local tests for provider metadata, handler factory behavior,
  row-order policy, ledger validation, preflight, and strict-sequence routing.
- Verified focused TSA29 checks with editable install, ruff, and pytest.
