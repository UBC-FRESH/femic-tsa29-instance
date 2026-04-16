# THLB Reconstruction Comparison: TSA 29 (Williams Lake)

- Generated UTC: `2026-04-16T16:59:49.050540+00:00`
- THLB recipe path: `config/tsr/thlb_netdown.recipe.yaml`
- Reviewed bridge status report: `config/tsr/thlb_netdown.status.md`
- Reconstructed audit JSON: `config/tsr/thlb_reconstructed.audit.json`
- Reconstructed baseline signal (context only): `checkpoint1_aflb_initialization`

## Summary

- Locked strict chain latest row: `24` (`thlb_parent_024_long_term_thlb`)
- Locked strict chain THLB: `1648497.622 ha`
- TSR cumulative benchmark at the latest locked checkpoint: `1660053.000 ha`
- Generic reconstructed audit final area (secondary context only): `2247992.122 ha`
- Strict vs TSR delta: `-11555.378 ha`
- Locked chain cumulative delta: `-11555.378 ha`

## Methodology

- Locked rows are the governing ledger.
- Locked stepwise and cumulative values come from `thlb_locked_chain_ledger.json` when that ledger exists.
- Unlocked rows are stale/unrefreshed context only and must not be blended into the locked cumulative story.
- Generic reconstructed audit values are supporting context only; they do not override the locked chain summary.

## Reviewed Bridge Context

- Reviewed bridge THLB: `1649049.232 ha`
- Reviewed vs TSR delta: `-11003.768 ha`
- Strict vs reviewed delta: `-551.610 ha`

## Why Reviewed Was Accepted Anyway

- The reviewed lane was accepted because its cumulative THLB was close enough to the TSR benchmark for practical exploratory modeling use.
- Reviewed per-step behavior is therefore useful context, not automatic gold-standard truth for strict reconstruction.
- A parent step is a top-priority strict-lane repair when strict is materially bad against TSR, not merely because strict differs from reviewed.
- The current strict lane now starts from raw checkpoint1 geometry rather than an AFLB-style prefiltered subset, so early `GLB -> AFLB` rows are intended to be read as real stepwise deductions.

## Strict-vs-TSR Fit Counts

- `not_comparable_to_tsr`: `16`
- `strict_under_tsr_major`: `5`
- `strict_under_tsr_minor`: `1`
- `tsr_close_enough`: `2`

## Reviewed-Difference Context Counts

- `aspatial_bridge_difference`: `3`
- `blocked_or_missing_source`: `12`
- `manual_or_reviewed_override`: `3`
- `not_comparable`: `4`
- `reviewed_bridge_only`: `2`

## Problem Ownership Counts

- `data_exogenous`: `3`
- `mixed`: `5`
- `model_endogenous`: `7`
- `not_applicable`: `4`
- `reviewed_bridge_choice`: `5`

## Stepwise Adjudication Queue

- 2. `thlb_parent_002_land_not_administered_by_the_province` | Land not administered by the Province | action=`fix_strict_logic` | tsr-fit=`strict_under_tsr_major` | ownership=`model_endogenous`
- 3. `thlb_parent_003_non_forest` | Non-forest | action=`keep_reviewed_bridge` | tsr-fit=`strict_under_tsr_major` | ownership=`model_endogenous`
- 4. `thlb_parent_004_roads_and_landings` | Roads and landings | action=`use_documented_aspatial_fallback` | tsr-fit=`strict_under_tsr_major` | ownership=`mixed`
- 6. `thlb_parent_006_parks_protected_areas_area_base_tenures` | Parks, protected areas, area-base tenures | action=`fix_strict_logic` | tsr-fit=`not_comparable_to_tsr` | ownership=`mixed`
- 7. `thlb_parent_007_old_growth_management_areas` | Old growth management areas | action=`fix_strict_logic` | tsr-fit=`not_comparable_to_tsr` | ownership=`model_endogenous`
- 8. `thlb_parent_008_wildlife_habitat_areas` | Wildlife habitat areas | action=`fix_strict_logic` | tsr-fit=`not_comparable_to_tsr` | ownership=`model_endogenous`
- 9. `thlb_parent_009_critical_habitat_for_fish` | Critical habitat for fish | action=`fix_strict_logic` | tsr-fit=`not_comparable_to_tsr` | ownership=`model_endogenous`
- 10. `thlb_parent_010_lakeshore_management` | Lakeshore management | action=`defer_low_priority` | tsr-fit=`tsr_close_enough` | ownership=`data_exogenous`
- 11. `thlb_parent_011_community_areas_of_special_concern` | Community areas of special concern | action=`keep_reviewed_bridge` | tsr-fit=`not_comparable_to_tsr` | ownership=`model_endogenous`
- 12. `thlb_parent_012_proven_aboriginal_rights_areas` | Proven Aboriginal Rights areas | action=`improve_data_or_source` | tsr-fit=`strict_under_tsr_major` | ownership=`data_exogenous`
- 13. `thlb_parent_013_areas_considered_inoperable` | Areas considered inoperable | action=`keep_reviewed_bridge` | tsr-fit=`not_comparable_to_tsr` | ownership=`reviewed_bridge_choice`
- 14. `thlb_parent_014_sites_with_low_growing_timber_potential` | Sites with low growing timber potential | action=`keep_reviewed_bridge` | tsr-fit=`not_comparable_to_tsr` | ownership=`mixed`
- 15. `thlb_parent_015_non_merchantable_timber_profiles` | Non-merchantable timber profiles | action=`keep_reviewed_bridge` | tsr-fit=`not_comparable_to_tsr` | ownership=`model_endogenous`
- 16. `thlb_parent_016_recreation_features` | Recreation features | action=`fix_strict_logic` | tsr-fit=`not_comparable_to_tsr` | ownership=`mixed`
- 17. `thlb_parent_017_growth_and_yield_permanent_sample_plots` | Growth and yield permanent sample plots | action=`improve_data_or_source` | tsr-fit=`not_comparable_to_tsr` | ownership=`data_exogenous`
- 18. `thlb_parent_018_riparian_areas` | Riparian areas | action=`improve_data_or_source` | tsr-fit=`not_comparable_to_tsr` | ownership=`mixed`
- 19. `thlb_parent_019_buffered_trails` | Buffered trails | action=`keep_reviewed_bridge` | tsr-fit=`not_comparable_to_tsr` | ownership=`reviewed_bridge_choice`
- 20. `thlb_parent_020_wildlife_tree_retention_areas` | Wildlife tree retention areas | action=`use_documented_aspatial_fallback` | tsr-fit=`strict_under_tsr_major` | ownership=`reviewed_bridge_choice`
- 21. `thlb_parent_021_cultural_heritage_and_archaeological_resources` | Cultural heritage and archaeological resources | action=`use_documented_aspatial_fallback` | tsr-fit=`strict_under_tsr_minor` | ownership=`reviewed_bridge_choice`
- 23. `thlb_parent_023_future_roads` | Future roads | action=`defer_low_priority` | tsr-fit=`tsr_close_enough` | ownership=`reviewed_bridge_choice`

## Top 5 Strict-vs-TSR Contributors

- `thlb_parent_003_non_forest` | Non-forest | tsr-fit=`strict_under_tsr_major` | strict-TSR net deduction delta=`-30035.783 ha`
- `thlb_parent_008_wildlife_habitat_areas` | Wildlife habitat areas | tsr-fit=`not_comparable_to_tsr` | strict-TSR net deduction delta=`-22488.408 ha`
- `thlb_parent_011_community_areas_of_special_concern` | Community areas of special concern | tsr-fit=`not_comparable_to_tsr` | strict-TSR net deduction delta=`16133.956 ha`
- `thlb_parent_009_critical_habitat_for_fish` | Critical habitat for fish | tsr-fit=`not_comparable_to_tsr` | strict-TSR net deduction delta=`14453.994 ha`
- `thlb_parent_007_old_growth_management_areas` | Old growth management areas | tsr-fit=`not_comparable_to_tsr` | strict-TSR net deduction delta=`12919.262 ha`

## Top 5 Strict-vs-Reviewed Context Differences

- `thlb_parent_003_non_forest` | Non-forest | reviewed-role=`reviewed_bridge_only` | strict-reviewed net deduction delta=`-939248.729 ha`
- `thlb_parent_002_land_not_administered_by_the_province` | Land not administered by the Province | reviewed-role=`reviewed_bridge_only` | strict-reviewed net deduction delta=`475179.272 ha`
- `thlb_parent_020_wildlife_tree_retention_areas` | Wildlife tree retention areas | reviewed-role=`aspatial_bridge_difference` | strict-reviewed net deduction delta=`60789.057 ha`
- `thlb_parent_015_non_merchantable_timber_profiles` | Non-merchantable timber profiles | reviewed-role=`blocked_or_missing_source` | strict-reviewed net deduction delta=`-55321.010 ha`
- `thlb_parent_004_roads_and_landings` | Roads and landings | reviewed-role=`aspatial_bridge_difference` | strict-reviewed net deduction delta=`48876.889 ha`

## Plain-Language Read

- This report does not change THLB logic. It explains how the strict reconstructed lane fits against the TSR benchmark and uses the reviewed lane as supporting context.
- The governing question is whether strict is close enough to TSR, not whether strict matches reviewed step-for-step.
- Reviewed differences still matter, but mainly because they explain accepted bridges, skips, calibrations, or semantic differences that the strict lane does not automatically share.
- For the current TSA29 adjudication pass, this report is an active repair ledger: once a parent step is understood well enough to choose an actionable next move, land that change before moving to the next step.
- Only leave a step as analysis-only when the chosen action is explicitly to defer, keep a reviewed bridge for now, or wait on missing data/source improvements.

## Backbone Milestones

- `thlb_parent_001_total_tsa_area` | Total TSA area | benchmark cumulative area=`4933635.000 ha` | strict cumulative area=`4933664.212 ha` | strict cumulative delta=`29.212 ha`
- `thlb_parent_005_analysis_forest_land_base` | Analysis forest land base | benchmark cumulative area=`3098168.000 ha` | strict cumulative area=`3110576.671 ha` | strict cumulative delta=`12408.671 ha`
- `thlb_parent_022_timber_harvesting_land_base` | Timber harvesting land base | benchmark cumulative area=`1682843.000 ha` | strict cumulative area=`1671251.622 ha` | strict cumulative delta=`-11591.378 ha`
- `thlb_parent_024_long_term_thlb` | Long-term THLB | benchmark cumulative area=`1660053.000 ha` | strict cumulative area=`1648497.622 ha` | strict cumulative delta=`-11555.378 ha`

## Parent-Step Comparison

### GLB -> AFLB

#### 2. Land not administered by the Province

- Parent step id: `thlb_parent_002_land_not_administered_by_the_province`
- Strict TSR fit: `strict_under_tsr_major`
- Reviewed difference role: `reviewed_bridge_only`
- Problem ownership: `model_endogenous`
- Difference nature: `strict_logic_overcut`
- Reconstructed status: `fragment_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `bounded_step_run`
- Locked source note: clean GLB + valid paged F_OWN + treaty/title residual aspatial fallback
- TSR benchmark marginal deduction: `697033.000 ha`
- TSR benchmark cumulative area: `4236602.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `4236882.888 ha`
- Strict cumulative vs TSR cumulative delta: `280.888 ha`
- Strict reconstructed net deduction: `696781.324 ha`
- Reviewed bridge net deduction: `221602.052 ha`
- Strict vs TSR delta: `-251.676 ha`
- Reviewed vs TSR delta: `-475430.948 ha`
- Strict vs reviewed delta: `475179.272 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The reviewed lane removed material area here, but the strict lane did not produce a comparable removal.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: The strict lane is using a broader ownership interpretation than the reviewed bridge, so it is cutting too much area here.
- Recommended next move: Tighten the strict ownership mapping and separate the dedicated title/treaty exclusions from the generic F_OWN ownership classes.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Decide whether the reviewed bridge should stay an accepted difference or be translated into strict semantics.
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
- Reconstructed status: `not_executed`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `bounded_step_run`
- Locked source note: clean GLB + harvest-history restoration + polygonal FWA handling
- TSR benchmark marginal deduction: `1105908.000 ha`
- TSR benchmark cumulative area: `3130694.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `3161010.671 ha`
- Strict cumulative vs TSR cumulative delta: `30316.671 ha`
- Strict reconstructed net deduction: `1075872.217 ha`
- Reviewed bridge net deduction: `2015120.946 ha`
- Strict vs TSR delta: `-30035.783 ha`
- Reviewed vs TSR delta: `909212.946 ha`
- Strict vs reviewed delta: `-939248.729 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The reviewed lane removed material area here, but the strict lane did not produce a comparable removal.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: The strict lane is only doing a narrow direct waterbody removal here, while the reviewed lane is carrying a much broader non-forest interpretation; in addition, this early GLB-to-AFLB comparison is conditioned by checkpoint1/AFLB initialization rather than a literal raw-GLB replay.
- Recommended next move: Decide and document the intended strict non-forest semantics before changing code again; this is not just a missing-data problem, and the current stepwise delta should be read as a baseline-conditioned diagnostic rather than a literal raw-GLB replay.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Decide whether the reviewed bridge should stay an accepted difference or be translated into strict semantics.
- Supporting notes:
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`

#### 4. Roads and landings

- Parent step id: `thlb_parent_004_roads_and_landings`
- Strict TSR fit: `strict_under_tsr_major`
- Reviewed difference role: `aspatial_bridge_difference`
- Problem ownership: `mixed`
- Difference nature: `accepted_aspatial_bridge`
- Reconstructed status: `aspatial_fallback`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `documented_aspatial_bridge`
- Locked source note: settled roads/trails/landings residual aspatial fallback
- TSR benchmark marginal deduction: `50434.000 ha`
- TSR benchmark cumulative area: `3080260.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `3110576.671 ha`
- Strict cumulative vs TSR cumulative delta: `30316.671 ha`
- Strict reconstructed net deduction: `50434.000 ha`
- Reviewed bridge net deduction: `1557.111 ha`
- Strict vs TSR delta: `0.000 ha`
- Reviewed vs TSR delta: `-48876.889 ha`
- Strict vs reviewed delta: `48876.889 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The strict lane used a documented aspatial fallback here instead of exact spatial reproduction.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: The TSR itself says existing roads, trails, and landings are modeled non-spatially through partial AFLB reductions because the features are too small and incomplete to track cleanly at landscape scale. The strict lane should therefore be judged against the documented aspatial benchmark first, with the narrow permanent-road overlays treated as supporting evidence only.
- Recommended next move: Keep the documented step-4 aspatial AFLB fallback in place unless you later adopt a better exact road-footprint contract.
- Adjudication queue action: `use_documented_aspatial_fallback` (Keep or formalize a documented aspatial fallback.)
- Actionability: Decide whether this documented aspatial fallback should remain the working contract or be replaced by a better exact implementation later.
- Supporting notes:
  - strict spatial modes: `aspatial_fallback`
  - strict compiled steps: `thlb_parent_004_roads_and_landings_compiled_01`, `thlb_parent_004_roads_and_landings_compiled_02`, `thlb_parent_004_roads_and_landings_compiled_03`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.2.3 says existing roads, trails, and landings are modeled non-spatially through partial AFLB reductions because the mapped features are too small and incomplete to track reliably at landscape scale.
  - strict note: Use the TSR benchmark marginal deduction of 50,434 ha for this step; do not use the conflicting 32,526 ha prose sentence as the governing fallback target.
  - strict note: Subtract any exact same-parent permanent-road overlap already removed so the fallback only fills the remaining benchmark gap.

### AFLB -> LHLB

#### 6. Parks, protected areas, area-base tenures

- Parent step id: `thlb_parent_006_parks_protected_areas_area_base_tenures`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `mixed`
- Difference nature: `strict_logic_undercut`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `exact_plus_residual_bridge`
- Locked source note: exact parks/protected overlay + residual aspatial woodlot/lease bridge from AFLB checkpoint
- TSR benchmark marginal deduction: `306327.000 ha`
- TSR benchmark cumulative area: `2791841.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `2804249.671 ha`
- Strict cumulative vs TSR cumulative delta: `12408.671 ha`
- Strict reconstructed net deduction: `306327.000 ha`
- Reviewed bridge net deduction: `275618.199 ha`
- Strict vs TSR delta: `0.000 ha`
- Reviewed vs TSR delta: `-30708.801 ha`
- Strict vs reviewed delta: `30708.801 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane is lighter than the reviewed lane here, likely because tenure and ownership semantics are still not fully aligned.
- Recommended next move: Refine the strict tenure/ownership logic first, then reassess whether any supporting data gaps remain material.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
  - strict compiled steps: `thlb_parent_006_parks_protected_areas_area_base_tenures_compiled_01`, `thlb_parent_006_parks_protected_areas_area_base_tenures_compiled_02`
  - reviewed ratchet state: `benchmarked`
  - strict note: TSA29 section 6.2.1 keeps woodlots in AFLB but removes them when defining the LHLB, so woodlot schedules A/B are included here.
  - strict note: This first runnable pass uses the explicit F_OWN ownership descriptions for woodlots and the small miscellaneous crown-lease class cited in TSA29 Table 7.
  - strict note: Community forest agreements and first nations woodland licences were already netted out upstream in TSA29 step 2 and are therefore intentionally excluded from this step-6 executable filter.
  - strict note: FTEN managed-licence and TANTALIS crown-tenure layers remain supporting metadata/reference surfaces, but F_OWN is the executable ownership overlay in the TSA29 bridge.

#### 7. Old growth management areas

- Parent step id: `thlb_parent_007_old_growth_management_areas`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `model_endogenous`
- Difference nature: `strict_logic_overcut`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `bounded_step_run`
- Locked source note: exact OGMA overlay after fractional-state fix
- TSR benchmark marginal deduction: `210719.000 ha`
- TSR benchmark cumulative area: `2581122.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `2580611.409 ha`
- Strict cumulative vs TSR cumulative delta: `-510.591 ha`
- Strict reconstructed net deduction: `223638.262 ha`
- Reviewed bridge net deduction: `227336.336 ha`
- Strict vs TSR delta: `12919.262 ha`
- Reviewed vs TSR delta: `16617.336 ha`
- Strict vs reviewed delta: `-3698.074 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane is likely treating OGMA area too broadly relative to the reviewed TSA29 interpretation.
- Recommended next move: Tighten the OGMA logic before looking for new data; this looks like an over-selection problem.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
  - strict compiled steps: `thlb_parent_007_old_growth_management_areas_compiled_01`
  - reviewed approval scope: `full_tsa_validation`
  - reviewed ratchet state: `approved`
  - strict note: Current notebook execution treats only permanent and rotating legal OGMAs as the direct no-harvest exclusion surface.
  - strict note: Transition OGMAs remain contextual/temporal logic and are not hard-excluded in this base-case executable mask.
  - strict note: Harvest exceptions, overlap replacement, and transition restoration timing remain later review/calibration work.

#### 8. Wildlife habitat areas

- Parent step id: `thlb_parent_008_wildlife_habitat_areas`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `model_endogenous`
- Difference nature: `strict_logic_overcut`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `bounded_step_run`
- Locked source note: locked post-step-7 wildlife habitat no-harvest slice
- TSR benchmark marginal deduction: `154056.000 ha`
- TSR benchmark cumulative area: `2427066.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `2449043.817 ha`
- Strict cumulative vs TSR cumulative delta: `21977.817 ha`
- Strict reconstructed net deduction: `131567.592 ha`
- Reviewed bridge net deduction: `133005.883 ha`
- Strict vs TSR delta: `-22488.408 ha`
- Reviewed vs TSR delta: `-21050.117 ha`
- Strict vs reviewed delta: `-1438.291 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane is selecting far more wildlife-area land than either the reviewed lane or the TSR benchmark supports.
- Recommended next move: Audit the strict no-harvest selection logic and keep conditional/modified zones out unless the TSR clearly says otherwise.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
  - strict compiled steps: `thlb_parent_008_wildlife_habitat_areas_compiled_01`, `thlb_parent_008_wildlife_habitat_areas_compiled_02`
  - reviewed approval scope: `full_tsa_validation`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.3.3 states that only no-harvest wildlife areas are excluded at this stage.
  - strict note: Conditional harvest zones are deferred to later forest-management assumptions and silviculture logic.
  - strict note: General Wildlife Measures with no-harvest direction are excluded here; modified/conditional zones are not.

#### 9. Critical habitat for fish

- Parent step id: `thlb_parent_009_critical_habitat_for_fish`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `model_endogenous`
- Difference nature: `strict_logic_overcut`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `bounded_step_run`
- Locked source note: legal-planning fish subset extent fix; cumulative fit accepted as good enough
- TSR benchmark marginal deduction: `11521.000 ha`
- TSR benchmark cumulative area: `2415545.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `2423068.823 ha`
- Strict cumulative vs TSR cumulative delta: `7523.823 ha`
- Strict reconstructed net deduction: `25974.994 ha`
- Reviewed bridge net deduction: `17482.824 ha`
- Strict vs TSR delta: `14453.994 ha`
- Reviewed vs TSR delta: `5961.824 ha`
- Strict vs reviewed delta: `8492.170 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane is applying a much broader legal fish-objective surface than the reviewed lane or TSR benchmark supports.
- Recommended next move: Narrow the strict fish-habitat interpretation; this is one of the clearest strict overcut seams in the whole ladder.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
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
- Reconstructed status: `not_executed`
- Reviewed status: `approved`
- Locked dashboard row: `yes`
- Locked source kind: `reviewed_skip`
- Locked source note: Accepted trivial full-TSA skip; current public layers do not expose a trusted Class A lake discriminator.
- TSR benchmark marginal deduction: `327.000 ha`
- TSR benchmark cumulative area: `2415218.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `2423068.823 ha`
- Strict cumulative vs TSR cumulative delta: `7850.823 ha`
- Strict reconstructed net deduction: `0.000 ha`
- Reviewed bridge net deduction: `not recorded`
- Strict vs TSR delta: `-327.000 ha`
- Strict vs TSR: The strict lane is close enough to the TSR benchmark here for practical exploratory use.
- Reviewed difference: The reviewed lane is carrying an accepted override, skip, calibration, or no-op choice that the strict lane does not automatically share.
- Practical meaning: Strict is close enough to TSR here, so this is not a top-priority repair. The reviewed lane is using an accepted override, calibration, skip, or no-op that the strict lane does not automatically share.
- Engineering interpretation: This step depends on a trusted Class A lake discriminator that the current public-input lane still does not have.
- Recommended next move: Keep the reviewed skip or a tiny aspatial fallback unless a trustworthy lake-class source appears.
- Adjudication queue action: `defer_low_priority` (Defer; this is not a top-priority repair right now.)
- Actionability: Review the accepted reviewed override before changing the strict lane.
- Supporting notes:
  - reviewed approval scope: `full_tsa_trivial_benchmark_skip`
  - reviewed ratchet state: `approved`

#### 11. Community areas of special concern

- Parent step id: `thlb_parent_011_community_areas_of_special_concern`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `model_endogenous`
- Difference nature: `reviewed_bridge_semantics`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `bounded_step_run`
- Locked source note: bounded chained replay from official AFLB checkpoint through locked steps 6-9, then exact step-11 legal-planning CASC overlay
- TSR benchmark marginal deduction: `62460.000 ha`
- TSR benchmark cumulative area: `2352758.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `2344474.867 ha`
- Strict cumulative vs TSR cumulative delta: `-8283.133 ha`
- Strict reconstructed net deduction: `78593.956 ha`
- Reviewed bridge net deduction: `69545.637 ha`
- Strict vs TSR delta: `16133.956 ha`
- Reviewed vs TSR delta: `7085.637 ha`
- Strict vs reviewed delta: `9048.319 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict literal source choice is not reproducing the reviewed meaning of this step at all.
- Recommended next move: Fix the strict semantics/source interpretation instead of treating this as a pure missing-data problem.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
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
- Reconstructed status: `not_executed`
- Reviewed status: `approved`
- Locked dashboard row: `yes`
- Locked source kind: `documented_aspatial_bridge`
- Locked source note: benchmark-anchored public-data aspatial bridge for Proven Aboriginal Rights areas; exact PRA boundary not publicly trustworthy
- TSR benchmark marginal deduction: `68401.000 ha`
- TSR benchmark cumulative area: `2284357.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `2276073.867 ha`
- Strict cumulative vs TSR cumulative delta: `-8283.133 ha`
- Strict reconstructed net deduction: `68401.000 ha`
- Reviewed bridge net deduction: `not recorded`
- Strict vs TSR delta: `0.000 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The reviewed lane is carrying an accepted override, skip, calibration, or no-op choice that the strict lane does not automatically share.
- Practical meaning: Strict is badly low against TSR here, but the main reason looks exogenous: the needed data or source contract is missing.
- Engineering interpretation: The strict lane still lacks a trustworthy public boundary source for this step.
- Recommended next move: Keep this as a reviewed skip or documented fallback until a real source is available.
- Adjudication queue action: `improve_data_or_source` (Improve or replace the missing/weak source data.)
- Actionability: Review the accepted reviewed override before changing the strict lane.
- Supporting notes:
  - reviewed approval scope: `full_tsa_public_data_unavailable_aspatial_bridge`
  - reviewed ratchet state: `approved`

### LHLB -> THLB

#### 13. Areas considered inoperable

- Parent step id: `thlb_parent_013_areas_considered_inoperable`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `reviewed_bridge_choice`
- Difference nature: `accepted_reviewed_override`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `exact_plus_calibrated_bridge`
- Locked source note: exact unstable-terrain overlay + direct-target steep-slope THLB rollback on selected steep subset
- TSR benchmark marginal deduction: `33533.000 ha`
- TSR benchmark cumulative area: `2250824.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `2240985.033 ha`
- Strict cumulative vs TSR cumulative delta: `-9838.967 ha`
- Strict reconstructed net deduction: `35088.834 ha`
- Reviewed bridge net deduction: `43628.139 ha`
- Strict vs TSR delta: `1555.834 ha`
- Reviewed vs TSR delta: `10095.139 ha`
- Strict vs reviewed delta: `-8539.305 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The reviewed lane uses accepted derived-attribute and calibrated bridge logic here that the strict checkpoint1 lane does not share.
- Recommended next move: Keep the accepted reviewed bridge unless you explicitly decide to port its late-stage derived attributes into strict semantics.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
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
- Locked dashboard row: `yes`
- Locked source kind: `official_curve_ready_restart_bounded_slice`
- Locked source note: official lhlb_curve_ready restart after validated atomic publish and LU-cache invalidation; step-14 total 314,591.438 ha
- TSR benchmark marginal deduction: `321044.000 ha`
- TSR benchmark cumulative area: `1929780.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1926393.594 ha`
- Strict cumulative vs TSR cumulative delta: `-3386.406 ha`
- Strict reconstructed net deduction: `314591.438 ha`
- Reviewed bridge net deduction: `329228.613 ha`
- Strict vs TSR delta: `-6452.562 ha`
- Reviewed vs TSR delta: `8184.613 ha`
- Strict vs reviewed delta: `-14637.174 ha`
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
- Locked dashboard row: `yes`
- Locked source kind: `official_curve_ready_restart_bounded_slice`
- Locked source note: official lhlb_curve_ready restart with broadleaf-leading plus PROJ_AGE_1 >= 95 minimum-age proxy; step-15 total 48,308.452 ha
- TSR benchmark marginal deduction: `49052.000 ha`
- TSR benchmark cumulative area: `1880728.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1878085.142 ha`
- Strict cumulative vs TSR cumulative delta: `-2642.858 ha`
- Strict reconstructed net deduction: `48308.452 ha`
- Reviewed bridge net deduction: `103629.462 ha`
- Strict vs TSR delta: `-743.548 ha`
- Reviewed vs TSR delta: `54577.462 ha`
- Strict vs reviewed delta: `-55321.010 ha`
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
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `mixed`
- Difference nature: `partial_strict_logic`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `official_curve_ready_restart_bounded_slice`
- Locked source note: official lhlb_curve_ready restart bounded slice through locked steps 13-15, then exact active recreation overlay; step-16 total 8,891.240 ha
- TSR benchmark marginal deduction: `9598.000 ha`
- TSR benchmark cumulative area: `1871130.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1869193.903 ha`
- Strict cumulative vs TSR cumulative delta: `-1936.097 ha`
- Strict reconstructed net deduction: `8891.240 ha`
- Reviewed bridge net deduction: `7562.895 ha`
- Strict vs TSR delta: `-706.760 ha`
- Reviewed vs TSR delta: `-2035.105 ha`
- Strict vs reviewed delta: `1328.345 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane only captures part of the reviewed recreation exclusion logic.
- Recommended next move: Low-priority cleanup: improve strict logic if this step later matters to the remaining gap.
- Adjudication queue action: `fix_strict_logic` (Fix strict logic or semantics in FEMIC.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
  - strict compiled steps: `thlb_parent_016_recreation_features_compiled_01`
  - reviewed approval scope: `full_tsa_user_directed_acceptance`
  - reviewed ratchet state: `approved`
  - strict note: TSA29 section 6.4.6 excludes identified recreation areas and features from THLB.
  - strict note: Notebook execution currently auto-runs the active FTEN recreation polygon subset only.
  - strict note: Recreation trails and FSP consultation/procedure language remain out of scope for this first runnable bridge pass.

#### 17. Growth and yield permanent sample plots

- Parent step id: `thlb_parent_017_growth_and_yield_permanent_sample_plots`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `data_exogenous`
- Difference nature: `weak_public_coverage`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `official_curve_ready_restart_bounded_slice`
- Locked source note: official lhlb_curve_ready restart bounded slice through locked steps 13-16, then exact PSP overlay; step-17 total 1,166.660 ha
- TSR benchmark marginal deduction: `3577.000 ha`
- TSR benchmark cumulative area: `1867553.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1868027.243 ha`
- Strict cumulative vs TSR cumulative delta: `474.243 ha`
- Strict reconstructed net deduction: `1166.660 ha`
- Reviewed bridge net deduction: `1261.158 ha`
- Strict vs TSR delta: `-2410.340 ha`
- Reviewed vs TSR delta: `-2315.842 ha`
- Strict vs reviewed delta: `-94.498 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane undercuts here, but the public PSP geometry signal is weak and the absolute area is small.
- Recommended next move: Treat this as a lower-priority data-coverage seam unless a better PSP source becomes available.
- Adjudication queue action: `improve_data_or_source` (Improve or replace the missing/weak source data.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
  - strict compiled steps: `thlb_parent_017_growth_and_yield_permanent_sample_plots_compiled_01`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`

#### 18. Riparian areas

- Parent step id: `thlb_parent_018_riparian_areas`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `mixed`
- Difference nature: `missing_or_blocked_data`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `official_curve_ready_restart_bounded_slice_tsa29_instance_hack`
- Locked source note: official lhlb_curve_ready restart bounded slice through locked steps 13-17, then TSA29-only riparian hack keeping only S4 streams and W5 wetlands active; step-18 total 57,651.598 ha
- TSR benchmark marginal deduction: `54833.000 ha`
- TSR benchmark cumulative area: `1812720.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1810375.644 ha`
- Strict cumulative vs TSR cumulative delta: `-2344.356 ha`
- Strict reconstructed net deduction: `57651.598 ha`
- Reviewed bridge net deduction: `72204.542 ha`
- Strict vs TSR delta: `2818.598 ha`
- Reviewed vs TSR delta: `17371.542 ha`
- Strict vs reviewed delta: `-14552.943 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The strict lane is still missing some of the lake-class and special-case riparian inputs that the reviewed bridge used.
- Recommended next move: Improve source coverage first, then revisit the strict riparian logic if the gap remains large.
- Adjudication queue action: `improve_data_or_source` (Improve or replace the missing/weak source data.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
  - strict compiled steps: `thlb_parent_018_riparian_areas_compiled_stream_s1`, `thlb_parent_018_riparian_areas_compiled_stream_s2`, `thlb_parent_018_riparian_areas_compiled_stream_s3`, `thlb_parent_018_riparian_areas_compiled_stream_s4`, `thlb_parent_018_riparian_areas_compiled_stream_s5`, `thlb_parent_018_riparian_areas_compiled_stream_s6`, `thlb_parent_018_riparian_areas_compiled_wetland_w1`, `thlb_parent_018_riparian_areas_compiled_wetland_w2`, `thlb_parent_018_riparian_areas_compiled_wetland_w3`, `thlb_parent_018_riparian_areas_compiled_wetland_w4`, `thlb_parent_018_riparian_areas_compiled_wetland_w5`
  - reviewed approval scope: `single_lu_smoke_subset_williams_lake`
  - reviewed ratchet state: `approved`
  - strict note: Step 3 already removed the direct non-forest waterbody area; this later THLB step models the additional riparian buffer.
  - strict note: The Table 15 riparian width already folds RRZ plus retained RMZ share into an equivalent full-exclusion width.
  - strict note: Step 3 already removed the direct wetland polygon area; this later THLB step models the additional riparian buffer.

#### 19. Buffered trails

- Parent step id: `thlb_parent_019_buffered_trails`
- Strict TSR fit: `not_comparable_to_tsr`
- Reviewed difference role: `blocked_or_missing_source`
- Problem ownership: `reviewed_bridge_choice`
- Difference nature: `accepted_reviewed_override`
- Reconstructed status: `blocked_exact_overlay`
- Reviewed status: `applied`
- Locked dashboard row: `yes`
- Locked source kind: `post_step18_restart_bounded_slice`
- Locked source note: bounded step-19-only replay from the locked post-step-18 late-stage restart surface; strict total 10,502.023 ha
- TSR benchmark marginal deduction: `8039.000 ha`
- TSR benchmark cumulative area: `1804681.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1799873.622 ha`
- Strict cumulative vs TSR cumulative delta: `-4807.378 ha`
- Strict reconstructed net deduction: `10502.023 ha`
- Reviewed bridge net deduction: `10244.748 ha`
- Strict vs TSR delta: `2463.023 ha`
- Reviewed vs TSR delta: `2205.748 ha`
- Strict vs reviewed delta: `257.275 ha`
- Strict vs TSR: The strict lane is still blocked here, so strict-vs-TSR fit is not yet a clean execution comparison.
- Reviewed difference: The strict lane is still blocked here, so the area gap is not yet a clean modeling comparison.
- Practical meaning: The reviewed difference here is not very informative yet because the strict lane is still blocked or missing a needed source.
- Engineering interpretation: The reviewed lane uses an accepted equivalent-corridor bridge here, while the strict lane currently does not reproduce that bridge.
- Recommended next move: Keep the accepted bridge unless you explicitly decide to formalize the same equivalent-corridor logic in strict mode.
- Adjudication queue action: `keep_reviewed_bridge` (Keep the reviewed bridge for now and do not force strict parity yet.)
- Actionability: Acquire or repair the missing source/blocked seam before treating this as a real strict comparison.
- Supporting notes:
  - strict spatial modes: `blocked_exact_overlay`
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
- Locked dashboard row: `yes`
- Locked source kind: `post_step19_restart_direct_target_aspatial`
- Locked source note: bounded step-20-only replay from the locked post-step-19 restart surface; WTRA modeled as a direct-target aspatial THLB rollback of 94,417 ha for the full TSA strict lane
- TSR benchmark marginal deduction: `94417.000 ha`
- TSR benchmark cumulative area: `1710264.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1705456.622 ha`
- Strict cumulative vs TSR cumulative delta: `-4807.378 ha`
- Strict reconstructed net deduction: `94417.000 ha`
- Reviewed bridge net deduction: `33627.943 ha`
- Strict vs TSR delta: `0.000 ha`
- Reviewed vs TSR delta: `-60789.057 ha`
- Strict vs reviewed delta: `60789.057 ha`
- Strict vs TSR: The strict lane is materially below the TSR benchmark here, so this looks like a real strict-lane undercut seam.
- Reviewed difference: The strict lane used a documented aspatial fallback here instead of exact spatial reproduction.
- Practical meaning: Strict is badly low against TSR here, so this is a real seam to fix or bridge explicitly.
- Engineering interpretation: This step is intentionally being modeled as an aspatial future-WTRA bridge rather than an exact mapped exclusion.
- Recommended next move: Keep the documented aspatial fallback unless a better exact contract is deliberately adopted later.
- Adjudication queue action: `use_documented_aspatial_fallback` (Keep or formalize a documented aspatial fallback.)
- Actionability: Decide whether this documented aspatial fallback should remain the working contract or be replaced by a better exact implementation later.
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
- Locked dashboard row: `yes`
- Locked source kind: `post_step20_restart_direct_target_aspatial`
- Locked source note: bounded step-21-only replay from the locked post-step-20 restart surface; cultural heritage modeled as a direct-target aspatial THLB rollback of 34,205 ha for the full TSA strict lane
- TSR benchmark marginal deduction: `34205.000 ha`
- TSR benchmark cumulative area: `1676059.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1671251.622 ha`
- Strict cumulative vs TSR cumulative delta: `-4807.378 ha`
- Strict reconstructed net deduction: `34205.000 ha`
- Reviewed bridge net deduction: `11512.712 ha`
- Strict vs TSR delta: `0.000 ha`
- Reviewed vs TSR delta: `-22692.288 ha`
- Strict vs reviewed delta: `22692.288 ha`
- Strict vs TSR: The strict lane is somewhat below the TSR benchmark here, but not yet in the worst problem tier.
- Reviewed difference: The strict lane used a documented aspatial fallback here instead of exact spatial reproduction.
- Practical meaning: Strict is off TSR here, but not in the very worst tier. The reviewed difference here is mostly about an explicit aspatial bridge choice rather than exact spatial truth.
- Engineering interpretation: This step is intentionally being modeled as an aspatial THLB bridge rather than a single exact spatial layer.
- Recommended next move: Keep the documented aspatial fallback unless a defensible exact spatial contract is introduced later.
- Adjudication queue action: `use_documented_aspatial_fallback` (Keep or formalize a documented aspatial fallback.)
- Actionability: Decide whether this documented aspatial fallback should remain the working contract or be replaced by a better exact implementation later.
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
- Locked dashboard row: `yes`
- Locked source kind: `post_step21_restart_direct_target_aspatial`
- Locked source note: bounded step-23-only replay from the locked post-step-21 restart surface; future roads modeled as a direct-target aspatial THLB rollback of 22,754 ha for the full TSA strict lane
- TSR benchmark marginal deduction: `22754.000 ha`
- Strict reconstructed cumulative area at this checkpoint: `1648497.622 ha`
- Strict cumulative vs TSR cumulative delta: `-1555.378 ha`
- Strict reconstructed net deduction: `22754.000 ha`
- Reviewed bridge net deduction: `0.000 ha`
- Strict vs TSR delta: `0.000 ha`
- Reviewed vs TSR delta: `-22754.000 ha`
- Strict vs reviewed delta: `22754.000 ha`
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
