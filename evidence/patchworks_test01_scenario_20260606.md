# TSA29 Patchworks `test01` scenario evidence (2026-06-06)

This note records the accepted interactive smoke evidence for the refreshed
TSA29 Patchworks package after the Phase 69 rebuild on the locked row-23 THLB
surface and accepted yield inputs.

## Scenario

- local saved scenario directory:
  `models/tsa29_patchworks_model/analysis/scenarios/test01`
- scenario shape:
  even-flow maximum harvest volume with an end-of-horizon NDY flow constraint
  on total growing stock

## Direct TSA29 result

Read from:

- `models/tsa29_patchworks_model/analysis/scenarios/test01/targets/product_HarvestedVolume_managed_Total_CC.csv`

Observed `CURRENT` values across periods 1-30:

- minimum periodic harvested volume:
  `13,835,537 m3 per 10-year period`
- maximum periodic harvested volume:
  `16,128,241 m3 per 10-year period`
- mean periodic harvested volume:
  `15,234,245.6 m3 per 10-year period`

Annualized interpretation:

- minimum:
  `1,383,553.7 m3/year`
- maximum:
  `1,612,824.1 m3/year`
- mean:
  `1,523,424.6 m3/year`

This lands the rebuilt version-0 TSA29 model in the expected mid-term band of
roughly `1.4` to `1.6 million m3/year`.

## Published comparison point

Reference:

- `reference/williams_lake_tsa_public_discussion.pdf`

Relevant published values:

- Figure 4 base-case harvest forecast mid-term level:
  `1,420,500 m3/year`
- Figure 6 alternative harvest forecast mid-term level:
  `1,504,998 m3/year`

## Interpretation

The rebuilt TSA29 Patchworks package now produces a representative interactive
smoke scenario whose even-flow managed harvest level is close to the published
post-2022 mid-term discussion range in the 2014 Williams Lake TSA public
discussion paper. This is acceptable version-0 evidence that the rebuilt THLB,
yield, export, Matrix Builder, and launch surfaces are operating in a
defensible range rather than obviously mis-scaled.
