Project Overview
================

Purpose
-------

This repository is the standalone FEMIC instance for TSA29, the Williams Lake
Timber Supply Area. It is built for two audiences:

- students and instructors who need a launchable forestry modeling package for
  scenario interpretation; and
- maintainers who need enough provenance to rebuild, audit, or extend the
  package without losing track of source assumptions.

The repository is not just an API example. It carries a published alpha
Patchworks package, rebuild contracts, TSR/THLB reconstruction evidence, yield
comparison figures, and publication notes. The docs explain how those pieces
fit together and where the current limits are.

Current Release Boundary
------------------------

The active published milestone is ``v1.0.0-alpha1``. Treat that tag as a
research/prototype release:

- it is suitable for inspection, classroom discussion, and exploratory
  scenario work;
- it has passed the recorded launch and representative scenario evidence in
  this repository; and
- it is not a final production timber-supply model or legal analysis record.

The most important release-facing surfaces are:

.. list-table::
   :header-rows: 1

   * - Surface
     - Role
   * - ``models/tsa29_patchworks_model/``
     - Launch-critical Patchworks package.
   * - ``output/patchworks_tsa29_validated/``
     - ForestModel XML, fragments, and editable rebuild outputs.
   * - ``data/model_input_bundle/``
     - Patchworks-facing bundle tables.
   * - ``config/rebuild.spec.yaml``
     - Instance rebuild contract.
   * - ``metadata/lineage_registry.yaml``
     - Snapshot lineage and known release issues.
   * - ``evidence/patchworks_test01_scenario_20260606.md``
     - Accepted representative interactive Patchworks scenario evidence.

What Is Complete
----------------

The current instance provides:

- a standalone DataLad/git-annex-managed TSA29 dataset;
- materializable launch-critical Patchworks payloads for the alpha package;
- a BTC-first rebuild contract;
- accepted TIPSY-vs-VDYP comparison plots for the current managed-AU surface;
- a locked strict THLB chain through the current release boundary; and
- Sphinx documentation suitable for GitHub Pages publication.

What Is Still In Progress
-------------------------

Several boundaries remain deliberately open:

- full rebuilds still need external Windows BTC and Patchworks runtimes;
- some THLB steps use accepted aspatial bridges or reviewed decisions rather
  than fully spatial public-data implementations;
- older comparison artifacts remain in the repo for audit history but are not
  all governing current validation surfaces; and
- scenario interpretation should be framed as exploratory teaching/research
  use, not operational prescription.

How To Read These Docs
----------------------

Start with :doc:`getting-started` if you want to materialize or launch the
package. Use :doc:`thlb-reconstruction` before interpreting THLB numbers. Use
:doc:`patchworks-runtime-status` and :doc:`teaching-workflows` before using the
package in a class or scenario exercise. Maintainers should read
:doc:`rebuild-and-qa` and :doc:`docs-ownership-and-release` before changing
model logic or publishing a refreshed package.
