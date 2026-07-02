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

Status: complete.

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
- [x] Deploy and verify representative public plot URLs return real PNG bytes.

## Detailed Next Steps Notes

Current edge: P91T is active under `UBC-FRESH/femic-tsa29-instance#17`.
The TSA29 TSR adjudication overlay is moving from FEMIC core into this
instance-owned `tsa29_femic` package while FEMIC keeps generic TSR recipe,
comparison, and report machinery.

## Phase H1: Runtime Tracking Hygiene (`#13`)

Status: active.

Goal: remove tracked `runtime/**` artifacts from the TSA29 instance so Windows
fresh clones are not blocked by deep runtime log paths. The `runtime/` tree is
local/generated only; durable evidence must live in explicit docs, config,
planning, evidence, or release surfaces instead.

### Tasks

- [x] Add a broad `runtime/` ignore rule.
- [x] Remove all tracked `runtime/**` files from the Git index without
  deleting local working-tree copies.
- [x] Verify `git ls-files runtime` returns no tracked files.
- [x] Verify the launch-critical Patchworks block payload remains
  materializable from `arbutus-s3`.
- [x] Prove a fresh short-path Windows clone can check out TSA29 and
  materialize `models/tsa29_patchworks_model/blocks`.
- [ ] Record the cleanup in `CHANGE_LOG.md`, push the branch, and update the
  parent FEMIC submodule pointer.

## Phase P90T: TSA29 Strict Locked-Chain Package (`#15`)

Status: complete.

Goal: own the TSA29 strict locked-chain named-pipeline contract from this
instance repository while FEMIC core keeps only generic named-pipeline
plumbing and reusable TSR/THLB execution primitives.

### Tasks

- [x] Create branch `feature/tsa29-femic-strict-chain`.
- [x] Open governing issue `UBC-FRESH/femic-tsa29-instance#15`.
- [x] Add installable package `tsa29_femic`.
- [x] Register `tsa29_locked_chain_strict` through the
  `femic.named_pipeline_contracts` entry point.
- [x] Move TSA29 row-order, ledger interpretation, seam preflight, GLB
  checkpoint materialization, strict sequence, and locked-ledger validation
  logic into `tsa29_femic`.
- [x] Migrate TSA29-specific strict-chain tests into this repository.
- [x] Verify the package with lint, tests, docs build, and editable
  integration against parent FEMIC.

## Phase P91T: TSA29 TSR Adjudication Overlay (`#17`)

Status: active.

Goal: own TSA29-specific TSR adjudication policy from this instance repository
while FEMIC core keeps generic TSR recipe parsing, execution primitives,
comparison payload construction, and report rendering.

### Tasks

- [x] Create branch `feature/tsa29-tsr-adjudication-overlays`.
- [x] Open governing issue `UBC-FRESH/femic-tsa29-instance#17`.
- [x] Add `tsa29_femic.tsr_adjudication`.
- [x] Register provider id `tsa29` through the
  `femic.tsr_adjudication_overlays` entry point.
- [x] Move TSA29 Table 3 row classifications into the instance package or
  instance config.
- [x] Move TSA29 checkpoint policy, reconstruction-gap interpretation
  overrides, and active adjudication report notes into the instance package.
- [x] Add `config/tsr/adjudication_overlay.yaml` selecting provider id
  `tsa29`.
- [ ] Verify row classification, checkpoint policy, interpretation overrides,
  and integration against editable parent FEMIC.
