Rebuild and QA
==============

Purpose
-------

This page explains how to validate, rebuild, and interpret the TSA29 instance
without confusing the published snapshot baseline with the current BTC-first
rebuild path.

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
- rebuild-runner step resolution without mutating the published baseline.

Deterministic Rebuild Script
----------------------------

Primary source of truth for TSA29 rebuild sequence and invariants:

- ``config/rebuild.spec.yaml``

Use instance-local FEMIC rebuild orchestration for reproducible TSA29 checks:

.. code-block:: bash

   femic instance rebuild \
     --spec config/rebuild.spec.yaml \
     --run-config config/run_profile.tsa29.yaml \
     --tipsy-config-dir config/tipsy \
     --patchworks-config config/patchworks.runtime.windows.yaml \
     --with-patchworks \
     --run-id tsa29_rebuild_check

Manual equivalent command sequence (mirrors the active contract):

.. code-block:: bash

   femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
   femic prep geospatial-preflight
   femic run --run-config config/run_profile.tsa29.yaml --run-id tsa29_rebuild_check
   femic tsa btc-post-tipsy --run-config config/run_profile.tsa29.yaml --tsa 29 --run-id tsa29_rebuild_check
   femic patchworks preflight --config config/patchworks.runtime.windows.yaml
   femic patchworks build-blocks --config config/patchworks.runtime.windows.yaml --with-topology
   femic patchworks matrix-build --config config/patchworks.runtime.windows.yaml --run-id tsa29_rebuild_check

Patchworks runtime assumptions for the supported Windows path:

- use a Windows workstation with a valid local Patchworks installation;
- prefer the real system-level ``SPS_LICENSE_SERVER`` setting already present
  on that workstation instead of injecting a replacement runtime value;
- treat ``output/patchworks_tsa29_validated/forestmodel.xml`` plus
  ``output/patchworks_tsa29_validated/fragments/`` as the canonical Matrix
  Builder input pair.

Interpret the seam this way:

- ``femic run`` is expected to stop at the BTC boundary.
- ``data/03_input-tsa29.csv`` is the canonical Stage 01a handoff artifact.
- ``femic tsa btc-post-tipsy`` is the supported continuation seam.
- ``data/04_output-tsa29.csv`` and ``data/04_error-tsa29.csv`` are the
  canonical returned BTC artifacts.

Outputs
-------

- Rebuild report:
  ``vdyp_io/logs/instance_rebuild_report-<run_id>.json``
- Matrix logs:
  ``vdyp_io/logs/patchworks_matrixbuilder_{stdout,stderr,manifest}-<run_id>.log``

Primary Evidence Files
----------------------

Read these files first after a rebuild or validation pass:

- ``evidence/reference_rebuild_report.latest.json``
- ``evidence/ws3_smoke_report.latest.json``
- ``evidence/curve_stability_report.20260315.md``
- ``evidence/curve_selection_summary-tsa29-20260315T184955Z.csv``
- ``vdyp_io/logs/`` manifests/logs referenced by the rebuild report

Acceptance Checklist
--------------------

Treat the QA pass as acceptable when:

- ``femic prep validate-case`` passes,
- ``femic instance validate-spec`` passes,
- dry-run rebuild resolves cleanly,
- a real ``femic run`` stops at the expected BTC boundary and emits
  ``data/03_input-tsa29.csv``,
- ``femic tsa btc-post-tipsy`` consumes the matching run and emits
  ``data/04_output-tsa29.csv`` plus ``data/04_error-tsa29.csv``,
- downstream Patchworks steps complete on the same run/evidence chain,
- the rebuild/evidence report is interpretable and any warning state is
  explicitly understood.

Legacy Note
----------- 

The older ``02_input-tsa29*.dat`` / ``04_output-tsa29.out`` seam remains
historical snapshot evidence only. Do not treat it as the current default
operator workflow.
