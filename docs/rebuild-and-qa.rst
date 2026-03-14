Rebuild and QA
==============

Deterministic Rebuild
---------------------

.. code-block:: bash

   femic instance validate-spec --spec config/rebuild.spec.yaml
   femic instance rebuild --spec config/rebuild.spec.yaml --run-id tsa29_full

Evidence Promotion
------------------

.. code-block:: bash

   femic instance promote-evidence --output evidence/reference_rebuild_report.latest.json

Known Regression (Current Workspace)
------------------------------------

Current Linux workspace runs can fail in 01a with TSA index mismatch for
``tsa='29'``. This is tracked in runbooks and does not invalidate the snapshot
baseline included in this repository.
