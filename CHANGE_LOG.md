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
- GitHub Pages was enabled for the repository with workflow deployment after
  the first PR run showed the Pages site had not been created yet.
- Validation: `sphinx-build -b html docs docs/_build/html -W` passed.

## 2026-06-27

- Started issue `#11` after finding the published yield-curve gallery served
  git-annex pointer payloads instead of real PNG images. The local maintainer
  checkout had materialized plot files, but GitHub Pages built from a plain Git
  checkout where `plots/tipsy_vdyp_tsa29-*.png` resolved to annex pointers.
- Added plain-Git copies of the accepted 54 TIPSY-vs-VDYP plot PNGs under
  `docs/_static/yield-curves/`, repointed `docs/yield-curve-comparisons.rst`
  to those docs-static assets, and kept the original annex-backed `plots/`
  evidence surface unchanged.
- Validation: `sphinx-build -b html docs docs/_build/html -W` passed.
- Deployed the D1.1 repair to GitHub Pages from `main` and verified the public yield-curve page plus representative image URL. `https://ubc-fresh.github.io/femic-tsa29-instance/_images/tipsy_vdyp_tsa29-21000.png` returned HTTP 200, `24485` bytes, and the PNG signature `89 50 4E 47`.
