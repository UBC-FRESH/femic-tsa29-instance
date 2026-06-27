Patchworks Runtime Status
=========================

Purpose
-------

This page summarizes what the TSA29 Patchworks package currently supports,
which artifacts are launch-critical, and how to interpret the recorded alpha
evidence.

Published Runtime Package
-------------------------

The launch-critical package lives under:

.. code-block:: text

   models/tsa29_patchworks_model/

The most important subdirectories are:

.. list-table::
   :header-rows: 1

   * - Path
     - Role
   * - ``analysis/``
     - Patchworks launch and scenario surfaces, including the base launch
       wiring.
   * - ``blocks/``
     - Block shapefile and shipped topology helper used by the runtime model.
   * - ``tracks/``
     - Matrix Builder outputs, including features, products, treatments,
       accounts, protoaccounts, and curves.

The editable rebuild surface lives under:

.. code-block:: text

   output/patchworks_tsa29_validated/

That directory contains the ForestModel XML and fragments package used for
Matrix Builder and review. The runtime package and editable rebuild surface are
both part of the release story.

Launch Evidence
---------------

The accepted representative scenario evidence is:

.. code-block:: text

   evidence/patchworks_test01_scenario_20260606.md

That evidence records an interactive ``test01`` scenario using an even-flow
maximum harvest volume with an end-of-horizon NDY flow constraint. The recorded
managed clearcut harvest volume ranged from about ``1.38`` to ``1.61`` million
``m3/year``, with a mean of about ``1.52`` million ``m3/year``.

The evidence note compares that result to the Williams Lake TSA public
discussion mid-term values cited in the repository note. This is a practical
sanity signal that the alpha package is not obviously mis-scaled. It is not a
claim that the package is a final production model.

Minimal Materialization
-----------------------

For a thin DataLad clone, materialize at least:

.. code-block:: bash

   datalad get models/tsa29_patchworks_model/blocks
   datalad get models/tsa29_patchworks_model/tracks
   datalad get models/tsa29_patchworks_model/analysis
   datalad get output/patchworks_tsa29_validated

If a collaborator sees pointer files or missing shapefile sidecars, the first
fix is materialization, not a rebuild.

Patchworks Host Boundary
------------------------

The repository can publish the model package, but it cannot publish a licensed
Patchworks workstation. Interactive launch and Matrix Builder work still
require a Windows host with Patchworks installed and a valid license seat.

Known-good institutional workstations should inherit their real
``SPS_LICENSE_SERVER`` environment. Do not replace a working host-level
license value with placeholder config just to make a file look portable.

What To Inspect After Rebuilds
------------------------------

Do not treat "Matrix Builder succeeded" as the only validation signal. After a
Patchworks-facing rebuild, inspect the rebuilt outputs most likely to reveal a
regression:

- ``output/patchworks_tsa29_validated/forestmodel.xml``;
- ``output/patchworks_tsa29_validated/fragments/``;
- ``models/tsa29_patchworks_model/tracks/features.csv``;
- ``models/tsa29_patchworks_model/tracks/protoaccounts.csv``;
- ``models/tsa29_patchworks_model/tracks/accounts.csv``;
- ``models/tsa29_patchworks_model/blocks/blocks.shp`` and sidecars; and
- at least one representative launch or scenario evidence surface.

Teaching Boundary
-----------------

For teaching, students can treat the published package as the starting
scenario environment. Maintainers should treat it as a generated package whose
source truth comes from configs, THLB ledgers, evidence reports, and rebuild
commands.
