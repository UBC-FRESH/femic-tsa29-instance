Data and Provenance
===================

Purpose
-------

This page summarizes what is actually published in the TSA29 snapshot and which
files are authoritative for provenance, evidence, and artifact integrity.

Snapshot Inventory
------------------

The published snapshot includes:

- ``data/model_input_bundle/*.csv``
- ``data/02_input-tsa29_si_plus2.dat``
- ``data/04_output-tsa29.out``
- ``data/tipsy_curves_tsa29.csv``
- ``data/tipsy_sppcomp_tsa29.csv``
- ``data/vdyp_curves_smooth-tsa29.feather``
- ``data/vdyp_lyr-tsa29.feather``
- ``data/vdyp_ply-tsa29.feather``

These artifacts support both immediate inspection and later rebuild/evidence
comparison. They are not just disposable intermediates.

Authoritative Provenance Files
------------------------------

Use these files as the source of truth for lineage and integrity:

- ``metadata/lineage_registry.yaml``
- ``metadata/artifact_checksums.sha256``
- ``metadata/large_artifacts.sha256``
- ``evidence/reference_rebuild_report.latest.json``
- ``evidence/ws3_smoke_report.latest.json``

Provenance Fields
-----------------

- Source FEMIC commit
- Source run manifests
- Build date
- Artifact checksums

See ``metadata/lineage_registry.yaml`` and
``metadata/artifact_checksums.sha256`` for canonical tracking.

Current Published Provenance State
----------------------------------

At the time of this snapshot:

- source FEMIC commit is recorded as ``5caa72c``
- snapshot date is recorded as ``2026-03-14``
- the published baseline is treated as validated for snapshot-first use
- the rebuild report records one known Linux workspace limitation in Stage 01a
  rather than claiming a clean full rebuild on that host

Evidence Files Worth Reading First
----------------------------------

- ``evidence/reference_rebuild_report.latest.json``
  Current rebuild/evidence summary and known issue note.
- ``evidence/ws3_smoke_report.latest.json``
  Woodstock/ws3 smoke evidence for the published output package.
- ``evidence/curve_stability_report.20260315.md``
  Reviewer-facing narrative summary of the TSA29 curve-stability rerun.
- ``evidence/curve_selection_summary-tsa29-20260315T184955Z.csv``
  Row-level selected-path evidence for the TSA29 curve pass.

Known Limitation Captured In Provenance
---------------------------------------

The lineage and rebuild evidence deliberately preserve the current known issue:

- a Linux workspace run can fail in Stage 01a with a TSA index mismatch
  (``KeyError`` on ``tsa='29'``)

That issue does **not** invalidate the published snapshot. It does mean readers
should distinguish between:

- the validity of the checked-in TSA29 baseline, and
- the current status of full live rebuilds on a given host.
