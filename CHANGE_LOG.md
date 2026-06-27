# Change Log

Newest entries are appended last.

## 2026-06-27

- Started the TSA29 documentation expansion lane under
  `UBC-FRESH/femic-tsa29-instance#9`.
- Added instance-local roadmap and changelog tracking because the TSA29 repo
  did not previously carry `ROADMAP.md`, `CHANGE_LOG.md`, or a `planning/`
  directory.
- Initial audit found an existing Sphinx docs tree and GitHub Pages workflow,
  so the docs lane is an expansion and publication-hardening pass rather than
  a blank-docs bootstrap.
- Expanded the Sphinx docs with TSA29-specific project overview, THLB
  reconstruction guidance, Patchworks runtime status, teaching workflows,
  advanced student challenges, and known limitations pages.
- Aligned the GitHub Pages workflow with the current TFL 6 pattern, including
  pull-request builds, Pages configuration, Node 24 compatibility env, and
  deploy-only-on-main/workflow-dispatch behavior.
- Follow-up workflow fix: enabled `actions/configure-pages` bootstrap for the
  TSA29 repo because the first PR run showed Pages had not been enabled yet.
- Validation: `sphinx-build -b html docs docs/_build/html -W` passed.
