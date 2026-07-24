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

Annexed Payload Reports "content is not available"
---------------------------------------------------

Symptoms in a fresh clone:

.. code-block:: text

   output/patchworks_tsa29_validated/fragments/fragments.dbf is a git-annex
   pointer file. Its content is not available in this repository.

   get(error): ... [not available;
     (Note that these git remotes have annex-ignore set: origin)]

First refresh the annex location metadata, then retry:

.. code-block:: bash

   git fetch origin git-annex
   git annex merge
   datalad get output/patchworks_tsa29_validated/fragments

Diagnostics:

- ``git annex whereis <path>`` should list ``[arbutus-s3]`` as a copy. If the
  only copy listed is a maintainer workstation, the published location log is
  stale and the maintainer must run ``git push origin git-annex``.
- ``[arbutus-s3]`` shown in brackets means the special remote is known but not
  locally enabled. That is expected and fine: the remote is published with
  ``public=yes`` and a ``publicurl``, so reads work over plain HTTPS with no
  S3 credentials.
- ``annex-ignore set: origin`` on the GitHub remote is also normal. GitHub
  stores git metadata only; payload content lives on ``arbutus-s3``.

Maintainer note: publishing an instance requires **two** pushes. ``git push
origin main`` does not publish the ``git-annex`` branch that carries per-key
location records. Verify with:

.. code-block:: bash

   git rev-list --count origin/git-annex..git-annex   # must be 0

Files Look Modified Immediately After ``git switch main``
----------------------------------------------------------

On Windows, git-annex detects a "crippled filesystem" and checks out an
``adjusted/main(unlocked)`` branch. Switching to plain ``main`` makes unlocked
annex pointer files appear modified even though you changed nothing.

Do not commit or discard those apparent edits. Return to the adjusted branch:

.. code-block:: bash

   git annex adjust --unlock

Work from ``adjusted/main(unlocked)`` on Windows; DataLad handles the mapping
back to ``main`` when you save.

Where To Escalate
-----------------

- Rebuild/evidence contract questions:
  see ``runbooks/REBUILD_RUNBOOK.md``
- Snapshot provenance questions:
  see ``metadata/lineage_registry.yaml``
- Parent FEMIC runtime/bootstrap questions:
  see the main FEMIC docs tree in the parent repository
