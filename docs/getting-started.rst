Getting Started
===============

Purpose
-------

This repository provides an immediate TSA29 baseline for research use while
retaining a reproducible rebuild pathway.

Use this page first when you need to decide whether you are:

- consuming the published snapshot as-is,
- validating that the snapshot contract is still wired correctly, or
- attempting a full rebuild on a host that has the required external runtime
  surfaces.

Prerequisites
-------------

- Python environment with ``femic`` installed.
- Access to shared base datasets (see external data notes in README).
- If you want a full rebuild rather than a dry-run/snapshot check, a host that
  can satisfy the Patchworks runtime requirements.

Quickstart
----------

.. code-block:: bash

   femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun

This quickstart is intentionally the portable baseline. It tells you:

1. the instance config still parses and points at the expected files,
2. the rebuild spec is structurally valid, and
3. the rebuild runner can resolve the declared steps without mutating the
   published baseline.

Snapshot-First Versus Rebuild-Capable Use
-----------------------------------------

Two valid usage modes exist for this repository:

- **Snapshot-first use**
  Treat the checked-in outputs under ``output/patchworks_tsa29_validated/`` as
  the immediate student/reviewer baseline.
- **Rebuild-capable use**
  Use the rebuild spec, runtime configs, and evidence workflow to confirm that
  a suitably provisioned host can reproduce the baseline or explain drift.

For most readers, snapshot-first use is the right starting point. Full rebuilds
are primarily for maintainers and reviewers working on reproducibility or
pipeline changes.

Recommended First Inspection Targets
------------------------------------

After the quickstart checks pass, inspect these files first:

- ``output/patchworks_tsa29_validated/forestmodel.xml``
- ``output/patchworks_tsa29_validated/fragments/``
- ``evidence/reference_rebuild_report.latest.json``
- ``evidence/ws3_smoke_report.latest.json``
- ``metadata/lineage_registry.yaml``

Authoritative Paths
-------------------

- Config: ``config/run_profile.tsa29.yaml``
- TIPSY rules: ``config/tipsy/tsa29.yaml``
- Rebuild contract: ``config/rebuild.spec.yaml``
- Allowlisted expected drift: ``config/rebuild.allowlist.yaml``
- Patchworks runtime config: ``config/patchworks.runtime.windows.yaml``
- Baseline output: ``output/patchworks_tsa29_validated/``
- Validation bundle: ``output/patchworks_tsa29_validation/``

Next Pages
----------

- :doc:`data-and-provenance`
- :doc:`rebuild-and-qa`
- :doc:`troubleshooting`
