Troubleshooting
===============

Purpose
-------

Use this page when the TSA29 snapshot validates poorly, a rebuild path fails,
or the evidence state looks surprising.

Case Validation Fails
---------------------

- Re-check ``config/run_profile.tsa29.yaml`` and ``config/tipsy/tsa29.yaml``.
- Confirm shared base datasets are available in your configured data root.
- Re-run the portable baseline checks in order:

  .. code-block:: bash

     femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
     femic instance validate-spec --spec config/rebuild.spec.yaml
     femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun

Stage 01a Rebuild Fails With TSA Index Mismatch
-----------------------------------------------

Current Linux workspace runs can fail in 01a with a TSA index-selection
``KeyError`` for ``tsa='29'``.

Interpret that failure correctly:

- it is a known current rebuild limitation,
- it is already captured in ``evidence/reference_rebuild_report.latest.json``,
- it does not invalidate the checked-in TSA29 snapshot baseline.

If you hit this failure, do not treat it as evidence that the published output
package is unusable. Treat it as an explicitly documented rebuild gap on the
current host/runtime path.

Patchworks Preflight Fails
--------------------------

- Confirm ``config/patchworks.runtime.windows.yaml`` matches your local
  Windows Patchworks installation paths.
- Run:

  .. code-block:: bash

     femic patchworks preflight --config config/patchworks.runtime.windows.yaml

Evidence Looks Worse Than Expected
----------------------------------

- Inspect ``evidence/reference_rebuild_report.latest.json`` first.
- Distinguish between:
  - a warning state that is already documented as the current known limitation,
  - and a new regression that changes the expected baseline/evidence story.
- If curve behavior is the concern, inspect:
  - ``evidence/curve_stability_report.20260315.md``
  - ``evidence/curve_selection_summary-tsa29-20260315T184955Z.csv``

Rebuild Diffs Unexpectedly
--------------------------

- Inspect latest report in ``vdyp_io/logs/``.
- Compare against ``config/rebuild.allowlist.yaml`` and only allowlist
  intentional structural changes.

Where To Escalate
-----------------

- Rebuild/evidence contract questions:
  see ``runbooks/REBUILD_RUNBOOK.md``
- Snapshot provenance questions:
  see ``metadata/lineage_registry.yaml``
- Parent FEMIC runtime/bootstrap questions:
  see the main FEMIC docs tree in the parent repository
