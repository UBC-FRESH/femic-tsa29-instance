# TSA29 Instance Roadmap

This roadmap tracks active work in the standalone TSA29 FEMIC instance
repository. It is intentionally instance-local: parent FEMIC roadmap entries
may point here, but this file owns TSA29-specific documentation, publication,
and package-readiness tasks.

## Phase D1: Teaching And Maintainer Documentation

Governing issue: `UBC-FRESH/femic-tsa29-instance#9`

Status: complete.

Goal: expand the existing TSA29 Sphinx documentation into a public,
teaching-facing and maintainer-facing guide comparable in depth and tone to
the completed TFL 6 teaching docs, while keeping every claim grounded in the
current TSA29 repository artifacts.

### Tasks

- [x] Audit current instance surfaces before editing:
  - existing `docs/` tree;
  - existing `.github/workflows/docs-pages.yml`;
  - `README.md`;
  - `runbooks/REBUILD_RUNBOOK.md`;
  - `metadata/lineage_registry.yaml`;
  - `config/rebuild.spec.yaml`;
  - `config/tsr/*status*`;
  - `config/tsr/thlb_locked_chain_ledger.json`;
  - `config/tsr/thlb_reconstruction_comparison.md`;
  - `evidence/patchworks_test01_scenario_20260606.md`; and
  - current GitHub issues and PRs.
- [x] Create the active GitHub documentation issue before substantive work.
- [x] Add roadmap/changelog/planning notes for the TSA29 docs lane.
- [x] Expand Sphinx docs with:
  - project overview and teaching purpose;
  - source data and TSR/THLB provenance;
  - strict/reviewed THLB reconstruction status;
  - Patchworks/runtime package status;
  - known caveats and unresolved validation boundaries;
  - maintainer rebuild/provenance guidance;
  - student-facing scenario workflows; and
  - advanced student challenge ideas.
- [x] Align the GitHub Pages workflow with the current TFL 6 pattern.
- [x] Build docs warning-clean with:
  `sphinx-build -b html docs docs/_build/html -W`.
- [x] Record the completed docs update in `CHANGE_LOG.md`, post a matching
  GitHub issue comment, commit, and push.

## Phase D1.1: Published Plot Asset Repair

Governing issue: `UBC-FRESH/femic-tsa29-instance#11`

Status: in progress.

Goal: repair the published Sphinx yield-curve gallery so GitHub Pages serves
real PNG plot bytes rather than git-annex pointer payloads copied from
`plots/`.

### Tasks

- [x] Diagnose the published Pages failure and confirm representative public
  image URLs return short annex-pointer payloads.
- [x] Add plain-Git docs-static copies of the accepted 54 TIPSY-vs-VDYP plot
  PNGs.
- [x] Repoint `docs/yield-curve-comparisons.rst` to the docs-static plot
  assets.
- [x] Build docs warning-clean.
- [ ] Deploy and verify representative public plot URLs return real PNG bytes.

## Detailed Next Steps Notes

Current edge: merge the D1.1 docs asset repair, then verify the GitHub Pages
deployment from `main` and confirm representative public plot URLs return real
PNG bytes. Do not regenerate yield curves or change TSA29 model/THLB/Patchworks
artifacts.
