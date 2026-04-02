Data and Provenance
===================

Purpose
-------

This page summarizes what is published in the TSA29 snapshot, what the current
BTC-first rebuild seam expects, and which files are authoritative for
provenance and evidence.

Published Snapshot Inventory
----------------------------

The checked-in snapshot currently includes:

- ``data/model_input_bundle/*.csv``
- historical TIPSY seam artifacts:
  - ``data/02_input-tsa29_si_plus2.dat``
  - ``data/04_output-tsa29.out``
- ``data/tipsy_curves_tsa29.csv``
- ``data/tipsy_sppcomp_tsa29.csv``
- ``data/vdyp_curves_smooth-tsa29.feather``
- ``data/vdyp_lyr-tsa29.feather``
- ``data/vdyp_ply-tsa29.feather``

These artifacts support both immediate inspection and later rebuild/evidence
comparison. They are not just disposable intermediates.

Current BTC-First Rebuild Artifacts
-----------------------------------

The active rebuild contract now targets these artifacts on a fresh run:

- Stage 01a boundary:
  - ``data/03_input-tsa29.csv``
  - ``data/tipsy_params_tsa29.xlsx``
  - optional legacy mirror: ``data/02_input-tsa29_si_plus2.dat``
- Returned BTC seam:
  - ``data/04_output-tsa29.csv``
  - ``data/04_error-tsa29.csv``

Those CSV files are the current operator-facing seam even if the historical
DAT/out artifacts remain present in the snapshot.

Authoritative Provenance Files
------------------------------

Use these files as the source of truth for lineage and integrity:

- ``metadata/lineage_registry.yaml``
- ``metadata/artifact_checksums.sha256``
- ``metadata/large_artifacts.sha256``
- ``evidence/reference_rebuild_report.latest.json``
- ``evidence/ws3_smoke_report.latest.json``

Current Published Provenance State
----------------------------------

At the time of the published snapshot:

- source FEMIC commit was recorded as ``5caa72c``
- snapshot date was recorded as ``2026-03-14``
- the published baseline was treated as validated for snapshot-first use

Current maintainer interpretation should add one more distinction:

- the snapshot preserves the older DAT/out seam as historical evidence,
- the active rebuild contract is now BTC-first and should be evaluated through
  ``03_input-tsa29.csv`` plus ``femic tsa btc-post-tipsy``.

Evidence Files Worth Reading First
----------------------------------

- ``evidence/reference_rebuild_report.latest.json``
  Current rebuild/evidence summary.
- ``evidence/ws3_smoke_report.latest.json``
  Woodstock/ws3 smoke evidence for the published output package.
- ``evidence/curve_stability_report.20260315.md``
  Reviewer-facing narrative summary of the TSA29 curve-stability rerun.
- ``evidence/curve_selection_summary-tsa29-20260315T184955Z.csv``
  Row-level selected-path evidence for the TSA29 curve pass.
