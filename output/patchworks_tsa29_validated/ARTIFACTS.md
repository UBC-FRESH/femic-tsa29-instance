# TSA29 validated output artifact manifest

This repository now publishes the validated TSA29 output package through a
DataLad/git-annex-managed large-artifact workflow.

## Published validated rebuild surfaces

- `forestmodel.xml`
- `fragments/fragments.shp`
- `fragments/fragments.dbf`
- `fragments/fragments.shx`
- `fragments/fragments.prj`
- `fragments/fragments.cpg`

These files may be annex-backed in thin clones. Materialize them with
`datalad get output/patchworks_tsa29_validated` before assuming the validated
package is incomplete.

## Related standalone runtime surfaces

The full runnable standalone Patchworks package also depends on:

- `models/tsa29_patchworks_model/blocks/`
- `models/tsa29_patchworks_model/tracks/`
- `models/tsa29_patchworks_model/analysis/`

See `metadata/large_artifacts.sha256` for hashes of the larger published
runtime and rebuild payloads.
