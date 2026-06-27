THLB Reconstruction
===================

Purpose
-------

This page explains how to interpret the TSA29 TSR/THLB reconstruction artifacts
that live in this repository. The short version is: use the locked strict chain
for current release accounting, use reviewed/reconstructed status reports for
method context, and treat deprecated comparison notes as audit history unless a
current page explicitly points at them.

Canonical Current Ledger
------------------------

The current release-facing THLB accounting surface is:

.. code-block:: text

   config/tsr/thlb_locked_chain_ledger.json

That ledger records a locked strict chain through
``thlb_parent_023_future_roads``. Its final locked cumulative remaining area is
``1,660,053.000 ha``, matching the TSR cumulative long-term THLB target
recorded in the ledger.

Important ledger milestones:

.. list-table::
   :header-rows: 1

   * - Row
     - Milestone
     - Locked Area
     - TSR Area
   * - 1
     - Total TSA area
     - ``4,933,664.212 ha``
     - ``4,933,635.000 ha``
   * - 5
     - Analysis forest land base
     - ``3,110,576.671 ha``
     - ``3,098,168.000 ha``
   * - 12
     - AFLB-to-LHLB stage close
     - ``2,284,357.000 ha``
     - ``2,284,357.000 ha``
   * - 23
     - Future roads / long-term THLB closeout
     - ``1,660,053.000 ha``
     - ``1,660,053.000 ha``

The ledger also records why particular rows are spatial, aspatial, or
stage-closing bridges. For example, roads and landings, WTRA, cultural
heritage, and the final future-roads closeout include explicit bridge logic.
Those are documentation-relevant modeling decisions, not hidden defects.

Strict, Reviewed, And Reconstructed Surfaces
--------------------------------------------

The TSA29 repo contains several THLB surfaces because the work progressed
through review, reconstruction, and strict-chain locking.

.. list-table::
   :header-rows: 1

   * - Surface
     - How To Use It
   * - ``config/tsr/thlb_locked_chain_ledger.json``
     - Current governing chain for locked cumulative values.
   * - ``config/tsr/thlb_netdown.status.md``
     - Reviewed recipe/status report with step prose, source links, and review
       notes.
   * - ``config/tsr/thlb_reconstructed.status.md``
     - Reconstructed-mode diagnostic report; useful for understanding runner
       behavior and blocked/executed steps.
   * - ``config/tsr/thlb_reconstruction_comparison.md``
     - Historical comparison and repair ledger. It includes an explicit
       deprecated-context warning and should not override the locked chain.

When the same parent step appears in multiple artifacts, prefer the locked
chain for current cumulative release accounting. Use the other reports to
explain method, review status, and unresolved modeling seams.

Current Interpretation Rules
----------------------------

- Do not blend unlocked or historical comparison rows into the locked
  cumulative story.
- Treat aspatial bridges as explicit modeling decisions. They should be
  documented and revisited only when a better defensible spatial contract is
  available.
- Treat strict-vs-TSR fit as the main benchmark for current strict-chain
  accounting.
- Treat strict-vs-reviewed differences as explanatory context, not automatic
  evidence that strict is wrong.
- Read ``net_removed_area_ha`` as the marginal area removed by a parent step;
  cumulative area should come from the ledger, not from ad hoc branch-local
  artifacts.

Known THLB Caveats
------------------

The current chain is good enough for the alpha teaching/research package, but
it still carries caveats that users should not hide:

- some rows are exact spatial overlays;
- some rows are documented aspatial bridges;
- some reviewed decisions were accepted because they reconcile the model to the
  TSR boundary without overpromising public spatial precision;
- the repository preserves older diagnostic comparison reports for audit
  history; and
- changing any THLB rule requires rebuilding downstream model-input,
  ForestModel XML, Matrix Builder, block, and launch surfaces before claiming a
  new Patchworks package is validated.

Maintainer Check
----------------

Before changing THLB documentation or model logic, inspect:

.. code-block:: text

   config/tsr/thlb_locked_chain_ledger.json
   config/tsr/thlb_netdown.recipe.yaml
   config/tsr/thlb_netdown.status.md
   config/tsr/thlb_reconstruction_comparison.md
   data/tsr/strict_chain/

If the question is cumulative area, answer from the locked ledger. If the
question is why a rule exists, read the recipe/status report. If the question
is whether a past repair queue is still current, verify against the ledger
before acting.
