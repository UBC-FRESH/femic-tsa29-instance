Rebuild and QA
==============

Purpose
-------

This page explains how to validate, rebuild, and interpret the TSA29 instance
without confusing the published snapshot baseline with the current status of a
live rebuild on your host.

Portable Validation Path
------------------------

Run this path first on any host:

.. code-block:: bash

   femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun

This sequence validates:

- instance config wiring,
- rebuild-spec structure, and
- rebuild-runner step resolution without mutating the published snapshot.

Deterministic Rebuild
---------------------

.. code-block:: bash

   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --run-id tsa29_full

Use a full rebuild only on a host that has the necessary external runtime
surfaces available for the configured steps.

Evidence Promotion
------------------

.. code-block:: bash

   femic instance promote-evidence --output evidence/reference_rebuild_report.latest.json

Primary Evidence Files
----------------------

Read these files first after a rebuild or validation pass:

- ``evidence/reference_rebuild_report.latest.json``
- ``evidence/ws3_smoke_report.latest.json``
- ``evidence/curve_stability_report.20260315.md``
- ``evidence/curve_selection_summary-tsa29-20260315T184955Z.csv``
- ``vdyp_io/logs/`` manifests/logs referenced by the rebuild report

Current Published Status
------------------------

The current checked-in rebuild evidence records:

- ``status: warning`` / ``regression_gate: warning`` for the latest reference
  rebuild report
- a known Linux workspace issue in Stage 01a TSA index selection
- a still-valid snapshot baseline for immediate student/reviewer use

That means the repository should currently be interpreted as:

- **validated snapshot baseline** for teaching/review use
- **rebuild-capable contract** with one explicitly documented host/runtime
  limitation rather than a silently broken rebuild story

Known Regression (Current Workspace)
------------------------------------

Current Linux workspace runs can fail in 01a with TSA index mismatch for
``tsa='29'``. This is tracked in runbooks and does not invalidate the snapshot
baseline included in this repository.


Curve Stability Evidence (P19.15)
---------------------------------

The latest TSA29 curve-QA rerun evidence is recorded in:

- ``evidence/curve_stability_report.20260315.md``
- ``evidence/curve_selection_summary-tsa29-20260315T184955Z.csv``

This evidence captures:

- regenerated stratum and AU-level curve diagnostics,
- selected-path outcomes across all TSA29 AU/SI rows, and
- acceptance/sign-off notes for the current curve-stability baseline.

Acceptance Checklist
--------------------

Treat the QA pass as acceptable when:

- ``femic prep validate-case`` passes,
- ``femic instance validate-spec`` passes,
- dry-run rebuild resolves cleanly,
- the rebuild/evidence report is interpretable and any warning state is
  explicitly understood,
- the curve-stability evidence still matches the intended published baseline.

