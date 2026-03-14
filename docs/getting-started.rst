Getting Started
===============

Purpose
-------

This repository provides an immediate TSA29 baseline for research use while
retaining a reproducible rebuild pathway.

Prerequisites
-------------

- Python environment with ``femic`` installed.
- Access to shared base datasets (see external data notes in README).

Quickstart
----------

.. code-block:: bash

   femic prep validate-case --run-config config/run_profile.tsa29.yaml --tipsy-config-dir config/tipsy
   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --dry-run --run-id tsa29_dryrun

Authoritative Paths
-------------------

- Config: ``config/run_profile.tsa29.yaml``
- Rebuild contract: ``config/rebuild.spec.yaml``
- Baseline output: ``output/patchworks_tsa29_validated/``
