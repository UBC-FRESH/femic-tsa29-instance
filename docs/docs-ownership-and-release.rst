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
