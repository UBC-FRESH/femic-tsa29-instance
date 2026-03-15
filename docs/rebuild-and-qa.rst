Rebuild and QA
==============

Deterministic Rebuild
---------------------

.. code-block:: bash

   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --run-id tsa29_full

Evidence Promotion
------------------

.. code-block:: bash

   femic instance promote-evidence --output evidence/reference_rebuild_report.latest.json

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

