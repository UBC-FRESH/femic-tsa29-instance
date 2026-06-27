Advanced Student Challenges
===========================

Purpose
-------

These prompts are suitable for longer student projects. They are intentionally
framed as extensions to the alpha package, not prerequisites for using the
published teaching model.

Challenge 1: Spatialize An Aspatial Bridge
------------------------------------------

Choose one accepted aspatial bridge in the THLB chain and ask whether a better
spatial implementation is defensible.

Candidate topics include:

- existing roads and landings;
- future wildlife tree retention areas;
- cultural heritage and archaeological resources; or
- future roads.

A strong project should:

- identify the current ledger row and source note;
- explain why the current bridge exists;
- locate or reject candidate public spatial data;
- compare the proposed spatial result to the TSR benchmark;
- rebuild downstream model surfaces only if the new rule is defensible; and
- report whether the changed THLB materially affects scenario outcomes.

Challenge 2: Improve A Weak Public-Data Seam
--------------------------------------------

Some THLB steps are limited by public data coverage or by source semantics that
do not map cleanly to the TSR prose. Students can pick a lower-priority seam
and evaluate whether a better source improves the model enough to matter.

Useful outputs include:

- a source-layer inventory;
- a repeatable materialization recipe;
- a before/after THLB comparison;
- a short explanation of remaining uncertainty; and
- a recommendation to adopt, reject, or defer the improvement.

Challenge 3: Yield Sensitivity Review
-------------------------------------

Use the accepted TIPSY-vs-VDYP comparison plot family as a starting point.
Students can test whether a small number of influential analysis units would
change scenario conclusions if curve smoothing, species composition, or TIPSY
parameter assumptions were varied.

The project should keep yield-provenance questions separate from Patchworks
treatment eligibility. A stand can be managed in Patchworks while still using
the correct natural-origin or treated-origin curve lane.

Challenge 4: Scenario Constraint Design
---------------------------------------

The accepted ``test01`` evidence is a representative smoke scenario, not a
complete teaching curriculum. Students can design alternate constraints and
compare how the model behaves.

Examples:

- even-flow versus stepped harvest-flow targets;
- end-of-horizon growing-stock constraints;
- old-forest or retention proxy constraints where available;
- treatment-area limits; or
- sensitivity runs that hold harvest flow stable while changing spatial or
  yield assumptions.

Reports should state which account or product each constraint uses and whether
that account is a direct model signal or a proxy.

Challenge 5: Publication And Reproducibility Audit
--------------------------------------------------

Students interested in reproducibility can audit the release package rather
than changing model logic.

A useful audit proves:

- which files are Git-tracked and which are annex-backed;
- whether the launch-critical payloads materialize in a fresh clone;
- whether Sphinx docs build warning-clean;
- whether checksums and lineage metadata are understandable; and
- which instructions would fail on a workstation without BTC or Patchworks.

This is a valid advanced challenge because reproducibility is part of model
quality, not just a packaging detail.
