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

Minimal functional Patchworks surface for TSA29:

Matrix-Builder-ready / rebuild minimum:

- ``config/patchworks.runtime.windows.yaml``
- ``output/patchworks_tsa29_validated/forestmodel.xml``
- the full validated fragments sidecar set under
  ``output/patchworks_tsa29_validated/fragments/``:
  ``fragments.shp``, ``fragments.dbf``, ``fragments.shx``,
  ``fragments.prj``, and ``fragments.cpg``

Standalone launch-ready published minimum:

- everything in the Matrix-Builder-ready tier
- after Matrix Builder, compiled tracks under
  ``models/tsa29_patchworks_model/tracks/`` including at least
  ``curves.csv``, ``features.csv``, ``products.csv``, ``treatments.csv``,
  ``protoaccounts.csv``, and ``accounts.csv``
- ``models/tsa29_patchworks_model/blocks/blocks.shp`` plus sidecars
- the topology CSV used by the shipped analysis surface
- the shipped analysis/PIN launch surfaces under
  ``models/tsa29_patchworks_model/analysis/``

Do not treat a thin checkout that only contains
``output/patchworks_tsa29_validated/fragments/README.md`` as Patchworks-ready.
Restore or regenerate the validated fragments sidecar set before Patchworks
preflight or Matrix Builder work.

Do not treat a checkout with XML/fragments/tracks but no shipped
``blocks/blocks.shp`` payload as a runnable standalone Patchworks model.

Current development-mode runtime note:

- for interactive prototype work, use
  ``models/tsa29_patchworks_model/analysis/base_gui.pin`` as the explicit
  GUI-facing launch wrapper;
- the shared TSA29 baseline analysis wiring currently loads
  ``../blocks/topology_blocks_0r.csv`` with topology distance ``0 m`` so the
  runtime adjacency graph stays smaller while the model is still under active
  development.

Interpret the seam this way:

- ``femic run`` is expected to stop at the BTC boundary.
- ``data/03_input-tsa29.csv`` is the canonical Stage 01a handoff artifact.
- ``femic tsa btc-post-tipsy`` is the supported continuation seam.
- ``data/04_output-tsa29.csv`` and ``data/04_error-tsa29.csv`` are the
  canonical returned BTC artifacts.

Outputs
-------

- Rebuild report:
  ``runtime/logs/instance_rebuild_report-<run_id>.json``
- Matrix logs:
  ``runtime/logs/patchworks_matrixbuilder_{stdout,stderr,manifest}-<run_id>.log``

Primary Evidence Files
----------------------

Read these files first after a rebuild or validation pass:

- ``evidence/reference_rebuild_report.latest.json``
- ``evidence/ws3_smoke_report.latest.json``
- ``evidence/curve_stability_report.20260315.md``
- ``evidence/curve_selection_summary-tsa29-20260315T184955Z.csv``
- ``runtime/logs/`` manifests/logs referenced by the rebuild report

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
