Troubleshooting
===============

Purpose
-------

Use this page when the TSA29 snapshot validates poorly, the BTC-first rebuild
path fails, or the evidence state looks surprising.

Case Validation Fails
---------------------

- Re-check ``config/run_profile.tsa29.yaml`` and ``config/tipsy/tsa29.yaml``.
- Confirm shared base datasets are available in your configured data root.
- If you are using the linked FEMIC public-data mirror, set
  ``FEMIC_EXTERNAL_DATA_ROOT`` before running the case checks.
- Re-run the portable validation path in order:

  .. code-block:: bash

     femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
     femic instance validate-spec --spec config/rebuild.spec.yaml
     femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun

``femic run`` Stops Before Bundle Assembly
------------------------------------------

On the current contract, that is expected if FEMIC has successfully reached the
BTC boundary.

Confirm the boundary artifacts:

- ``data/03_input-tsa29.csv``

Then resume with:

.. code-block:: bash

   femic tsa btc-post-tipsy --run-config config/run_profile.tsa29.yaml --tsa 29 --run-id <id>

Do not treat the stop at ``03_input-tsa29.csv`` as a failure unless the
expected boundary artifacts are missing or malformed.

BTC Output Looks Missing or Stale
---------------------------------

- Confirm you resumed the same ``--run-id`` that produced
  ``data/03_input-tsa29.csv``.
- Confirm unattended BTC refreshed:
  - ``data/04_output-tsa29.csv``
  - ``data/04_error-tsa29.csv``
- Do not diagnose the current rebuild lane from removed DAT/``.out`` seam
  artifacts; the active handoff is CSV-only.

Patchworks Preflight Fails
--------------------------

- Confirm ``config/patchworks.runtime.windows.yaml`` matches your local Windows
  Patchworks installation paths.
- Confirm the TSA29 runtime no longer points at K3Z model paths.
- Run:

  .. code-block:: bash

     femic patchworks preflight --config config/patchworks.runtime.windows.yaml

Evidence Looks Worse Than Expected
----------------------------------

- Inspect ``evidence/reference_rebuild_report.latest.json`` first.
- Distinguish between:
  - a warning state already documented in the repo, and
  - a new regression that changes the expected baseline/evidence story.
- If curve behavior is the concern, inspect:
  - ``plots/tipsy_vdyp_tsa29-*.png`` (accepted ``54``-plot comparison family)
  - ``evidence/curve_selection_summary-tsa29-p67_3b_tsa29_smoothed_default_20260510g.csv``
  - ``evidence/managed_au_rule_audit-tsa29-p68_1f_20260510a.csv``

Rebuild Diffs Unexpectedly
--------------------------

- Inspect the latest report in ``runtime/logs/``.
- Compare against ``config/rebuild.allowlist.yaml`` and only allowlist
  intentional structural changes.
- For repeatable bootstrap sampling during investigation, prefer setting
  ``FEMIC_SAMPLING_SEED=29`` in the shell rather than assuming the run-profile
  YAML carries that value.

Where To Escalate
-----------------

- Rebuild/evidence contract questions:
  see ``runbooks/REBUILD_RUNBOOK.md``
- Snapshot provenance questions:
  see ``metadata/lineage_registry.yaml``
- Parent FEMIC runtime/bootstrap questions:
  see the main FEMIC docs tree in the parent repository
