# TSA29 Docs Lane Audit

Governing issue: `UBC-FRESH/femic-tsa29-instance#9`

Date: 2026-06-27

## Starting State

- Branch at audit start: `main`.
- Working tree at audit start: clean.
- Existing docs source: `docs/`.
- Existing docs workflow: `.github/workflows/docs-pages.yml`.
- Existing instance-local roadmap/changelog/planning surfaces: absent before
  this lane.
- Open GitHub issues before creating the docs-lane issue: none.
- Prior relevant closed issues:
  - `#8` published `v1.0.0-alpha1`;
  - `#6` rebuilt the TSA29 Patchworks model on the new THLB and yield
    surfaces;
  - `#4` refreshed the TIPSY-vs-VDYP comparison plot surface; and
  - `#3` reread docs and rebuilt yield-curve figures.

## Read Surfaces

- `README.md`
- `docs/`
- `.github/workflows/docs-pages.yml`
- `runbooks/REBUILD_RUNBOOK.md`
- `metadata/lineage_registry.yaml`
- `config/rebuild.spec.yaml`
- `config/tsr/thlb_locked_chain_ledger.json`
- `config/tsr/thlb_netdown.status.md`
- `config/tsr/thlb_reconstructed.status.md`
- `config/tsr/thlb_reconstruction_comparison.md`
- `evidence/patchworks_test01_scenario_20260606.md`
- TFL 6 reference docs under `../femic-tfl6-instance/docs/`
- TFL 6 Pages workflow under
  `../femic-tfl6-instance/.github/workflows/docs-pages.yml`

## Documentation Boundary

The TSA29 repository already contains a released alpha Patchworks package and a
first-pass docs tree. The new docs lane should therefore:

- teach the existing release and evidence boundaries more clearly;
- explain strict, reviewed, and deprecated THLB artifacts without blending
  them into one unqualified truth surface;
- document Patchworks/runtime launch and rebuild prerequisites;
- add student scenario workflows and challenge prompts; and
- avoid claiming a final production-grade model.

The docs lane should not:

- rerun TSR/THLB or Patchworks workflows;
- change release payloads;
- repair model semantics; or
- invent new validation evidence.
