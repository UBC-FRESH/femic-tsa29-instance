# THLB Reconstruction Comparison: TSA 29 (Williams Lake)

- Generated UTC: `2026-04-12T01:46:00.381590+00:00`
- THLB recipe path: `config/tsr/thlb_netdown.recipe.yaml`
- Reviewed bridge status report: `config/tsr/thlb_netdown.status.md`
- Reconstructed audit JSON: `config/tsr/thlb_reconstructed.audit.json`

## Summary

- Strict reconstructed THLB: `903685.409 ha`
- TSR reported THLB: `1660053.000 ha`
- Strict vs TSR delta: `-756367.591 ha`

## Reviewed Bridge Context

- Reviewed bridge THLB: `1649049.232 ha`
- Reviewed vs TSR delta: `-11003.768 ha`
- Strict vs reviewed delta: `-745363.823 ha`

## Why Reviewed Was Accepted Anyway

- The reviewed lane was accepted because its cumulative THLB was close enough to the TSR benchmark for practical exploratory modeling use.
- Reviewed per-step behavior is therefore useful context, not automatic gold-standard truth for strict reconstruction.
- A parent step is a top-priority strict-lane repair when strict is materially bad against TSR, not merely because strict differs from reviewed.

## Strict-vs-TSR Fit Counts

- `not_comparable_to_tsr`: `6`
- `strict_over_tsr_major`: `2`
- `strict_over_tsr_minor`: `1`
- `strict_under_tsr_major`: `6`
- `strict_under_tsr_minor`: `3`
- `tsr_close_enough`: `6`

## Reviewed-Difference Context Counts

- `aspatial_bridge_difference`: `2`
- `blocked_or_missing_source`: `2`
- `close_match`: `1`
- `manual_or_reviewed_override`: `6`
- `not_comparable`: `4`
- `reviewed_bridge_only`: `2`
- `strict_overcut_candidate`: `4`
- `strict_undercut_candidate`: `3`

## Problem Ownership Counts

- `data_exogenous`: `3`
- `mixed`: `5`
- `model_endogenous`: `7`
- `not_applicable`: `4`
- `reviewed_bridge_choice`: `5`

## Stepwise Adjudication Queue

- 2. `thlb_parent_002_land_not_administered_by_the_province` | Land not administered by the Province | action=`defer_low_priority` | tsr-fit=`tsr_close_enough` | ownership=`model_endogenous`
- 3. `thlb_parent_003_non_forest` | Non-forest | action=`keep_reviewed_bridge` | tsr-fit=`strict_under_tsr_major` | ownership=`model_endogenous`
- 4. `thlb_parent_004_roads_and_landings` | Roads and landings | action=`defer_low_priority` | tsr-fit=`strict_under_tsr_major` | ownership=`mixed`
- 6. `thlb_parent_006_parks_protected_areas_area_base_tenures` | Parks, protected areas, area-base tenures | action=`fix_strict_logic` | tsr-fit=`strict_under_tsr_major` | ownership=`mixed`
- 7. `thlb_parent_007_old_growth_management_areas` | Old growth management areas | action=`fix_strict_logic` | tsr-fit=`strict_over_tsr_minor` | ownership=`model_endogenous`
- 8. `thlb_parent_008_wildlife_habitat_areas` | Wildlife habitat areas | action=`fix_strict_logic` | tsr-fit=`strict_over_tsr_major` | ownership=`model_endogenous`
- 9. `thlb_parent_009_critical_habitat_for_fish` | Critical habitat for fish | action=`fix_strict_logic` | tsr-fit=`strict_over_tsr_major` | ownership=`model_endogenous`
- 10. `thlb_parent_010_lakeshore_management` | Lakeshore management | action=`defer_low_priority` | tsr-fit=`tsr_close_enough` | ownership=`data_exogenous`
- 11. `thlb_parent_011_community_areas_of_special_concern` | Community areas of special concern | action=`keep_reviewed_bridge` | tsr-fit=`strict_under_tsr_major` | ownership=`model_endogenous`
- 12. `thlb_parent_012_proven_aboriginal_rights_areas` | Proven Aboriginal Rights areas | action=`improve_data_or_source` | tsr-fit=`strict_under_tsr_major` | ownership=`data_exogenous`
- 13. `thlb_parent_013_areas_considered_inoperable` | Areas considered inoperable | action=`keep_reviewed_bridge` | tsr-fit=`strict_under_tsr_minor` | ownership=`reviewed_bridge_choice`
- 14. `thlb_parent_014_sites_with_low_growing_timber_potential` | Sites with low growing timber potential | action=`keep_reviewed_bridge` | tsr-fit=`not_comparable_to_tsr` | ownership=`mixed`
- 15. `thlb_parent_015_non_merchantable_timber_profiles` | Non-merchantable timber profiles | action=`keep_reviewed_bridge` | tsr-fit=`not_comparable_to_tsr` | ownership=`model_endogenous`
- 16. `thlb_parent_016_recreation_features` | Recreation features | action=`defer_low_priority` | tsr-fit=`tsr_close_enough` | ownership=`mixed`
- 17. `thlb_parent_017_growth_and_yield_permanent_sample_plots` | Growth and yield permanent sample plots | action=`defer_low_priority` | tsr-fit=`tsr_close_enough` | ownership=`data_exogenous`
- 18. `thlb_parent_018_riparian_areas` | Riparian areas | action=`improve_data_or_source` | tsr-fit=`strict_under_tsr_minor` | ownership=`mixed`
- 19. `thlb_parent_019_buffered_trails` | Buffered trails | action=`defer_low_priority` | tsr-fit=`tsr_close_enough` | ownership=`reviewed_bridge_choice`
- 20. `thlb_parent_020_wildlife_tree_retention_areas` | Wildlife tree retention areas | action=`use_documented_aspatial_fallback` | tsr-fit=`strict_under_tsr_major` | ownership=`reviewed_bridge_choice`
- 21. `thlb_parent_021_cultural_heritage_and_archaeological_resources` | Cultural heritage and archaeological resources | action=`use_documented_aspatial_fallback` | tsr-fit=`strict_under_tsr_minor` | ownership=`reviewed_bridge_choice`
- 23. `thlb_parent_023_future_roads` | Future roads | action=`defer_low_priority` | tsr-fit=`tsr_close_enough` | ownership=`reviewed_bridge_choice`

## Top 5 Strict-vs-TSR Contributors

- `thlb_parent_003_non_forest` | Non-forest | tsr-fit=`strict_under_tsr_major` | strict-TSR marginal delta=`-1104217.299 ha`
- `thlb_parent_009_critical_habitat_for_fish` | Critical habitat for fish | tsr-fit=`strict_over_tsr_major` | strict-TSR marginal delta=`738027.058 ha`
- `thlb_parent_014_sites_with_low_growing_timber_potential` | Sites with low growing timber potential | tsr-fit=`not_comparable_to_tsr` | strict-TSR marginal delta=`-321044.000 ha`
- `thlb_parent_008_wildlife_habitat_areas` | Wildlife habitat areas | tsr-fit=`strict_over_tsr_major` | strict-TSR marginal delta=`244225.358 ha`
- `thlb_parent_006_parks_protected_areas_area_base_tenures` | Parks, protected areas, area-base tenures | tsr-fit=`strict_under_tsr_major` | strict-TSR marginal delta=`-79159.260 ha`

## Top 5 Strict-vs-Reviewed Context Differences

- `thlb_parent_003_non_forest` | Non-forest | reviewed-role=`reviewed_bridge_only` | strict-reviewed removed-area delta=`-2013430.245 ha`
- `thlb_parent_009_critical_habitat_for_fish` | Critical habitat for fish | reviewed-role=`strict_overcut_candidate` | strict-reviewed removed-area delta=`732065.235 ha`
- `thlb_parent_002_land_not_administered_by_the_province` | Land not administered by the Province | reviewed-role=`strict_overcut_candidate` | strict-reviewed removed-area delta=`491992.156 ha`
- `thlb_parent_014_sites_with_low_growing_timber_potential` | Sites with low growing timber potential | reviewed-role=`blocked_or_missing_source` | strict-reviewed removed-area delta=`-329228.613 ha`
- `thlb_parent_008_wildlife_habitat_areas` | Wildlife habitat areas | reviewed-role=`strict_overcut_candidate` | strict-reviewed removed-area delta=`265275.475 ha`

## Plain-Language Read

- This report does not change THLB logic. It explains how the strict reconstructed lane fits against the TSR benchmark and uses the reviewed lane as supporting context.
- The governing question is whether strict is close enough to TSR, not whether strict matches reviewed step-for-step.
- Reviewed differences still matter, but mainly because they explain accepted bridges, skips, calibrations, or semantic differences that the strict lane does not automatically share.

## Backbone Milestones

- `thlb_parent_001_total_tsa_area` | Total TSA area | benchmark cumulative area=`4933635.000 ha`
- `thlb_parent_005_analysis_forest_land_base` | Analysis forest land base | benchmark cumulative area=`3098168.000 ha`
- `thlb_parent_022_timber_harvesting_land_base` | Timber harvesting land base | benchmark cumulative area=`1682843.000 ha`
- `thlb_parent_024_long_term_thlb` | Long-term THLB | benchmark cumulative area=`1660053.000 ha`

## Parent-Step Comparison

### GLB -> AFLB

#### 2. Land not administered by the Province

- Parent step id: `thlb_parent_002_land_not_administered_by_the_province`
- Strict TSR fit: `tsr_close_enough`
- Reviewed difference role: `strict_overcut_candidate`
- Problem ownership: `model_endogenous`
- Difference nature: `strict_logic_overcut`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `697033.000 ha`
- TSR benchmark cumulative area: `4236602.000 ha`
- Strict reconstructed removed area: `713594.208 ha`
- Reviewed bridge removed area: `221602.052 ha`
- Strict vs TSR delta: `16561.208 ha`
- Reviewed vs TSR delta: `-475430.948 ha`
- Strict vs reviewed delta: `491992.156 ha`
- Strict vs TSR: The strict lane is close enough to the TSR benchmark here for practical exploratory use.
- Reviewed difference: The strict lane is removing materially more area than the reviewed lane here.
- Practical meaning: Strict is close enough to TSR here, so this is not a top-priority repair. The reviewed lane is lighter here than the strict lane.
- Engineering interpretation: The strict lane is using a broader ownership interpretation than the reviewed bridge, so it is cutting too much area here.
- Recommended next move: Tighten the strict ownership mapping and separate the dedicated title/treaty exclusions from the generic F_OWN ownership classes.
- Adjudication queue action: `defer_low_priority` (Defer; this is not a top-priority repair right now.)
- Actionability: Inspect strict source inputs and exact logic first; this step may be cutting more area than the reviewed lane intended.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_002_land_not_administered_by_the_province_compiled_01`, `thlb_parent_002_land_not_administered_by_the_province_compiled_02`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`
  - strict note: The TSA29 prose cites dedicated NStQ and Tsilhqot'in title exclusions that are not yet separated cleanly from the generic F_OWN ownership classes in the notebook bridge.

#### 3. Non-forest

- Parent step id: `thlb_parent_003_non_forest`
- Strict TSR fit: `strict_under_tsr_major`
- Reviewed difference role: `reviewed_bridge_only`
- Problem ownership: `model_endogenous`
- Difference nature: `reviewed_bridge_semantics`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `1105908.000 ha`
- TSR benchmark cumulative area: `3130694.000 ha`
- Strict reconstructed removed area: `1690.701 ha`
- Reviewed bridge removed area: `2015120.946 ha`
- Strict vs TSR delta: `-1104217.299 ha`
- Reviewed vs TSR delta: `909212.946 ha`
- Strict vs reviewed delta: `-2013430.245 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The reviewed lane removed material area here, but the strict lane did not produce a comparable removal.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: The strict lane is only doing a narrow direct waterbody removal here, while the reviewed lane is carrying a much broader non-forest interpretation.
- Recommended next move: Decide and document the intended strict non-forest semantics before changing code again; this is not just a missing-data problem.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Decide whether the reviewed bridge should stay an accepted difference or be translated into strict semantics.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_003_non_forest_compiled_01`, `thlb_parent_003_non_forest_compiled_02`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`
  - strict note: Riparian reserve and riparian management zone buffers are handled in the later riparian parent step, not here.
  - strict note: This subrule only performs the direct Freshwater Atlas lakes/rivers/wetlands exclusion described in the non-forest step.

#### 4. Roads and landings

- Parent step id: `thlb_parent_004_roads_and_landings`
- Strict TSR fit: `strict_under_tsr_major`
- Reviewed difference role: `close_match`
- Problem ownership: `mixed`
- Difference nature: `close_match`
- Reconstructed status: `applied_noop+unsupported`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `50434.000 ha`
- TSR benchmark cumulative area: `3080260.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `1557.111 ha`
- Strict vs TSR delta: `-50434.000 ha`
- Reviewed vs TSR delta: `-48876.889 ha`
- Strict vs reviewed delta: `-1557.111 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The strict and reviewed lanes are close enough here that this parent step does not look like a major driver of the remaining gap.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: The strict and reviewed lanes are close enough here that this step does not look like a major source of the overall THLB gap.
- Recommended next move: No immediate action; treat this as a lower-priority reference step.
- Adjudication queue action: `defer_low_priority` (Defer; this is not a top-priority repair right now.)
- Actionability: No immediate action; keep this as a reference step.
- Supporting notes:
  - strict compiled steps: `thlb_parent_004_roads_and_landings_compiled_01`, `thlb_parent_004_roads_and_landings_compiled_02`, `thlb_parent_004_roads_and_landings_compiled_03`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`
  - strict note: Temporary roads and landings remain a review item in the notebook bridge until the non-spatial deduction path is formalized.

### AFLB -> LHLB

#### 6. Parks, protected areas, area-base tenures

- Parent step id: `thlb_parent_006_parks_protected_areas_area_base_tenures`
- Strict TSR fit: `strict_under_tsr_major`
- Reviewed difference role: `strict_undercut_candidate`
- Problem ownership: `mixed`
- Difference nature: `strict_logic_undercut`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `306327.000 ha`
- TSR benchmark cumulative area: `2791841.000 ha`
- Strict reconstructed removed area: `227167.740 ha`
- Reviewed bridge removed area: `275618.199 ha`
- Strict vs TSR delta: `-79159.260 ha`
- Reviewed vs TSR delta: `-30708.801 ha`
- Strict vs reviewed delta: `-48450.459 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The strict lane is removing materially less area than the reviewed lane here.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: The strict lane is lighter than the reviewed lane here, likely because tenure and ownership semantics are still not fully aligned.
- Recommended next move: Refine the strict tenure/ownership logic first, then reassess whether any supporting data gaps remain material.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Inspect missing strict semantics, missing source layers, or reviewed bridge logic the strict lane does not yet share.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_006_parks_protected_areas_area_base_tenures_compiled_01`, `thlb_parent_006_parks_protected_areas_area_base_tenures_compiled_02`
  - reviewed ratchet state: `benchmarked`
  - strict note: TSA29 section 6.2.1 keeps woodlots in AFLB but removes them when defining the LHLB, so woodlot schedules A/B are included here.
  - strict note: This first runnable pass uses the explicit F_OWN ownership descriptions for woodlots and the small miscellaneous crown-lease class cited in TSA29 Table 7.
  - strict note: Community forest agreements and first nations woodland licences were already netted out upstream in TSA29 step 2 and are therefore intentionally excluded from this step-6 executable filter.
  - strict note: FTEN managed-licence and TANTALIS crown-tenure layers remain supporting metadata/reference surfaces, but F_OWN is the executable ownership overlay in the TSA29 bridge.

#### 7. Old growth management areas

- Parent step id: `thlb_parent_007_old_growth_management_areas`
- Strict TSR fit: `strict_over_tsr_minor`
- Reviewed difference role: `strict_overcut_candidate`
- Problem ownership: `model_endogenous`
- Difference nature: `strict_logic_overcut`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `210719.000 ha`
- TSR benchmark cumulative area: `2581122.000 ha`
- Strict reconstructed removed area: `253734.798 ha`
- Reviewed bridge removed area: `227336.336 ha`
- Strict vs TSR delta: `43015.798 ha`
- Reviewed vs TSR delta: `16617.336 ha`
- Strict vs reviewed delta: `26398.462 ha`
- Strict vs TSR: The strict lane is somewhat above the TSR benchmark here, but not yet in the worst problem tier.
- Reviewed difference: The strict lane is removing materially more area than the reviewed lane here.
- Practical meaning: Strict is off TSR here, but not in the very worst tier. The reviewed lane is lighter here than the strict lane.
- Engineering interpretation: The strict lane is likely treating OGMA area too broadly relative to the reviewed TSA29 interpretation.
- Recommended next move: Tighten the OGMA logic before looking for new data; this looks like an over-selection problem.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Inspect strict source inputs and exact logic first; this step may be cutting more area than the reviewed lane intended.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_007_old_growth_management_areas_compiled_01`
  - reviewed approval scope: `full_tsa_validation`
  - reviewed ratchet state: `approved`
  - strict note: Current notebook execution treats only permanent and rotating legal OGMAs as the direct no-harvest exclusion surface.
  - strict note: Transition OGMAs remain contextual/temporal logic and are not hard-excluded in this base-case executable mask.
  - strict note: Harvest exceptions, overlap replacement, and transition restoration timing remain later review/calibration work.

#### 8. Wildlife habitat areas

- Parent step id: `thlb_parent_008_wildlife_habitat_areas`
- Strict TSR fit: `strict_over_tsr_major`
- Reviewed difference role: `strict_overcut_candidate`
- Problem ownership: `model_endogenous`
- Difference nature: `strict_logic_overcut`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `154056.000 ha`
- TSR benchmark cumulative area: `2427066.000 ha`
- Strict reconstructed removed area: `398281.358 ha`
- Reviewed bridge removed area: `133005.883 ha`
- Strict vs TSR delta: `244225.358 ha`
- Reviewed vs TSR delta: `-21050.117 ha`
- Strict vs reviewed delta: `265275.475 ha`
- Strict vs TSR: The strict lane is materially above the TSR benchmark here, so this looks like a real strict-lane overcut seam.
- Reviewed difference: The strict lane is removing materially more area than the reviewed lane here.
- Practical meaning: Strict is badly high against TSR here, so this is a real problem to fix even before looking at the reviewed lane.
- Engineering interpretation: The strict lane is selecting far more wildlife-area land than either the reviewed lane or the TSR benchmark supports.
- Recommended next move: Audit the strict no-harvest selection logic and keep conditional/modified zones out unless the TSR clearly says otherwise.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Inspect strict source inputs and exact logic first; this step may be cutting more area than the reviewed lane intended.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_008_wildlife_habitat_areas_compiled_01`, `thlb_parent_008_wildlife_habitat_areas_compiled_02`, `thlb_parent_008_wildlife_habitat_areas_compiled_03`
  - reviewed approval scope: `full_tsa_validation`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.3.3 states that only no-harvest wildlife areas are excluded at this stage.
  - strict note: Conditional harvest zones are deferred to later forest-management assumptions and silviculture logic.
  - strict note: General Wildlife Measures with no-harvest direction are excluded here; modified/conditional zones are not.
  - strict note: Section 6.3.3 / later Section 7 wording defers conditional harvest zones instead of excluding them at this stage.

#### 9. Critical habitat for fish

- Parent step id: `thlb_parent_009_critical_habitat_for_fish`
- Strict TSR fit: `strict_over_tsr_major`
- Reviewed difference role: `strict_overcut_candidate`
- Problem ownership: `model_endogenous`
- Difference nature: `strict_logic_overcut`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `11521.000 ha`
- TSR benchmark cumulative area: `2415545.000 ha`
- Strict reconstructed removed area: `749548.058 ha`
- Reviewed bridge removed area: `17482.824 ha`
- Strict vs TSR delta: `738027.058 ha`
- Reviewed vs TSR delta: `5961.824 ha`
- Strict vs reviewed delta: `732065.235 ha`
- Strict vs TSR: The strict lane is materially above the TSR benchmark here, so this looks like a real strict-lane overcut seam.
- Reviewed difference: The strict lane is removing materially more area than the reviewed lane here.
- Practical meaning: Strict is badly high against TSR here, so this is a real problem to fix even before looking at the reviewed lane.
- Engineering interpretation: The strict lane is applying a much broader legal fish-objective surface than the reviewed lane or TSR benchmark supports.
- Recommended next move: Narrow the strict fish-habitat interpretation; this is one of the clearest strict overcut seams in the whole ladder.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Inspect strict source inputs and exact logic first; this step may be cutting more area than the reviewed lane intended.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_009_critical_habitat_for_fish_compiled_01`
  - reviewed approval scope: `full_tsa_validation`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.3.4 cites the Section 93.4 LAO establishing objectives for the CCLUP, Map 4, as the critical-fish-habitat source.
  - strict note: Notebook execution therefore uses the legal-planning fish objective polygons instead of wildlife-habitat proxy layers.
  - strict note: If the full-TSA result still runs materially high, the next refinement seam is inside the legal fish objective attributes themselves, not a return to wildlife proxy sources.

#### 10. Lakeshore management

- Parent step id: `thlb_parent_010_lakeshore_management`
- Strict TSR fit: `tsr_close_enough`
- Reviewed difference role: `manual_or_reviewed_override`
- Problem ownership: `data_exogenous`
- Difference nature: `missing_or_blocked_data`
- Reconstructed status: `unsupported`
- Reviewed status: `approved`
- TSR benchmark marginal deduction: `327.000 ha`
- TSR benchmark cumulative area: `2415218.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `not recorded`
- Strict vs TSR delta: `-327.000 ha`
- Strict vs TSR: The strict lane is close enough to the TSR benchmark here for practical exploratory use.
- Reviewed difference: The reviewed lane is carrying an accepted override, skip, calibration, or no-op choice that the strict lane does not automatically share.
- Practical meaning: Strict is close enough to TSR here, so this is not a top-priority repair. The reviewed lane is using an accepted override, calibration, skip, or no-op that the strict lane does not automatically share.
- Engineering interpretation: This step depends on a trusted Class A lake discriminator that the current public-input lane still does not have.
- Recommended next move: Keep the reviewed skip or a tiny aspatial fallback unless a trustworthy lake-class source appears.
- Adjudication queue action: `defer_low_priority` (Defer; this is not a top-priority repair right now.)
- Actionability: Review the accepted reviewed override before changing the strict lane.
- Supporting notes:
  - strict compiled steps: `thlb_parent_010_lakeshore_management_compiled_01`
  - reviewed approval scope: `full_tsa_trivial_benchmark_skip`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.3.5 is a very small benchmark step and only applies to Class A lakes overlapping preservation VQO.
  - strict note: The currently adopted public layers do not yet expose a trusted Class A lake discriminator for TSA29.
  - strict note: Do not substitute the whole scenic-PR legal surface; it materially overcuts.
  - strict note: Class B-E lakes are deferred to Section 7.2.6 assumptions logic, not excluded here.

#### 11. Community areas of special concern

- Parent step id: `thlb_parent_011_community_areas_of_special_concern`
- Strict TSR fit: `strict_under_tsr_major`
- Reviewed difference role: `reviewed_bridge_only`
- Problem ownership: `model_endogenous`
- Difference nature: `reviewed_bridge_semantics`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `62460.000 ha`
- TSR benchmark cumulative area: `2352758.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `69545.637 ha`
- Strict vs TSR delta: `-62460.000 ha`
- Reviewed vs TSR delta: `7085.637 ha`
- Strict vs reviewed delta: `-69545.637 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The reviewed lane removed material area here, but the strict lane did not produce a comparable removal.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: The strict literal source choice is not reproducing the reviewed meaning of this step at all.
- Recommended next move: Fix the strict semantics/source interpretation instead of treating this as a pure missing-data problem.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Decide whether the reviewed bridge should stay an accepted difference or be translated into strict semantics.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_011_community_areas_of_special_concern_compiled_01`
  - reviewed approval scope: `full_tsa_validation`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.3.7 points to LUO / CCLUP Map 5 boundaries, so notebook execution uses the legal CCLUP planning polygons instead of broad designated-area overlays.

#### 12. Proven Aboriginal Rights areas

- Parent step id: `thlb_parent_012_proven_aboriginal_rights_areas`
- Strict TSR fit: `strict_under_tsr_major`
- Reviewed difference role: `manual_or_reviewed_override`
- Problem ownership: `data_exogenous`
- Difference nature: `missing_or_blocked_data`
- Reconstructed status: `unsupported`
- Reviewed status: `approved`
- TSR benchmark marginal deduction: `68401.000 ha`
- TSR benchmark cumulative area: `2284357.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `not recorded`
- Strict vs TSR delta: `-68401.000 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The reviewed lane is carrying an accepted override, skip, calibration, or no-op choice that the strict lane does not automatically share.
- Practical meaning: Strict is badly low against TSR here, but the main reason looks exogenous: the needed data or source contract is missing.
- Engineering interpretation: The strict lane still lacks a trustworthy public boundary source for this step.
- Recommended next move: Keep this as a reviewed skip or documented fallback until a real source is available.
- Adjudication queue action: `improve_data_or_source` (Improve or replace the missing/weak source data.)
- Actionability: Review the accepted reviewed override before changing the strict lane.
- Supporting notes:
  - strict compiled steps: `thlb_parent_012_proven_aboriginal_rights_areas_compiled_01`
  - reviewed approval scope: `full_tsa_public_data_unavailable_skip`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.4.1 defines the Proven Aboriginal Rights area conceptually but does not cite a clean public vector source in the data-package text.
  - strict note: Current public lead is the PIP Consultation Areas public map service; treat this step as review/manual until a trustworthy boundary source or override is adopted.

### LHLB -> THLB

#### 13. Areas considered inoperable

- Parent step id: `thlb_parent_013_areas_considered_inoperable`
- Strict TSR fit: `strict_under_tsr_minor`
- Reviewed difference role: `manual_or_reviewed_override`
- Problem ownership: `reviewed_bridge_choice`
- Difference nature: `accepted_reviewed_override`
- Reconstructed status: `applied_noop`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `33533.000 ha`
- TSR benchmark cumulative area: `2250824.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `43628.139 ha`
- Strict vs TSR delta: `-33533.000 ha`
- Reviewed vs TSR delta: `10095.139 ha`
- Strict vs reviewed delta: `-43628.139 ha`
- Strict vs TSR: The strict lane is somewhat below the TSR benchmark here, but not yet in the worst problem tier.
- Reviewed difference: The reviewed lane is carrying an accepted override, skip, calibration, or no-op choice that the strict lane does not automatically share.
- Practical meaning: Strict is off TSR here, but not in the very worst tier. The reviewed lane is using an accepted override, calibration, skip, or no-op that the strict lane does not automatically share.
- Engineering interpretation: The reviewed lane uses accepted derived-attribute and calibrated bridge logic here that the strict checkpoint1 lane does not share.
- Recommended next move: Keep the accepted reviewed bridge unless you explicitly decide to port its late-stage derived attributes into strict semantics.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Review the accepted reviewed override before changing the strict lane.
- Supporting notes:
  - strict compiled steps: `thlb_parent_013_areas_considered_inoperable_compiled_01`, `thlb_parent_013_areas_considered_inoperable_compiled_02`
  - reviewed approval scope: `full_tsa_user_directed_acceptance`
  - reviewed ratchet state: `approved`
  - strict note: The terrain-stability branch remains the current public-data executable proxy for the TSR's Unstable (U) / Terrain Class 5 clause.
  - strict note: The v1 terrain filter uses terrain-stability classes U (Unstable) and V (Terrain Class 5 proxy) as the current executable subset.
  - strict note: TSA29 section 6.4.3 splits steep-slope exclusions east and west of Highway 97.
  - strict note: Checkpoint execution expects `femic_slope_pct_median`, `femic_hwy97_side`, and `femic_step13_steep_slope_flag` to be precompiled onto the curve-ready checkpoint.

#### 14. Sites with low growing timber potential

- Parent step id: `thlb_parent_014_sites_with_low_growing_timber_potential`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `mixed`
- Difference nature: `missing_late_stage_semantics`
- Reconstructed status: `blocked_missing_source`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `321044.000 ha`
- TSR benchmark cumulative area: `1929780.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `329228.613 ha`
- Strict vs TSR delta: `-321044.000 ha`
- Reviewed vs TSR delta: `8184.613 ha`
- Strict vs reviewed delta: `-329228.613 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane is blocked because this is late-stage curve-ready logic, not because the universe of land is inherently unknowable.
- Recommended next move: Bridge or port the late-stage curve logic explicitly; do not mislabel this as a simple raw-data problem.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict compiled steps: `thlb_parent_014_sites_with_low_growing_timber_potential_compiled_01`, `thlb_parent_014_sites_with_low_growing_timber_potential_compiled_02`
  - reviewed approval scope: `full_tsa_user_directed_calibrated_acceptance`
  - reviewed ratchet state: `approved`
  - strict note: Step 14 runs late in the pipeline on the curve-ready checkpoint rather than on checkpoint1.
  - strict note: Notebook execution uses the current assigned bundle curves and evaluates volume at age 160, matching the TSR wording for low-productivity stands.
  - strict note: This branch reuses the accepted step-13 steep-slope flag and applies the calibrated non-steep 67.1 m3/ha bridge threshold only where `femic_step13_steep_slope_flag == False`.
  - strict note: The threshold is calibrated to approximate the TSR step-14 benchmark with the current public-input curve family rather than claiming exact parity with the Chief Forester's yield tables.
  - strict note: TSA29 section 6.4.4 raises the threshold to 250 m3/ha on steep slopes.
  - strict note: This branch reuses the accepted step-13 steep-slope flag and applies the 250 m3/ha threshold only where `femic_step13_steep_slope_flag == True`.
  - strict note: Together with the calibrated non-steep 67.1 m3/ha branch, this keeps the step-14 partition mutually exclusive and avoids applying the lower threshold to steep stands.

#### 15. Non-merchantable timber profiles

- Parent step id: `thlb_parent_015_non_merchantable_timber_profiles`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `model_endogenous`
- Difference nature: `missing_late_stage_semantics`
- Reconstructed status: `blocked_missing_source`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `49052.000 ha`
- TSR benchmark cumulative area: `1880728.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `103629.462 ha`
- Strict vs TSR delta: `-49052.000 ha`
- Reviewed vs TSR delta: `54577.462 ha`
- Strict vs reviewed delta: `-103629.462 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane is missing the later broadleaf-leading yield logic that the reviewed lane applies here.
- Recommended next move: Port the reviewed late-stage logic or keep this as an explicit bridge/fallback step.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict compiled steps: `thlb_parent_015_non_merchantable_timber_profiles_compiled_01`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.4.5 excludes broadleaf-leading stands from THLB.
  - strict note: Notebook execution uses the leading VRI species code on the late-stage curve-ready checkpoint surface.
  - strict note: The deciduous component of conifer-leading stands is explicitly deferred to the later broadleaf volume-exclusion assumption.

#### 16. Recreation features

- Parent step id: `thlb_parent_016_recreation_features`
- Strict TSR fit: `tsr_close_enough`
- Reviewed difference role: `manual_or_reviewed_override`
- Problem ownership: `mixed`
- Difference nature: `partial_strict_logic`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `9598.000 ha`
- TSR benchmark cumulative area: `1871130.000 ha`
- Strict reconstructed removed area: `4018.595 ha`
- Reviewed bridge removed area: `7562.895 ha`
- Strict vs TSR delta: `-5579.405 ha`
- Reviewed vs TSR delta: `-2035.105 ha`
- Strict vs reviewed delta: `-3544.300 ha`
- Strict vs TSR: The strict lane is close enough to the TSR benchmark here for practical exploratory use.
- Reviewed difference: The reviewed lane is carrying an accepted override, skip, calibration, or no-op choice that the strict lane does not automatically share.
- Practical meaning: Strict is close enough to TSR here, so this is not a top-priority repair. The reviewed lane is using an accepted override, calibration, skip, or no-op that the strict lane does not automatically share.
- Engineering interpretation: The strict lane only captures part of the reviewed recreation exclusion logic.
- Recommended next move: Low-priority cleanup: improve strict logic if this step later matters to the remaining gap.
- Adjudication queue action: `defer_low_priority` (Defer; this is not a top-priority repair right now.)
- Actionability: Review the accepted reviewed override before changing the strict lane.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_016_recreation_features_compiled_01`
  - reviewed approval scope: `full_tsa_user_directed_acceptance`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.4.6 excludes identified recreation areas and features from THLB.
  - strict note: Notebook execution currently auto-runs the active FTEN recreation polygon subset only.
  - strict note: Recreation trails and FSP consultation/procedure language remain out of scope for this first runnable bridge pass.

#### 17. Growth and yield permanent sample plots

- Parent step id: `thlb_parent_017_growth_and_yield_permanent_sample_plots`
- Strict TSR fit: `tsr_close_enough`
- Reviewed difference role: `strict_undercut_candidate`
- Problem ownership: `data_exogenous`
- Difference nature: `weak_public_coverage`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `3577.000 ha`
- TSR benchmark cumulative area: `1867553.000 ha`
- Strict reconstructed removed area: `240.685 ha`
- Reviewed bridge removed area: `1261.158 ha`
- Strict vs TSR delta: `-3336.315 ha`
- Reviewed vs TSR delta: `-2315.842 ha`
- Strict vs reviewed delta: `-1020.473 ha`
- Strict vs TSR: The strict lane is close enough to the TSR benchmark here for practical exploratory use.
- Reviewed difference: The strict lane is removing materially less area than the reviewed lane here.
- Practical meaning: Strict is close enough to TSR here, so this is not a top-priority repair. The reviewed lane is heavier here than the strict lane.
- Engineering interpretation: The strict lane undercuts here, but the public PSP geometry signal is weak and the absolute area is small.
- Recommended next move: Treat this as a lower-priority data-coverage seam unless a better PSP source becomes available.
- Adjudication queue action: `defer_low_priority` (Defer; this is not a top-priority repair right now.)
- Actionability: Inspect missing strict semantics, missing source layers, or reviewed bridge logic the strict lane does not yet share.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_017_growth_and_yield_permanent_sample_plots_compiled_01`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`

#### 18. Riparian areas

- Parent step id: `thlb_parent_018_riparian_areas`
- Strict TSR fit: `strict_under_tsr_minor`
- Reviewed difference role: `strict_undercut_candidate`
- Problem ownership: `mixed`
- Difference nature: `missing_or_blocked_data`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `54833.000 ha`
- TSR benchmark cumulative area: `1812720.000 ha`
- Strict reconstructed removed area: `15975.371 ha`
- Reviewed bridge removed area: `72204.542 ha`
- Strict vs TSR delta: `-38857.629 ha`
- Reviewed vs TSR delta: `17371.542 ha`
- Strict vs reviewed delta: `-56229.170 ha`
- Strict vs TSR: The strict lane is somewhat below the TSR benchmark here, but not yet in the worst problem tier.
- Reviewed difference: The strict lane is removing materially less area than the reviewed lane here.
- Practical meaning: Strict is off TSR here, but not in the very worst tier. The reviewed lane is heavier here than the strict lane.
- Engineering interpretation: The strict lane is still missing some of the lake-class and special-case riparian inputs that the reviewed bridge used.
- Recommended next move: Improve source coverage first, then revisit the strict riparian logic if the gap remains large.
- Adjudication queue action: `improve_data_or_source` (Improve or replace the missing/weak source data.)
- Actionability: Inspect missing strict semantics, missing source layers, or reviewed bridge logic the strict lane does not yet share.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_018_riparian_areas_compiled_stream_s1`, `thlb_parent_018_riparian_areas_compiled_stream_s2`, `thlb_parent_018_riparian_areas_compiled_stream_s3`, `thlb_parent_018_riparian_areas_compiled_stream_s4`, `thlb_parent_018_riparian_areas_compiled_stream_s5`, `thlb_parent_018_riparian_areas_compiled_stream_s6`, `thlb_parent_018_riparian_areas_compiled_wetland_w1`, `thlb_parent_018_riparian_areas_compiled_wetland_w2`, `thlb_parent_018_riparian_areas_compiled_wetland_w3`, `thlb_parent_018_riparian_areas_compiled_wetland_w4`, `thlb_parent_018_riparian_areas_compiled_wetland_w5`, `thlb_parent_018_riparian_areas_compiled_lakes_review`, `thlb_parent_018_riparian_areas_compiled_s4_special_review`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`
  - strict note: Step 3 already removed the direct non-forest waterbody area; this later THLB step models the additional riparian buffer.
  - strict note: The Table 15 riparian width already folds RRZ plus retained RMZ share into an equivalent full-exclusion width.
  - strict note: Step 3 already removed the direct wetland polygon area; this later THLB step models the additional riparian buffer.
  - strict note: Table 15 includes lake classes L1-B, L2, and L3/L4, but the current TSA29 instance does not yet have a trustworthy lake-class artifact wired into the notebook bridge.
  - strict note: TSA29 section 6.4.2 increases the S4 riparian area width in the Niut SRDZ and South Chilcotin SRDZ to protect dolly varden trout habitat. This first runnable pass leaves that special-case refinement as reviewed/manual logic.

#### 19. Buffered trails

- Parent step id: `thlb_parent_019_buffered_trails`
- Strict TSR fit: `tsr_close_enough`
- Reviewed difference role: `manual_or_reviewed_override`
- Problem ownership: `reviewed_bridge_choice`
- Difference nature: `accepted_reviewed_override`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `8039.000 ha`
- TSR benchmark cumulative area: `1804681.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `10244.748 ha`
- Strict vs TSR delta: `-8039.000 ha`
- Reviewed vs TSR delta: `2205.748 ha`
- Strict vs reviewed delta: `-10244.748 ha`
- Strict vs TSR: The strict lane is close enough to the TSR benchmark here for practical exploratory use.
- Reviewed difference: The reviewed lane is carrying an accepted override, skip, calibration, or no-op choice that the strict lane does not automatically share.
- Practical meaning: Strict is close enough to TSR here, so this is not a top-priority repair. The reviewed lane is using an accepted override, calibration, skip, or no-op that the strict lane does not automatically share.
- Engineering interpretation: The reviewed lane uses an accepted equivalent-corridor bridge here, while the strict lane currently does not reproduce that bridge.
- Recommended next move: Keep the accepted bridge unless you explicitly decide to formalize the same equivalent-corridor logic in strict mode.
- Adjudication queue action: `defer_low_priority` (Defer; this is not a top-priority repair right now.)
- Actionability: Review the accepted reviewed override before changing the strict lane.
- Supporting notes:
  - strict spatial modes: `fragment_overlay`
  - strict compiled steps: `thlb_parent_019_buffered_trails_compiled_01`
  - reviewed approval scope: `full_tsa_user_directed_acceptance`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.3.6 says at least 85% of the area within the 100-metre trail corridor will not be available for harvest.
  - strict note: Notebook execution models that rule by shrinking the legal 100-metre buffered-trail polygons inward by 7.5 metres on each side, yielding an 85-metre equivalent full-exclusion corridor.

#### 20. Wildlife tree retention areas

- Parent step id: `thlb_parent_020_wildlife_tree_retention_areas`
- Strict TSR fit: `strict_under_tsr_major`
- Reviewed difference role: `aspatial_bridge_difference`
- Problem ownership: `reviewed_bridge_choice`
- Difference nature: `accepted_aspatial_bridge`
- Reconstructed status: `aspatial_fallback`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `94417.000 ha`
- TSR benchmark cumulative area: `1710264.000 ha`
- Strict reconstructed removed area: `17754.716 ha`
- Reviewed bridge removed area: `33627.943 ha`
- Strict vs TSR delta: `-76662.284 ha`
- Reviewed vs TSR delta: `-60789.057 ha`
- Strict vs reviewed delta: `-15873.226 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The strict lane used a documented aspatial fallback here instead of exact spatial reproduction.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: This step is intentionally being modeled as an aspatial future-WTRA bridge rather than an exact mapped exclusion.
- Recommended next move: Keep the documented aspatial fallback unless a better exact contract is deliberately adopted later.
- Adjudication queue action: `use_documented_aspatial_fallback` (Keep or formalize a documented aspatial fallback.)
- Actionability: Decide whether this documented aspatial fallback should remain a bridge or be replaced by exact spatial logic later.
- Supporting notes:
  - strict spatial modes: `aspatial_fallback`
  - strict compiled steps: `thlb_parent_020_wildlife_tree_retention_areas_compiled_01`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.4.8 says existing mapped WTRA remain in THLB and are deferred from harvest for 80 years.
  - strict note: Notebook execution models only the future WTRA requirement here as an aspatial THLB reduction factor.
  - strict note: The deduction magnitude is anchored to the TSR benchmark area and scaled to the current smoke subset.

#### 21. Cultural heritage and archaeological resources

- Parent step id: `thlb_parent_021_cultural_heritage_and_archaeological_resources`
- Strict TSR fit: `strict_under_tsr_minor`
- Reviewed difference role: `aspatial_bridge_difference`
- Problem ownership: `reviewed_bridge_choice`
- Difference nature: `accepted_aspatial_bridge`
- Reconstructed status: `aspatial_fallback`
- Reviewed status: `applied`
- TSR benchmark marginal deduction: `34205.000 ha`
- TSR benchmark cumulative area: `1676059.000 ha`
- Strict reconstructed removed area: `6309.011 ha`
- Reviewed bridge removed area: `11512.712 ha`
- Strict vs TSR delta: `-27895.989 ha`
- Reviewed vs TSR delta: `-22692.288 ha`
- Strict vs reviewed delta: `-5203.701 ha`
- Strict vs TSR: The strict lane is somewhat below the TSR benchmark here, but not yet in the worst problem tier.
- Reviewed difference: The strict lane used a documented aspatial fallback here instead of exact spatial reproduction.
- Practical meaning: Strict is off TSR here, but not in the very worst tier. The reviewed difference here is mostly about an explicit aspatial bridge choice rather than exact spatial truth.
- Engineering interpretation: This step is intentionally being modeled as an aspatial THLB bridge rather than a single exact spatial layer.
- Recommended next move: Keep the documented aspatial fallback unless a defensible exact spatial contract is introduced later.
- Adjudication queue action: `use_documented_aspatial_fallback` (Keep or formalize a documented aspatial fallback.)
- Actionability: Decide whether this documented aspatial fallback should remain a bridge or be replaced by exact spatial logic later.
- Supporting notes:
  - strict spatial modes: `aspatial_fallback`
  - strict compiled steps: `thlb_parent_021_cultural_heritage_and_archaeological_resources_compiled_01`
  - reviewed approval scope: `full_tsa_user_directed_acceptance`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.4.9 models this as an aspatial THLB reduction rather than a single public spatial layer.
  - strict note: The deduction is anchored to the TSR benchmark area and informed by TNG plus FSP practice (Tolko #780, West Fraser #755, BCTS #828).
  - strict note: Do not infer road or other generic spatial layers from the permit/FSP discussion in this subsection.

#### 23. Future roads

- Parent step id: `thlb_parent_023_future_roads`
- Strict TSR fit: `tsr_close_enough`
- Reviewed difference role: `manual_or_reviewed_override`
- Problem ownership: `reviewed_bridge_choice`
- Difference nature: `accepted_skip_or_noop`
- Reconstructed status: `applied_noop`
- Reviewed status: `applied_noop`
- TSR benchmark marginal deduction: `22754.000 ha`
- Strict reconstructed removed area: `0.000 ha`
- Reviewed bridge removed area: `0.000 ha`
- Strict vs TSR delta: `-22754.000 ha`
- Reviewed vs TSR delta: `-22754.000 ha`
- Strict vs reviewed delta: `0.000 ha`
- Strict vs TSR: The strict lane is close enough to the TSR benchmark here for practical exploratory use.
- Reviewed difference: The reviewed lane is carrying an accepted override, skip, calibration, or no-op choice that the strict lane does not automatically share.
- Practical meaning: Strict is close enough to TSR here, so this is not a top-priority repair. The reviewed lane is using an accepted override, calibration, skip, or no-op that the strict lane does not automatically share.
- Engineering interpretation: The accepted TSA29 closeout keeps this as an explicit 0 ha no-op tail step after step 21.
- Recommended next move: Leave it alone unless you intentionally reopen the reviewed closeout decision.
- Adjudication queue action: `defer_low_priority` (Defer; this is not a top-priority repair right now.)
- Actionability: Review the accepted reviewed override before changing the strict lane.
- Supporting notes:
  - strict compiled steps: `thlb_parent_023_future_roads_compiled_01`
  - reviewed approval scope: `full_tsa_user_directed_skip`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.2.3 says future roads are estimated from current performance and RESULTS data rather than a mapped future-road layer.
  - strict note: User-directed TSA29 closeout now keeps this as a tail-end reference step after step 21 but applies 0 ha of executable deduction.
  - strict note: Do not reuse the existing present-day roads spatial overlay for this parent step.
  - strict note: Same-instrument reruns showed the accepted lane was already slightly below the final TSR cumulative THLB benchmark after step 21, so a positive deduction here would only worsen reconciliation.
