# TSA29 Instance Roadmap

This roadmap tracks active work in the standalone TSA29 FEMIC instance
repository. It is intentionally instance-local: parent FEMIC roadmap entries
may point here, but this file owns TSA29-specific documentation, publication,
and package-readiness tasks.

## Phase D1: Teaching And Maintainer Documentation

Governing issue: `UBC-FRESH/femic-tsa29-instance#9`

Status: in progress.

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

## Detailed Next Steps Notes

Current edge: Phase D1 docs content and workflow edits are ready for review on
the feature branch. The docs build passed warning-clean with
`sphinx-build -b html docs docs/_build/html -W`. No TSA29 model rebuilds were
run in this docs lane. Next step after merge is to verify the GitHub Pages
deployment from `main`.
