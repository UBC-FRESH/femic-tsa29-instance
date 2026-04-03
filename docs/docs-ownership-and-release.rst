Docs Ownership and Release
==========================

Ownership
---------

- Primary maintainers: FEMIC core maintainers and TSA29 case operators.
- This standalone instance repo owns the canonical TSA29 student-facing and
  instance-facing documentation.
- The parent FEMIC repo should keep only pointer/context pages for TSA29, not a
  second parallel narrative copy of these docs.

Release Policy
--------------

- Publish snapshot-style tags (starting at ``v0.1.0``).
- Each release should include updated lineage metadata and evidence summary.
- Publish bulky standalone-instance payloads through the repo's DataLad /
  git-annex workflow rather than forcing them through plain Git history.

DataLad Publication Policy
--------------------------

- Keep docs, config, small canonical text artifacts, and lightweight launch
  wrappers in Git.
- Annex bulky instance payloads and oversized rebuild/runtime artifacts.
- Do **not** publish transient local runtime spill such as saved-stage dumps,
  scratch logs, or temporary launcher traces.

Maintainer Publish Sequence
---------------------------

When publishing a refreshed TSA29 standalone package:

1. confirm the intended files are classified correctly by ``.gitattributes``
   and ``.gitignore``
2. ``datalad save`` the intended Git-tracked and annex-tracked changes
3. configure/verify the intended special remote (for example ``arbutus-s3``)
4. push dataset metadata and annex content to the publication remotes
5. cold-clone or re-materialize the instance and verify the launch-critical
   runtime payloads can be retrieved without tribal knowledge
6. record the canonical collaborator bootstrap remote name in the published
   release notes / quickstart docs

When To Update These Docs
-------------------------

Update this docs set whenever any of the following change materially:

- published snapshot outputs under ``output/patchworks_tsa29_validated/``
- rebuild/evidence contract files under ``config/`` or ``evidence/``
- known limitations or acceptance status
- figure appendix or land-base interpretation artifacts

Release Checklist
-----------------

Before tagging a new TSA29 snapshot release:

1. refresh lineage/checksum metadata
2. confirm rebuild/evidence files describe the current published state
3. rebuild the Sphinx docs successfully
4. update any sections that still describe superseded known issues or baseline
   artifacts
5. verify the DataLad materialization instructions still match the published
   remote/bootstrap workflow
