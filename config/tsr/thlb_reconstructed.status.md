# THLB Netdown Status Report: TSA 29 (Williams Lake)

- Generated UTC: `2026-04-05T21:46:35.615164+00:00`
- Execution mode: `reconstructed`
- Baseline signal: `checkpoint1_aflb_initialization`
- Recipe path: `config/tsr/thlb_netdown.recipe.yaml`
- Checkpoint input: `data/ria_vri_vclr1p_checkpoint1.feather`
- Output checkpoint: `data/tsr/thlb_reconstructed_checkpoint.feather`
- Audit JSON: `config/tsr/thlb_reconstructed.audit.json`
- Runtime history copy: `runtime/logs/tsr/thlb_reconstructed_status_report-20260405T214635Z.md`

## Scope

- Selected MAP_ID subset: `092O071`
- Step count: `24`

## Backbone Summary

- Input checkpoint area: `27072.529 ha`
- GLB / current input proxy: `27072.529 ha`
- AFLB / baseline managed area: `26350.175 ha`
- LHLB current: `not yet materialized separately in the current runner`
- THLB / final managed area: `0.000 ha`
- Legacy raster THLB reference: `1513233.574 ha`
- TSR reported AFLB benchmark: `3098168.000 ha`
- TSR reported THLB benchmark: `1660053.000 ha`

## Ratios

- GLB:AFLB current proxy = `0.9733 (97.33%)`
- AFLB:LHLB current = `n/a yet`
- AFLB:THLB current = `0.0000 (0.00%)`
- GLB:THLB current proxy = `0.0000 (0.00%)`
- TSR AFLB:THLB = `0.5358 (53.58%)`

## Outcomes

- `applied`: `1`
- `applied_noop`: `10`
- `blocked_missing_source`: `7`
- `unsupported`: `6`

## Locking / Convergence

- AFLB lock state: `unlocked`
- THLB lock state: `unlocked`
- Lock dependency: cutting the AFLB lock automatically invalidates the THLB lock because THLB is downstream from the AFLB universe definition.
- Current note: FEMIC now records benchmark ratios and runtime history for convergence review, but explicit user lock/cut-lock controls are not implemented yet.

## Interpretation

- Non-AFLB polygons are excluded from the reconstruction universe before THLB logic applies.
- Non-THLB polygons or fragments remain inside that working universe and are assigned THLB state downstream from AFLB initialization.
- GLB -> AFLB rows define the modeled universe, AFLB -> LHLB rows define legal harvestability, and LHLB -> THLB rows define projected operational harvestability.
- AU/VDYP-oriented filters are not assumed to be valid THLB filters unless the TSR logic says so explicitly.
- Legacy raster THLB values are reference-only in reconstructed mode.

## Stage-by-Stage THLB Steps

### GLB -> AFLB

### 2. Land not administered by the Province

- Parent step id: `thlb_parent_002_land_not_administered_by_the_province`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `697033.000 ha`
- Benchmark cumulative remaining area: `4236602.000 ha`
- Supporting prose section: `6.2.1 Land not administered by the Province for TSA timber supply`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=25`
- Draft subrules:
  - `thlb_parent_002_land_not_administered_by_the_province_draft_01` | summary=`Certain types of lands do not contribute to timber supply for the purpose of this timber supply analysis.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_02` | summary=`This includes privately held lands, First Nations reserves, some lands under the jurisdiction of the federal government and area-based forest tenures.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_03` | summary=`Parks and protected areas are included in the AFLB because they can be relied on to continually contribute to forest cover management objectives such as landscape-level biodiversit` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `ta_park_ecores_pa_svw`, `whse_land_use_planning_rmp_plan_legal_poly`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_04` | summary=`The CCLUP specifies that woodlots also contribute to landscape-level forest management objectives for biodiversity, although the AAC for these woodlots is determined under a separa` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_05` | summary=`Area-based licences such as community forest agreements and First Nations woodland licences (FNWL) are expected to manage for landscape-level biodiversity objectives within their t` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_admin_boundaries_fadm_tsa`, `whse_land_use_planning_fadm_designated`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_06` | summary=`Woodlots are not required to manage for landscape-level biodiversity objectives, so they are left in the AFLB and removed when defining the LHLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_rmp_plan_legal_poly`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_07` | summary=`The Northern Secwepemc te Qelmucw (NStQ) Treaty Negotiations Agreement in Principle was signed on July 22, 2018, and the Parties are in Stage 5 negotiations to conclude treaty.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tfl`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_08` | summary=`The NStQ Interim Treaty Agreement (ITA) Phase 1 land transfer parcels are no longer administered by the Province and will be excluded from the AFLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tfl`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_09` | summary=`Additional NStQ Agreement in Principle (AIP) lands which are detailed in the signed AIP may also be transferred soon.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_ste_ter`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_10` | summary=`The implications of these additional transfers to timber supply implications will be explored through sensitivity analysis.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_11` | summary=`On June 26, 2014, the Supreme Court of Canada (SCC) released its decision on Tsilhqot’in Nation v.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_pip_consultation`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_12` | summary=`British Columbia (Tsilhqot’in decision).` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_landscape_unit_svw`, `rmp_landscape_unit_svw_no_multiples`, `whse_land_use_planning_rmp_landscape_unit_svw`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_13` | summary=`In that decision the SCC outlined areas over which the Tsilhqot’in Nation has proven and declared Aboriginal title.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_pip_consultation`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_14` | summary=`Proven and declared Aboriginal title lands are not considered Crown land.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_crown_tenures_svw`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_15` | summary=`As such, those lands do not contribute to timber supply in the Williams Lake TSA and are excluded from the AFLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_16` | summary=`A spatial data set of land ownership was developed using information from the Crown Land Registry and the Integrated Cadastral Information Society.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_crown_tenures_svw`, `whse_tantalis_ta_crown_tenures_svw`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_17` | summary=`Areas classified in this data set with ownership codes 62 (Forest Management Unit) or 69 (Community Watershed) are generally administered by the Province for TSA timber supply.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_18` | summary=`These areas were reviewed by district staff to ensure all categories they contain can appropriately be considered AFLB for purposes of this analysis.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_19` | summary=`Minor areas, including those identified as development project, institutional and residential, were excluded from the AFLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_20` | summary=`Otherwise, the remaining area with these ownership codes will be modelled as managed for TSA timber supply.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_21` | summary=`Areas classified with ownership code 99 (crown leases) are not generally managed for TSA timber supply but were similarly reviewed prior to this analysis.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_crown_tenures_svw`, `whse_tantalis_ta_crown_tenures_svw`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_22` | summary=`Minor areas, including those categorized as grazing leases, will be considered as contributing to TSA timber supply because harvesting that occurs on these lease areas contributes ` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_23` | summary=`Land ownership types Land ownership type Total area Area excluded Private 186,582 186,582 Federal 71,825 71,825 CFA and FNWL 244,692 244,692 Municipal and Leases 2,688 2,688 NStQ I` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
- Compiled logic:

### 2. Land not administered by the Province

- Step id: `thlb_parent_002_land_not_administered_by_the_province_compiled_01`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `applied`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=25`
- TSR page: `25`
- TSR text: `Certain types of lands do not contribute to timber supply for the purpose of this timber supply analysis. This includes privately held lands, First Nations reserves, some lands under the jurisdiction of the federal government and area-based forest tenures. Parks and protected areas are included in the AFLB because they can be relied on to continually contribute to forest cover management objectives such as landscape-level biodiversity, visual quality, and wildlife habitat objectives. The CCLUP specifies that woodlots also contribute to landscape-level forest management objectives for biodiversity, although the AAC for these woodlots is determined under a separate process. Area-based licences such as community forest agreements and First Nations woodland licences (FNWL) are expected to manage for landscape-level biodiversity objectives within their tenured areas, therefore they are removed from the AFLB. Woodlots are not required to manage for landscape-level biodiversity objectives, so they are left in the AFLB and removed when defining the LHLB. The Northern Secwepemc te Qelmucw (NStQ) Treaty Negotiations Agreement in Principle was signed on July 22, 2018, and the Parties are in Stage 5 negotiations to conclude treaty. The NStQ Interim Treaty Agreement (ITA) Phase 1 land transfer parcels are no longer administered by the Province and will be excluded from the AFLB. Additional NStQ Agreement in Principle (AIP) lands which are detailed in the signed AIP may also be transferred soon. The implications of these additional transfers to timber supply implications will be explored through sensitivity analysis. On June 26, 2014, the Supreme Court of Canada (SCC) released its decision on Tsilhqot’in Nation v. British Columbia (Tsilhqot’in decision). In that decision the SCC outlined areas over which the Tsilhqot’in Nation has proven and declared Aboriginal title. Proven and declared Aboriginal title lands are not considered Crown land. As such, those lands do not contribute to timber supply in the Williams Lake TSA and are excluded from the AFLB. A spatial data set of land ownership was developed using information from the Crown Land Registry and the Integrated Cadastral Information Society. Areas classified in this data set with ownership codes 62 (Forest Management Unit) or 69 (Community Watershed) are generally administered by the Province for TSA timber supply. These areas were reviewed by district staff to ensure all categories they contain can appropriately be considered AFLB for purposes of this analysis. Minor areas, including those identified as development project, institutional and residential, were excluded from the AFLB. Otherwise, the remaining area with these ownership codes will be modelled as managed for TSA timber supply. Areas classified with ownership code 99 (crown leases) are not generally managed for TSA timber supply but were similarly reviewed prior to this analysis. Minor areas, including those categorized as grazing leases, will be considered as contributing to TSA timber supply because harvesting that occurs on these lease areas contributes to the TSA harvest level. Table 4. Land ownership types Land ownership type Total area Area excluded Private 186,582 186,582 Federal 71,825 71,825 CFA and FNWL 244,692 244,692 Municipal and Leases 2,688 2,688 NStQ Interim Treaty Agreement 2,796 2,702 Tsilhqot’in Nation Title 193,216 188,544 Data source and comments: WHSE_FOREST_VEGETATION.F_OWN`
- FEMIC proposed logic: Overlay the linked polygon layers onto the working land base, fragment intersected geometry, and assign binary THLB {0,1} so excluded fragments are 0 and retained fragments remain 1.
- Linked source layers:
  - `rmp_landscape_unit_svw` | query=`RMP_LANDSCAPE_UNIT_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_LANDSCAPE_UNIT_SVW/RMP_LANDSCAPE_UNIT_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_LANDSCAPE_UNIT_SVW`
    - top match: `Landscape Units of British Columbia - Current`
  - `rmp_landscape_unit_svw_no_multiples` | query=`RMP_LANDSCAPE_UNIT_SVW_NO_MULTIPLES` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_LANDSCAPE_UNIT_SVW_NO_MULTIPLES/RMP_LANDSCAPE_UNIT_SVW_NO_MULTIPLES.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_LANDSCAPE_UNIT_SVW`
    - top match: `Landscape Units of British Columbia - Current`
  - `ta_park_ecores_pa_svw` | query=`TA_PARK_ECORES_PA_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/TA_PARK_ECORES_PA_SVW/TA_PARK_ECORES_PA_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW`
    - top match: `BC Parks, Ecological Reserves, and Protected Areas`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `rmp_landscape_unit_svw`
- Run notes:
  - Applied fragment/resultant exclusion with binary THLB output in EPSG:3005.

### 3. Non-forest

- Parent step id: `thlb_parent_003_non_forest`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `1105908.000 ha`
- Benchmark cumulative remaining area: `3130694.000 ha`
- Supporting prose section: `6.2.2 Land classified as non-forest`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=26`
- Draft subrules:
  - `thlb_parent_003_non_forest_draft_01` | summary=`All land classified as non-forest (alpine, lakes, swamp, brush, rock, etc.), non-productive forest (e.g., wetlands and avalanche tracks), or not typed (unreported) are excluded fro` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_003_non_forest_draft_02` | summary=`These areas do not contribute to forest management objectives such as seral objectives for landscape-level biodiversity.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `rmp_plan_non_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly`
  - `thlb_parent_003_non_forest_draft_03` | summary=`The VRI attribute ‘Forest Management Land Base’ (FMLB) will be used to identify areas of non-forest.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`, `whse_land_use_planning_rmp_plan_non_legal_poly_svw`
  - `thlb_parent_003_non_forest_draft_04` | summary=`The FMLB attribute categorizes land as forested if it is described as ‘treed’ under the British Columbia Land Cover Classification Scheme (BCLCS) and has a site index greater than ` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_landscape_unit_svw`, `rmp_landscape_unit_svw_no_multiples`, `whse_forest_vegetation_rslt_forest`
  - `thlb_parent_003_non_forest_draft_05` | summary=`Where the VRI has no data for site index or species composition, and no history of harvest, the area will be considered non-forest.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_003_non_forest_draft_06` | summary=`In addition to the FMLB criteria, areas with a crown closure less than 10% also be considered non-forest and will be excluded.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`, `whse_land_use_planning_rmp_plan_non_legal_poly_svw`
  - `thlb_parent_003_non_forest_draft_07` | summary=`Areas with low crown closure resulting from past harvest, losses from MPB (since 2002) or recent fire (since 2017) are exceptions that will remain in the AFLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`, `whse_land_use_planning_rmp_plan_non_legal_poly_svw`
  - `thlb_parent_003_non_forest_draft_08` | summary=`A final check will use data from the Freshwater Atlas (FWA) data to ensure lakes, rivers and wetlands are appropriately excluded.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_fwa_lakes_poly`
  - `thlb_parent_003_non_forest_draft_09` | summary=`Land classified as non-forest Attributes Description Logging history Total area (hectares) Missing leading species and site index VRI leading species and site index are none, while` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`, `consolidated_cutblocks_2020`
  - `thlb_parent_003_non_forest_draft_10` | summary=`There are no instances of treed alpine areas within the TSA.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`, `whse_land_use_planning_rmp_plan_non_legal_poly_svw`
  - `thlb_parent_003_non_forest_draft_11` | summary=`Treed wetlands are removed in the riparian reserve and riparian management zones netdown.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`
- Compiled logic:

### 3. Non-forest

- Step id: `thlb_parent_003_non_forest_compiled_01`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=26`
- TSR page: `26`
- TSR text: `All land classified as non-forest (alpine, lakes, swamp, brush, rock, etc.), non-productive forest (e.g., wetlands and avalanche tracks), or not typed (unreported) are excluded from the AFLB, unless they were harvested in the past. These areas do not contribute to forest management objectives such as seral objectives for landscape-level biodiversity. The VRI attribute ‘Forest Management Land Base’ (FMLB) will be used to identify areas of non-forest. The FMLB attribute categorizes land as forested if it is described as ‘treed’ under the British Columbia Land Cover Classification Scheme (BCLCS) and has a site index greater than or equal to five metres. Where the VRI has no data for site index or species composition, and no history of harvest, the area will be considered non-forest. In addition to the FMLB criteria, areas with a crown closure less than 10% also be considered non-forest and will be excluded. Areas with low crown closure resulting from past harvest, losses from MPB (since 2002) or recent fire (since 2017) are exceptions that will remain in the AFLB. A final check will use data from the Freshwater Atlas (FWA) data to ensure lakes, rivers and wetlands are appropriately excluded. Table 5. Land classified as non-forest Attributes Description Logging history Total area (hectares) Missing leading species and site index VRI leading species and site index are none, while FMLB = ‘Y’ No 9,374 Wetlands VRI FMLB defined as ‘Y’ No 50,191 Lakes VRI FMLB defined as ‘Y’ No 4,455 Rivers VRI FMLB defined as ‘Y’ No 741 Crown closure < 10% VRI FMLB defined as ‘Y’ No 4,413 Non-FMLB VRI FMLB defined as ‘N’ No 976,656 Data source and comments: Areas with a harvest history are identified using the consolidated harvest depletion layer produced by FAIB. There are no instances of treed alpine areas within the TSA. Treed wetlands are removed in the riparian reserve and riparian management zones netdown.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_basemapping_fwa_lakes_poly` | query=`WHSE_BASEMAPPING.FWA_LAKES_POLY` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_FWA_LAKES_POLY/WHSE_BASEMAPPING_FWA_LAKES_POLY.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.FWA_LAKES_POLY`
    - top match: `Freshwater Atlas Lakes`
- Logic mode: `femic_core`
- Run notes:
  - No active land-base geometries intersected the exclusion mask.

### 4. Roads and landings

- Parent step id: `thlb_parent_004_roads_and_landings`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `50434.000 ha`
- Benchmark cumulative remaining area: `3080260.000 ha`
- Supporting prose section: `6.2.3 Roads and landings`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- Draft subrules:
  - `thlb_parent_004_roads_and_landings_draft_01` | summary=`The purpose of this section is to identify the portion of the land base that is occupied by roads, trails, and landings (RTL) that have been constructed to access and facilitate ha` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_004_roads_and_landings_draft_02` | summary=`The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_004_roads_and_landings_draft_03` | summary=`Separate estimates are made to reflect the loss in productive forest land due to existing and future RTL.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_004_roads_and_landings_draft_04` | summary=`Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially ` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_05` | summary=`To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these ` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_004_roads_and_landings_draft_06` | summary=`Forest service roads and public roads were buffered 25 metres (12.5 metres from center line) and active/retired road permit roads were buffered 15 metres (7.5 metres from center li` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_forest_tenure_ften_road_lines`, `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_004_roads_and_landings_draft_07` | summary=`The mapped non-status roads are known to be inaccurate, and the information is incomplete.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_08` | summary=`Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-sta` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_09` | summary=`The estimated area within existing RTL maintained clearing widths is categorized below.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_004_roads_and_landings_draft_10` | summary=`On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_11` | summary=`They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_004_roads_and_landings_draft_12` | summary=`Width and area of existing road to calculate reductions Road class Width (m) Hectares Forest Service roads 25 8,343 Ministry of Transportation and Infrastructure 25 6,280 Road perm` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`, `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_004_roads_and_landings_draft_13` | summary=`There are indications that some productivity loss is associated with the use of roadside harvesting systems, but no definitive research to date has quantified a level of productivi` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_004_roads_and_landings_draft_14` | summary=`In-block roads that are temporary in nature will have no deduction from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_004_roads_and_landings_draft_15` | summary=`In total, 32 526 hectares will be excluded for all roads.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_004_roads_and_landings_draft_16` | summary=`Future roads, trails and landings The AFLB area removed to account for future RTL was estimated based on current performance and RESULTS data.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_004_roads_and_landings_draft_17` | summary=`The future RTL reduction will be applied to future harvested areas in the timber supply model after stands are harvested for the first time.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`, `consolidated_cutblocks_2020`, `veg_consolidated_cut_blocks_sp`
  - `thlb_parent_004_roads_and_landings_draft_18` | summary=`Reduction factors for future RTL were calculated based on the average amount of on-block road permit structures with an estimated 15 metres width that have been observed in the fiv` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_19` | summary=`The average factor is 2.28% for all three Cariboo TSAs.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_004_roads_and_landings_draft_20` | summary=`The yields of all stands aged 70 years and above will be reduced by this factor after they are harvested.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_004_roads_and_landings_draft_21` | summary=`In total, 22 754 hectares will be excluded from the forested land base at the time of first harvest to represent the area lost due to future road development.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_22` | summary=`Data source and comments: Roads will be identified from forest tenure road mapping as roads with a description of ‘Forest Service Road’ or ‘Road Permit’ and have a status of ‘activ` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_forest_tenure_ften_road_lines`
  - `thlb_parent_004_roads_and_landings_draft_23` | summary=`Digital road atlas mapping will also be used but will exclude roads classed as ‘resource’.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`, `whse_basemapping_dra_digital_road_atlas_line_sp`
  - `thlb_parent_004_roads_and_landings_draft_24` | summary=`The last five years of road construction in recent cutblocks were examined using existing road permit data for all three TSAs in the CNRR.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_25` | summary=`Road lengths were derived from the following data sets from the BCGW.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_26` | summary=`FSR 25 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Public 25 m WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP Road permit 15 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTIO` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_004_roads_and_landings_draft_27` | summary=`This means if a public road overlaps with any other type of road the area will be allocated to the public road.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_004_roads_and_landings_draft_28` | summary=`Removed all roads that fall over managed licences, tree farms, private, federal, and municipal lands.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_managed_lic`, `ften_managed_lic_poly_svw`, `whse_forest_tenure_ften_managed_lic`
  - `thlb_parent_004_roads_and_landings_draft_29` | summary=`6.3 Identification of the legally harvestable land base The LHLB is the portion of the AFLB where timber harvesting is legal, subject to forest management objectives and constraint` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal`, `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal`
  - `thlb_parent_004_roads_and_landings_draft_30` | summary=`It excludes protected areas such as national parks, provincial parks, protected areas and legally established areas where timber harvesting is prohibited.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_park_ecores_pa_svw`, `whse_tantalis_ta_park_ecores_pa_svw`
  - `thlb_parent_004_roads_and_landings_draft_31` | summary=`Areas excluded from the LHLB are also excluded from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
- Compiled logic:

### 4. Roads and landings

- Step id: `thlb_parent_004_roads_and_landings_compiled_01`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- TSR page: `27`
- TSR text: `The purpose of this section is to identify the portion of the land base that is occupied by roads, trails, and landings (RTL) that have been constructed to access and facilitate harvest operations. The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives. Separate estimates are made to reflect the loss in productive forest land due to existing and future RTL. Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially through partial reductions to the AFLB (i.e., the area considered to be AFLB within each hectare will be reduced by a percentage). To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these access features. Forest service roads and public roads were buffered 25 metres (12.5 metres from center line) and active/retired road permit roads were buffered 15 metres (7.5 metres from center line). The mapped non-status roads are known to be inaccurate, and the information is incomplete. Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-status roads will not impact future yield. The estimated area within existing RTL maintained clearing widths is categorized below. On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations. They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate. Table 6. Width and area of existing road to calculate reductions Road class Width (m) Hectares Forest Service roads 25 8,343 Ministry of Transportation and Infrastructure 25 6,280 Road permit and landings 15 19,641 Mapped non-status roads 5 16,169 Most harvesting now uses a roadside processing system, and landings are less common in current harvest systems. There are indications that some productivity loss is associated with the use of roadside harvesting systems, but no definitive research to date has quantified a level of productivity loss. In-block roads that are temporary in nature will have no deduction from the THLB. In total, 32 526 hectares will be excluded for all roads. Future roads, trails and landings The AFLB area removed to account for future RTL was estimated based on current performance and RESULTS data. The future RTL reduction will be applied to future harvested areas in the timber supply model after stands are harvested for the first time. Reduction factors for future RTL were calculated based on the average amount of on-block road permit structures with an estimated 15 metres width that have been observed in the five-year period from January 2015 to April 2021. The average factor is 2.28% for all three Cariboo TSAs. The yields of all stands aged 70 years and above will be reduced by this factor after they are harvested. In total, 22 754 hectares will be excluded from the forested land base at the time of first harvest to represent the area lost due to future road development. Data source and comments: Roads will be identified from forest tenure road mapping as roads with a description of ‘Forest Service Road’ or ‘Road Permit’ and have a status of ‘active’, ‘retired’ or ‘pending’. Digital road atlas mapping will also be used but will exclude roads classed as ‘resource’. The last five years of road construction in recent cutblocks were examined using existing road permit data for all three TSAs in the CNRR. Road lengths were derived from the following data sets from the BCGW. FSR 25 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Public 25 m WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP Road permit 15 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Non-status 5 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (Outside of cutblocks) On-block roads (temporary) 0 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (roads that are inside cutblocks harvested from 2015 to present using WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP) Note: Because there is overlap between the different types of roads, the following priority was used: public, FSR, permit, non-status. This means if a public road overlaps with any other type of road the area will be allocated to the public road. Removed all roads that fall over managed licences, tree farms, private, federal, and municipal lands. 6.3 Identification of the legally harvestable land base The LHLB is the portion of the AFLB where timber harvesting is legal, subject to forest management objectives and constraints. It excludes protected areas such as national parks, provincial parks, protected areas and legally established areas where timber harvesting is prohibited. Areas excluded from the LHLB are also excluded from the THLB.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_basemapping_dra_dgtl_road_atlas_mpar_sp` | query=`WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP`
    - top match: `Digital Road Atlas (DRA) - Master Partially-Attributed Roads`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 5. Analysis forest land base

- Parent step id: `thlb_parent_005_analysis_forest_land_base`
- Stage: `GLB -> AFLB`
- Execution class: `reference_only`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark cumulative remaining area: `3098168.000 ha`
- Supporting prose section: `6.2.1 Land not administered by the Province for TSA timber supply`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=25`
- Draft subrules:
  - `thlb_parent_005_analysis_forest_land_base_draft_01` | summary=`Certain types of lands do not contribute to timber supply for the purpose of this timber supply analysis.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_005_analysis_forest_land_base_draft_02` | summary=`This includes privately held lands, First Nations reserves, some lands under the jurisdiction of the federal government and area-based forest tenures.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_005_analysis_forest_land_base_draft_03` | summary=`Parks and protected areas are included in the AFLB because they can be relied on to continually contribute to forest cover management objectives such as landscape-level biodiversit` | operation=`reference_only` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `ta_park_ecores_pa_svw`, `whse_land_use_planning_rmp_plan_legal_poly`
  - `thlb_parent_005_analysis_forest_land_base_draft_04` | summary=`The CCLUP specifies that woodlots also contribute to landscape-level forest management objectives for biodiversity, although the AAC for these woodlots is determined under a separa` | operation=`reference_only` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
  - `thlb_parent_005_analysis_forest_land_base_draft_05` | summary=`Area-based licences such as community forest agreements and First Nations woodland licences (FNWL) are expected to manage for landscape-level biodiversity objectives within their t` | operation=`reference_only` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_admin_boundaries_fadm_tsa`, `whse_land_use_planning_fadm_designated`
  - `thlb_parent_005_analysis_forest_land_base_draft_06` | summary=`Woodlots are not required to manage for landscape-level biodiversity objectives, so they are left in the AFLB and removed when defining the LHLB.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_land_use_planning_rmp_plan_legal_poly`
  - `thlb_parent_005_analysis_forest_land_base_draft_07` | summary=`The Northern Secwepemc te Qelmucw (NStQ) Treaty Negotiations Agreement in Principle was signed on July 22, 2018, and the Parties are in Stage 5 negotiations to conclude treaty.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tfl`
  - `thlb_parent_005_analysis_forest_land_base_draft_08` | summary=`The NStQ Interim Treaty Agreement (ITA) Phase 1 land transfer parcels are no longer administered by the Province and will be excluded from the AFLB.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tfl`
  - `thlb_parent_005_analysis_forest_land_base_draft_09` | summary=`Additional NStQ Agreement in Principle (AIP) lands which are detailed in the signed AIP may also be transferred soon.` | operation=`reference_only` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_ste_ter`
  - `thlb_parent_005_analysis_forest_land_base_draft_10` | summary=`The implications of these additional transfers to timber supply implications will be explored through sensitivity analysis.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_005_analysis_forest_land_base_draft_11` | summary=`On June 26, 2014, the Supreme Court of Canada (SCC) released its decision on Tsilhqot’in Nation v.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_pip_consultation`
  - `thlb_parent_005_analysis_forest_land_base_draft_12` | summary=`British Columbia (Tsilhqot’in decision).` | operation=`reference_only` | review=`draft`
    - candidate layers: `rmp_landscape_unit_svw`, `rmp_landscape_unit_svw_no_multiples`, `whse_land_use_planning_rmp_landscape_unit_svw`
  - `thlb_parent_005_analysis_forest_land_base_draft_13` | summary=`In that decision the SCC outlined areas over which the Tsilhqot’in Nation has proven and declared Aboriginal title.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_pip_consultation`
  - `thlb_parent_005_analysis_forest_land_base_draft_14` | summary=`Proven and declared Aboriginal title lands are not considered Crown land.` | operation=`reference_only` | review=`draft`
    - candidate layers: `ta_crown_tenures_svw`
  - `thlb_parent_005_analysis_forest_land_base_draft_15` | summary=`As such, those lands do not contribute to timber supply in the Williams Lake TSA and are excluded from the AFLB.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_005_analysis_forest_land_base_draft_16` | summary=`A spatial data set of land ownership was developed using information from the Crown Land Registry and the Integrated Cadastral Information Society.` | operation=`reference_only` | review=`draft`
    - candidate layers: `ta_crown_tenures_svw`, `whse_tantalis_ta_crown_tenures_svw`
  - `thlb_parent_005_analysis_forest_land_base_draft_17` | summary=`Areas classified in this data set with ownership codes 62 (Forest Management Unit) or 69 (Community Watershed) are generally administered by the Province for TSA timber supply.` | operation=`reference_only` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_005_analysis_forest_land_base_draft_18` | summary=`These areas were reviewed by district staff to ensure all categories they contain can appropriately be considered AFLB for purposes of this analysis.` | operation=`reference_only` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_005_analysis_forest_land_base_draft_19` | summary=`Minor areas, including those identified as development project, institutional and residential, were excluded from the AFLB.` | operation=`reference_only` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_005_analysis_forest_land_base_draft_20` | summary=`Otherwise, the remaining area with these ownership codes will be modelled as managed for TSA timber supply.` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_005_analysis_forest_land_base_draft_21` | summary=`Areas classified with ownership code 99 (crown leases) are not generally managed for TSA timber supply but were similarly reviewed prior to this analysis.` | operation=`reference_only` | review=`draft`
    - candidate layers: `ta_crown_tenures_svw`, `whse_tantalis_ta_crown_tenures_svw`
  - `thlb_parent_005_analysis_forest_land_base_draft_22` | summary=`Minor areas, including those categorized as grazing leases, will be considered as contributing to TSA timber supply because harvesting that occurs on these lease areas contributes ` | operation=`reference_only` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_005_analysis_forest_land_base_draft_23` | summary=`Land ownership types Land ownership type Total area Area excluded Private 186,582 186,582 Federal 71,825 71,825 CFA and FNWL 244,692 244,692 Municipal and Leases 2,688 2,688 NStQ I` | operation=`reference_only` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
- Compiled logic:

### 5. Analysis forest land base

- Step id: `thlb_parent_005_analysis_forest_land_base_compiled_01`
- Kind: `reference_target`
- Stage: `GLB -> AFLB`
- Execution class: `reference_only`
- Run status: `unsupported`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=25`
- TSR page: `25`
- TSR text: `Certain types of lands do not contribute to timber supply for the purpose of this timber supply analysis. This includes privately held lands, First Nations reserves, some lands under the jurisdiction of the federal government and area-based forest tenures. Parks and protected areas are included in the AFLB because they can be relied on to continually contribute to forest cover management objectives such as landscape-level biodiversity, visual quality, and wildlife habitat objectives. The CCLUP specifies that woodlots also contribute to landscape-level forest management objectives for biodiversity, although the AAC for these woodlots is determined under a separate process. Area-based licences such as community forest agreements and First Nations woodland licences (FNWL) are expected to manage for landscape-level biodiversity objectives within their tenured areas, therefore they are removed from the AFLB. Woodlots are not required to manage for landscape-level biodiversity objectives, so they are left in the AFLB and removed when defining the LHLB. The Northern Secwepemc te Qelmucw (NStQ) Treaty Negotiations Agreement in Principle was signed on July 22, 2018, and the Parties are in Stage 5 negotiations to conclude treaty. The NStQ Interim Treaty Agreement (ITA) Phase 1 land transfer parcels are no longer administered by the Province and will be excluded from the AFLB. Additional NStQ Agreement in Principle (AIP) lands which are detailed in the signed AIP may also be transferred soon. The implications of these additional transfers to timber supply implications will be explored through sensitivity analysis. On June 26, 2014, the Supreme Court of Canada (SCC) released its decision on Tsilhqot’in Nation v. British Columbia (Tsilhqot’in decision). In that decision the SCC outlined areas over which the Tsilhqot’in Nation has proven and declared Aboriginal title. Proven and declared Aboriginal title lands are not considered Crown land. As such, those lands do not contribute to timber supply in the Williams Lake TSA and are excluded from the AFLB. A spatial data set of land ownership was developed using information from the Crown Land Registry and the Integrated Cadastral Information Society. Areas classified in this data set with ownership codes 62 (Forest Management Unit) or 69 (Community Watershed) are generally administered by the Province for TSA timber supply. These areas were reviewed by district staff to ensure all categories they contain can appropriately be considered AFLB for purposes of this analysis. Minor areas, including those identified as development project, institutional and residential, were excluded from the AFLB. Otherwise, the remaining area with these ownership codes will be modelled as managed for TSA timber supply. Areas classified with ownership code 99 (crown leases) are not generally managed for TSA timber supply but were similarly reviewed prior to this analysis. Minor areas, including those categorized as grazing leases, will be considered as contributing to TSA timber supply because harvesting that occurs on these lease areas contributes to the TSA harvest level. Table 4. Land ownership types Land ownership type Total area Area excluded Private 186,582 186,582 Federal 71,825 71,825 CFA and FNWL 244,692 244,692 Municipal and Leases 2,688 2,688 NStQ Interim Treaty Agreement 2,796 2,702 Tsilhqot’in Nation Title 193,216 188,544 Data source and comments: WHSE_FOREST_VEGETATION.F_OWN`
- FEMIC proposed logic: No executable logic has been normalized for this row yet.
- Linked source layers:
  - `rmp_landscape_unit_svw` | query=`RMP_LANDSCAPE_UNIT_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_LANDSCAPE_UNIT_SVW/RMP_LANDSCAPE_UNIT_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_LANDSCAPE_UNIT_SVW`
    - top match: `Landscape Units of British Columbia - Current`
  - `rmp_landscape_unit_svw_no_multiples` | query=`RMP_LANDSCAPE_UNIT_SVW_NO_MULTIPLES` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_LANDSCAPE_UNIT_SVW_NO_MULTIPLES/RMP_LANDSCAPE_UNIT_SVW_NO_MULTIPLES.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_LANDSCAPE_UNIT_SVW`
    - top match: `Landscape Units of British Columbia - Current`
  - `ta_park_ecores_pa_svw` | query=`TA_PARK_ECORES_PA_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/TA_PARK_ECORES_PA_SVW/TA_PARK_ECORES_PA_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW`
    - top match: `BC Parks, Ecological Reserves, and Protected Areas`
- Logic mode: `femic_core`
- Run notes:
  - Normalized action `reference_target` is not executable in v1.

### 23. Future roads

- Parent step id: `thlb_parent_023_future_roads`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Supporting prose section: `6.2.3 Roads and landings`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- Draft subrules:
  - `thlb_parent_023_future_roads_draft_01` | summary=`The purpose of this section is to identify the portion of the land base that is occupied by roads, trails, and landings (RTL) that have been constructed to access and facilitate ha` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_023_future_roads_draft_02` | summary=`The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_023_future_roads_draft_03` | summary=`Separate estimates are made to reflect the loss in productive forest land due to existing and future RTL.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_023_future_roads_draft_04` | summary=`Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially ` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_05` | summary=`To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these ` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_023_future_roads_draft_06` | summary=`Forest service roads and public roads were buffered 25 metres (12.5 metres from center line) and active/retired road permit roads were buffered 15 metres (7.5 metres from center li` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_forest_tenure_ften_road_lines`, `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_023_future_roads_draft_07` | summary=`The mapped non-status roads are known to be inaccurate, and the information is incomplete.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_08` | summary=`Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-sta` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_09` | summary=`The estimated area within existing RTL maintained clearing widths is categorized below.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_023_future_roads_draft_10` | summary=`On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_11` | summary=`They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_023_future_roads_draft_12` | summary=`Width and area of existing road to calculate reductions Road class Width (m) Hectares Forest Service roads 25 8,343 Ministry of Transportation and Infrastructure 25 6,280 Road perm` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`, `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_023_future_roads_draft_13` | summary=`There are indications that some productivity loss is associated with the use of roadside harvesting systems, but no definitive research to date has quantified a level of productivi` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_023_future_roads_draft_14` | summary=`In-block roads that are temporary in nature will have no deduction from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_023_future_roads_draft_15` | summary=`In total, 32 526 hectares will be excluded for all roads.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_023_future_roads_draft_16` | summary=`Future roads, trails and landings The AFLB area removed to account for future RTL was estimated based on current performance and RESULTS data.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_023_future_roads_draft_17` | summary=`The future RTL reduction will be applied to future harvested areas in the timber supply model after stands are harvested for the first time.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`, `consolidated_cutblocks_2020`, `veg_consolidated_cut_blocks_sp`
  - `thlb_parent_023_future_roads_draft_18` | summary=`Reduction factors for future RTL were calculated based on the average amount of on-block road permit structures with an estimated 15 metres width that have been observed in the fiv` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_19` | summary=`The average factor is 2.28% for all three Cariboo TSAs.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`
  - `thlb_parent_023_future_roads_draft_20` | summary=`The yields of all stands aged 70 years and above will be reduced by this factor after they are harvested.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_023_future_roads_draft_21` | summary=`In total, 22 754 hectares will be excluded from the forested land base at the time of first harvest to represent the area lost due to future road development.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_22` | summary=`Data source and comments: Roads will be identified from forest tenure road mapping as roads with a description of ‘Forest Service Road’ or ‘Road Permit’ and have a status of ‘activ` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_forest_tenure_ften_road_lines`
  - `thlb_parent_023_future_roads_draft_23` | summary=`Digital road atlas mapping will also be used but will exclude roads classed as ‘resource’.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`, `whse_basemapping_dra_digital_road_atlas_line_sp`
  - `thlb_parent_023_future_roads_draft_24` | summary=`The last five years of road construction in recent cutblocks were examined using existing road permit data for all three TSAs in the CNRR.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_25` | summary=`Road lengths were derived from the following data sets from the BCGW.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_lines`, `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_26` | summary=`FSR 25 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Public 25 m WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP Road permit 15 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTIO` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
  - `thlb_parent_023_future_roads_draft_27` | summary=`This means if a public road overlaps with any other type of road the area will be allocated to the public road.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar`, `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_023_future_roads_draft_28` | summary=`Removed all roads that fall over managed licences, tree farms, private, federal, and municipal lands.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_managed_lic`, `ften_managed_lic_poly_svw`, `whse_forest_tenure_ften_managed_lic`
  - `thlb_parent_023_future_roads_draft_29` | summary=`6.3 Identification of the legally harvestable land base The LHLB is the portion of the AFLB where timber harvesting is legal, subject to forest management objectives and constraint` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal`, `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal`
  - `thlb_parent_023_future_roads_draft_30` | summary=`It excludes protected areas such as national parks, provincial parks, protected areas and legally established areas where timber harvesting is prohibited.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_park_ecores_pa_svw`, `whse_tantalis_ta_park_ecores_pa_svw`
  - `thlb_parent_023_future_roads_draft_31` | summary=`Areas excluded from the LHLB are also excluded from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
- Compiled logic:

### 23. Future roads

- Step id: `thlb_parent_023_future_roads_compiled_01`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- TSR page: `27`
- TSR text: `The purpose of this section is to identify the portion of the land base that is occupied by roads, trails, and landings (RTL) that have been constructed to access and facilitate harvest operations. The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives. Separate estimates are made to reflect the loss in productive forest land due to existing and future RTL. Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially through partial reductions to the AFLB (i.e., the area considered to be AFLB within each hectare will be reduced by a percentage). To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these access features. Forest service roads and public roads were buffered 25 metres (12.5 metres from center line) and active/retired road permit roads were buffered 15 metres (7.5 metres from center line). The mapped non-status roads are known to be inaccurate, and the information is incomplete. Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-status roads will not impact future yield. The estimated area within existing RTL maintained clearing widths is categorized below. On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations. They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate. Table 6. Width and area of existing road to calculate reductions Road class Width (m) Hectares Forest Service roads 25 8,343 Ministry of Transportation and Infrastructure 25 6,280 Road permit and landings 15 19,641 Mapped non-status roads 5 16,169 Most harvesting now uses a roadside processing system, and landings are less common in current harvest systems. There are indications that some productivity loss is associated with the use of roadside harvesting systems, but no definitive research to date has quantified a level of productivity loss. In-block roads that are temporary in nature will have no deduction from the THLB. In total, 32 526 hectares will be excluded for all roads. Future roads, trails and landings The AFLB area removed to account for future RTL was estimated based on current performance and RESULTS data. The future RTL reduction will be applied to future harvested areas in the timber supply model after stands are harvested for the first time. Reduction factors for future RTL were calculated based on the average amount of on-block road permit structures with an estimated 15 metres width that have been observed in the five-year period from January 2015 to April 2021. The average factor is 2.28% for all three Cariboo TSAs. The yields of all stands aged 70 years and above will be reduced by this factor after they are harvested. In total, 22 754 hectares will be excluded from the forested land base at the time of first harvest to represent the area lost due to future road development. Data source and comments: Roads will be identified from forest tenure road mapping as roads with a description of ‘Forest Service Road’ or ‘Road Permit’ and have a status of ‘active’, ‘retired’ or ‘pending’. Digital road atlas mapping will also be used but will exclude roads classed as ‘resource’. The last five years of road construction in recent cutblocks were examined using existing road permit data for all three TSAs in the CNRR. Road lengths were derived from the following data sets from the BCGW. FSR 25 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Public 25 m WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP Road permit 15 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Non-status 5 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (Outside of cutblocks) On-block roads (temporary) 0 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (roads that are inside cutblocks harvested from 2015 to present using WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP) Note: Because there is overlap between the different types of roads, the following priority was used: public, FSR, permit, non-status. This means if a public road overlaps with any other type of road the area will be allocated to the public road. Removed all roads that fall over managed licences, tree farms, private, federal, and municipal lands. 6.3 Identification of the legally harvestable land base The LHLB is the portion of the AFLB where timber harvesting is legal, subject to forest management objectives and constraints. It excludes protected areas such as national parks, provincial parks, protected areas and legally established areas where timber harvesting is prohibited. Areas excluded from the LHLB are also excluded from the THLB.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_basemapping_dra_dgtl_road_atlas_mpar_sp` | query=`WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP`
    - top match: `Digital Road Atlas (DRA) - Master Partially-Attributed Roads`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### AFLB -> LHLB

### 6. Parks, protected areas, area-base tenures

- Parent step id: `thlb_parent_006_parks_protected_areas_area_base_tenures`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `306327.000 ha`
- Benchmark cumulative remaining area: `2791841.000 ha`
- Supporting prose section: `6.3.1 Parks, protected areas, and small area-based tenures`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=28`
- Draft subrules:
  - `thlb_parent_006_parks_protected_areas_area_base_tenures_draft_01` | summary=`The parks, protected areas, and woodlots that were included in the AFLB to contribute to forest management objectives in the context of TSA timber supply, will be removed at this s` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_park_ecores_pa_svw`, `whse_tantalis_ta_park_ecores_pa_svw`
  - `thlb_parent_006_parks_protected_areas_area_base_tenures_draft_02` | summary=`A further check will be performed using current boundary mapping for woodlots, parks, and protected areas to ensure all areas were appropriately excluded.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_park_ecores_pa_svw`, `whse_tantalis_ta_park_ecores_pa_svw`
  - `thlb_parent_006_parks_protected_areas_area_base_tenures_draft_03` | summary=`Woodlots that are no longer active will be included in the LHLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_park_ecores_pa_svw`, `whse_tantalis_ta_park_ecores_pa_svw`
  - `thlb_parent_006_parks_protected_areas_area_base_tenures_draft_04` | summary=`Parks, protected areas, and small area-based tenures Designations Total (ha) Forested (ha) Excluded (ha) Conservancy areas 596,471 260,215 260,028 Wildlife management areas 521 221` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_park_ecores_pa_svw`, `whse_tantalis_ta_park_ecores_pa_svw`
- Compiled logic:

### 6. Parks, protected areas, area-base tenures

- Step id: `thlb_parent_006_parks_protected_areas_area_base_tenures_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=28`
- TSR page: `28`
- TSR text: `The parks, protected areas, and woodlots that were included in the AFLB to contribute to forest management objectives in the context of TSA timber supply, will be removed at this stage. A further check will be performed using current boundary mapping for woodlots, parks, and protected areas to ensure all areas were appropriately excluded. Woodlots that are no longer active will be included in the LHLB. Table 7. Parks, protected areas, and small area-based tenures Designations Total (ha) Forested (ha) Excluded (ha) Conservancy areas 596,471 260,215 260,028 Wildlife management areas 521 221 221 Heritage sites 106 81 78 Miscellaneous reserves 271,808 184,769 11,586 Woodlots 35,789 34,133 33,217 Crown and miscellaneous leases 31,049 24,842 1,197`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `ta_park_ecores_pa_svw` | query=`TA_PARK_ECORES_PA_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/TA_PARK_ECORES_PA_SVW/TA_PARK_ECORES_PA_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW`
    - top match: `BC Parks, Ecological Reserves, and Protected Areas`
  - `whse_tantalis_ta_park_ecores_pa_svw` | query=`WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_TANTALIS_TA_PARK_ECORES_PA_SVW/WHSE_TANTALIS_TA_PARK_ECORES_PA_SVW.gpkg`
    - matched by: `object_name:WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW`
    - top match: `BC Parks, Ecological Reserves, and Protected Areas`
- Logic mode: `femic_core`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### 7. Old growth management areas

- Parent step id: `thlb_parent_007_old_growth_management_areas`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `210719.000 ha`
- Benchmark cumulative remaining area: `2581122.000 ha`
- Supporting prose section: `6.3.2 Old growth management areas`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- Draft subrules:
  - `thlb_parent_007_old_growth_management_areas_draft_01` | summary=`Permanent and Permanent-Rotating Old Growth Management Areas (OGMA) are removed from the LHLB as no harvest areas.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `rmp_ogma_legal_current_svw`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_02` | summary=`A limited amount of harvest is permitted in OGMAs for specified exceptions including insect control and wildfire risk reduction treatments.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_03` | summary=`Loss of OGMAs for other reasons such as Land Act tenure overlap must be replaced with equivalent area in the same BEC subzone within the same landscape unit.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_04` | summary=`This replacement process ensures that OGMA targets are maintained over time and result in no impact to timber supply.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `rmp_ogma_legal_current_svw`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_05` | summary=`Transition OGMAs will cease to exist in 2030.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_06` | summary=`Until then they are available for harvest if conifer mortality exceeds 50%.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `rmp_ogma_legal_current_svw`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_07` | summary=`It is assumed that any such harvest has already occurred in Transition OGMAs, therefore Transition OGMAs will be removed from the LHLB until 2030 after which they will be fully res` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_08` | summary=`Old growth management areas Designations Total (ha) Forested (ha) Excluded (ha) Permanent and rotating 292,759 211,183 210,719 Transitional 105,888 80,835` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `rmp_ogma_legal_current_svw`, `whse_land_use_planning_rmp_ogma_legal`
- Compiled logic:

### 7. Old growth management areas

- Step id: `thlb_parent_007_old_growth_management_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- TSR page: `29`
- TSR text: `Permanent and Permanent-Rotating Old Growth Management Areas (OGMA) are removed from the LHLB as no harvest areas. A limited amount of harvest is permitted in OGMAs for specified exceptions including insect control and wildfire risk reduction treatments. Loss of OGMAs for other reasons such as Land Act tenure overlap must be replaced with equivalent area in the same BEC subzone within the same landscape unit. This replacement process ensures that OGMA targets are maintained over time and result in no impact to timber supply. Transition OGMAs will cease to exist in 2030. Until then they are available for harvest if conifer mortality exceeds 50%. It is assumed that any such harvest has already occurred in Transition OGMAs, therefore Transition OGMAs will be removed from the LHLB until 2030 after which they will be fully restored to the LHLB. Table 8. Old growth management areas Designations Total (ha) Forested (ha) Excluded (ha) Permanent and rotating 292,759 211,183 210,719 Transitional 105,888 80,835`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `rmp_ogma_legal` | query=`RMP_OGMA_LEGAL` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_OGMA_LEGAL/RMP_OGMA_LEGAL.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_OGMA_LEGAL_CURRENT_SVW`
    - top match: `Old Growth Management Areas - Legal - Current`
  - `whse_land_use_planning_rmp_ogma_legal` | query=`WHSE_LAND_USE_PLANNING.RMP_OGMA_LEGAL` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_OGMA_LEGAL/WHSE_LAND_USE_PLANNING_RMP_OGMA_LEGAL.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_OGMA_LEGAL_CURRENT_SVW`
    - top match: `Old Growth Management Areas - Legal - Current`
- Logic mode: `femic_core`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### 8. Wildlife habitat areas

- Parent step id: `thlb_parent_008_wildlife_habitat_areas`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `154056.000 ha`
- Benchmark cumulative remaining area: `2427066.000 ha`
- Supporting prose section: `6.3.3 Wildlife habitat areas`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- Draft subrules:
  - `thlb_parent_008_wildlife_habitat_areas_draft_01` | summary=`Wildlife habitat reductions may be identified and managed through several processes including the Identified Wildlife Management Strategy, identification, and approval of ungulate ` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `wcp_ungulate_winter_range`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
  - `thlb_parent_008_wildlife_habitat_areas_draft_02` | summary=`Management practices may include no harvesting in core areas as well as modified harvesting in associated management zones.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_008_wildlife_habitat_areas_draft_03` | summary=`Several approved wildlife habitat areas (WHA) are designated within the CNRR.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_008_wildlife_habitat_areas_draft_04` | summary=`The associated General Wildlife Measures (GWM) established by ministerial order under the GARs guide harvest practices in WHAs.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_wildlife_management_wcp_wildlife`
  - `thlb_parent_008_wildlife_habitat_areas_draft_05` | summary=`Areas designated through GWMs as “no harvest” will be excluded from the LHLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_008_wildlife_habitat_areas_draft_06` | summary=`Areas designated as “conditional harvest zone” will be addressed in Section 7 – ‘Current forest management assumptions’ and Section 7.1.8 – ‘Silviculture systems’.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_008_wildlife_habitat_areas_draft_07` | summary=`Wildlife habitat areas Designations Total (ha) Forested (ha) Excluded (ha) UWR no-harvest area 25 23 23 Caribou no-harvest area 208,868 163,217 154,033 There is a Caribou Herd Plan` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_008_wildlife_habitat_areas_draft_08` | summary=`The outcome of additional area protection through no harvest or modified harvest resulting from this process are currently unknown.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_008_wildlife_habitat_areas_draft_09` | summary=`There may potentially be additional protections put in place for caribou that will have a downward pressure on the timber supply.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_008_wildlife_habitat_areas_draft_10` | summary=`Ministry staff will stay informed on the progress of this working group and inform the TSR throughout the process.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
- Compiled logic:

### 8. Wildlife habitat areas

- Step id: `thlb_parent_008_wildlife_habitat_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- TSR page: `29`
- TSR text: `Wildlife habitat reductions may be identified and managed through several processes including the Identified Wildlife Management Strategy, identification, and approval of ungulate winter range (UWR), and management practices specified in plans such as the CCLUP that establish legal wildlife habitat objectives. Management practices may include no harvesting in core areas as well as modified harvesting in associated management zones. Several approved wildlife habitat areas (WHA) are designated within the CNRR. The associated General Wildlife Measures (GWM) established by ministerial order under the GARs guide harvest practices in WHAs. Areas designated through GWMs as “no harvest” will be excluded from the LHLB. Areas designated as “conditional harvest zone” will be addressed in Section 7 – ‘Current forest management assumptions’ and Section 7.1.8 – ‘Silviculture systems’. Table 9. Wildlife habitat areas Designations Total (ha) Forested (ha) Excluded (ha) UWR no-harvest area 25 23 23 Caribou no-harvest area 208,868 163,217 154,033 There is a Caribou Herd Planning process currently ongoing within the CNRR. The outcome of additional area protection through no harvest or modified harvest resulting from this process are currently unknown. There may potentially be additional protections put in place for caribou that will have a downward pressure on the timber supply. Ministry staff will stay informed on the progress of this working group and inform the TSR throughout the process.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `wcp_ungulate_winter_range` | query=`WCP_UNGULATE_WINTER_RANGE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WCP_UNGULATE_WINTER_RANGE/WCP_UNGULATE_WINTER_RANGE.gpkg`
    - matched by: `object_name_suffix:WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE_SP`
    - top match: `Ungulate Winter Range - Approved`
  - `whse_wildlife_management_wcp_ungulate` | query=`WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE.gpkg`
    - matched by: `object_name:WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE_SP`
    - top match: `Ungulate Winter Range - Approved`
  - `whse_wildlife_management_wcp_ungulate_winter_range` | query=`WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE_WINTER_RANGE/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE_WINTER_RANGE.gpkg`
    - matched by: `object_name:WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE_SP`
    - top match: `Ungulate Winter Range - Approved`
- Logic mode: `femic_core`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### 9. Critical habitat for fish

- Parent step id: `thlb_parent_009_critical_habitat_for_fish`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `11521.000 ha`
- Benchmark cumulative remaining area: `2415545.000 ha`
- Supporting prose section: `6.3.4 Critical habitat for fish`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- Draft subrules:
  - `thlb_parent_009_critical_habitat_for_fish_draft_01` | summary=`Areas of critical habitat for fish that require protection and site-specific management actions were identified as part of the LAO.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_009_critical_habitat_for_fish_draft_02` | summary=`The LAO specifies that the areas are to be maintained as no-harvest areas.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_009_critical_habitat_for_fish_draft_03` | summary=`Critical fish habitat will be excluded from the LHLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld`
  - `thlb_parent_009_critical_habitat_for_fish_draft_04` | summary=`Critical habitat for fish Designations Total (ha) Forested (ha) Excluded (ha) Critical habitat for fish 51,553 20,501 11,521 Data source and comments: Critical fish habitat area bo` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area_sp`, `rmp_plan_legal_poly_svw`, `whse_admin_boundaries_fadm_bcts_area_sp`
- Compiled logic:

### 9. Critical habitat for fish

- Step id: `thlb_parent_009_critical_habitat_for_fish_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- TSR page: `30`
- TSR text: `Areas of critical habitat for fish that require protection and site-specific management actions were identified as part of the LAO. The LAO specifies that the areas are to be maintained as no-harvest areas. Critical fish habitat will be excluded from the LHLB. Table 10. Critical habitat for fish Designations Total (ha) Forested (ha) Excluded (ha) Critical habitat for fish 51,553 20,501 11,521 Data source and comments: Critical fish habitat area boundaries are from the Section 93.4 LAO establishing objectives for the CCLUP, May 19, 2010, amended April 18, 2011, and consolidated to September 6, 2018. Map 4.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `rmp_plan_legal_poly_svw` | query=`RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_PLAN_LEGAL_POLY_SVW/RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `rmp_plan_legal_poly_svw`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### 10. Lakeshore management

- Parent step id: `thlb_parent_010_lakeshore_management`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `327.000 ha`
- Benchmark cumulative remaining area: `2415218.000 ha`
- Supporting prose section: `6.3.5 Lakeshore management`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- Draft subrules:
  - `thlb_parent_010_lakeshore_management_draft_01` | summary=`The LAO designates a selection of lakes as Class A lakes which includes a legal spatial data set that defines buffers around these lakes and are classified are considered to be no ` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `rmp_ogma_legal_current_svw`, `rmp_plan_legal_poly_svw`
  - `thlb_parent_010_lakeshore_management_draft_02` | summary=`These areas of overlap will be excluded from the LHLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_010_lakeshore_management_draft_03` | summary=`The management of Class B to E lakes through limits on allowed disturbance area will be discussed in Section 7.2.6 – ‘Lakeshore management’.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_010_lakeshore_management_draft_04` | summary=`Class A lakes Designations Total (ha) Forested (ha) Excluded (ha) Class A Lakes 18,988 13,060 327 Data source and comments: The Class A lakes are identified in the Section 93.4 LAO` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
  - `thlb_parent_010_lakeshore_management_draft_05` | summary=`Lake management zone boundaries are provided by the lake buffer mapping that also provides riparian management and reserve zones for lakes used in Section 5.4.1.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_fwa_lakes_poly`
- Compiled logic:

### 10. Lakeshore management

- Step id: `thlb_parent_010_lakeshore_management_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- TSR page: `30`
- TSR text: `The LAO designates a selection of lakes as Class A lakes which includes a legal spatial data set that defines buffers around these lakes and are classified are considered to be no harvest areas when they overlap with visual quality objective class ‘preservation’. These areas of overlap will be excluded from the LHLB. The management of Class B to E lakes through limits on allowed disturbance area will be discussed in Section 7.2.6 – ‘Lakeshore management’. Table 11. Class A lakes Designations Total (ha) Forested (ha) Excluded (ha) Class A Lakes 18,988 13,060 327 Data source and comments: The Class A lakes are identified in the Section 93.4 LAO establishing objectives for the CCLUP, May 19, 2010, amended April 18, 2011, and consolidated to September 6, 2018. Map 6. Lake management zone boundaries are provided by the lake buffer mapping that also provides riparian management and reserve zones for lakes used in Section 5.4.1.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `rmp_plan_legal_poly_svw` | query=`RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_PLAN_LEGAL_POLY_SVW/RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `rmp_plan_legal_poly_svw`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### 11. Community areas of special concern

- Parent step id: `thlb_parent_011_community_areas_of_special_concern`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `62460.000 ha`
- Benchmark cumulative remaining area: `2352758.000 ha`
- Supporting prose section: `6.3.7 Community areas of special concern (CASC)`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- Draft subrules:
  - `thlb_parent_011_community_areas_of_special_concern_draft_01` | summary=`Community areas of special concern are spatially delineated areas that have been designated as no-harvest areas in the LUO to address a mix of CCLUP objectives.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
  - `thlb_parent_011_community_areas_of_special_concern_draft_02` | summary=`Community areas of special concern are excluded from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_011_community_areas_of_special_concern_draft_03` | summary=`Community areas of special concern Designation Total (ha) Forested (ha) Excluded (ha) Community areas of special concern 436,210 69,346 62,460 Data source and comments: The communi` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
  - `thlb_parent_011_community_areas_of_special_concern_draft_04` | summary=`No changes were made to the mapped boundaries for CASC in the 2011 amendment.` | operation=`exclude` | review=`draft`
    - candidate layers: `clab_indian_reserves`, `consolidated_cutblocks_2011`, `fadm_bcts_area_sp`
  - `thlb_parent_011_community_areas_of_special_concern_draft_05` | summary=`Identification of the Timber Harvesting Land Base The THLB is the portion of the LHLB where timber harvesting is expected to occur in the context of the timber supply analysis supp` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
- Compiled logic:

### 11. Community areas of special concern

- Step id: `thlb_parent_011_community_areas_of_special_concern_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Community areas of special concern are spatially delineated areas that have been designated as no-harvest areas in the LUO to address a mix of CCLUP objectives. Community areas of special concern are excluded from the THLB. Table 13. Community areas of special concern Designation Total (ha) Forested (ha) Excluded (ha) Community areas of special concern 436,210 69,346 62,460 Data source and comments: The community areas of special concern boundaries are from the Land Use Order Objectives for the Cariboo-Chilcotin Land Use Plan, May 19, 2010, Map 5. No changes were made to the mapped boundaries for CASC in the 2011 amendment. 6.4. Identification of the Timber Harvesting Land Base The THLB is the portion of the LHLB where timber harvesting is expected to occur in the context of the timber supply analysis supporting this AAC determination.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `rmp_plan_legal_poly_svw` | query=`RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_PLAN_LEGAL_POLY_SVW/RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `rmp_plan_legal_poly_svw`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### 19. Buffered trails

- Parent step id: `thlb_parent_019_buffered_trails`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `8039.000 ha`
- Benchmark cumulative remaining area: `1804681.000 ha`
- Supporting prose section: `6.3.6 Buffered trails`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- Draft subrules:
  - `thlb_parent_019_buffered_trails_draft_01` | summary=`The LAO identifies regionally important trails and defines a 50-metre management zone on either side of the trail.` | operation=`exclude` | review=`draft`
  - `thlb_parent_019_buffered_trails_draft_02` | summary=`The LAO specifies that at least 85% of the current forest basal area must be maintained within the buffer.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_019_buffered_trails_draft_03` | summary=`At least 85% of the area within the 100-metre corridor along trails will not be available for harvest.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_019_buffered_trails_draft_04` | summary=`Buffered trails Designations Total (ha) Forested (ha) Excluded (ha) LAO buffered trails 46,020 25,372 8,039 Data source and comments: The land base reduction for identified trails ` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
- Compiled logic:

### 19. Buffered trails

- Step id: `thlb_parent_019_buffered_trails_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- TSR page: `30`
- TSR text: `The LAO identifies regionally important trails and defines a 50-metre management zone on either side of the trail. The LAO specifies that at least 85% of the current forest basal area must be maintained within the buffer. At least 85% of the area within the 100-metre corridor along trails will not be available for harvest. Table 12. Buffered trails Designations Total (ha) Forested (ha) Excluded (ha) LAO buffered trails 46,020 25,372 8,039 Data source and comments: The land base reduction for identified trails reflects the Section 93.4 LAO establishing objectives for the CCLUP, May 19, 2010, amended April 18, 2011, and consolidated to September 6, 2018. Map 10.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `rmp_plan_legal_poly_svw` | query=`RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_PLAN_LEGAL_POLY_SVW/RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `rmp_plan_legal_poly_svw`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### LHLB -> THLB

### 12. Proven Aboriginal Rights areas

- Parent step id: `thlb_parent_012_proven_aboriginal_rights_areas`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `68401.000 ha`
- Benchmark cumulative remaining area: `2284357.000 ha`
- Supporting prose section: `6.4.1 Proven Aboriginal Rights area`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- Draft subrules:
  - `thlb_parent_012_proven_aboriginal_rights_areas_draft_01` | summary=`The Tsilhqot’in 2012 BC Supreme Court decision confirmed a proven Aboriginal rights area (PRA) where Tsilhqot’in people hold rights to hunt and trap birds and animals.` | operation=`exclude` | review=`draft`
    - candidate layers: `bcmpb_v9_cumkill_projected`
  - `thlb_parent_012_proven_aboriginal_rights_areas_draft_02` | summary=`This area overlaps the Tsilhqot’in proven and declared Aboriginal title area and extends beyond encompassing the entire court case area.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_012_proven_aboriginal_rights_areas_draft_03` | summary=`This area, outside the title area, is still administered by the Province and contributes to timber supply within the Williams Lake TSA.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tsa`
  - `thlb_parent_012_proven_aboriginal_rights_areas_draft_04` | summary=`Deep consultation is required when considering proposed authorizations in this area and since 2014, very few provincial authorizations have been made in this area because managemen` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_012_proven_aboriginal_rights_areas_draft_05` | summary=`The PRA will be excluded from the THLB to reflect the lack of commercial forestry activity in the last nine years.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_012_proven_aboriginal_rights_areas_draft_06` | summary=`Proven Aboriginal Rights areas Designations Total (ha) Forested (ha) Excluded (ha) Proven Aboriginal Rights areas 432,155 123,369 68,401` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_fadm_designated`, `whse_wildlife_management_wcp_wildlife_habitat_area`
- Compiled logic:

### 12. Proven Aboriginal Rights areas

- Step id: `thlb_parent_012_proven_aboriginal_rights_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `The Tsilhqot’in 2012 BC Supreme Court decision confirmed a proven Aboriginal rights area (PRA) where Tsilhqot’in people hold rights to hunt and trap birds and animals. This area overlaps the Tsilhqot’in proven and declared Aboriginal title area and extends beyond encompassing the entire court case area. This area, outside the title area, is still administered by the Province and contributes to timber supply within the Williams Lake TSA. Deep consultation is required when considering proposed authorizations in this area and since 2014, very few provincial authorizations have been made in this area because management expectations are unique. The PRA will be excluded from the THLB to reflect the lack of commercial forestry activity in the last nine years. Table 14. Proven Aboriginal Rights areas Designations Total (ha) Forested (ha) Excluded (ha) Proven Aboriginal Rights areas 432,155 123,369 68,401`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_wld_wha_proposed_sp` | query=`REG_LAND_AND_NATURAL_RESOURCE.WLD_WHA_PROPOSED_SP` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_WLD_WHA_PROPOSED_SP/REG_LAND_AND_NATURAL_RESOURCE_WLD_WHA_PROPOSED_SP.gpkg`
    - matched by: `object_name:WHSE_WILDLIFE_MANAGEMENT.WCP_WHA_PROPOSED_SP`
    - top match: `Wildlife Habitat Areas - Proposed`
  - `whse_admin_boundaries_fadm_tsa` | query=`WHSE_ADMIN_BOUNDARIES.FADM_TSA` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_ADMIN_BOUNDARIES_FADM_TSA/WHSE_ADMIN_BOUNDARIES_FADM_TSA.gpkg`
    - matched by: `object_name:WHSE_ADMIN_BOUNDARIES.FADM_TSA`
    - top match: `FADM - Timber Supply Area (TSA)`
  - `whse_admin_boundaries_pip_consultation` | query=`WHSE_ADMIN_BOUNDARIES.PIP_CONSULTATION` | status=`no_hit` | strategy=`override_required`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `whse_admin_boundaries_pip_consultation`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### 13. Areas considered inoperable

- Parent step id: `thlb_parent_013_areas_considered_inoperable`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `33533.000 ha`
- Benchmark cumulative remaining area: `2250824.000 ha`
- Supporting prose section: `6.4.3 Areas considered inoperable`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=32`
- Draft subrules:
  - `thlb_parent_013_areas_considered_inoperable_draft_01` | summary=`Areas that are inoperable within the TSA are generally associated with steep slopes.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_013_areas_considered_inoperable_draft_02` | summary=`Steep slopes are unlikely to be harvested because of unstable terrain and sensitive soils.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`, `consolidated_cutblocks_2020`, `veg_consolidated_cut_blocks_sp`
  - `thlb_parent_013_areas_considered_inoperable_draft_03` | summary=`Also, steep slopes require the use of different harvest systems such as cable logging which may be uneconomic depending on volume per hectare.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_013_areas_considered_inoperable_draft_04` | summary=`Inoperable areas will be identified as follows: • Slopes that exceed 70% east of Highway 97.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_013_areas_considered_inoperable_draft_05` | summary=`Harvesting on slopes between 40% and 70%, and cable harvesting has been employed as a past practice east of Highway 97. • Slopes that exceed 40% west of Highway 97.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_013_areas_considered_inoperable_draft_06` | summary=`These slopes typically have lower volume per hectare which generally makes these types unsuitable for harvesting. • Slopes classified as Unstable (U) or Terrain Class 5.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_013_areas_considered_inoperable_draft_07` | summary=`Areas considered inoperable Designations Total (ha) Forested (ha) Excluded (ha) Steep slopes 491,492 92,748 31,974 Unstable terrain 15,051 3,923 1,559 Data source and comments: Slo` | operation=`exclude` | review=`draft`
    - candidate layers: `trim_contour_points`, `whse_basemapping_trim_contour_points`
- Compiled logic:

### 13. Areas considered inoperable

- Step id: `thlb_parent_013_areas_considered_inoperable_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=32`
- TSR page: `32`
- TSR text: `Areas that are inoperable within the TSA are generally associated with steep slopes. Steep slopes are unlikely to be harvested because of unstable terrain and sensitive soils. Also, steep slopes require the use of different harvest systems such as cable logging which may be uneconomic depending on volume per hectare. Inoperable areas will be identified as follows: • Slopes that exceed 70% east of Highway 97. Harvesting on slopes between 40% and 70%, and cable harvesting has been employed as a past practice east of Highway 97. • Slopes that exceed 40% west of Highway 97. These slopes typically have lower volume per hectare which generally makes these types unsuitable for harvesting. • Slopes classified as Unstable (U) or Terrain Class 5. Table 16. Areas considered inoperable Designations Total (ha) Forested (ha) Excluded (ha) Steep slopes 491,492 92,748 31,974 Unstable terrain 15,051 3,923 1,559 Data source and comments: Slope angle is derived from the provincial digital elevation model.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `trim_contour_points` | query=`TRIM_CONTOUR_POINTS` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/TRIM_CONTOUR_POINTS/TRIM_CONTOUR_POINTS.gpkg`
    - matched by: `object_name_suffix:WHSE_BASEMAPPING.TRIM_CONTOUR_POINTS`
    - top match: `TRIM Contours Points`
  - `whse_basemapping_trim_contour_points` | query=`WHSE_BASEMAPPING.TRIM_CONTOUR_POINTS` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_TRIM_CONTOUR_POINTS/WHSE_BASEMAPPING_TRIM_CONTOUR_POINTS.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.TRIM_CONTOUR_POINTS`
    - top match: `TRIM Contours Points`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `trim_contour_points`
  - `whse_basemapping_trim_contour_points`
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 14. Sites with low growing timber potential

- Parent step id: `thlb_parent_014_sites_with_low_growing_timber_potential`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `321044.000 ha`
- Benchmark cumulative remaining area: `1929780.000 ha`
- Supporting prose section: `6.4.4 Sites with low timber growing potential`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=33`
- Draft subrules:
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_01` | summary=`Sites may have low productivity because of inherent site factors such as nutrient availability, exposure or excessive moisture.` | operation=`exclude` | review=`draft`
    - candidate layers: `site_prod_bc`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_02` | summary=`Stands on these sites may contribute to non-timber objectives even though they are unlikely to grow a merchantable crop of trees in a reasonable amount of time.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_03` | summary=`As such, low productivity stands are removed from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `site_prod_bc`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_04` | summary=`Low productivity stands were identified as stands that are not capable of achieving the minimum harvestable volume applied in this analysis by 160 years.` | operation=`exclude` | review=`draft`
    - candidate layers: `site_prod_bc`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_05` | summary=`As discussed in Section 7.1.6 – ‘Minimum harvestable criteria’, the minimum threshold is 80 cubic metres per hectare except for steep slopes where the threshold increases to 250 cu` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_section_lines_svw`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_06` | summary=`The VRI has been adjusted to reflect losses due to the MPB epidemic and recent catastrophic fires.` | operation=`exclude` | review=`draft`
    - candidate layers: `veg_comp_lyr_r1`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_07` | summary=`It is now difficult to discern low productivity stands from recently disturbed stands based on the current adjusted attributes and yield projections created from these attributes a` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_08` | summary=`Site index was not adjusted and remains a reliable identifier of low productivity stands and will be used in this analysis.` | operation=`exclude` | review=`draft`
    - candidate layers: `site_prod_bc`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_09` | summary=`In order to utilize site index, an exercise was conducted to find the correlation between site index and the minimum harvestable criteria.` | operation=`exclude` | review=`draft`
    - candidate layers: `site_prod_bc`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_10` | summary=`Representative yield tables for the major leading species within Williams Lake TSA were produced at increasing increments of site index until a yield table that achieved the minimu` | operation=`exclude` | review=`draft`
    - candidate layers: `bec_biogeoclimatic_poly`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_11` | summary=`Site index threshold for sites with low timber growing potential Leading species BEC zone Total (ha) AFLB (ha) SI (m) at 80 m3/ha SI (m) at 250 m3/ha Bl BAFA 111 111 Bl CWH 897 897` | operation=`exclude` | review=`draft`
    - candidate layers: `bec_biogeoclimatic_poly`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_12` | summary=`Site index threshold for sites with low timber growing potential (concluded) Leading species BEC zone Total (ha) AFLB (ha) SI (m) at 80 m3/ha SI (m) at 250 m3/ha Pl CWH 4,570 4,570` | operation=`exclude` | review=`draft`
    - candidate layers: `bec_biogeoclimatic_poly`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_13` | summary=`Sites with low timber growing potential Designations Total (ha) Forested (ha) Excluded (ha) Sites with low timber growing potential 601,655 542,518 321,044 Data source and comments` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_gry_psp_status`
- Compiled logic:

### 14. Sites with low growing timber potential

- Step id: `thlb_parent_014_sites_with_low_growing_timber_potential_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=33`
- TSR page: `33`
- TSR text: `Sites may have low productivity because of inherent site factors such as nutrient availability, exposure or excessive moisture. Stands on these sites may contribute to non-timber objectives even though they are unlikely to grow a merchantable crop of trees in a reasonable amount of time. As such, low productivity stands are removed from the THLB. Low productivity stands were identified as stands that are not capable of achieving the minimum harvestable volume applied in this analysis by 160 years. As discussed in Section 7.1.6 – ‘Minimum harvestable criteria’, the minimum threshold is 80 cubic metres per hectare except for steep slopes where the threshold increases to 250 cubic metres per hectare. The VRI has been adjusted to reflect losses due to the MPB epidemic and recent catastrophic fires. It is now difficult to discern low productivity stands from recently disturbed stands based on the current adjusted attributes and yield projections created from these attributes are no longer reliable as they do not account for stand recovery and release of understory regeneration. Site index was not adjusted and remains a reliable identifier of low productivity stands and will be used in this analysis. In order to utilize site index, an exercise was conducted to find the correlation between site index and the minimum harvestable criteria. Representative yield tables for the major leading species within Williams Lake TSA were produced at increasing increments of site index until a yield table that achieved the minimum harvestable criteria was identified for each species and each BEC zone. Table 17. Site index threshold for sites with low timber growing potential Leading species BEC zone Total (ha) AFLB (ha) SI (m) at 80 m3/ha SI (m) at 250 m3/ha Bl BAFA 111 111 Bl CWH 897 897 4.73 7.01 Bl ESSF 124,601 124,299 5.82 9.96 Bl ICH 5,375 5,300 5.76 9.99 Bl IDF 321 321 5.56 9.40 Bl IMA 478 478 Bl MH 2,020 2,020 4.61 6.76 Bl MS 3,114 3,098 5.91 10.38 Bl SBPS 254 252 5.60 9.82 Bl SBS 3,283 3,217 5.73 9.82 Cw CWH 157 157 5.94 8.47 Cw ESSF 3,986 3,976 5.13 8.25 Cw ICH 43,254 42,937 5.49 8.09 Cw SBS 83 83 4.52 6.83 Deciduous BG 215 214 Deciduous CWH 471 471 7.75 16.36 Deciduous ESSF 486 486 8.62 16.85 Deciduous ICH 9,033 8,889 8.82 17.3 Deciduous IDF 20,712 20,471 9.28 20.11 Deciduous MS 1121 1,114 9.01 16.76 Deciduous SBPS 19,436 19,232 9.03 19.08 Deciduous SBS 21,515 21,151 8.88 17.46 Fd BG 26,405 26,351 Fd CWH 8,006 8,006 7.89 12.33 Fd ESSF 6,194 6,178 9.39 14.48 Fd ICH 56,684 55,967 8.98 13.9 Fd IDF 355,725 352,157 8.65 13.96 Fd MH 458 458 7.75 12.00 Fd MS 3,231 3,223.425 9.26 14.47 Fd SBPS 13,990 13,872 8.64 13.62 Fd SBS 63,975 62,771 9.06 14.08 Pl BAFA 14 14 Pl BG 272 272 (continued) Table 17. Site index threshold for sites with low timber growing potential (concluded) Leading species BEC zone Total (ha) AFLB (ha) SI (m) at 80 m3/ha SI (m) at 250 m3/ha Pl CWH 4,570 4,570 6.69 12.36 Pl ESSF 139,272 138,717 8.69 15.53 Pl ICH 44,850 44,279 7.79 14.96 Pl IDF 215,072 212,472 6.93 13.11 Pl IMA 1 1 Pl MH 1,212 1,212 6.76 11.98 Pl MS 476,984 473,526 8.64 16.49 Pl SBPS 937,325 926,646 6.66 12.54 Pl SBS 67,624 65,310 8.25 16.04 Sx BAFA 40 40 Sx BG 5 5 Sx CWH 996 996 4.86 7.99 Sx ESSF 131,173 130,175 9.19 16.47 Sx ICH 68,280 67,069 8.50 15.21 Sx IDF 52,276 51,494 7.42 13.18 Sx IMA 46 46 Sx MH 918 918 4.52 7.25 Sx MS 54,171 53,886 9.33 16.64 Sx SBPS 95,107 94,285 8.00 14.00 Sx SBS 44,895 44,075 9.01 15.92 All stands with a site index below the values listed above in FMLB without harvest history, matched by corresponding leading-species and BEC zone, were excluded from the THLB. Table 18. Sites with low timber growing potential Designations Total (ha) Forested (ha) Excluded (ha) Sites with low timber growing potential 601,655 542,518 321,044 Data source and comments: Yield tables were produced using VDYP 7 by FAIB growth and yield experts using default stocking criteria for Williams Lake TSA.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `site_prod_bc` | query=`SITE_PROD_BC` | status=`alias_hit` | strategy=`direct_download`
    - artifact: `data/downloads/bcdc/SITE_PROD_BC/Site_Prod_BC.zip`
    - matched by: `exact_text:Provincial Site Productivity Layer`
    - top match: `Provincial Site Productivity Layer`
  - `whse_forest_vegetation_gry_psp_status` | query=`WHSE_FOREST_VEGETATION.GRY_PSP_STATUS` | status=`exact_hit` | strategy=`dwds_order`
    - matched by: `object_name_stem:WHSE_FOREST_VEGETATION.GRY_PSP_STATUS_ACTIVE`
    - top match: `Growth and Yield  Samples - All Status`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `site_prod_bc`
  - `whse_forest_vegetation_gry_psp_status`
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 15. Non-merchantable timber profiles

- Parent step id: `thlb_parent_015_non_merchantable_timber_profiles`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `49052.000 ha`
- Benchmark cumulative remaining area: `1880728.000 ha`
- Supporting prose section: `6.4.5 Non-merchantable timber profiles`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=35`
- Draft subrules:
  - `thlb_parent_015_non_merchantable_timber_profiles_draft_01` | summary=`Non-merchantable timber profiles are stands that are physically operable, meet minimum harvestable criteria for age and volume, yet contain tree species that are not currently util` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`
  - `thlb_parent_015_non_merchantable_timber_profiles_draft_02` | summary=`In the Williams Lake TSA, stands predominately composed of broadleaf species are not utilized, and often left standing for biodiversity value.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`
  - `thlb_parent_015_non_merchantable_timber_profiles_draft_03` | summary=`Therefore, broadleaf-leading stands will be excluded from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`
  - `thlb_parent_015_non_merchantable_timber_profiles_draft_04` | summary=`The deciduous component of conifer-leading stands is discussed under Section 7.1.5 – ‘Volume exclusions for broadleaf species’.` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_road_section_lines_svw`
  - `thlb_parent_015_non_merchantable_timber_profiles_draft_05` | summary=`Broadleaf-leading stands Designations Total (ha) Forested (ha) Excluded (ha) Aspen-leading stands 160,809 99,616 45,113 Birch-leading stands 11,278 8,051 3,939 The potential contri` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`
- Compiled logic:

### 15. Non-merchantable timber profiles

- Step id: `thlb_parent_015_non_merchantable_timber_profiles_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=35`
- TSR page: `35`
- TSR text: `Non-merchantable timber profiles are stands that are physically operable, meet minimum harvestable criteria for age and volume, yet contain tree species that are not currently utilized. In the Williams Lake TSA, stands predominately composed of broadleaf species are not utilized, and often left standing for biodiversity value. Therefore, broadleaf-leading stands will be excluded from the THLB. The deciduous component of conifer-leading stands is discussed under Section 7.1.5 – ‘Volume exclusions for broadleaf species’. Table 19. Broadleaf-leading stands Designations Total (ha) Forested (ha) Excluded (ha) Aspen-leading stands 160,809 99,616 45,113 Birch-leading stands 11,278 8,051 3,939 The potential contribution of broadleaf-deciduous leading stands to timber supply will be explored through sensitivity analysis.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `ften_road_section_lines_svw` | query=`FTEN_ROAD_SECTION_LINES_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/FTEN_ROAD_SECTION_LINES_SVW/FTEN_ROAD_SECTION_LINES_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW`
    - top match: `Forest Tenure Road Section Lines`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `ften_road_section_lines_svw`
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 16. Recreation features

- Parent step id: `thlb_parent_016_recreation_features`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `9598.000 ha`
- Benchmark cumulative remaining area: `1871130.000 ha`
- Supporting prose section: `6.4.6 Recreation features`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=36`
- Draft subrules:
  - `thlb_parent_016_recreation_features_draft_01` | summary=`Recreation sites and trails have been legally established within the Williams Lake TSA under the FRPA.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_tenure_ften_recreation`
  - `thlb_parent_016_recreation_features_draft_02` | summary=`These include campsites and trails as well as sites created for a variety of education and recreation activities.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_tenure_ften_recreation`
  - `thlb_parent_016_recreation_features_draft_03` | summary=`Approved FSPs include a strategy related to legally established recreations sites and trails.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_tenure_ften_recreation`
  - `thlb_parent_016_recreation_features_draft_04` | summary=`This strategy is to refer proposed harvesting and road construction to the ministry responsible for recreation requesting input on the proposal.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_016_recreation_features_draft_05` | summary=`Any input received will be incorporated into the harvesting and road construction management strategy.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_016_recreation_features_draft_06` | summary=`While logging is possible, it is likely that harvesting of recreation sites will be very limited so identified recreational areas and features will be excluded from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`, `whse_forest_tenure_ften_recreation`, `whse_land_use_planning_rmp_plan_non_legal_poly_svw`
  - `thlb_parent_016_recreation_features_draft_07` | summary=`Recreation features Land classification Total (ha) Forested (ha) Excluded (ha) Use, Recreation and Enjoyment of the Public (UREP) 3,551 2,356 1,320 Forest recreation 15,699 13,058 ` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
- Compiled logic:

### 16. Recreation features

- Step id: `thlb_parent_016_recreation_features_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=36`
- TSR page: `36`
- TSR text: `Recreation sites and trails have been legally established within the Williams Lake TSA under the FRPA. These include campsites and trails as well as sites created for a variety of education and recreation activities. Approved FSPs include a strategy related to legally established recreations sites and trails. This strategy is to refer proposed harvesting and road construction to the ministry responsible for recreation requesting input on the proposal. Any input received will be incorporated into the harvesting and road construction management strategy. While logging is possible, it is likely that harvesting of recreation sites will be very limited so identified recreational areas and features will be excluded from the THLB. Table 20. Recreation features Land classification Total (ha) Forested (ha) Excluded (ha) Use, Recreation and Enjoyment of the Public (UREP) 3,551 2,356 1,320 Forest recreation 15,699 13,058 8,051 Recreation features 23,727 14,774 227 Data source and comments: Tolko Industries Ltd. - FSP #780; West Fraser Mills Ltd. - FSP #755; and BCTS - FSP #828.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_imagery_and_base_maps_mot_road_features_invntry_sp` | query=`WHSE_IMAGERY_AND_BASE_MAPS.MOT_ROAD_FEATURES_INVNTRY_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_IMAGERY_AND_BASE_MAPS_MOT_ROAD_FEATURES_INVNTRY_SP/WHSE_IMAGERY_AND_BASE_MAPS_MOT_ROAD_FEATURES_INVNTRY_SP.gpkg`
    - matched by: `object_name:WHSE_IMAGERY_AND_BASE_MAPS.MOT_ROAD_FEATURES_INVNTRY_SP`
    - top match: `Ministry of Transportation (MOT) Road Features Inventory (RFI)`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 17. Growth and yield permanent sample plots

- Parent step id: `thlb_parent_017_growth_and_yield_permanent_sample_plots`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `3577.000 ha`
- Benchmark cumulative remaining area: `1867553.000 ha`
- Supporting prose section: `6.4.7 Growth and yield permanent sample plots and research installations`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=36`
- Draft subrules:
  - `thlb_parent_017_growth_and_yield_permanent_sample_plots_draft_01` | summary=`The ministry maintains a network of growth and yield permanent sample plots (PSP) across the province for the purposes of understanding forest growth and calibrating growth and yie` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_gry_psp_status`
  - `thlb_parent_017_growth_and_yield_permanent_sample_plots_draft_02` | summary=`Objectives for these plots have not been established under FRPA.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_gry_psp_status`
  - `thlb_parent_017_growth_and_yield_permanent_sample_plots_draft_03` | summary=`However, harvesting within these active research sites is currently avoided and only occurs after consultation with the research team.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_gry_psp_status`
  - `thlb_parent_017_growth_and_yield_permanent_sample_plots_draft_04` | summary=`Research scientists from within the ministry confirm that these areas should be excluded from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_gry_psp_status`
  - `thlb_parent_017_growth_and_yield_permanent_sample_plots_draft_05` | summary=`Growth and yield permanent sample plots Land classification Total (ha) Forested (ha) Excluded (ha) Growth and yield permanent sample plots 6,290 5,156 3,577` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_gry_psp_status`
- Compiled logic:

### 17. Growth and yield permanent sample plots

- Step id: `thlb_parent_017_growth_and_yield_permanent_sample_plots_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `blocked_missing_source`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=36`
- TSR page: `36`
- TSR text: `The ministry maintains a network of growth and yield permanent sample plots (PSP) across the province for the purposes of understanding forest growth and calibrating growth and yield models. Objectives for these plots have not been established under FRPA. However, harvesting within these active research sites is currently avoided and only occurs after consultation with the research team. Research scientists from within the ministry confirm that these areas should be excluded from the THLB. Table 21. Growth and yield permanent sample plots Land classification Total (ha) Forested (ha) Excluded (ha) Growth and yield permanent sample plots 6,290 5,156 3,577`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_forest_vegetation_gry_psp_status` | query=`WHSE_FOREST_VEGETATION.GRY_PSP_STATUS` | status=`exact_hit` | strategy=`dwds_order`
    - matched by: `object_name_stem:WHSE_FOREST_VEGETATION.GRY_PSP_STATUS_ACTIVE`
    - top match: `Growth and Yield  Samples - All Status`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `whse_forest_vegetation_gry_psp_status`
- Run notes:
  - No fetched polygon artifact was available for the linked source entries.

### 18. Riparian areas

- Parent step id: `thlb_parent_018_riparian_areas`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `54833.000 ha`
- Benchmark cumulative remaining area: `1812720.000 ha`
- Supporting prose section: `6.4.2 Riparian areas`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- Draft subrules:
  - `thlb_parent_018_riparian_areas_draft_01` | summary=`Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995).` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_fadm_designated`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_018_riparian_areas_draft_02` | summary=`Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ).` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_fadm_designated`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_018_riparian_areas_draft_03` | summary=`The zone widths are consistent with those specified under FPPR and current FSPs.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_018_riparian_areas_draft_04` | summary=`Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelle` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_fadm_designated`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_018_riparian_areas_draft_05` | summary=`Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harve` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_fadm_designated`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_018_riparian_areas_draft_06` | summary=`The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_fadm_designated`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_018_riparian_areas_draft_07` | summary=`Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 ` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_fadm_designated`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_018_riparian_areas_draft_08` | summary=`However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_018_riparian_areas_draft_09` | summary=`Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varde` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_018_riparian_areas_draft_10` | summary=`For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_landscape_unit_svw`, `rmp_landscape_unit_svw_no_multiples`, `whse_land_use_planning_fadm_designated`
  - `thlb_parent_018_riparian_areas_draft_11` | summary=`In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_018_riparian_areas_draft_12` | summary=`Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`
  - `thlb_parent_018_riparian_areas_draft_13` | summary=`Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 4` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
  - `thlb_parent_018_riparian_areas_draft_14` | summary=`RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; ` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_legal_poly_svw`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
- Compiled logic:

### 18. Riparian areas

- Step id: `thlb_parent_018_riparian_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `applied_noop`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `rmp_plan_legal_poly_svw` | query=`RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_PLAN_LEGAL_POLY_SVW/RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
  - `whse_basemapping_fwa_lakes_poly` | query=`WHSE_BASEMAPPING.FWA_LAKES_POLY` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_FWA_LAKES_POLY/WHSE_BASEMAPPING_FWA_LAKES_POLY.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.FWA_LAKES_POLY`
    - top match: `Freshwater Atlas Lakes`
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`
- Missing linked source entries:
  - `rmp_plan_legal_poly_svw`
- Run notes:
  - No active fragment geometries intersected the exclusion mask.

### 20. Wildlife tree retention areas

- Parent step id: `thlb_parent_020_wildlife_tree_retention_areas`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `94417.000 ha`
- Benchmark cumulative remaining area: `1710264.000 ha`
- Supporting prose section: `6.4.8 Wildlife tree retention areas`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- Draft subrules:
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_01` | summary=`Wildlife tree retention areas (WTRA) are established within and adjacent to cutblocks to maintain stand-level biodiversity and are discussed in more detail in Section 7.2.4 – ‘Stan` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`, `consolidated_cutblocks_2020`, `reg_land_and_natural_resource_wld_wha_proposed_sp`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_02` | summary=`Currently mapped WTRA are recorded in RESULTS (identified by Type = ‘Group’ and Objective = ‘WTR’).` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `ta_wildlife_mgmt_areas`, `ta_wildlife_mgmt_areas_svw`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_03` | summary=`Harvesting of WTRA is only restricted until the regenerating cutblock has reached maturity so the existing mapped WTRA will be included in the THLB but will be deferred from harves` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `ta_wildlife_mgmt_areas`, `ta_wildlife_mgmt_areas_svw`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_04` | summary=`Although individual WTRA can eventually be harvested there will always be WTRA established in conjunction with every cutblock harvested.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2011`, `consolidated_cutblocks_2020`, `reg_land_and_natural_resource_wld_wha_proposed_sp`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_05` | summary=`In the base case, the land base that will continually be required for WTRA will be modelled as an aspatial THLB reduction factor.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `ta_wildlife_mgmt_areas`, `ta_wildlife_mgmt_areas_svw`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_06` | summary=`In total, 94 417 hectares will be excluded to represent future WTRA.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld_wha_proposed_sp`, `ta_wildlife_mgmt_areas`, `ta_wildlife_mgmt_areas_svw`
- Compiled logic:

### 20. Wildlife tree retention areas

- Step id: `thlb_parent_020_wildlife_tree_retention_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `unsupported`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- TSR page: `37`
- TSR text: `Wildlife tree retention areas (WTRA) are established within and adjacent to cutblocks to maintain stand-level biodiversity and are discussed in more detail in Section 7.2.4 – ‘Stand-level biodiversity’. Currently mapped WTRA are recorded in RESULTS (identified by Type = ‘Group’ and Objective = ‘WTR’). Harvesting of WTRA is only restricted until the regenerating cutblock has reached maturity so the existing mapped WTRA will be included in the THLB but will be deferred from harvest for 80 years. Although individual WTRA can eventually be harvested there will always be WTRA established in conjunction with every cutblock harvested. In the base case, the land base that will continually be required for WTRA will be modelled as an aspatial THLB reduction factor. In total, 94 417 hectares will be excluded to represent future WTRA.`
- FEMIC proposed logic: Wildlife tree retention areas (WTRA) are established within and adjacent to cutblocks to maintain stand-level biodiversity and are discussed in more detail in Section 7.2.4 – ‘Stand-level biodiversity’. Currently mapped WTRA are recorded in RESULTS (identified by Type = ‘Group’ and Objective = ‘WTR’). Harvesting of WTRA is only restricted until the regenerating cutblock has reached maturity so the existing mapped WTRA will be 80 years
- Linked source layers:
  - `consolidated_cutblocks_2011` | query=`CONSOLIDATED_CUTBLOCKS_2011` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/CONSOLIDATED_CUTBLOCKS_2011/CONSOLIDATED_CUTBLOCKS_2011.gpkg`
    - matched by: `none`
    - top match: `Harvested Areas of BC (Consolidated Cutblocks)`
  - `consolidated_cutblocks_2020` | query=`CONSOLIDATED_CUTBLOCKS_2020` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/CONSOLIDATED_CUTBLOCKS_2020/CONSOLIDATED_CUTBLOCKS_2020.gpkg`
    - matched by: `none`
    - top match: `Harvested Areas of BC (Consolidated Cutblocks)`
  - `veg_consolidated_cut_blocks_sp` | query=`VEG_CONSOLIDATED_CUT_BLOCKS_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/VEG_CONSOLIDATED_CUT_BLOCKS_SP/VEG_CONSOLIDATED_CUT_BLOCKS_SP.gpkg`
    - matched by: `object_name_suffix:WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP`
    - top match: `Harvested Areas of BC (Consolidated Cutblocks)`
- Logic mode: `femic_core`
- Run notes:
  - Normalized action `defer` is not executable in v1.

### 21. Cultural heritage and archaeological resources

- Parent step id: `thlb_parent_021_cultural_heritage_and_archaeological_resources`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `34205.000 ha`
- Benchmark cumulative remaining area: `1676059.000 ha`
- Supporting prose section: `6.4.9 Cultural heritage and archaeological resources.`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- Draft subrules:
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_01` | summary=`The Heritage Conservation Act (HCA) recognizes the historical, cultural, scientific, spiritual, and educational value of archaeological sites to First Nations, local communities, a` | operation=`exclude` | review=`draft`
    - candidate layers: `veg_burn_severity_sp`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_02` | summary=`Archaeological sites on both public and private land are protected under the HCA and must not be altered without a permit.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_plan_non_legal_poly_svw`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_03` | summary=`A cultural heritage resource is an object, site or location of a traditional societal practice that is of historical, cultural, societal or archaeological significance to the provi` | operation=`exclude` | review=`draft`
    - candidate layers: `site_prod_bc`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_04` | summary=`This can include archaeological sites, structural features, heritage landscape features and traditional use sites.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_landscape_unit_svw`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_05` | summary=`Cultural heritage resources not applicable to the HCA are managed for by the licensees through the cultural heritage resource sections in the applicable FSPs as per FPPR Section 10` | operation=`exclude` | review=`draft`
    - candidate layers: `ften_managed_lic`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_06` | summary=`Cultural heritage resources are identified by the licensees through information sharing prior to the submission of cutting permit and road permit applications to the ministry.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_imagery_and_base_maps_mot_road_features_invntry_sp`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_07` | summary=`The most common practice by licensees is to manage for these sites by excluding them from the harvest area through boundary amendments and the placement of wildlife tree retention ` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_admin_boundaries_fadm_tfl`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_08` | summary=`The incremental excluded area required to protect these sites in current practices was discussions with licensees and the Tsilhqot’in National Government.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_09` | summary=`It was estimated that, on average, an additional two percent of the cutblock area was now included in these expanded exclusions and/or reserves.` | operation=`exclude` | review=`draft`
    - candidate layers: `clab_indian_reserves`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_10` | summary=`This will be modelled as an aspatial reduction to the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_human_cultural_economic_fnirs`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_11` | summary=`In total, 34 205 hectares will be excluded to represent cultural heritage resources.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_human_cultural_economic_fnirs`
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_12` | summary=`Data source and comments: Tsilhqot’in National Government Tolko Industries Ltd. - FSP #780; West Fraser Mills Ltd. - FSP #755; and BCTS - FSP #828.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
- Compiled logic:

### 21. Cultural heritage and archaeological resources

- Step id: `thlb_parent_021_cultural_heritage_and_archaeological_resources_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `unsupported`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- TSR page: `37`
- TSR text: `The Heritage Conservation Act (HCA) recognizes the historical, cultural, scientific, spiritual, and educational value of archaeological sites to First Nations, local communities, and the public. Archaeological sites on both public and private land are protected under the HCA and must not be altered without a permit. A cultural heritage resource is an object, site or location of a traditional societal practice that is of historical, cultural, societal or archaeological significance to the province, community or an Aboriginal People. This can include archaeological sites, structural features, heritage landscape features and traditional use sites. Cultural heritage resources not applicable to the HCA are managed for by the licensees through the cultural heritage resource sections in the applicable FSPs as per FPPR Section 10. Cultural heritage resources are identified by the licensees through information sharing prior to the submission of cutting permit and road permit applications to the ministry. The most common practice by licensees is to manage for these sites by excluding them from the harvest area through boundary amendments and the placement of wildlife tree retention and/or cultural resource management zones. The incremental excluded area required to protect these sites in current practices was discussions with licensees and the Tsilhqot’in National Government. It was estimated that, on average, an additional two percent of the cutblock area was now included in these expanded exclusions and/or reserves. This will be modelled as an aspatial reduction to the THLB. In total, 34 205 hectares will be excluded to represent cultural heritage resources. Data source and comments: Tsilhqot’in National Government Tolko Industries Ltd. - FSP #780; West Fraser Mills Ltd. - FSP #755; and BCTS - FSP #828.`
- FEMIC proposed logic: Apply a final aspatial THLB reduction of the TSR-cited magnitude after the spatially executable steps have completed.
- Linked source layers:
  - `whse_imagery_and_base_maps_mot_road_features_invntry_sp` | query=`WHSE_IMAGERY_AND_BASE_MAPS.MOT_ROAD_FEATURES_INVNTRY_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_IMAGERY_AND_BASE_MAPS_MOT_ROAD_FEATURES_INVNTRY_SP/WHSE_IMAGERY_AND_BASE_MAPS_MOT_ROAD_FEATURES_INVNTRY_SP.gpkg`
    - matched by: `object_name:WHSE_IMAGERY_AND_BASE_MAPS.MOT_ROAD_FEATURES_INVNTRY_SP`
    - top match: `Ministry of Transportation (MOT) Road Features Inventory (RFI)`
- Logic mode: `femic_core`
- Run notes:
  - Aspatial reduction steps are preserved for review but not executed in v1.

### 22. Timber harvesting land base

- Parent step id: `thlb_parent_022_timber_harvesting_land_base`
- Stage: `LHLB -> THLB`
- Execution class: `reference_only`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark cumulative remaining area: `1682843.000 ha`
- Compiled logic:

### 22. Timber harvesting land base

- Step id: `thlb_parent_022_timber_harvesting_land_base_compiled_01`
- Kind: `reference_target`
- Stage: `LHLB -> THLB`
- Execution class: `reference_only`
- Run status: `unsupported`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- TSR text: `Timber harvesting land base`
- FEMIC proposed logic: No executable logic has been normalized for this row yet.
- Logic mode: `femic_core`
- Run notes:
  - Normalized action `reference_target` is not executable in v1.

### Reference targets

### 1. Total TSA area

- Parent step id: `thlb_parent_001_total_tsa_area`
- Stage: `Reference targets`
- Execution class: `reference_only`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Compiled logic:

### 1. Total TSA area

- Step id: `thlb_parent_001_total_tsa_area_compiled_01`
- Kind: `reference_target`
- Stage: `Reference targets`
- Execution class: `reference_only`
- Run status: `unsupported`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- TSR text: `Total TSA area`
- FEMIC proposed logic: No executable logic has been normalized for this row yet.
- Linked source layers:
  - `fadm_bcts_area` | query=`FADM_BCTS_AREA` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/FADM_BCTS_AREA/FADM_BCTS_AREA.gpkg`
    - matched by: `object_name_suffix:WHSE_ADMIN_BOUNDARIES.FADM_BCTS_AREA_SP`
    - top match: `FADM - BC Timber Sales Area`
- Logic mode: `femic_core`
- Run notes:
  - Normalized action `reference_target` is not executable in v1.

### 24. Long-term THLB

- Parent step id: `thlb_parent_024_long_term_thlb`
- Stage: `Reference targets`
- Execution class: `reference_only`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark cumulative remaining area: `1660053.000 ha`
- Compiled logic:

### 24. Long-term THLB

- Step id: `thlb_parent_024_long_term_thlb_compiled_01`
- Kind: `reference_target`
- Stage: `Reference targets`
- Execution class: `reference_only`
- Run status: `unsupported`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- TSR text: `Long-term THLB`
- FEMIC proposed logic: long-term thlb Long-term THLB
- Logic mode: `femic_core`
- Run notes:
  - Normalized action `reference_target` is not executable in v1.

