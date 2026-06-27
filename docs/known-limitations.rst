Known Limitations
=================

Purpose
-------

This page states the current TSA29 alpha boundaries plainly. It should be read
before using the package for teaching, scenario interpretation, or maintainer
work.

Release Status
--------------

The current package is an alpha-quality research/prototype release. It is
useful because it is launchable, documented, and tied to concrete evidence. It
is limited because several modeling, runtime, and publication assumptions
remain outside a final production guarantee.

The release is:

- a standalone TSA29 teaching/research package;
- a reproducible package boundary for maintainers;
- a recorded Patchworks launch and representative scenario evidence surface;
  and
- a base for student scenario and reproducibility exercises.

The release is not:

- a final timber-supply determination;
- a legal or consultation record;
- a complete production planning model;
- a guarantee that every workstation can run Patchworks; or
- a claim that every THLB source-data question is permanently settled.

THLB Caveats
------------

The current locked THLB ledger is the release accounting surface, but the chain
contains a mix of exact spatial steps, documented aspatial bridges, reviewed
decisions, and stage-closing logic. That mix is acceptable for the alpha
package only because it is explicit.

Users should not:

- hide aspatial bridges;
- treat deprecated comparison context as current governing truth;
- answer cumulative questions from branch-local artifacts; or
- rerun downstream model surfaces without inspecting the rebuilt outputs.

Patchworks Runtime Caveats
--------------------------

The published dataset can carry the runtime package. It cannot remove external
runtime requirements:

- Matrix Builder and interactive launch require a valid Patchworks
  installation and license seat;
- known-good Windows workstations should inherit their real license
  environment;
- modal dialogs may still block unattended automation; and
- saved scenario outputs are evidence, not canonical source input.

DataLad And Publication Caveats
-------------------------------

Large release payloads may be annex-backed. A thin clone with pointer files is
not necessarily broken; it may simply need ``datalad get``.

Before claiming a package is publicly materializable, maintainers should prove
that a fresh clone can fetch the launch-critical payloads from the configured
public remote.

Yield And Treatment Caveats
---------------------------

The accepted yield comparison surface is the refreshed ``54``-plot
TIPSY-vs-VDYP family. It is a review surface, not a claim that no future curve
sensitivity work is useful.

Patchworks ``managed`` and ``unmanaged`` describe treatment eligibility. They
must not be confused with natural-origin and treated-origin curve provenance.

Scenario Caveats
----------------

The accepted ``test01`` scenario is a sanity check. It shows that the alpha
package can produce a representative harvest-flow signal in a plausible range.
It does not prove that all possible constraints, accounts, or stakeholder
questions are settled.

Student and maintainer reports should state:

- the package version or commit used;
- the scenario target and constraints;
- whether outputs came from the published package or a rebuilt package;
- which caveats are relevant to the interpretation; and
- what evidence would be needed before making stronger claims.

Release-Readiness Checklist
---------------------------

Before a future TSA29 release is declared ready, check:

.. list-table::
   :header-rows: 1

   * - Check
     - Acceptance Signal
   * - Docs build
     - ``sphinx-build -b html docs docs/_build/html -W`` passes.
   * - Materialization
     - Fresh clone can retrieve launch-critical annex-backed payloads.
   * - THLB accounting
     - Locked ledger and docs agree on the governing cumulative story.
   * - Rebuild contract
     - ``config/rebuild.spec.yaml`` matches the intended command sequence.
   * - Patchworks package
     - ForestModel XML, fragments, tracks, blocks, and launch surfaces are
       inspected after rebuild.
   * - Scenario evidence
     - Representative evidence is current or explicitly marked historical.
   * - Issue and changelog
     - GitHub issue comments, roadmap notes, and changelog entries match the
       repo state.
