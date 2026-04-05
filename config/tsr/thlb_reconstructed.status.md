# THLB Netdown Status Report: TSA 29 (Williams Lake)

- Generated UTC: `2026-04-05T18:52:02.296300+00:00`
- Execution mode: `reconstructed`
- Baseline signal: `checkpoint1_aflb_initialization`
- Recipe path: `config/tsr/thlb_netdown.recipe.yaml`
- Checkpoint input: `data/ria_vri_vclr1p_checkpoint1.feather`
- Output checkpoint: `data/tsr/thlb_reconstructed_checkpoint.feather`
- Audit JSON: `config/tsr/thlb_reconstructed.audit.json`
- Runtime history copy: `runtime/logs/tsr/thlb_reconstructed_status_report-20260405T185202Z.md`

## Scope

- Selected MAP_ID subset: `092O071`
- Step count: `18`

## Areas

- Input checkpoint area: `27072.529 ha`
- AFLB / baseline managed area: `26350.175 ha`
- Final THLB area: `25690.668 ha`
- Legacy raster THLB reference: `1513233.574 ha`
- TSR reported AFLB benchmark: `3098168.000 ha`
- TSR reported THLB benchmark: `1660053.000 ha`

## Ratios

- Input:AFLB = `0.9733 (97.33%)`
- AFLB:THLB = `0.9750 (97.50%)`
- Input:THLB = `0.9490 (94.90%)`
- TSR AFLB:THLB = `0.5358 (53.58%)`

## Outcomes

- `applied`: `2`
- `applied_noop`: `2`
- `blocked_missing_source`: `3`
- `needs_review`: `10`
- `unsupported`: `1`

## Locking / Convergence

- AFLB lock state: `unlocked`
- THLB lock state: `unlocked`
- Current note: FEMIC now records benchmark ratios and runtime history for convergence review, but explicit user lock/cut-lock controls are not implemented yet.

## Interpretation

- Non-AFLB polygons are excluded from the reconstruction universe before THLB logic applies.
- Non-THLB polygons or fragments remain inside that working universe and are assigned THLB state by the recipe run.
- AU/VDYP-oriented filters are not assumed to be valid THLB filters unless the TSR logic says so explicitly.
- Legacy raster THLB values are reference-only in reconstructed mode.

## Sequential THLB Steps

### 1. 6. Timber Harvesting Land Base Definition ......................................

- Step id: `thlb_step_001_6_timber_harvesting_land_base_definition`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=2`
- TSR page: `2`
- TSR text: `6. Timber Harvesting Land Base Definition ....................................................................................... 16`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Run notes:
  - Context-only THLB row; no execution attempted.

### 2. 6.4. Identification of the Timber Harvesting Land Base .........................

- Step id: `thlb_step_002_6_4_identification_of_the_timber_harvesting_land_base`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=2`
- TSR page: `2`
- TSR text: `6.4. Identification of the Timber Harvesting Land Base .................................................................... 25`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Run notes:
  - Context-only THLB row; no execution attempted.

### 3. 7.4.4 Disturbance outside of the timber harvesting land base ...................

- Step id: `thlb_step_003_7_4_4_disturbance_outside_of_the_timber_harvesting_land_base`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=3`
- TSR page: `3`
- TSR text: `7.4.4 Disturbance outside of the timber harvesting land base ...................................................... 55`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Linked source layers:
  - `whse_basemapping_dra_dgtl_road_atlas_mpar_sp` | query=`WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP`
    - top match: `Digital Road Atlas (DRA) - Master Partially-Attributed Roads`
- Run notes:
  - Context-only THLB row; no execution attempted.

### 5. 6. Timber Harvesting Land Base Definition

- Step id: `thlb_step_005_6_timber_harvesting_land_base_definition`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=22`
- TSR page: `22`
- TSR text: `6. Timber Harvesting Land Base Definition`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Run notes:
  - Context-only THLB row; no execution attempted.

### 7. THLB definition

- Step id: `thlb_step_007_thlb_definition`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=22`
- TSR page: `22`
- TSR text: `The THLB is the portion of the AFLB where timber harvesting is projected to occur. It includes areas`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Linked source layers:
  - `bcmpb_v9_cumkill_projected` | query=`BCMPB.V9.CUMKILL.PROJECTED` | status=`no_hit` | strategy=`override_required`
- Run notes:
  - Context-only THLB row; no execution attempted.

### 12. THLB decrease conditions

- Step id: `thlb_step_012_thlb_decrease_conditions`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=23`
- TSR page: `23`
- TSR text: `The THLB may also decrease in size where:`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Run notes:
  - Context-only THLB row; no execution attempted.

### 13. THLB increase conditions

- Step id: `thlb_step_013_thlb_increase_conditions`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=23`
- TSR page: `23`
- TSR text: `The THLB may increase in size over time in the following situations:`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Run notes:
  - Context-only THLB row; no execution attempted.

### 16. lands that are

- Step id: `thlb_step_016_lands_that_are`
- Kind: `netdown_rule`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=25`
- TSR page: `25`
- TSR text: `lands that are excluded from the AFLB are also excluded from the THLB. The AFLB is approximately`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 17. roads that are temporary in nature

- Step id: `thlb_step_017_roads_that_are_temporary_in_nature`
- Kind: `netdown_rule`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- TSR page: `27`
- TSR text: `roads that are temporary in nature will have no deduction from the THLB.`
- FEMIC proposed logic: Apply no THLB deduction for this rule.
- Linked source layers:
  - `ften_road_lines` | query=`FTEN_ROAD_LINES` | status=`exact_hit` | strategy=`dwds_order`
    - matched by: `object_name_suffix:WHSE_FOREST_TENURE.FTEN_ROAD_LINES`
    - top match: `Forest Tenure Road Lines`
- Run notes:
  - No spatial deduction applied for this rule.

### 19. 6.4. Identification of the Timber Harvesting Land Base

- Step id: `thlb_step_019_6_4_identification_of_the_timber_harvesting_land_base`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `6.4. Identification of the Timber Harvesting Land Base`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Run notes:
  - Context-only THLB row; no execution attempted.

### 20. THLB definition

- Step id: `thlb_step_020_thlb_definition`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `The THLB is the portion of the LHLB where timber harvesting is expected to occur in the context of the`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Run notes:
  - Context-only THLB row; no execution attempted.

### 24. stands

- Step id: `thlb_step_024_stands`
- Kind: `netdown_rule`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=33`
- TSR page: `33`
- TSR text: `stands are removed from the THLB.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 30. required for WTRA

- Step id: `thlb_step_030_required_for_wtra`
- Kind: `netdown_rule`
- Run status: `unsupported`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- TSR page: `37`
- TSR text: `required for WTRA will be modelled as an aspatial THLB reduction factor.`
- FEMIC proposed logic: Apply a final aspatial THLB reduction of the TSR-cited magnitude after the spatially executable steps have completed.
- Run notes:
  - Aspatial reduction steps are preserved for review but not executed in v1.

### 34. OGMAs

- Step id: `thlb_step_034_ogmas`
- Kind: `netdown_rule`
- Run status: `applied`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=48`
- TSR page: `48`
- TSR text: `OGMAs are removed from the THLB as no harvest areas. A limited amount of harvest is permitted in`
- FEMIC proposed logic: Overlay the linked polygon layers onto the working land base, fragment intersected geometry, and assign binary THLB {0,1} so excluded fragments are 0 and retained fragments remain 1.
- Linked source layers:
  - `rmp_ogma_legal` | query=`RMP_OGMA_LEGAL` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_OGMA_LEGAL/RMP_OGMA_LEGAL.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_OGMA_LEGAL_CURRENT_SVW`
    - top match: `Old Growth Management Areas - Legal - Current`
  - `whse_land_use_planning_rmp_ogma_legal` | query=`WHSE_LAND_USE_PLANNING.RMP_OGMA_LEGAL` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_OGMA_LEGAL/WHSE_LAND_USE_PLANNING_RMP_OGMA_LEGAL.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_OGMA_LEGAL_CURRENT_SVW`
    - top match: `Old Growth Management Areas - Legal - Current`
- Run notes:
  - Applied fragment/resultant exclusion with binary THLB output in EPSG:3005.

### 42. 7.4.4 Disturbance outside of the timber harvesting land base

- Step id: `thlb_step_042_7_4_4_disturbance_outside_of_the_timber_harvesting_land_base`
- Kind: `context`
- Run status: `needs_review`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=61`
- TSR page: `61`
- TSR text: `7.4.4 Disturbance outside of the timber harvesting land base`
- FEMIC proposed logic: Context/interpretation row only; no executable THLB logic is applied automatically.
- Linked source layers:
  - `whse_basemapping_dra_dgtl_road_atlas_mpar_sp` | query=`WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP`
    - top match: `Digital Road Atlas (DRA) - Master Partially-Attributed Roads`
- Run notes:
  - Context-only THLB row; no execution attempted.

### 49. Dasiqox

- Step id: `thlb_step_049_dasiqox`
- Kind: `netdown_rule`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=69`
- TSR page: `69`
- TSR text: `Dasiqox excluded Exclude from the THLB`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 50. Mule Deer winter range

- Step id: `thlb_step_050_mule_deer_winter_range`
- Kind: `netdown_rule`
- Run status: `applied`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=69`
- TSR page: `69`
- TSR text: `Mule Deer winter range Remove moderate to shallow MDWRs from the THLB`
- FEMIC proposed logic: Overlay the linked polygon layers onto the working land base, fragment intersected geometry, and assign binary THLB {0,1} so excluded fragments are 0 and retained fragments remain 1.
- Linked source layers:
  - `reg_land_and_natural_resource_l_mule_deer` | query=`REG_LAND_AND_NATURAL_RESOURCE.L_MULE_DEER` | status=`no_hit` | strategy=`override_required`
  - `reg_land_and_natural_resource_wld` | query=`REG_LAND_AND_NATURAL_RESOURCE.WLD` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_WLD/REG_LAND_AND_NATURAL_RESOURCE_WLD.gpkg`
    - matched by: `object_name_stem:REG_LAND_AND_NATURAL_RESOURCE.WLD_MULE_DEER_STND_STRC_CAR_SP`
    - top match: `Stand Structure Habitat Classes in Mule Deer Winter Range - Cariboo Region`
  - `whse_wildlife_management_wcp_ungulate` | query=`WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE.gpkg`
    - matched by: `object_name:WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE_SP`
    - top match: `Ungulate Winter Range - Approved`
- Missing linked source entries:
  - `reg_land_and_natural_resource_l_mule_deer`
- Run notes:
  - Applied fragment/resultant exclusion with binary THLB output in EPSG:3005.

### 51. Timber harvesting land base

- Step id: `thlb_step_051_timber_harvesting_land_base`
- Kind: `netdown_rule`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=69`
- TSR page: `69`
- TSR text: `Timber harvesting land base Use LHLB`
- FEMIC proposed logic: Use the AFLB-style initialized land base as the THLB starting universe.
- Run notes:
  - No spatial deduction applied for this rule.

