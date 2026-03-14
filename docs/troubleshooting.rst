Troubleshooting
===============

Case Validation Fails
---------------------

- Re-check ``config/run_profile.tsa29.yaml`` and ``config/tipsy/tsa29.yaml``.
- Confirm shared base datasets are available in your configured data root.

Patchworks Preflight Fails
--------------------------

- Confirm ``config/patchworks.runtime.windows.yaml`` matches your local
  Windows Patchworks installation paths.
- Run:

  .. code-block:: bash

     femic patchworks preflight --config config/patchworks.runtime.windows.yaml

Rebuild Diffs Unexpectedly
--------------------------

- Inspect latest report in ``vdyp_io/logs/``.
- Compare against ``config/rebuild.allowlist.yaml`` and only allowlist
  intentional structural changes.
