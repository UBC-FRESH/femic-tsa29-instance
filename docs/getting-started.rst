Getting Started
===============

Purpose
-------

This repository provides an immediate TSA29 baseline for research and teaching
while also carrying the current BTC-first rebuild contract for issue ``#10``.

Use this page first when you need to decide whether you are:

- consuming the published snapshot as-is,
- validating that the instance contract still resolves cleanly, or
- preparing for a fresh BTC-first rebuild on a host with the required external
  runtimes.

Prerequisites
-------------

- Python environment with ``femic`` installed.
- ``git-annex`` plus DataLad if you need to materialize annex-backed TSA29
  payloads from a thin clone.
- Access to the shared public-data mirror used by the parent FEMIC workflow.
- If you want a full rebuild, a Windows host with BatchTIPSY/BTC and
  Patchworks already installed and licensed.
- Known-good Patchworks runs on UBC institutional Windows workstations inherit
  the real ``SPS_LICENSE_SERVER`` value from system-level environment
  configuration. Do not override that working host configuration with a
  placeholder runtime value.

Quickstart
----------

If this checkout was cloned as a DataLad dataset and large payloads are not yet
materialized locally, start here:

.. code-block:: bash

   git annex version
   datalad --version
   git annex info --fast
   datalad get models/tsa29_patchworks_model/blocks
   datalad get models/tsa29_patchworks_model/tracks
   datalad get output/patchworks_tsa29_validated

If the published snapshot names a specific special remote, enable that remote
before the ``datalad get`` calls above.

On Windows inside a parent FEMIC checkout, prefer the active virtual
environment explicitly:

.. code-block:: powershell

   .\.venv\Scripts\python.exe -m datalad get models/tsa29_patchworks_model/blocks
   .\.venv\Scripts\python.exe -m datalad get models/tsa29_patchworks_model/tracks
   .\.venv\Scripts\python.exe -m datalad get output/patchworks_tsa29_validated

Run the portable contract checks first:

.. code-block:: bash

   femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun

This sequence confirms:

1. the instance config still parses and points at the expected files,
2. the rebuild spec is structurally valid, and
3. the rebuild runner resolves the declared BTC-first step order without
   mutating the instance.

Snapshot-First Versus Rebuild-Capable Use
-----------------------------------------

Two valid usage modes exist for this repository:

- **Snapshot-first use**
  Treat the checked-in outputs under ``output/patchworks_tsa29_validated/`` as
  the immediate baseline for teaching/review use.
- **Rebuild-capable use**
  Use the rebuild spec, runtime configs, and evidence workflow to confirm that
  a suitably provisioned host can reproduce the baseline through the BTC-first
  seam.

For most readers, snapshot-first use is still the right starting point. Full
rebuilds are primarily for maintainers and reviewers working on reproducibility
or pipeline changes.

Current BTC-First Rebuild Seam
------------------------------

The active supported rebuild contract is now:

.. code-block:: bash

   femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
   femic prep geospatial-preflight
   femic run --run-config config/run_profile.tsa29.yaml --run-id tsa29_stage01a
   femic tsa btc-post-tipsy --run-config config/run_profile.tsa29.yaml --tsa 29 --run-id tsa29_stage01a

Expected boundary files:

- after ``femic run``:
  - ``data/03_input-tsa29.csv``
  - ``data/tipsy_params_tsa29.xlsx``
  - optional legacy mirror: ``data/02_input-tsa29_si_plus2.dat``
- after ``femic tsa btc-post-tipsy``:
  - ``data/04_output-tsa29.csv``
  - ``data/04_error-tsa29.csv``

``femic run`` is expected to stop at the BTC boundary. The supported
continuation seam is ``femic tsa btc-post-tipsy ...``.

Authoritative Paths
-------------------

- Config: ``config/run_profile.tsa29.yaml``
- TIPSY rules: ``config/tipsy/tsa29.yaml``
- Rebuild contract: ``config/rebuild.spec.yaml``
- Allowlisted expected drift: ``config/rebuild.allowlist.yaml``
- Patchworks runtime config: ``config/patchworks.runtime.windows.yaml``
- Baseline output: ``output/patchworks_tsa29_validated/``
- Validation bundle: ``output/patchworks_tsa29_validation/``
- Canonical Matrix Builder XML + fragments pair:
  ``output/patchworks_tsa29_validated/forestmodel.xml`` plus
  ``output/patchworks_tsa29_validated/fragments/``
- Canonical standalone runtime payloads:
  ``models/tsa29_patchworks_model/blocks/``,
  ``models/tsa29_patchworks_model/tracks/``, and
  ``models/tsa29_patchworks_model/analysis/``

Next Pages
----------

- :doc:`data-and-provenance`
- :doc:`rebuild-and-qa`
- :doc:`troubleshooting`
