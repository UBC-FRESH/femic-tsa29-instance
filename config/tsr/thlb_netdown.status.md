# THLB Recipe Build Report: TSA 29 (Williams Lake)

- Generated UTC: `2026-04-09T04:13:26.037453+00:00`
- Report mode: `recipe_build`
- THLB recipe path: `config/tsr/thlb_netdown.recipe.yaml`
- Source-layer recipe path: `config/tsr/source_layers.recipe.yaml`
- Runtime history copy: `runtime/logs/tsr/thlb_recipe_build_status_report-20260409T032831Z.md`

## Scope

- Parent step count: `24`
- Compiled step count: `45`
- Selected TSR documents:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf`

## Stage Counts

- `GLB -> AFLB`: `5`
- `AFLB -> LHLB`: `7`
- `LHLB -> THLB`: `10`
- `Reference targets`: `2`
- `Context`: `0`

## Backbone Milestones

- `Total TSA area` | stage=`Reference targets` | benchmark remaining area=`benchmark not parsed`
- `Analysis forest land base` | stage=`GLB -> AFLB` | benchmark remaining area=`3098168.000 ha`
- `Timber harvesting land base` | stage=`LHLB -> THLB` | benchmark remaining area=`1682843.000 ha`
- `Long-term THLB` | stage=`Reference targets` | benchmark remaining area=`1660053.000 ha`

## Stage-by-Stage THLB Steps

### GLB -> AFLB

### 2. Land not administered by the Province

- Parent step id: `thlb_parent_002_land_not_administered_by_the_province`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `697033.000 ha`
- Benchmark cumulative remaining area: `4236602.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved on the Williams Lake landscape-unit smoke subset; pending definitive full-TSA validation after the remaining parent steps are soft-validated.
- Approved UTC: `2026-04-06T04:01:51.687245+00:00`
- Approved by: `user_directed_review`
- Supporting prose section: `6.2.1 Land not administered by the Province for TSA timber supply`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=25`
- Draft subrules:
  - `thlb_parent_002_land_not_administered_by_the_province_draft_01` | summary=`Certain types of lands do not contribute to timber supply for the purpose of this timber supply analysis.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_02` | summary=`This includes privately held lands, First Nations reserves, some lands under the jurisdiction of the federal government and area-based forest tenures.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CLASS`
    - candidate values: `private`, `federal`, `first_nations_reserve`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_03` | summary=`Parks and protected areas are included in the AFLB because they can be relied on to continually contribute to forest cover management objectives such as landscape-level biodiversit` | operation=`no_deduction` | review=`draft`
    - candidate layers: `wildlife_habitat`, `whse_forest_vegetation_f_own`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_04` | summary=`The CCLUP specifies that woodlots also contribute to landscape-level forest management objectives for biodiversity, although the AAC for these woodlots is determined under a separa` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CLASS`
    - candidate values: `woodlot`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_05` | summary=`Area-based licences such as community forest agreements and First Nations woodland licences (FNWL) are expected to manage for landscape-level biodiversity objectives within their t` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CLASS`
    - candidate values: `community_forest_agreement`, `fnwl`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_06` | summary=`Woodlots are not required to manage for landscape-level biodiversity objectives, so they are left in the AFLB and removed when defining the LHLB.` | operation=`defer_to_lhlb` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CLASS`
    - candidate values: `woodlot`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_08` | summary=`The NStQ Interim Treaty Agreement (ITA) Phase 1 land transfer parcels are no longer administered by the Province and will be excluded from the AFLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_09` | summary=`Additional NStQ Agreement in Principle (AIP) lands which are detailed in the signed AIP may also be transferred soon.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_13` | summary=`Proven and declared Aboriginal title lands are not considered Crown land.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_14` | summary=`As such, those lands do not contribute to timber supply in the Williams Lake TSA and are excluded from the AFLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_16` | summary=`Areas classified in this data set with ownership codes 62 (Forest Management Unit) or 69 (Community Watershed) are generally administered by the Province for TSA timber supply.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CODE`
    - candidate values: `62`, `69`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_18` | summary=`Minor areas, including those identified as development project, institutional and residential, were excluded from the AFLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_19` | summary=`Otherwise, the remaining area with these ownership codes will be modelled as managed for TSA timber supply.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_20` | summary=`Areas classified with ownership code 99 (crown leases) are not generally managed for TSA timber supply but were similarly reviewed prior to this analysis.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CODE`, `OWNERSHIP_CLASS`
    - candidate values: `99`, `lease`
  - `thlb_parent_002_land_not_administered_by_the_province_draft_21` | summary=`Minor areas, including those categorized as grazing leases, will be considered as contributing to TSA timber supply because harvesting that occurs on these lease areas contributes ` | operation=`no_deduction` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CLASS`
    - candidate values: `lease`
- Current compiled status summary: `manual_review_required`=1, `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `221602.052 ha`
- Last notebook remaining area: `4937338.492 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_002_land_not_administered_by_the_province.20260406T190950Z.json`
- Compiled logic:

#### 2.1. Ownership classes not administered for TSA timber supply

- Step id: `thlb_parent_002_land_not_administered_by_the_province_compiled_01`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=25`
- TSR page: `25`
- TSR text: `Certain types of lands do not contribute to timber supply for the purpose of this timber supply analysis. This includes privately held lands, First Nations reserves, some lands under the jurisdiction of the federal government and area-based forest tenures. Parks and protected areas are included in the AFLB because they can be relied on to continually contribute to forest cover management objectives such as landscape-level biodiversity, visual quality, and wildlife habitat objectives. The CCLUP specifies that woodlots also contribute to landscape-level forest management objectives for biodiversity, although the AAC for these woodlots is determined under a separate process. Area-based licences such as community forest agreements and First Nations woodland licences (FNWL) are expected to manage for landscape-level biodiversity objectives within their tenured areas, therefore they are removed from the AFLB. Woodlots are not required to manage for landscape-level biodiversity objectives, so they are left in the AFLB and removed when defining the LHLB. The Northern Secwepemc te Qelmucw (NStQ) Treaty Negotiations Agreement in Principle was signed on July 22, 2018, and the Parties are in Stage 5 negotiations to conclude treaty. The NStQ Interim Treaty Agreement (ITA) Phase 1 land transfer parcels are no longer administered by the Province and will be excluded from the AFLB. Additional NStQ Agreement in Principle (AIP) lands which are detailed in the signed AIP may also be transferred soon. The implications of these additional transfers to timber supply implications will be explored through sensitivity analysis. On June 26, 2014, the Supreme Court of Canada (SCC) released its decision on Tsilhqot’in Nation v. British Columbia (Tsilhqot’in decision). In that decision the SCC outlined areas over which the Tsilhqot’in Nation has proven and declared Aboriginal title. Proven and declared Aboriginal title lands are not considered Crown land. As such, those lands do not contribute to timber supply in the Williams Lake TSA and are excluded from the AFLB. A spatial data set of land ownership was developed using information from the Crown Land Registry and the Integrated Cadastral Information Society. Areas classified in this data set with ownership codes 62 (Forest Management Unit) or 69 (Community Watershed) are generally administered by the Province for TSA timber supply. These areas were reviewed by district staff to ensure all categories they contain can appropriately be considered AFLB for purposes of this analysis. Minor areas, including those identified as development project, institutional and residential, were excluded from the AFLB. Otherwise, the remaining area with these ownership codes will be modelled as managed for TSA timber supply. Areas classified with ownership code 99 (crown leases) are not generally managed for TSA timber supply but were similarly reviewed prior to this analysis. Minor areas, including those categorized as grazing leases, will be considered as contributing to TSA timber supply because harvesting that occurs on these lease areas contributes to the TSA harvest level. Table 4. Land ownership types Land ownership type Total area Area excluded Private 186,582 186,582 Federal 71,825 71,825 CFA and FNWL 244,692 244,692 Municipal and Leases 2,688 2,688 NStQ Interim Treaty Agreement 2,796 2,702 Tsilhqot’in Nation Title 193,216 188,544 Data source and comments: WHSE_FOREST_VEGETATION.F_OWN`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_forest_vegetation_f_own` | query=`WHSE_FOREST_VEGETATION.F_OWN` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_FOREST_VEGETATION_F_OWN/WHSE_FOREST_VEGETATION_F_OWN.gpkg`
    - matched by: `object_name:WHSE_FOREST_VEGETATION.F_OWN`
    - top match: `Generalized Forest Cover Ownership`
- Logic mode: `femic_core`

#### 2.2. Treaty and title transfers requiring reviewed overlays

- Step id: `thlb_parent_002_land_not_administered_by_the_province_compiled_02`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `manual_review_required`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=25`
- TSR page: `25`
- TSR text: `Certain types of lands do not contribute to timber supply for the purpose of this timber supply analysis. This includes privately held lands, First Nations reserves, some lands under the jurisdiction of the federal government and area-based forest tenures. Parks and protected areas are included in the AFLB because they can be relied on to continually contribute to forest cover management objectives such as landscape-level biodiversity, visual quality, and wildlife habitat objectives. The CCLUP specifies that woodlots also contribute to landscape-level forest management objectives for biodiversity, although the AAC for these woodlots is determined under a separate process. Area-based licences such as community forest agreements and First Nations woodland licences (FNWL) are expected to manage for landscape-level biodiversity objectives within their tenured areas, therefore they are removed from the AFLB. Woodlots are not required to manage for landscape-level biodiversity objectives, so they are left in the AFLB and removed when defining the LHLB. The Northern Secwepemc te Qelmucw (NStQ) Treaty Negotiations Agreement in Principle was signed on July 22, 2018, and the Parties are in Stage 5 negotiations to conclude treaty. The NStQ Interim Treaty Agreement (ITA) Phase 1 land transfer parcels are no longer administered by the Province and will be excluded from the AFLB. Additional NStQ Agreement in Principle (AIP) lands which are detailed in the signed AIP may also be transferred soon. The implications of these additional transfers to timber supply implications will be explored through sensitivity analysis. On June 26, 2014, the Supreme Court of Canada (SCC) released its decision on Tsilhqot’in Nation v. British Columbia (Tsilhqot’in decision). In that decision the SCC outlined areas over which the Tsilhqot’in Nation has proven and declared Aboriginal title. Proven and declared Aboriginal title lands are not considered Crown land. As such, those lands do not contribute to timber supply in the Williams Lake TSA and are excluded from the AFLB. A spatial data set of land ownership was developed using information from the Crown Land Registry and the Integrated Cadastral Information Society. Areas classified in this data set with ownership codes 62 (Forest Management Unit) or 69 (Community Watershed) are generally administered by the Province for TSA timber supply. These areas were reviewed by district staff to ensure all categories they contain can appropriately be considered AFLB for purposes of this analysis. Minor areas, including those identified as development project, institutional and residential, were excluded from the AFLB. Otherwise, the remaining area with these ownership codes will be modelled as managed for TSA timber supply. Areas classified with ownership code 99 (crown leases) are not generally managed for TSA timber supply but were similarly reviewed prior to this analysis. Minor areas, including those categorized as grazing leases, will be considered as contributing to TSA timber supply because harvesting that occurs on these lease areas contributes to the TSA harvest level. Table 4. Land ownership types Land ownership type Total area Area excluded Private 186,582 186,582 Federal 71,825 71,825 CFA and FNWL 244,692 244,692 Municipal and Leases 2,688 2,688 NStQ Interim Treaty Agreement 2,796 2,702 Tsilhqot’in Nation Title 193,216 188,544 Data source and comments: WHSE_FOREST_VEGETATION.F_OWN`
- FEMIC proposed logic: Treaty and title transfers requiring reviewed overlays review NStQ interim treaty parcels and Tsilhqot'in title lands with dedicated reviewed overlays before lock
- Linked source layers:
  - `whse_forest_vegetation_f_own` | query=`WHSE_FOREST_VEGETATION.F_OWN` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_FOREST_VEGETATION_F_OWN/WHSE_FOREST_VEGETATION_F_OWN.gpkg`
    - matched by: `object_name:WHSE_FOREST_VEGETATION.F_OWN`
    - top match: `Generalized Forest Cover Ownership`
- Logic mode: `femic_core`

### 3. Non-forest

- Parent step id: `thlb_parent_003_non_forest`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `1105908.000 ha`
- Benchmark cumulative remaining area: `3130694.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved on the Williams Lake landscape-unit smoke subset; pending definitive full-TSA validation after the remaining parent steps are soft-validated.
- Approved UTC: `2026-04-06T04:20:00+00:00`
- Approved by: `user_directed_review`
- Supporting prose section: `6.2.2 Land classified as non-forest`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=26`
- Draft subrules:
  - `thlb_parent_003_non_forest_draft_01` | summary=`All land classified as non-forest (alpine, lakes, swamp, brush, rock, etc.), non-productive forest (e.g., wetlands and avalanche tracks), or not typed (unreported) are excluded fro` | operation=`exclude` | review=`draft`
    - candidate layers: `freshwater_atlas`, `consolidated_harvest_depletion`
  - `thlb_parent_003_non_forest_draft_03` | summary=`The VRI attribute ‘Forest Management Land Base’ (FMLB) will be used to identify areas of non-forest.` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`
    - candidate fields: `FOR_MGMT_LAND_BASE_IND`
    - field/value mapping notes:
      - TSR prose refers to the VRI FMLB/Forest Management Land Base attribute; validate its mapping to the current FEMIC/VRI field before locking logic.
  - `thlb_parent_003_non_forest_draft_04` | summary=`The FMLB attribute categorizes land as forested if it is described as ‘treed’ under the British Columbia Land Cover Classification Scheme (BCLCS) and has a site index greater than ` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`
    - candidate fields: `FOR_MGMT_LAND_BASE_IND`
    - field/value mapping notes:
      - TSR prose refers to the VRI FMLB/Forest Management Land Base attribute; validate its mapping to the current FEMIC/VRI field before locking logic.
  - `thlb_parent_003_non_forest_draft_05` | summary=`Where the VRI has no data for site index or species composition, and no history of harvest, the area will be considered non-forest.` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`
  - `thlb_parent_003_non_forest_draft_06` | summary=`In addition to the FMLB criteria, areas with a crown closure less than 10% also be considered non-forest and will be excluded.` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`
    - candidate fields: `FOR_MGMT_LAND_BASE_IND`, `CROWN_CLOSURE`
    - candidate values: `< 10`
    - field/value mapping notes:
      - TSR prose refers to the VRI FMLB/Forest Management Land Base attribute; validate its mapping to the current FEMIC/VRI field before locking logic.
  - `thlb_parent_003_non_forest_draft_07` | summary=`Areas with low crown closure resulting from past harvest, losses from MPB (since 2002) or recent fire (since 2017) are exceptions that will remain in the AFLB.` | operation=`no_deduction` | review=`draft`
    - candidate layers: `vri`, `consolidated_harvest_depletion`
    - candidate fields: `CROWN_CLOSURE`
  - `thlb_parent_003_non_forest_draft_08` | summary=`A final check will use data from the Freshwater Atlas (FWA) data to ensure lakes, rivers and wetlands are appropriately excluded.` | operation=`exclude` | review=`draft`
    - candidate layers: `freshwater_atlas`
- Current compiled status summary: `ready`=2
- Last notebook run status: `applied`
- Last notebook removed area: `2015120.946 ha`
- Last notebook remaining area: `2922217.545 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_003_non_forest.20260406T194836Z.json`
- Compiled logic:

#### 3.1. Non-forest

- Step id: `thlb_parent_003_non_forest_compiled_01`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=26`
- TSR page: `26`
- TSR text: `All land classified as non-forest (alpine, lakes, swamp, brush, rock, etc.), non-productive forest (e.g., wetlands and avalanche tracks), or not typed (unreported) are excluded from the AFLB, unless they were harvested in the past. These areas do not contribute to forest management objectives such as seral objectives for landscape-level biodiversity. The VRI attribute ‘Forest Management Land Base’ (FMLB) will be used to identify areas of non-forest. The FMLB attribute categorizes land as forested if it is described as ‘treed’ under the British Columbia Land Cover Classification Scheme (BCLCS) and has a site index greater than or equal to five metres. Where the VRI has no data for site index or species composition, and no history of harvest, the area will be considered non-forest. In addition to the FMLB criteria, areas with a crown closure less than 10% also be considered non-forest and will be excluded. Areas with low crown closure resulting from past harvest, losses from MPB (since 2002) or recent fire (since 2017) are exceptions that will remain in the AFLB. A final check will use data from the Freshwater Atlas (FWA) data to ensure lakes, rivers and wetlands are appropriately excluded. Table 5. Land classified as non-forest Attributes Description Logging history Total area (hectares) Missing leading species and site index VRI leading species and site index are none, while FMLB = ‘Y’ No 9,374 Wetlands VRI FMLB defined as ‘Y’ No 50,191 Lakes VRI FMLB defined as ‘Y’ No 4,455 Rivers VRI FMLB defined as ‘Y’ No 741 Crown closure < 10% VRI FMLB defined as ‘Y’ No 4,413 Non-FMLB VRI FMLB defined as ‘N’ No 976,656 Data source and comments: Areas with a harvest history are identified using the consolidated harvest depletion layer produced by FAIB. There are no instances of treed alpine areas within the TSA. Treed wetlands are removed in the riparian reserve and riparian management zones netdown.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Logic mode: `femic_core`

#### 3.2. Freshwater Atlas final water check

- Step id: `thlb_parent_003_non_forest_compiled_02`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=26`
- TSR page: `26`
- TSR text: `All land classified as non-forest (alpine, lakes, swamp, brush, rock, etc.), non-productive forest (e.g., wetlands and avalanche tracks), or not typed (unreported) are excluded from the AFLB, unless they were harvested in the past. These areas do not contribute to forest management objectives such as seral objectives for landscape-level biodiversity. The VRI attribute ‘Forest Management Land Base’ (FMLB) will be used to identify areas of non-forest. The FMLB attribute categorizes land as forested if it is described as ‘treed’ under the British Columbia Land Cover Classification Scheme (BCLCS) and has a site index greater than or equal to five metres. Where the VRI has no data for site index or species composition, and no history of harvest, the area will be considered non-forest. In addition to the FMLB criteria, areas with a crown closure less than 10% also be considered non-forest and will be excluded. Areas with low crown closure resulting from past harvest, losses from MPB (since 2002) or recent fire (since 2017) are exceptions that will remain in the AFLB. A final check will use data from the Freshwater Atlas (FWA) data to ensure lakes, rivers and wetlands are appropriately excluded. Table 5. Land classified as non-forest Attributes Description Logging history Total area (hectares) Missing leading species and site index VRI leading species and site index are none, while FMLB = ‘Y’ No 9,374 Wetlands VRI FMLB defined as ‘Y’ No 50,191 Lakes VRI FMLB defined as ‘Y’ No 4,455 Rivers VRI FMLB defined as ‘Y’ No 741 Crown closure < 10% VRI FMLB defined as ‘Y’ No 4,413 Non-FMLB VRI FMLB defined as ‘N’ No 976,656 Data source and comments: Areas with a harvest history are identified using the consolidated harvest depletion layer produced by FAIB. There are no instances of treed alpine areas within the TSA. Treed wetlands are removed in the riparian reserve and riparian management zones netdown.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_basemapping_fwa_lakes_poly` | query=`WHSE_BASEMAPPING.FWA_LAKES_POLY` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_FWA_LAKES_POLY/WHSE_BASEMAPPING_FWA_LAKES_POLY.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.FWA_LAKES_POLY`
    - top match: `Freshwater Atlas Lakes`
  - `whse_basemapping_fwa_rivers_poly` | query=`WHSE_BASEMAPPING.FWA_RIVERS_POLY` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_FWA_RIVERS_POLY/WHSE_BASEMAPPING_FWA_RIVERS_POLY.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.FWA_RIVERS_POLY`
    - top match: `Freshwater Atlas Rivers`
  - `whse_basemapping_fwa_wetlands_poly` | query=`WHSE_BASEMAPPING.FWA_WETLANDS_POLY` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_FWA_WETLANDS_POLY/WHSE_BASEMAPPING_FWA_WETLANDS_POLY.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.FWA_WETLANDS_POLY`
    - top match: `Freshwater Atlas Wetlands`
- Logic mode: `femic_core`

### 4. Roads and landings

- Parent step id: `thlb_parent_004_roads_and_landings`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `50434.000 ha`
- Benchmark cumulative remaining area: `3080260.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved on the Williams Lake landscape-unit smoke subset; pending definitive full-TSA validation after the remaining parent steps are soft-validated.
- Approved UTC: `2026-04-06T04:22:30+00:00`
- Approved by: `user_directed_review`
- Supporting prose section: `6.2.3 Roads and landings`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- Draft subrules:
  - `thlb_parent_004_roads_and_landings_draft_02` | summary=`The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`, `whse_forest_tenure_ften_road_section_lines_svw`, `whse_forest_vegetation_veg_consolidated_cut_blocks_sp`, `whse_imagery_and_base_maps_mot_highway_profiles_sp`
  - `thlb_parent_004_roads_and_landings_draft_04` | summary=`Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially ` | operation=`exclude` | review=`draft`
    - candidate layers: `road_network`
  - `thlb_parent_004_roads_and_landings_draft_05` | summary=`To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these ` | operation=`exclude` | review=`draft`
    - candidate layers: `road_network`
  - `thlb_parent_004_roads_and_landings_draft_06` | summary=`The mapped non-status roads are known to be inaccurate, and the information is incomplete.` | operation=`exclude` | review=`draft`
    - candidate layers: `road_network`
  - `thlb_parent_004_roads_and_landings_draft_07` | summary=`Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-sta` | operation=`exclude` | review=`draft`
    - candidate layers: `road_network`
  - `thlb_parent_004_roads_and_landings_draft_08` | summary=`The estimated area within existing RTL maintained clearing widths is categorized below.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_basemapping_dra_dgtl_road_atlas_mpar_sp`, `whse_forest_tenure_ften_road_section_lines_svw`, `whse_forest_vegetation_veg_consolidated_cut_blocks_sp`, `whse_imagery_and_base_maps_mot_highway_profiles_sp`
  - `thlb_parent_004_roads_and_landings_draft_09` | summary=`On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations.` | operation=`exclude` | review=`draft`
    - candidate layers: `road_network`
  - `thlb_parent_004_roads_and_landings_draft_10` | summary=`They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate.` | operation=`exclude` | review=`draft`
    - candidate layers: `road_network`
- Current compiled status summary: `manual_review_required`=1, `ready`=2
- Last notebook run status: `applied`
- Last notebook removed area: `1557.111 ha`
- Last notebook remaining area: `75982.254 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_004_roads_and_landings.20260406T223553Z.json`
- Compiled logic:

#### 4.1. Existing public and resource roads

- Step id: `thlb_parent_004_roads_and_landings_compiled_01`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- TSR page: `27`
- TSR text: `The purpose of this section is to identify the portion of the land base that is occupied by roads, trails, and landings (RTL) that have been constructed to access and facilitate harvest operations. The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives. Separate estimates are made to reflect the loss in productive forest land due to existing and future RTL. Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially through partial reductions to the AFLB (i.e., the area considered to be AFLB within each hectare will be reduced by a percentage). To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these access features. Forest service roads and public roads were buffered 25 metres (12.5 metres from center line) and active/retired road permit roads were buffered 15 metres (7.5 metres from center line). The mapped non-status roads are known to be inaccurate, and the information is incomplete. Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-status roads will not impact future yield. The estimated area within existing RTL maintained clearing widths is categorized below. On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations. They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate. Table 6. Width and area of existing road to calculate reductions Road class Width (m) Hectares Forest Service roads 25 8,343 Ministry of Transportation and Infrastructure 25 6,280 Road permit and landings 15 19,641 Mapped non-status roads 5 16,169 Most harvesting now uses a roadside processing system, and landings are less common in current harvest systems. There are indications that some productivity loss is associated with the use of roadside harvesting systems, but no definitive research to date has quantified a level of productivity loss. In-block roads that are temporary in nature will have no deduction from the THLB. In total, 32 526 hectares will be excluded for all roads. Future roads, trails and landings The AFLB area removed to account for future RTL was estimated based on current performance and RESULTS data. The future RTL reduction will be applied to future harvested areas in the timber supply model after stands are harvested for the first time. Reduction factors for future RTL were calculated based on the average amount of on-block road permit structures with an estimated 15 metres width that have been observed in the five-year period from January 2015 to April 2021. The average factor is 2.28% for all three Cariboo TSAs. The yields of all stands aged 70 years and above will be reduced by this factor after they are harvested. In total, 22 754 hectares will be excluded from the forested land base at the time of first harvest to represent the area lost due to future road development. Data source and comments: Roads will be identified from forest tenure road mapping as roads with a description of ‘Forest Service Road’ or ‘Road Permit’ and have a status of ‘active’, ‘retired’ or ‘pending’. Digital road atlas mapping will also be used but will exclude roads classed as ‘resource’. The last five years of road construction in recent cutblocks were examined using existing road permit data for all three TSAs in the CNRR. Road lengths were derived from the following data sets from the BCGW. FSR 25 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Public 25 m WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP Road permit 15 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Non-status 5 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (Outside of cutblocks) On-block roads (temporary) 0 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (roads that are inside cutblocks harvested from 2015 to present using WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP) Note: Because there is overlap between the different types of roads, the following priority was used: public, FSR, permit, non-status. This means if a public road overlaps with any other type of road the area will be allocated to the public road. Removed all roads that fall over managed licences, tree farms, private, federal, and municipal lands. The LHLB is the portion of the AFLB where timber harvesting is legal, subject to forest management objectives and constraints. It excludes protected areas such as national parks, provincial parks, protected areas and legally established areas where timber harvesting is prohibited. Areas excluded from the LHLB are also excluded from the THLB.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_basemapping_dra_dgtl_road_atlas_mpar_sp` | query=`WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP/WHSE_BASEMAPPING_DRA_DGTL_ROAD_ATLAS_MPAR_SP.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP`
    - top match: `Digital Road Atlas (DRA) - Master Partially-Attributed Roads`
- Logic mode: `femic_core`

#### 4.2. Active or retired road permit roads

- Step id: `thlb_parent_004_roads_and_landings_compiled_02`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- TSR page: `27`
- TSR text: `The purpose of this section is to identify the portion of the land base that is occupied by roads, trails, and landings (RTL) that have been constructed to access and facilitate harvest operations. The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives. Separate estimates are made to reflect the loss in productive forest land due to existing and future RTL. Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially through partial reductions to the AFLB (i.e., the area considered to be AFLB within each hectare will be reduced by a percentage). To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these access features. Forest service roads and public roads were buffered 25 metres (12.5 metres from center line) and active/retired road permit roads were buffered 15 metres (7.5 metres from center line). The mapped non-status roads are known to be inaccurate, and the information is incomplete. Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-status roads will not impact future yield. The estimated area within existing RTL maintained clearing widths is categorized below. On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations. They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate. Table 6. Width and area of existing road to calculate reductions Road class Width (m) Hectares Forest Service roads 25 8,343 Ministry of Transportation and Infrastructure 25 6,280 Road permit and landings 15 19,641 Mapped non-status roads 5 16,169 Most harvesting now uses a roadside processing system, and landings are less common in current harvest systems. There are indications that some productivity loss is associated with the use of roadside harvesting systems, but no definitive research to date has quantified a level of productivity loss. In-block roads that are temporary in nature will have no deduction from the THLB. In total, 32 526 hectares will be excluded for all roads. Future roads, trails and landings The AFLB area removed to account for future RTL was estimated based on current performance and RESULTS data. The future RTL reduction will be applied to future harvested areas in the timber supply model after stands are harvested for the first time. Reduction factors for future RTL were calculated based on the average amount of on-block road permit structures with an estimated 15 metres width that have been observed in the five-year period from January 2015 to April 2021. The average factor is 2.28% for all three Cariboo TSAs. The yields of all stands aged 70 years and above will be reduced by this factor after they are harvested. In total, 22 754 hectares will be excluded from the forested land base at the time of first harvest to represent the area lost due to future road development. Data source and comments: Roads will be identified from forest tenure road mapping as roads with a description of ‘Forest Service Road’ or ‘Road Permit’ and have a status of ‘active’, ‘retired’ or ‘pending’. Digital road atlas mapping will also be used but will exclude roads classed as ‘resource’. The last five years of road construction in recent cutblocks were examined using existing road permit data for all three TSAs in the CNRR. Road lengths were derived from the following data sets from the BCGW. FSR 25 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Public 25 m WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP Road permit 15 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Non-status 5 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (Outside of cutblocks) On-block roads (temporary) 0 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (roads that are inside cutblocks harvested from 2015 to present using WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP) Note: Because there is overlap between the different types of roads, the following priority was used: public, FSR, permit, non-status. This means if a public road overlaps with any other type of road the area will be allocated to the public road. Removed all roads that fall over managed licences, tree farms, private, federal, and municipal lands. The LHLB is the portion of the AFLB where timber harvesting is legal, subject to forest management objectives and constraints. It excludes protected areas such as national parks, provincial parks, protected areas and legally established areas where timber harvesting is prohibited. Areas excluded from the LHLB are also excluded from the THLB.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_forest_tenure_ften_road_section_lines_svw` | query=`WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_FOREST_TENURE_FTEN_ROAD_SECTION_LINES_SVW/WHSE_FOREST_TENURE_FTEN_ROAD_SECTION_LINES_SVW.gpkg`
    - matched by: `object_name:WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW`
    - top match: `Forest Tenure Road Section Lines`
- Logic mode: `femic_core`

#### 4.3. Landings and temporary roads

- Step id: `thlb_parent_004_roads_and_landings_compiled_03`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `manual_review_required`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- TSR page: `27`
- TSR text: `The purpose of this section is to identify the portion of the land base that is occupied by roads, trails, and landings (RTL) that have been constructed to access and facilitate harvest operations. The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives. Separate estimates are made to reflect the loss in productive forest land due to existing and future RTL. Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially through partial reductions to the AFLB (i.e., the area considered to be AFLB within each hectare will be reduced by a percentage). To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these access features. Forest service roads and public roads were buffered 25 metres (12.5 metres from center line) and active/retired road permit roads were buffered 15 metres (7.5 metres from center line). The mapped non-status roads are known to be inaccurate, and the information is incomplete. Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-status roads will not impact future yield. The estimated area within existing RTL maintained clearing widths is categorized below. On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations. They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate. Table 6. Width and area of existing road to calculate reductions Road class Width (m) Hectares Forest Service roads 25 8,343 Ministry of Transportation and Infrastructure 25 6,280 Road permit and landings 15 19,641 Mapped non-status roads 5 16,169 Most harvesting now uses a roadside processing system, and landings are less common in current harvest systems. There are indications that some productivity loss is associated with the use of roadside harvesting systems, but no definitive research to date has quantified a level of productivity loss. In-block roads that are temporary in nature will have no deduction from the THLB. In total, 32 526 hectares will be excluded for all roads. Future roads, trails and landings The AFLB area removed to account for future RTL was estimated based on current performance and RESULTS data. The future RTL reduction will be applied to future harvested areas in the timber supply model after stands are harvested for the first time. Reduction factors for future RTL were calculated based on the average amount of on-block road permit structures with an estimated 15 metres width that have been observed in the five-year period from January 2015 to April 2021. The average factor is 2.28% for all three Cariboo TSAs. The yields of all stands aged 70 years and above will be reduced by this factor after they are harvested. In total, 22 754 hectares will be excluded from the forested land base at the time of first harvest to represent the area lost due to future road development. Data source and comments: Roads will be identified from forest tenure road mapping as roads with a description of ‘Forest Service Road’ or ‘Road Permit’ and have a status of ‘active’, ‘retired’ or ‘pending’. Digital road atlas mapping will also be used but will exclude roads classed as ‘resource’. The last five years of road construction in recent cutblocks were examined using existing road permit data for all three TSAs in the CNRR. Road lengths were derived from the following data sets from the BCGW. FSR 25 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Public 25 m WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP Road permit 15 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Non-status 5 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (Outside of cutblocks) On-block roads (temporary) 0 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (roads that are inside cutblocks harvested from 2015 to present using WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP) Note: Because there is overlap between the different types of roads, the following priority was used: public, FSR, permit, non-status. This means if a public road overlaps with any other type of road the area will be allocated to the public road. Removed all roads that fall over managed licences, tree farms, private, federal, and municipal lands. The LHLB is the portion of the AFLB where timber harvesting is legal, subject to forest management objectives and constraints. It excludes protected areas such as national parks, provincial parks, protected areas and legally established areas where timber harvesting is prohibited. Areas excluded from the LHLB are also excluded from the THLB.`
- FEMIC proposed logic: Landings and temporary roads requires non-spatial or additional harvested-area treatment logic
- Linked source layers:
  - `whse_forest_vegetation_veg_consolidated_cut_blocks_sp` | query=`WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_FOREST_VEGETATION_VEG_CONSOLIDATED_CUT_BLOCKS_SP/WHSE_FOREST_VEGETATION_VEG_CONSOLIDATED_CUT_BLOCKS_SP.gpkg`
    - matched by: `object_name:WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP`
    - top match: `Harvested Areas of BC (Consolidated Cutblocks)`
- Logic mode: `femic_core`

### 23. Future roads

- Parent step id: `thlb_parent_023_future_roads`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Ratchet state: `compiled`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `22754.000 ha`
- Supporting prose section: `6.2.3 Roads and landings`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- Draft subrules:
  - `thlb_parent_023_future_roads_draft_01` | summary=`Apply the TSR's future-RTL factor as an aspatial area reduction across the current AFLB working land base.` | operation=`aspatial_area_reduction` | review=`draft`
    - candidate values: `2.28% future RTL factor`, `22,754 ha total TSR benchmark`
    - field/value mapping notes:
      - Do not reuse the existing-roads spatial overlay logic for this parent step.
      - Do not model this step through THLB retention; reduce the stand-area fields that flow downstream into fragments instead.
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `13461.641 ha`
- Last notebook remaining area: `2905358.090 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_023_future_roads.20260409T041319Z.json`
- Compiled logic:

#### 23.1. Future roads, trails, and landings area reduction

- Step id: `thlb_parent_023_future_roads_compiled_01`
- Kind: `netdown_rule`
- Stage: `GLB -> AFLB`
- Execution class: `drop_from_universe`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=27`
- TSR page: `27`
- TSR text: `The purpose of this section is to identify the portion of the land base that is occupied by roads, trails, and landings (RTL) that have been constructed to access and facilitate harvest operations. The existing permanent RTL area will be removed from the AFLB and will not contribute to timber supply or biodiversity objectives. Separate estimates are made to reflect the loss in productive forest land due to existing and future RTL. Existing roads, trails and landings The area within RTL is typically too small to delineate and track efficiently in a landscape-level model so they will be modelled non-spatially through partial reductions to the AFLB (i.e., the area considered to be AFLB within each hectare will be reduced by a percentage). To estimate the current contribution of roads, a geographic information system (GIS) was used to buffer all road lines to estimate the area of productive forest land lost to these access features. Forest service roads and public roads were buffered 25 metres (12.5 metres from center line) and active/retired road permit roads were buffered 15 metres (7.5 metres from center line). The mapped non-status roads are known to be inaccurate, and the information is incomplete. Since it is impossible to estimate the future state of these roads, only the mapped non-status roads will be assumed to impact future yield, which assumes that the unmapped non-status roads will not impact future yield. The estimated area within existing RTL maintained clearing widths is categorized below. On-block (temporary) roads are those roads that are only used to access cutblocks for harvesting or silviculture operations. They are assigned a width of zero metres, as these temporary roads are either reforested by planting or fill in over time as stands regenerate. Table 6. Width and area of existing road to calculate reductions Road class Width (m) Hectares Forest Service roads 25 8,343 Ministry of Transportation and Infrastructure 25 6,280 Road permit and landings 15 19,641 Mapped non-status roads 5 16,169 Most harvesting now uses a roadside processing system, and landings are less common in current harvest systems. There are indications that some productivity loss is associated with the use of roadside harvesting systems, but no definitive research to date has quantified a level of productivity loss. In-block roads that are temporary in nature will have no deduction from the THLB. In total, 32 526 hectares will be excluded for all roads. Future roads, trails and landings The AFLB area removed to account for future RTL was estimated based on current performance and RESULTS data. The future RTL reduction will be applied to future harvested areas in the timber supply model after stands are harvested for the first time. Reduction factors for future RTL were calculated based on the average amount of on-block road permit structures with an estimated 15 metres width that have been observed in the five-year period from January 2015 to April 2021. The average factor is 2.28% for all three Cariboo TSAs. The yields of all stands aged 70 years and above will be reduced by this factor after they are harvested. In total, 22 754 hectares will be excluded from the forested land base at the time of first harvest to represent the area lost due to future road development. Data source and comments: Roads will be identified from forest tenure road mapping as roads with a description of ‘Forest Service Road’ or ‘Road Permit’ and have a status of ‘active’, ‘retired’ or ‘pending’. Digital road atlas mapping will also be used but will exclude roads classed as ‘resource’. The last five years of road construction in recent cutblocks were examined using existing road permit data for all three TSAs in the CNRR. Road lengths were derived from the following data sets from the BCGW. FSR 25 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Public 25 m WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP Road permit 15 m WHSE_FOREST_TENURE.FTEN_ROAD_SECTION_LINES_SVW (Active) Non-status 5 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (Outside of cutblocks) On-block roads (temporary) 0 m WHSE_BASEMAPPING.DRA_DGTL_ROAD_ATLAS_MPAR_SP (roads that are inside cutblocks harvested from 2015 to present using WHSE_FOREST_VEGETATION.VEG_CONSOLIDATED_CUT_BLOCKS_SP) Note: Because there is overlap between the different types of roads, the following priority was used: public, FSR, permit, non-status. This means if a public road overlaps with any other type of road the area will be allocated to the public road. Removed all roads that fall over managed licences, tree farms, private, federal, and municipal lands. The LHLB is the portion of the AFLB where timber harvesting is legal, subject to forest management objectives and constraints. It excludes protected areas such as national parks, provincial parks, protected areas and legally established areas where timber harvesting is prohibited. Areas excluded from the LHLB are also excluded from the THLB.`
- FEMIC proposed logic: Future roads, trails, and landings area reduction apply the TSR-cited future RTL deduction as an aspatial stand-area reduction across the AFLB working land base
- Logic mode: `femic_core`

### AFLB -> LHLB

### 6. Parks, protected areas, area-base tenures

- Parent step id: `thlb_parent_006_parks_protected_areas_area_base_tenures`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Ratchet state: `benchmarked`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `306327.000 ha`
- Benchmark cumulative remaining area: `2791841.000 ha`
- Ratchet note: Runnable on the Williams Lake landscape-unit smoke subset, but the current auto-runnable parks/protected-areas portion produced a no-signal result and the area-based tenure / woodlot sublogic remains review-driven. Hold for later validation on a more informative subset or after deeper automation.
- Supporting prose section: `6.3.1 Parks, protected areas, and small area-based tenures`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=28`
- Draft subrules:
  - `thlb_parent_006_parks_protected_areas_area_base_tenures_draft_01` | summary=`The parks, protected areas, and woodlots that were included in the AFLB to contribute to forest management objectives in the context of TSA timber supply, will be removed at this s` | operation=`no_deduction` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CLASS`
    - candidate values: `woodlot`
  - `thlb_parent_006_parks_protected_areas_area_base_tenures_draft_02` | summary=`A further check will be performed using current boundary mapping for woodlots, parks, and protected areas to ensure all areas were appropriately excluded.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CLASS`
    - candidate values: `woodlot`
  - `thlb_parent_006_parks_protected_areas_area_base_tenures_draft_03` | summary=`Woodlots that are no longer active will be included in the LHLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_vegetation_f_own`
    - candidate fields: `OWNERSHIP_CLASS`
    - candidate values: `woodlot`
- Current compiled status summary: `ready`=2
- Last notebook run status: `applied`
- Last notebook removed area: `275618.199 ha`
- Last notebook remaining area: `2701885.541 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_006_parks_protected_areas_area_base_tenures.20260407T223257Z.json`
- Compiled logic:

#### 6.1. Parks and protected areas

- Step id: `thlb_parent_006_parks_protected_areas_area_base_tenures_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=28`
- TSR page: `28`
- TSR text: `The parks, protected areas, and woodlots that were included in the AFLB to contribute to forest management objectives in the context of TSA timber supply, will be removed at this stage. A further check will be performed using current boundary mapping for woodlots, parks, and protected areas to ensure all areas were appropriately excluded. Woodlots that are no longer active will be included in the LHLB. Table 7. Parks, protected areas, and small area-based tenures Designations Total (ha) Forested (ha) Excluded (ha) Conservancy areas 596,471 260,215 260,028 Wildlife management areas 521 221 221 Heritage sites 106 81 78 Miscellaneous reserves 271,808 184,769 11,586 Woodlots 35,789 34,133 33,217 Crown and miscellaneous leases 31,049 24,842 1,197`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_tantalis_ta_park_ecores_pa_svw` | query=`WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_TANTALIS_TA_PARK_ECORES_PA_SVW/WHSE_TANTALIS_TA_PARK_ECORES_PA_SVW.gpkg`
    - matched by: `object_name:WHSE_TANTALIS.TA_PARK_ECORES_PA_SVW`
    - top match: `BC Parks, Ecological Reserves, and Protected Areas`
- Logic mode: `femic_core`

#### 6.2. Area-based tenures and woodlots

- Step id: `thlb_parent_006_parks_protected_areas_area_base_tenures_compiled_02`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=28`
- TSR page: `28`
- TSR text: `The parks, protected areas, and woodlots that were included in the AFLB to contribute to forest management objectives in the context of TSA timber supply, will be removed at this stage. A further check will be performed using current boundary mapping for woodlots, parks, and protected areas to ensure all areas were appropriately excluded. Woodlots that are no longer active will be included in the LHLB. Table 7. Parks, protected areas, and small area-based tenures Designations Total (ha) Forested (ha) Excluded (ha) Conservancy areas 596,471 260,215 260,028 Wildlife management areas 521 221 221 Heritage sites 106 81 78 Miscellaneous reserves 271,808 184,769 11,586 Woodlots 35,789 34,133 33,217 Crown and miscellaneous leases 31,049 24,842 1,197`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_forest_vegetation_f_own` | query=`WHSE_FOREST_VEGETATION.F_OWN` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_FOREST_VEGETATION_F_OWN/WHSE_FOREST_VEGETATION_F_OWN.gpkg`
    - matched by: `object_name:WHSE_FOREST_VEGETATION.F_OWN`
    - top match: `Generalized Forest Cover Ownership`
- Logic mode: `femic_core`

### 7. Old growth management areas

- Parent step id: `thlb_parent_007_old_growth_management_areas`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `210719.000 ha`
- Benchmark cumulative remaining area: `2581122.000 ha`
- Approval: `soft-approved`
- Approval scope: `full_tsa_validation`
- Approval note: Soft-approved after full-TSA validation. Step 7 now follows TSA29 section 6.3.2 more faithfully by excluding only PERM and ROT legal OGMAs in the executable base-case mask while keeping transition OGMAs as contextual/temporal follow-up logic.
- Approved UTC: `2026-04-06T04:45:00+00:00`
- Approved by: `user_directed_review`
- Ratchet note: Soft-approved after full-TSA validation using the narrowed PERM/ROT-only legal OGMA mask. Keep transition OGMA timing/restoration and harvest-exception logic out of the base executable exclusion surface for now.
- Supporting prose section: `6.3.2 Old growth management areas`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- Draft subrules:
  - `thlb_parent_007_old_growth_management_areas_draft_01` | summary=`Permanent and Permanent-Rotating Old Growth Management Areas (OGMA) are removed from the LHLB as no harvest areas.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_02` | summary=`A limited amount of harvest is permitted in OGMAs for specified exceptions including insect control and wildfire risk reduction treatments.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_03` | summary=`Loss of OGMAs for other reasons such as Land Act tenure overlap must be replaced with equivalent area in the same BEC subzone within the same landscape unit.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_04` | summary=`This replacement process ensures that OGMA targets are maintained over time and result in no impact to timber supply.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_05` | summary=`Transition OGMAs will cease to exist in 2030.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_06` | summary=`Until then they are available for harvest if conifer mortality exceeds 50%.` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
  - `thlb_parent_007_old_growth_management_areas_draft_07` | summary=`It is assumed that any such harvest has already occurred in Transition OGMAs, therefore Transition OGMAs will be removed from the LHLB until 2030 after which they will be fully res` | operation=`exclude` | review=`draft`
    - candidate layers: `rmp_ogma_legal`, `whse_land_use_planning_rmp_ogma_legal`
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `227336.336 ha`
- Last notebook remaining area: `2474549.205 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_007_old_growth_management_areas.20260408T004016Z.json`
- Compiled logic:

#### 7.1. Old growth management areas

- Step id: `thlb_parent_007_old_growth_management_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- TSR page: `29`
- TSR text: `Permanent and Permanent-Rotating Old Growth Management Areas (OGMA) are removed from the LHLB as no harvest areas. A limited amount of harvest is permitted in OGMAs for specified exceptions including insect control and wildfire risk reduction treatments. Loss of OGMAs for other reasons such as Land Act tenure overlap must be replaced with equivalent area in the same BEC subzone within the same landscape unit. This replacement process ensures that OGMA targets are maintained over time and result in no impact to timber supply. Transition OGMAs will cease to exist in 2030. Until then they are available for harvest if conifer mortality exceeds 50%. It is assumed that any such harvest has already occurred in Transition OGMAs, therefore Transition OGMAs will be removed from the LHLB until 2030 after which they will be fully restored to the LHLB. Table 8. Old growth management areas Designations Total (ha) Forested (ha) Excluded (ha) Permanent and rotating 292,759 211,183 210,719 Transitional 105,888 80,835`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `rmp_ogma_legal` | query=`RMP_OGMA_LEGAL` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_OGMA_LEGAL/RMP_OGMA_LEGAL.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_OGMA_LEGAL_CURRENT_SVW`
    - top match: `Old Growth Management Areas - Legal - Current`
- Logic mode: `femic_core`

### 8. Wildlife habitat areas

- Parent step id: `thlb_parent_008_wildlife_habitat_areas`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `154056.000 ha`
- Benchmark cumulative remaining area: `2427066.000 ha`
- Approval: `soft-approved`
- Approval scope: `full_tsa_validation`
- Approval note: Soft-approved after full-TSA validation. Step 8 keeps the TSA29 section 6.3.3 contract intact by excluding only no-harvest wildlife zones while deferring conditional harvest zones to later assumptions logic, and the full-TSA result is reasonably close to the Table 3 benchmark.
- Approved UTC: `2026-04-08T01:05:00+00:00`
- Approved by: `user_directed_review`
- Ratchet note: Soft-approved after full-TSA validation using the no-harvest-only wildlife exclusion mask. Keep conditional harvest zones deferred to later assumptions and silviculture logic.
- Supporting prose section: `6.3.3 Wildlife habitat areas`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- Draft subrules:
  - `thlb_parent_008_wildlife_habitat_areas_draft_01` | summary=`Wildlife habitat reductions may be identified and managed through several processes including the Identified Wildlife Management Strategy, identification, and approval of ungulate ` | operation=`exclude` | review=`draft`
    - candidate layers: `wildlife_habitat`
  - `thlb_parent_008_wildlife_habitat_areas_draft_02` | summary=`Management practices may include no harvesting in core areas as well as modified harvesting in associated management zones.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_008_wildlife_habitat_areas_draft_03` | summary=`Several approved wildlife habitat areas (WHA) are designated within the CNRR.` | operation=`exclude` | review=`draft`
    - candidate layers: `wildlife_habitat`
  - `thlb_parent_008_wildlife_habitat_areas_draft_04` | summary=`The associated General Wildlife Measures (GWM) established by ministerial order under the GARs guide harvest practices in WHAs.` | operation=`exclude` | review=`draft`
    - candidate layers: `wildlife_habitat`
  - `thlb_parent_008_wildlife_habitat_areas_draft_05` | summary=`Areas designated through GWMs as “no harvest” will be excluded from the LHLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `wildlife_habitat`
  - `thlb_parent_008_wildlife_habitat_areas_draft_06` | summary=`Areas designated as “conditional harvest zone” will be addressed in Section 7 – ‘Current forest management assumptions’ and Section 7.1.8 – ‘Silviculture systems’.` | operation=`exclude` | review=`draft`
    - candidate layers: `wildlife_habitat`
    - candidate fields: `TIMBER_HARVEST_CODE`
    - candidate values: `CONDITIONAL HARVEST ZONE`
- Current compiled status summary: `manual_review_required`=1, `ready`=2
- Last notebook run status: `applied`
- Last notebook removed area: `133005.883 ha`
- Last notebook remaining area: `2341543.322 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_008_wildlife_habitat_areas.20260408T005044Z.json`
- Compiled logic:

#### 8.1. Ungulate winter range no-harvest polygons

- Step id: `thlb_parent_008_wildlife_habitat_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- TSR page: `29`
- TSR text: `Wildlife habitat reductions may be identified and managed through several processes including the Identified Wildlife Management Strategy, identification, and approval of ungulate winter range (UWR), and management practices specified in plans such as the CCLUP that establish legal wildlife habitat objectives. Management practices may include no harvesting in core areas as well as modified harvesting in associated management zones. Several approved wildlife habitat areas (WHA) are designated within the CNRR. The associated General Wildlife Measures (GWM) established by ministerial order under the GARs guide harvest practices in WHAs. Areas designated through GWMs as “no harvest” will be excluded from the LHLB. Areas designated as “conditional harvest zone” will be addressed in Section 7 – ‘Current forest management assumptions’ and Section 7.1.8 – ‘Silviculture systems’. Table 9. Wildlife habitat areas Designations Total (ha) Forested (ha) Excluded (ha) UWR no-harvest area 25 23 23 Caribou no-harvest area 208,868 163,217 154,033 There is a Caribou Herd Planning process currently ongoing within the CNRR. The outcome of additional area protection through no harvest or modified harvest resulting from this process are currently unknown. There may potentially be additional protections put in place for caribou that will have a downward pressure on the timber supply. Ministry staff will stay informed on the progress of this working group and inform the TSR throughout the process.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_wildlife_management_wcp_ungulate` | query=`WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE.gpkg`
    - matched by: `object_name:WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE_SP`
    - top match: `Ungulate Winter Range - Approved`
  - `wcp_ungulate_winter_range` | query=`WCP_UNGULATE_WINTER_RANGE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WCP_UNGULATE_WINTER_RANGE/WCP_UNGULATE_WINTER_RANGE.gpkg`
    - matched by: `object_name_suffix:WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE_SP`
    - top match: `Ungulate Winter Range - Approved`
- Logic mode: `femic_core`

#### 8.2. Wildlife habitat area no-harvest polygons

- Step id: `thlb_parent_008_wildlife_habitat_areas_compiled_02`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- TSR page: `29`
- TSR text: `Wildlife habitat reductions may be identified and managed through several processes including the Identified Wildlife Management Strategy, identification, and approval of ungulate winter range (UWR), and management practices specified in plans such as the CCLUP that establish legal wildlife habitat objectives. Management practices may include no harvesting in core areas as well as modified harvesting in associated management zones. Several approved wildlife habitat areas (WHA) are designated within the CNRR. The associated General Wildlife Measures (GWM) established by ministerial order under the GARs guide harvest practices in WHAs. Areas designated through GWMs as “no harvest” will be excluded from the LHLB. Areas designated as “conditional harvest zone” will be addressed in Section 7 – ‘Current forest management assumptions’ and Section 7.1.8 – ‘Silviculture systems’. Table 9. Wildlife habitat areas Designations Total (ha) Forested (ha) Excluded (ha) UWR no-harvest area 25 23 23 Caribou no-harvest area 208,868 163,217 154,033 There is a Caribou Herd Planning process currently ongoing within the CNRR. The outcome of additional area protection through no harvest or modified harvest resulting from this process are currently unknown. There may potentially be additional protections put in place for caribou that will have a downward pressure on the timber supply. Ministry staff will stay informed on the progress of this working group and inform the TSR throughout the process.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_wildlife_management_wcp_wildlife` | query=`WHSE_WILDLIFE_MANAGEMENT.WCP_WILDLIFE` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_WILDLIFE_MANAGEMENT_WCP_WILDLIFE/WHSE_WILDLIFE_MANAGEMENT_WCP_WILDLIFE.gpkg`
    - matched by: `object_name_stem:WHSE_WILDLIFE_MANAGEMENT.WCP_WILDLIFE_HABITAT_AREA_POLY`
    - top match: `Wildlife Habitat Areas - Approved`
- Logic mode: `femic_core`

#### 8.3. Conditional harvest wildlife zones

- Step id: `thlb_parent_008_wildlife_habitat_areas_compiled_03`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `manual_review_required`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=29`
- TSR page: `29`
- TSR text: `Wildlife habitat reductions may be identified and managed through several processes including the Identified Wildlife Management Strategy, identification, and approval of ungulate winter range (UWR), and management practices specified in plans such as the CCLUP that establish legal wildlife habitat objectives. Management practices may include no harvesting in core areas as well as modified harvesting in associated management zones. Several approved wildlife habitat areas (WHA) are designated within the CNRR. The associated General Wildlife Measures (GWM) established by ministerial order under the GARs guide harvest practices in WHAs. Areas designated through GWMs as “no harvest” will be excluded from the LHLB. Areas designated as “conditional harvest zone” will be addressed in Section 7 – ‘Current forest management assumptions’ and Section 7.1.8 – ‘Silviculture systems’. Table 9. Wildlife habitat areas Designations Total (ha) Forested (ha) Excluded (ha) UWR no-harvest area 25 23 23 Caribou no-harvest area 208,868 163,217 154,033 There is a Caribou Herd Planning process currently ongoing within the CNRR. The outcome of additional area protection through no harvest or modified harvest resulting from this process are currently unknown. There may potentially be additional protections put in place for caribou that will have a downward pressure on the timber supply. Ministry staff will stay informed on the progress of this working group and inform the TSR throughout the process.`
- FEMIC proposed logic: Conditional harvest wildlife zones defer conditional harvest zone treatment to later silviculture and assumptions logic
- Linked source layers:
  - `whse_wildlife_management_wcp_ungulate` | query=`WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE/WHSE_WILDLIFE_MANAGEMENT_WCP_UNGULATE.gpkg`
    - matched by: `object_name:WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE_SP`
    - top match: `Ungulate Winter Range - Approved`
  - `whse_wildlife_management_wcp_wildlife` | query=`WHSE_WILDLIFE_MANAGEMENT.WCP_WILDLIFE` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_WILDLIFE_MANAGEMENT_WCP_WILDLIFE/WHSE_WILDLIFE_MANAGEMENT_WCP_WILDLIFE.gpkg`
    - matched by: `object_name_stem:WHSE_WILDLIFE_MANAGEMENT.WCP_WILDLIFE_HABITAT_AREA_POLY`
    - top match: `Wildlife Habitat Areas - Approved`
  - `wcp_ungulate_winter_range` | query=`WCP_UNGULATE_WINTER_RANGE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WCP_UNGULATE_WINTER_RANGE/WCP_UNGULATE_WINTER_RANGE.gpkg`
    - matched by: `object_name_suffix:WHSE_WILDLIFE_MANAGEMENT.WCP_UNGULATE_WINTER_RANGE_SP`
    - top match: `Ungulate Winter Range - Approved`
- Logic mode: `femic_core`

### 9. Critical habitat for fish

- Parent step id: `thlb_parent_009_critical_habitat_for_fish`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `11521.000 ha`
- Benchmark cumulative remaining area: `2415545.000 ha`
- Ratchet note: Full-TSA validation brought step 9 into the right benchmark regime. Residual overcut versus the TSR benchmark was judged acceptable and the step is green-lit so the TSA29 ladder can keep moving.
- Supporting prose section: `6.3.4 Critical habitat for fish`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- Draft subrules:
  - `thlb_parent_009_critical_habitat_for_fish_draft_01` | summary=`Use the legal CCLUP critical-fish-habitat polygons from the Section 93.4 LAO / Map 4 source, not wildlife proxy layers.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_rmp_plan_legal_poly_svw`
    - candidate fields: `STRGC_LAND_RSRCE_PLAN_NAME`, `LEGAL_FEAT_OBJECTIVE`, `LEGAL_FEAT_ATRB_1_VALUE`
    - candidate values: `Cariboo Chilcotin Land Use Plan`, `Critical Habitat for Fish`, `CRITFISH`
    - field/value mapping notes:
      - Keep the executable query inside the legal-planning fish-objective layer.
      - Do not revert to wildlife-habitat proxy layers for this parent step.
  - `thlb_parent_009_critical_habitat_for_fish_draft_02` | summary=`Treat the mapped critical-fish-habitat polygons as no-harvest areas within the LHLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_rmp_plan_legal_poly_svw`
    - candidate values: `no harvest`, `Section 93.4 LAO`
    - field/value mapping notes:
      - If later refinement is needed, narrow the legal fish-objective attributes rather than swapping data sources.
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `17482.824 ha`
- Last notebook remaining area: `2324060.498 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_009_critical_habitat_for_fish.20260408T063444Z.json`
- Compiled logic:

#### 9.1. Critical fish habitat

- Step id: `thlb_parent_009_critical_habitat_for_fish_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- TSR page: `30`
- TSR text: `Areas of critical habitat for fish that require protection and site-specific management actions were identified as part of the LAO. The LAO specifies that the areas are to be maintained as no-harvest areas. Critical fish habitat will be excluded from the LHLB. Table 10. Critical habitat for fish Designations Total (ha) Forested (ha) Excluded (ha) Critical habitat for fish 51,553 20,501 11,521 Data source and comments: Critical fish habitat area boundaries are from the Section 93.4 LAO establishing objectives for the CCLUP, May 19, 2010, amended April 18, 2011, and consolidated to September 6, 2018. Map 4.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`

### 10. Lakeshore management

- Parent step id: `thlb_parent_010_lakeshore_management`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `327.000 ha`
- Benchmark cumulative remaining area: `2415218.000 ha`
- Approval: `soft-approved`
- Approval scope: `full_tsa_trivial_benchmark_skip`
- Approval note: User-directed skip after source review. TSA29 step 10 is only a 327 ha benchmark on a 5 million ha landscape and the currently adopted public layers do not yet expose a trusted Class A lake discriminator, so detailed validation is deferred.
- Approved UTC: `2026-04-08T07:35:00+00:00`
- Approved by: `user_directed_review`
- Ratchet note: Trivial TSR benchmark area; detailed TSA29 validation skipped by user direction. Keep this step out of the active blocker set and revisit only if a trustworthy Class A lake source is later adopted.
- Supporting prose section: `6.3.5 Lakeshore management`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- Draft subrules:
  - `thlb_parent_010_lakeshore_management_draft_01` | summary=`Only the no-harvest overlap between Class A lake management areas and VQO preservation should be excluded here.` | operation=`review` | review=`draft`
    - candidate layers: `whse_land_use_planning_rmp_plan_legal_poly_svw`, `whse_forest_vegetation_rec_visual_landscape`
    - candidate fields: `LEGAL_FEAT_OBJECTIVE`, `LEGAL_FEAT_ATRB_2_VALUE`, `REC_EVQO_CODE`
    - candidate values: `Scenic Areas / Scenic Corridors`, `PR`, `Class A lake subset still required`
    - field/value mapping notes:
      - The currently adopted public layers do not yet expose a trusted Class A lake discriminator for TSA29.
      - Do not use the whole scenic-PR legal surface as a surrogate; it overcuts badly.
  - `thlb_parent_010_lakeshore_management_draft_02` | summary=`Class B-E lakes are not excluded here; they are handled later through Section 7.2.6 disturbance assumptions.` | operation=`reference_only` | review=`draft`
    - candidate values: `Section 7.2.6 later assumptions`
    - field/value mapping notes:
      - This step is tiny in the TSR benchmark and is being skipped for detailed TSA29 validation.
- Current compiled status summary: `manual_review_required`=1
- Compiled logic:

#### 10.1. Class A lakes with preservation VQO overlap

- Step id: `thlb_parent_010_lakeshore_management_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `manual_review_required`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- TSR page: `30`
- TSR text: `The LAO designates a selection of lakes as Class A lakes which includes a legal spatial data set that defines buffers around these lakes and are classified are considered to be no harvest areas when they overlap with visual quality objective class ‘preservation’. These areas of overlap will be excluded from the LHLB. The management of Class B to E lakes through limits on allowed disturbance area will be discussed in Section 7.2.6 – ‘Lakeshore management’. Table 11. Class A lakes Designations Total (ha) Forested (ha) Excluded (ha) Class A Lakes 18,988 13,060 327 Data source and comments: The Class A lakes are identified in the Section 93.4 LAO establishing objectives for the CCLUP, May 19, 2010, amended April 18, 2011, and consolidated to September 6, 2018. Map 6. Lake management zone boundaries are provided by the lake buffer mapping that also provides riparian management and reserve zones for lakes used in Section 5.4.1.`
- FEMIC proposed logic: Class A lakes with preservation VQO overlap exclude only the Class A lake legal buffer areas that overlap VQO preservation once a trusted Class A lake source is adopted
- Linked source layers:
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
  - `whse_forest_vegetation_rec_visual_landscape` | query=`WHSE_FOREST_VEGETATION.REC_VISUAL_LANDSCAPE` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_FOREST_VEGETATION_REC_VISUAL_LANDSCAPE/WHSE_FOREST_VEGETATION_REC_VISUAL_LANDSCAPE.gpkg`
    - matched by: `object_name:WHSE_FOREST_VEGETATION.REC_VISUAL_LANDSCAPE_INVENTORY`
    - top match: `Visual Landscape Inventory`
- Logic mode: `femic_core`

### 11. Community areas of special concern

- Parent step id: `thlb_parent_011_community_areas_of_special_concern`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `62460.000 ha`
- Benchmark cumulative remaining area: `2352758.000 ha`
- Approval: `soft-approved`
- Approval scope: `full_tsa_validation`
- Approval note: Full-TSA cached 8-bundle run removed 69,545.637 ha against the TSR benchmark 62,460 ha. Residual overcut is small enough to accept as good enough for forward progress.
- Approved UTC: `2026-04-08T07:25:00+00:00`
- Approved by: `user_directed_review`
- Ratchet note: Green-lit on the full-TSA basis after narrowing the executable logic to the legal CCLUP / LUO polygons for Community Areas of Special Concern. The full-TSA run removed 69,545.637 ha against the 62,460 ha TSR benchmark, which is close enough to accept and move on.
- Supporting prose section: `6.3.7 Community areas of special concern (CASC)`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- Draft subrules:
  - `thlb_parent_011_community_areas_of_special_concern_draft_01` | summary=`Exclude the legal LUO / CCLUP Map 5 community areas of special concern polygons from the harvestable land base.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_land_use_planning_rmp_plan_legal_poly_svw`
    - candidate fields: `STRGC_LAND_RSRCE_PLAN_NAME`, `LEGAL_FEAT_OBJECTIVE`
    - candidate values: `Cariboo Chilcotin Land Use Plan`, `Community Areas of Special Concern`
    - field/value mapping notes:
      - Use the legal planning polygons for the CCLUP / LUO Map 5 boundaries.
      - Do not substitute broad designated-area overlays or unrelated disturbance layers.
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `69545.637 ha`
- Last notebook remaining area: `2254514.861 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_011_community_areas_of_special_concern.20260408T072034Z.json`
- Compiled logic:

#### 11.1. Community areas of special concern

- Step id: `thlb_parent_011_community_areas_of_special_concern_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Community areas of special concern are spatially delineated areas that have been designated as no-harvest areas in the LUO to address a mix of CCLUP objectives. Community areas of special concern are excluded from the THLB. Table 13. Community areas of special concern Designation Total (ha) Forested (ha) Excluded (ha) Community areas of special concern 436,210 69,346 62,460 Data source and comments: The community areas of special concern boundaries are from the Land Use Order Objectives for the Cariboo-Chilcotin Land Use Plan, May 19, 2010, Map 5. No changes were made to the mapped boundaries for CASC in the 2011 amendment. 6.4. Identification of the Timber Harvesting Land Base The THLB is the portion of the LHLB where timber harvesting is expected to occur in the context of the timber supply analysis supporting this AAC determination.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`

### 12. Proven Aboriginal Rights areas

- Parent step id: `thlb_parent_012_proven_aboriginal_rights_areas`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `68401.000 ha`
- Benchmark cumulative remaining area: `2284357.000 ha`
- Approval: `soft-approved`
- Approval scope: `full_tsa_public_data_unavailable_skip`
- Approval note: User-directed skip for public-data-only research/teaching use. The TSR logic is documented, but the cited/public PRA boundary path is not publicly downloadable/queryable enough to support a trustworthy automated exclusion surface.
- Ratchet note: Backing PRA boundary data is not publicly available enough for defensible automation. Skip detailed validation for the public-data-only FEMIC lane and revisit only if a vetted public/reviewed PRA boundary source is later adopted.
- Supporting prose section: `6.4.1 Proven Aboriginal Rights area`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- Draft subrules:
  - `thlb_parent_012_proven_aboriginal_rights_areas_draft_01` | summary=`Exclude the Proven Aboriginal Rights area from the THLB to reflect the current lack of commercial forestry activity and the unique consultation / authorization regime.` | operation=`review` | review=`draft`
    - candidate layers: `whse_admin_boundaries_pip_consultation`
    - candidate fields: `boundary source still required`
    - candidate values: `Proven Aboriginal Rights area boundary`
    - field/value mapping notes:
      - The PRA is not the same thing as the proven Aboriginal title area and extends beyond the court case area.
      - Do not substitute the title area, caretaker area, TSA boundary, or broad ownership layers for the PRA boundary.
  - `thlb_parent_012_proven_aboriginal_rights_areas_draft_02` | summary=`Keep the logic manual until a reviewed PRA boundary source is adopted into the instance.` | operation=`manual_review_required` | review=`draft`
    - candidate layers: `whse_admin_boundaries_pip_consultation`
    - candidate values: `reviewed PRA boundary override required`
    - field/value mapping notes:
      - Older-cycle TSR material clarifies the distinction between title, caretaker-area, and PRA concepts, but still does not provide a stable public PRA vector source for automation.
- Current compiled status summary: `manual_review_required`=1
- Compiled logic:

#### 12.1. Proven Aboriginal Rights area boundary

- Step id: `thlb_parent_012_proven_aboriginal_rights_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `AFLB -> LHLB`
- Execution class: `legal_harvest_exclusion`
- Run status: `manual_review_required`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `The Tsilhqot’in 2012 BC Supreme Court decision confirmed a proven Aboriginal rights area (PRA) where Tsilhqot’in people hold rights to hunt and trap birds and animals. This area overlaps the Tsilhqot’in proven and declared Aboriginal title area and extends beyond encompassing the entire court case area. This area, outside the title area, is still administered by the Province and contributes to timber supply within the Williams Lake TSA. Deep consultation is required when considering proposed authorizations in this area and since 2014, very few provincial authorizations have been made in this area because management expectations are unique. The PRA will be excluded from the THLB to reflect the lack of commercial forestry activity in the last nine years. Table 14. Proven Aboriginal Rights areas Designations Total (ha) Forested (ha) Excluded (ha) Proven Aboriginal Rights areas 432,155 123,369 68,401`
- FEMIC proposed logic: Proven Aboriginal Rights area boundary requires a reviewed PRA boundary overlay before automation; do not auto-exclude with broad TSA or designated-area polygons
- Linked source layers:
  - `whse_admin_boundaries_pip_consultation` | query=`WHSE_ADMIN_BOUNDARIES.PIP_CONSULTATION` | status=`no_hit` | strategy=`override_required`
  - `whse_land_use_planning_fadm_designated` | query=`WHSE_LAND_USE_PLANNING.FADM_DESIGNATED` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_FADM_DESIGNATED/WHSE_LAND_USE_PLANNING_FADM_DESIGNATED.gpkg`
    - matched by: `object_name:WHSE_ADMIN_BOUNDARIES.FADM_DESIGNATED_AREAS`
    - top match: `FADM - Designated Areas`
- Logic mode: `femic_core`

### LHLB -> THLB

### 13. Areas considered inoperable

- Parent step id: `thlb_parent_013_areas_considered_inoperable`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `33533.000 ha`
- Benchmark cumulative remaining area: `2250824.000 ha`
- Approval: `soft-approved`
- Approval scope: `full_tsa_user_directed_acceptance`
- Approval note: User directed acceptance on the attribute-first 40% west-side run so the TSA29 validation lane can proceed to step 14. The accepted run removed 43,628.139 ha against the TSR benchmark of 33,533 ha, with 16.620 ha from the terrain branch and 43,611.519 ha from the steep-slope branch; keep that overcut caveat explicit for any future refinement.
- Approved UTC: `2026-04-08T20:08:00Z`
- Approved by: `user_directive`
- Ratchet note: Approved by user direction on the attribute-first full-TSA 40% west-side run so the validation pass can move forward. The accepted run still overcuts materially versus the TSR benchmark, so treat the result as an accepted bridge for onward TSA29 work rather than as a reconciled final model of TSR step 13.
- Supporting prose section: `6.4.3 Areas considered inoperable`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=32`
  - `reference/res_xSteepSlopeLogging.pdf#page=1`
- Draft subrules:
  - `thlb_parent_013_areas_considered_inoperable_draft_01` | summary=`Areas that are inoperable within the TSA are generally associated with steep slopes.` | operation=`exclude` | review=`draft`
    - candidate layers: `terrain_stability`
  - `thlb_parent_013_areas_considered_inoperable_draft_02` | summary=`Also, steep slopes require the use of different harvest systems such as cable logging which may be uneconomic depending on volume per hectare.` | operation=`exclude` | review=`draft`
    - candidate layers: `terrain_stability`
  - `thlb_parent_013_areas_considered_inoperable_draft_03` | summary=`Inoperable areas will be identified as follows: • Slopes that exceed 70% east of Highway 97.` | operation=`exclude` | review=`draft`
    - candidate layers: `terrain_stability`
- Current compiled status summary: `ready`=2
- Last notebook run status: `applied`
- Last notebook removed area: `43628.139 ha`
- Last notebook remaining area: `2210886.722 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_013_areas_considered_inoperable.20260408T171029Z.json`
- Compiled logic:

#### 13.1. Unstable terrain and terrain class 5

- Step id: `thlb_parent_013_areas_considered_inoperable_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=32`
- TSR page: `32`
- TSR text: `Areas that are inoperable within the TSA are generally associated with steep slopes. Steep slopes are unlikely to be harvested because of unstable terrain and sensitive soils. Also, steep slopes require the use of different harvest systems such as cable logging which may be uneconomic depending on volume per hectare. Inoperable areas will be identified as follows: • Slopes that exceed 70% east of Highway 97. Harvesting on slopes between 40% and 70%, and cable harvesting has been employed as a past practice east of Highway 97. • Slopes that exceed 40% west of Highway 97. These slopes typically have lower volume per hectare which generally makes these types unsuitable for harvesting. • Slopes classified as Unstable (U) or Terrain Class 5. Table 16. Areas considered inoperable Designations Total (ha) Forested (ha) Excluded (ha) Steep slopes 491,492 92,748 31,974 Unstable terrain 15,051 3,923 1,559 Data source and comments: Slope angle is derived from the provincial digital elevation model.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_terrain_stability` | query=`REG_LAND_AND_NATURAL_RESOURCE.TERRAIN_STABILITY` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_TERRAIN_STABILITY/REG_LAND_AND_NATURAL_RESOURCE_TERRAIN_STABILITY.gpkg`
    - matched by: `object_name:WHSE_TERRESTRIAL_ECOLOGY.STE_TER_STABILITY_POLYS_SVW`
    - top match: `Terrain Stability Mapping (TSM) Detailed Polygons with Short Attribute Table Spatial View`
- Logic mode: `femic_core`

#### 13.2. Steep slope thresholds east and west of Highway 97

- Step id: `thlb_parent_013_areas_considered_inoperable_compiled_02`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=32`
- TSR page: `32`
- TSR text: `Areas that are inoperable within the TSA are generally associated with steep slopes. Steep slopes are unlikely to be harvested because of unstable terrain and sensitive soils. Also, steep slopes require the use of different harvest systems such as cable logging which may be uneconomic depending on volume per hectare. Inoperable areas will be identified as follows: • Slopes that exceed 70% east of Highway 97. Harvesting on slopes between 40% and 70%, and cable harvesting has been employed as a past practice east of Highway 97. • Slopes that exceed 40% west of Highway 97. These slopes typically have lower volume per hectare which generally makes these types unsuitable for harvesting. • Slopes classified as Unstable (U) or Terrain Class 5. Table 16. Areas considered inoperable Designations Total (ha) Forested (ha) Excluded (ha) Steep slopes 491,492 92,748 31,974 Unstable terrain 15,051 3,923 1,559 Data source and comments: Slope angle is derived from the provincial digital elevation model.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_terrain_stability` | query=`REG_LAND_AND_NATURAL_RESOURCE.TERRAIN_STABILITY` | status=`alias_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_TERRAIN_STABILITY/REG_LAND_AND_NATURAL_RESOURCE_TERRAIN_STABILITY.gpkg`
    - matched by: `object_name:WHSE_TERRESTRIAL_ECOLOGY.STE_TER_STABILITY_POLYS_SVW`
    - top match: `Terrain Stability Mapping (TSM) Detailed Polygons with Short Attribute Table Spatial View`
  - `whse_imagery_and_base_maps_mot_highway_profiles_sp` | query=`WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_IMAGERY_AND_BASE_MAPS_MOT_HIGHWAY_PROFILES_SP/WHSE_IMAGERY_AND_BASE_MAPS_MOT_HIGHWAY_PROFILES_SP.gpkg`
    - matched by: `object_name:WHSE_IMAGERY_AND_BASE_MAPS.MOT_HIGHWAY_PROFILES_SP`
    - top match: `Ministry of Transportation (MOT) Highway Profile`
- Logic mode: `femic_core`

### 14. Sites with low growing timber potential

- Parent step id: `thlb_parent_014_sites_with_low_growing_timber_potential`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `321044.000 ha`
- Benchmark cumulative remaining area: `1929780.000 ha`
- Approval: `soft-approved`
- Approval scope: `full_tsa_user_directed_calibrated_acceptance`
- Approval note: User directed acceptance on the calibrated age-160 bridge run. The accepted run uses a non-steep threshold of 67.1 m3/ha with the steep branch held at 250 m3/ha, and removed 329,228.613 ha against the TSR benchmark of 321,044 ha. This is an explicitly calibrated bridge to the TSR benchmark with the current public-input curve family, not a claim of exact parity with the Chief Forester's yield tables.
- Approved UTC: `2026-04-09T03:31:11Z`
- Approved by: `user_directive`
- Ratchet note: Approved by user direction on the calibrated age-160 bridge run so the TSA29 validation lane can move past step 14. The accepted run lands within 8,184.613 ha of the TSR marginal benchmark, but still sits 48,121.891 ha below the TSR cumulative remaining-area benchmark because the current coarse AU/curve structure produces a cliff-like response around the calibrated threshold.
- Supporting prose section: `6.4.4 Sites with low timber growing potential`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=33`
- Draft subrules:
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_01` | summary=`Sites may have low productivity because of inherent site factors such as nutrient availability, exposure or excessive moisture.` | operation=`exclude` | review=`draft`
    - candidate layers: `site_prod_bc`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_02` | summary=`As such, low productivity stands are removed from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `site_prod_bc`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_03` | summary=`The VRI has been adjusted to reflect losses due to the MPB epidemic and recent catastrophic fires.` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_04` | summary=`It is now difficult to discern low productivity stands from recently disturbed stands based on the current adjusted attributes and yield projections created from these attributes a` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wld`
  - `thlb_parent_014_sites_with_low_growing_timber_potential_draft_05` | summary=`Site index was not adjusted and remains a reliable identifier of low productivity stands and will be used in this analysis.` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`
- Current compiled status summary: `ready`=2
- Last notebook run status: `applied`
- Last notebook removed area: `329228.613 ha`
- Last notebook remaining area: `1881658.109 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_014_sites_with_low_growing_timber_potential.20260409T033111Z.json`
- Compiled logic:

#### 14.1. Non-steep 67.1 m3/ha threshold

- Step id: `thlb_parent_014_sites_with_low_growing_timber_potential_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=33`
- TSR page: `33`
- TSR text: `Sites may have low productivity because of inherent site factors such as nutrient availability, exposure or excessive moisture. Stands on these sites may contribute to non-timber objectives even though they are unlikely to grow a merchantable crop of trees in a reasonable amount of time. As such, low productivity stands are removed from the THLB. Low productivity stands were identified as stands that are not capable of achieving the minimum harvestable volume applied in this analysis by 160 years. As discussed in Section 7.1.6 – ‘Minimum harvestable criteria’, the minimum threshold is 80 cubic metres per hectare except for steep slopes where the threshold increases to 250 cubic metres per hectare. The VRI has been adjusted to reflect losses due to the MPB epidemic and recent catastrophic fires. It is now difficult to discern low productivity stands from recently disturbed stands based on the current adjusted attributes and yield projections created from these attributes are no longer reliable as they do not account for stand recovery and release of understory regeneration. Site index was not adjusted and remains a reliable identifier of low productivity stands and will be used in this analysis. In order to utilize site index, an exercise was conducted to find the correlation between site index and the minimum harvestable criteria. Representative yield tables for the major leading species within Williams Lake TSA were produced at increasing increments of site index until a yield table that achieved the minimum harvestable criteria was identified for each species and each BEC zone. Table 17. Site index threshold for sites with low timber growing potential Leading species BEC zone Total (ha) AFLB (ha) SI (m) at 80 m3/ha SI (m) at 250 m3/ha Bl BAFA 111 111 Bl CWH 897 897 4.73 7.01 Bl ESSF 124,601 124,299 5.82 9.96 Bl ICH 5,375 5,300 5.76 9.99 Bl IDF 321 321 5.56 9.40 Bl IMA 478 478 Bl MH 2,020 2,020 4.61 6.76 Bl MS 3,114 3,098 5.91 10.38 Bl SBPS 254 252 5.60 9.82 Bl SBS 3,283 3,217 5.73 9.82 Cw CWH 157 157 5.94 8.47 Cw ESSF 3,986 3,976 5.13 8.25 Cw ICH 43,254 42,937 5.49 8.09 Cw SBS 83 83 4.52 6.83 Deciduous BG 215 214 Deciduous CWH 471 471 7.75 16.36 Deciduous ESSF 486 486 8.62 16.85 Deciduous ICH 9,033 8,889 8.82 17.3 Deciduous IDF 20,712 20,471 9.28 20.11 Deciduous MS 1121 1,114 9.01 16.76 Deciduous SBPS 19,436 19,232 9.03 19.08 Deciduous SBS 21,515 21,151 8.88 17.46 Fd BG 26,405 26,351 Fd CWH 8,006 8,006 7.89 12.33 Fd ESSF 6,194 6,178 9.39 14.48 Fd ICH 56,684 55,967 8.98 13.9 Fd IDF 355,725 352,157 8.65 13.96 Fd MH 458 458 7.75 12.00 Fd MS 3,231 3,223.425 9.26 14.47 Fd SBPS 13,990 13,872 8.64 13.62 Fd SBS 63,975 62,771 9.06 14.08 Pl BAFA 14 14 Pl BG 272 272 (continued) Table 17. Site index threshold for sites with low timber growing potential (concluded) Leading species BEC zone Total (ha) AFLB (ha) SI (m) at 80 m3/ha SI (m) at 250 m3/ha Pl CWH 4,570 4,570 6.69 12.36 Pl ESSF 139,272 138,717 8.69 15.53 Pl ICH 44,850 44,279 7.79 14.96 Pl IDF 215,072 212,472 6.93 13.11 Pl IMA 1 1 Pl MH 1,212 1,212 6.76 11.98 Pl MS 476,984 473,526 8.64 16.49 Pl SBPS 937,325 926,646 6.66 12.54 Pl SBS 67,624 65,310 8.25 16.04 Sx BAFA 40 40 Sx BG 5 5 Sx CWH 996 996 4.86 7.99 Sx ESSF 131,173 130,175 9.19 16.47 Sx ICH 68,280 67,069 8.50 15.21 Sx IDF 52,276 51,494 7.42 13.18 Sx IMA 46 46 Sx MH 918 918 4.52 7.25 Sx MS 54,171 53,886 9.33 16.64 Sx SBPS 95,107 94,285 8.00 14.00 Sx SBS 44,895 44,075 9.01 15.92 All stands with a site index below the values listed above in FMLB without harvest history, matched by corresponding leading-species and BEC zone, were excluded from the THLB. Table 18. Sites with low timber growing potential Designations Total (ha) Forested (ha) Excluded (ha) Sites with low timber growing potential 601,655 542,518 321,044 Data source and comments: Yield tables were produced using VDYP 7 by FAIB growth and yield experts using default stocking criteria for Williams Lake TSA.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Logic mode: `femic_core`

#### 14.2. Steep-slope 250 m3/ha threshold

- Step id: `thlb_parent_014_sites_with_low_growing_timber_potential_compiled_02`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=33`
- TSR page: `33`
- TSR text: `Sites may have low productivity because of inherent site factors such as nutrient availability, exposure or excessive moisture. Stands on these sites may contribute to non-timber objectives even though they are unlikely to grow a merchantable crop of trees in a reasonable amount of time. As such, low productivity stands are removed from the THLB. Low productivity stands were identified as stands that are not capable of achieving the minimum harvestable volume applied in this analysis by 160 years. As discussed in Section 7.1.6 – ‘Minimum harvestable criteria’, the minimum threshold is 80 cubic metres per hectare except for steep slopes where the threshold increases to 250 cubic metres per hectare. The VRI has been adjusted to reflect losses due to the MPB epidemic and recent catastrophic fires. It is now difficult to discern low productivity stands from recently disturbed stands based on the current adjusted attributes and yield projections created from these attributes are no longer reliable as they do not account for stand recovery and release of understory regeneration. Site index was not adjusted and remains a reliable identifier of low productivity stands and will be used in this analysis. In order to utilize site index, an exercise was conducted to find the correlation between site index and the minimum harvestable criteria. Representative yield tables for the major leading species within Williams Lake TSA were produced at increasing increments of site index until a yield table that achieved the minimum harvestable criteria was identified for each species and each BEC zone. Table 17. Site index threshold for sites with low timber growing potential Leading species BEC zone Total (ha) AFLB (ha) SI (m) at 80 m3/ha SI (m) at 250 m3/ha Bl BAFA 111 111 Bl CWH 897 897 4.73 7.01 Bl ESSF 124,601 124,299 5.82 9.96 Bl ICH 5,375 5,300 5.76 9.99 Bl IDF 321 321 5.56 9.40 Bl IMA 478 478 Bl MH 2,020 2,020 4.61 6.76 Bl MS 3,114 3,098 5.91 10.38 Bl SBPS 254 252 5.60 9.82 Bl SBS 3,283 3,217 5.73 9.82 Cw CWH 157 157 5.94 8.47 Cw ESSF 3,986 3,976 5.13 8.25 Cw ICH 43,254 42,937 5.49 8.09 Cw SBS 83 83 4.52 6.83 Deciduous BG 215 214 Deciduous CWH 471 471 7.75 16.36 Deciduous ESSF 486 486 8.62 16.85 Deciduous ICH 9,033 8,889 8.82 17.3 Deciduous IDF 20,712 20,471 9.28 20.11 Deciduous MS 1121 1,114 9.01 16.76 Deciduous SBPS 19,436 19,232 9.03 19.08 Deciduous SBS 21,515 21,151 8.88 17.46 Fd BG 26,405 26,351 Fd CWH 8,006 8,006 7.89 12.33 Fd ESSF 6,194 6,178 9.39 14.48 Fd ICH 56,684 55,967 8.98 13.9 Fd IDF 355,725 352,157 8.65 13.96 Fd MH 458 458 7.75 12.00 Fd MS 3,231 3,223.425 9.26 14.47 Fd SBPS 13,990 13,872 8.64 13.62 Fd SBS 63,975 62,771 9.06 14.08 Pl BAFA 14 14 Pl BG 272 272 (continued) Table 17. Site index threshold for sites with low timber growing potential (concluded) Leading species BEC zone Total (ha) AFLB (ha) SI (m) at 80 m3/ha SI (m) at 250 m3/ha Pl CWH 4,570 4,570 6.69 12.36 Pl ESSF 139,272 138,717 8.69 15.53 Pl ICH 44,850 44,279 7.79 14.96 Pl IDF 215,072 212,472 6.93 13.11 Pl IMA 1 1 Pl MH 1,212 1,212 6.76 11.98 Pl MS 476,984 473,526 8.64 16.49 Pl SBPS 937,325 926,646 6.66 12.54 Pl SBS 67,624 65,310 8.25 16.04 Sx BAFA 40 40 Sx BG 5 5 Sx CWH 996 996 4.86 7.99 Sx ESSF 131,173 130,175 9.19 16.47 Sx ICH 68,280 67,069 8.50 15.21 Sx IDF 52,276 51,494 7.42 13.18 Sx IMA 46 46 Sx MH 918 918 4.52 7.25 Sx MS 54,171 53,886 9.33 16.64 Sx SBPS 95,107 94,285 8.00 14.00 Sx SBS 44,895 44,075 9.01 15.92 All stands with a site index below the values listed above in FMLB without harvest history, matched by corresponding leading-species and BEC zone, were excluded from the THLB. Table 18. Sites with low timber growing potential Designations Total (ha) Forested (ha) Excluded (ha) Sites with low timber growing potential 601,655 542,518 321,044 Data source and comments: Yield tables were produced using VDYP 7 by FAIB growth and yield experts using default stocking criteria for Williams Lake TSA.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Logic mode: `femic_core`

### 15. Non-merchantable timber profiles

- Parent step id: `thlb_parent_015_non_merchantable_timber_profiles`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `49052.000 ha`
- Benchmark cumulative remaining area: `1880728.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved on the Williams Lake landscape-unit smoke subset. The step now implements the TSA29 6.4.5 rule correctly as a later-stage THLB exclusion of broadleaf-leading stands only. Section 7.1.5 mixed conifer broadleaf-volume handling is tracked separately under issue #139.
- Approved UTC: `2026-04-06T08:00:00+00:00`
- Approved by: `user`
- Ratchet note: Soft-approved on the Williams Lake landscape-unit smoke subset as the 6.4.5 broadleaf-leading-stand exclusion. Keep Section 7.1.5 broadleaf-volume exclusions for conifer-leading stands out of the THLB area-netdown lane.
- Supporting prose section: `6.4.5 Non-merchantable timber profiles`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=35`
- Draft subrules:
  - `thlb_parent_015_non_merchantable_timber_profiles_draft_01` | summary=`In the Williams Lake TSA, stands predominately composed of broadleaf species are not utilized, and often left standing for biodiversity value.` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`, `road_network`
    - candidate fields: `SPECIES_CD_1`
    - candidate values: `BROADLEAF_SPECIES_CODES`
  - `thlb_parent_015_non_merchantable_timber_profiles_draft_02` | summary=`Therefore, broadleaf-leading stands will be excluded from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`, `road_network`
    - candidate fields: `SPECIES_CD_1`
    - candidate values: `BROADLEAF_SPECIES_CODES`
  - `thlb_parent_015_non_merchantable_timber_profiles_draft_03` | summary=`The deciduous component of conifer-leading stands is discussed under Section 7.1.5 – ‘Volume exclusions for broadleaf species’.` | operation=`exclude` | review=`draft`
    - candidate layers: `vri`, `road_network`
    - candidate fields: `SPECIES_CD_1`
    - candidate values: `BROADLEAF_SPECIES_CODES`
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `103629.462 ha`
- Last notebook remaining area: `1778028.647 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_015_non_merchantable_timber_profiles.20260409T034428Z.json`
- Compiled logic:

#### 15.1. Broadleaf-leading stands

- Step id: `thlb_parent_015_non_merchantable_timber_profiles_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=35`
- TSR page: `35`
- TSR text: `Non-merchantable timber profiles are stands that are physically operable, meet minimum harvestable criteria for age and volume, yet contain tree species that are not currently utilized. In the Williams Lake TSA, stands predominately composed of broadleaf species are not utilized, and often left standing for biodiversity value. Therefore, broadleaf-leading stands will be excluded from the THLB. The deciduous component of conifer-leading stands is discussed under Section 7.1.5 – ‘Volume exclusions for broadleaf species’. Table 19. Broadleaf-leading stands Designations Total (ha) Forested (ha) Excluded (ha) Aspen-leading stands 160,809 99,616 45,113 Birch-leading stands 11,278 8,051 3,939 The potential contribution of broadleaf-deciduous leading stands to timber supply will be explored through sensitivity analysis.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Logic mode: `femic_core`

### 16. Recreation features

- Parent step id: `thlb_parent_016_recreation_features`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `9598.000 ha`
- Benchmark cumulative remaining area: `1871130.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved on the Williams Lake landscape-unit smoke subset. The step now uses the active FTEN recreation polygons instead of the earlier road-features proxy and produces a real THLB signal; recreation trails and FSP consultation procedure details remain out of scope for this first runnable bridge pass.
- Approved UTC: `2026-04-06T08:30:00+00:00`
- Approved by: `user`
- Ratchet note: Soft-approved on the Williams Lake landscape-unit smoke subset using active FTEN recreation polygons. Keep recreation trails and FSP consultation/procedure language explicitly out of scope until a later refinement pass.
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
    - candidate layers: `road_network`
  - `thlb_parent_016_recreation_features_draft_05` | summary=`Any input received will be incorporated into the harvesting and road construction management strategy.` | operation=`exclude` | review=`draft`
    - candidate layers: `road_network`
  - `thlb_parent_016_recreation_features_draft_06` | summary=`While logging is possible, it is likely that harvesting of recreation sites will be very limited so identified recreational areas and features will be excluded from the THLB.` | operation=`exclude` | review=`draft`
    - candidate layers: `whse_forest_tenure_ften_recreation`
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `7562.895 ha`
- Last notebook remaining area: `1770465.752 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_016_recreation_features.20260409T034739Z.json`
- Compiled logic:

#### 16.1. Active recreation polygons

- Step id: `thlb_parent_016_recreation_features_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=36`
- TSR page: `36`
- TSR text: `Recreation sites and trails have been legally established within the Williams Lake TSA under the FRPA. These include campsites and trails as well as sites created for a variety of education and recreation activities. Approved FSPs include a strategy related to legally established recreations sites and trails. This strategy is to refer proposed harvesting and road construction to the ministry responsible for recreation requesting input on the proposal. Any input received will be incorporated into the harvesting and road construction management strategy. While logging is possible, it is likely that harvesting of recreation sites will be very limited so identified recreational areas and features will be excluded from the THLB. Table 20. Recreation features Land classification Total (ha) Forested (ha) Excluded (ha) Use, Recreation and Enjoyment of the Public (UREP) 3,551 2,356 1,320 Forest recreation 15,699 13,058 8,051 Recreation features 23,727 14,774 227 Data source and comments: Tolko Industries Ltd. - FSP #780; West Fraser Mills Ltd. - FSP #755; and BCTS - FSP #828.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_forest_tenure_ften_recreation` | query=`WHSE_FOREST_TENURE.FTEN_RECREATION` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_FOREST_TENURE_FTEN_RECREATION/WHSE_FOREST_TENURE_FTEN_RECREATION.gpkg`
    - matched by: `object_name_stem:WHSE_FOREST_TENURE.FTEN_RECREATION_POLY_SVW`
    - top match: `Recreation Polygons`
- Logic mode: `femic_core`

### 17. Growth and yield permanent sample plots

- Parent step id: `thlb_parent_017_growth_and_yield_permanent_sample_plots`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `3577.000 ha`
- Benchmark cumulative remaining area: `1867553.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved on the Williams Lake landscape-unit smoke subset. The DWDS-backed active PSP layer is now materialized and the later-stage THLB exclusion produces a real, reviewable signal; hold definitive sign-off for broader/full-TSA validation.
- Approved UTC: `2026-04-06T08:34:06.018545+00:00`
- Approved by: `user_directed_review`
- Ratchet note: Soft-approved on the Williams Lake landscape-unit smoke subset using the materialized active PSP GeoPackage from the DWDS pickup-by-GUID flow. Keep definitive validation for the later full-TSA run.
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
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `247.099 ha`
- Last notebook remaining area: `1770218.653 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_017_growth_and_yield_permanent_sample_plots.20260409T035022Z.json`
- Compiled logic:

#### 17.1. Growth and yield permanent sample plots

- Step id: `thlb_parent_017_growth_and_yield_permanent_sample_plots_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=36`
- TSR page: `36`
- TSR text: `The ministry maintains a network of growth and yield permanent sample plots (PSP) across the province for the purposes of understanding forest growth and calibrating growth and yield models. Objectives for these plots have not been established under FRPA. However, harvesting within these active research sites is currently avoided and only occurs after consultation with the research team. Research scientists from within the ministry confirm that these areas should be excluded from the THLB.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_forest_vegetation_gry_psp_status` | query=`WHSE_FOREST_VEGETATION.GRY_PSP_STATUS` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/WHSE_FOREST_VEGETATION_GRY_PSP_STATUS_ACTIVE/GRY_PSP_STATUS_ACTIVE.gpkg`
    - matched by: `object_name_stem:WHSE_FOREST_VEGETATION.GRY_PSP_STATUS_ACTIVE`
    - top match: `Growth and Yield  Samples - All Status`
- Logic mode: `femic_core`

### 18. Riparian areas

- Parent step id: `thlb_parent_018_riparian_areas`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `54833.000 ha`
- Benchmark cumulative remaining area: `1812720.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved after class-based riparian stream/wetland buffer execution on the Williams Lake LU smoke subset. Lake classes and special S4 width in Niut/South Chilcotin remain deferred review refinements pending later/full-TSA validation.
- Supporting prose section: `6.4.2 Riparian areas`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- Draft subrules:
  - `thlb_parent_018_riparian_areas_draft_01` | summary=`Buffer Cariboo stream-classification lines by the Table 15 effective riparian widths for S1-S6 streams.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_stream_classification_car_line`
    - candidate fields: `STREAM_CLASS`
    - candidate values: `S1`, `S2`, `S3`, `S4`, `S5`, `S6`
    - field/value mapping notes:
      - STREAM_CLASS uses numeric values 1-6 in the downloaded Cariboo stream-classification layer.
  - `thlb_parent_018_riparian_areas_draft_02` | summary=`Buffer Cariboo wetland-class polygons by the Table 15 effective riparian widths for W1-W5 wetlands.` | operation=`exclude` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_wetland_class_car_poly`
    - candidate fields: `SWAMP_CLASS`
    - candidate values: `w1`, `w2`, `w3`, `w4`, `w5`
    - field/value mapping notes:
      - SWAMP_CLASS uses lowercase values such as w1-w5 in the downloaded Cariboo wetland-class layer.
  - `thlb_parent_018_riparian_areas_draft_03` | summary=`Lake riparian classes L1-L4 remain a reviewed gap until a clean Cariboo lake-class spatial source is adopted.` | operation=`review` | review=`draft`
    - candidate layers: `whse_basemapping_fwa_lakes_poly`
    - field/value mapping notes:
      - FWA lakes polygons are present, but the lake classification surface still needs adoption.
  - `thlb_parent_018_riparian_areas_draft_04` | summary=`Apply the special S4=30 m riparian width in Niut SRDZ and South Chilcotin SRDZ as a later reviewed refinement.` | operation=`review` | review=`draft`
    - candidate layers: `reg_land_and_natural_resource_stream_classification_car_line`, `rmp_landscape_unit_svw`, `whse_land_use_planning_rmp_plan_legal_poly_svw`
    - candidate fields: `STREAM_CLASS`, `LANDSCAPE_UNIT_NAME`
    - candidate values: `S4`, `Niut`, `South Chilcotin`
    - field/value mapping notes:
      - Special-case LU/SRDZ overlays are not auto-executed in the first runnable bridge pass.
- Current compiled status summary: `manual_review_required`=2, `ready`=11
- Last notebook run status: `applied`
- Last notebook removed area: `1787.772 ha`
- Last notebook remaining area: `1768430.881 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_018_riparian_areas.20260409T035309Z.json`
- Compiled logic:

#### 18.1. Stream class S1 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_stream_s1`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_stream_classification_car_line` | query=`Stream Classification for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_STREAM_CLASSIFICATION_CAR_LINE/STREAM_CLASSIFICATION_CAR_LINE.gpkg`
    - matched by: `exact_text:Stream Classification for the Cariboo Region`
    - top match: `Stream Classification for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.2. Stream class S2 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_stream_s2`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_stream_classification_car_line` | query=`Stream Classification for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_STREAM_CLASSIFICATION_CAR_LINE/STREAM_CLASSIFICATION_CAR_LINE.gpkg`
    - matched by: `exact_text:Stream Classification for the Cariboo Region`
    - top match: `Stream Classification for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.3. Stream class S3 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_stream_s3`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_stream_classification_car_line` | query=`Stream Classification for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_STREAM_CLASSIFICATION_CAR_LINE/STREAM_CLASSIFICATION_CAR_LINE.gpkg`
    - matched by: `exact_text:Stream Classification for the Cariboo Region`
    - top match: `Stream Classification for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.4. Stream class S4 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_stream_s4`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_stream_classification_car_line` | query=`Stream Classification for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_STREAM_CLASSIFICATION_CAR_LINE/STREAM_CLASSIFICATION_CAR_LINE.gpkg`
    - matched by: `exact_text:Stream Classification for the Cariboo Region`
    - top match: `Stream Classification for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.5. Stream class S5 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_stream_s5`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_stream_classification_car_line` | query=`Stream Classification for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_STREAM_CLASSIFICATION_CAR_LINE/STREAM_CLASSIFICATION_CAR_LINE.gpkg`
    - matched by: `exact_text:Stream Classification for the Cariboo Region`
    - top match: `Stream Classification for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.6. Stream class S6 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_stream_s6`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_stream_classification_car_line` | query=`Stream Classification for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_STREAM_CLASSIFICATION_CAR_LINE/STREAM_CLASSIFICATION_CAR_LINE.gpkg`
    - matched by: `exact_text:Stream Classification for the Cariboo Region`
    - top match: `Stream Classification for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.7. Wetland class W1 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_wetland_w1`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_wetland_class_car_poly` | query=`Wetland Riparian Classes for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_WETLAND_CLASS_CAR_POLY/WETLAND_CLASS_CAR_POLY.gpkg`
    - matched by: `exact_text:Wetland Riparian Classes for the Cariboo Region`
    - top match: `Wetland Riparian Classes for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.8. Wetland class W2 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_wetland_w2`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_wetland_class_car_poly` | query=`Wetland Riparian Classes for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_WETLAND_CLASS_CAR_POLY/WETLAND_CLASS_CAR_POLY.gpkg`
    - matched by: `exact_text:Wetland Riparian Classes for the Cariboo Region`
    - top match: `Wetland Riparian Classes for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.9. Wetland class W3 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_wetland_w3`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_wetland_class_car_poly` | query=`Wetland Riparian Classes for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_WETLAND_CLASS_CAR_POLY/WETLAND_CLASS_CAR_POLY.gpkg`
    - matched by: `exact_text:Wetland Riparian Classes for the Cariboo Region`
    - top match: `Wetland Riparian Classes for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.10. Wetland class W4 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_wetland_w4`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_wetland_class_car_poly` | query=`Wetland Riparian Classes for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_WETLAND_CLASS_CAR_POLY/WETLAND_CLASS_CAR_POLY.gpkg`
    - matched by: `exact_text:Wetland Riparian Classes for the Cariboo Region`
    - top match: `Wetland Riparian Classes for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.11. Wetland class W5 effective riparian buffer

- Step id: `thlb_parent_018_riparian_areas_compiled_wetland_w5`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `reg_land_and_natural_resource_wetland_class_car_poly` | query=`Wetland Riparian Classes for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_WETLAND_CLASS_CAR_POLY/WETLAND_CLASS_CAR_POLY.gpkg`
    - matched by: `exact_text:Wetland Riparian Classes for the Cariboo Region`
    - top match: `Wetland Riparian Classes for the Cariboo Region`
- Logic mode: `femic_core`

#### 18.12. Lake riparian classes

- Step id: `thlb_parent_018_riparian_areas_compiled_lakes_review`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `manual_review_required`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Lake riparian classes requires a reviewed Cariboo lake-class surface before automated L1/L2/L3/L4 riparian buffering can run
- Linked source layers:
  - `whse_basemapping_fwa_lakes_poly` | query=`WHSE_BASEMAPPING.FWA_LAKES_POLY` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_BASEMAPPING_FWA_LAKES_POLY/WHSE_BASEMAPPING_FWA_LAKES_POLY.gpkg`
    - matched by: `object_name:WHSE_BASEMAPPING.FWA_LAKES_POLY`
    - top match: `Freshwater Atlas Lakes`
- Logic mode: `femic_core`

#### 18.13. Niut and South Chilcotin S4 special width

- Step id: `thlb_parent_018_riparian_areas_compiled_s4_special_review`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `manual_review_required`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=31`
- TSR page: `31`
- TSR text: `Riparian areas along streams and around wetlands will be modelled as managed according to the Forest Practices Code Riparian Management Area Guidebook (1995). Table 15 lists the area reductions to be applied to account for Riparian Reserve Zones (RRZ) and Riparian Management Zones (RMZ). The zone widths are consistent with those specified under FPPR and current FSPs. Each stream, lake, and wetland class were spatially identified, classified, and then buffered using GIS in accordance with Table 15 criteria to create a riparian area to be modelled in the analysis. Limited harvesting is permitted in riparian management zones so the zone width was adjusted by the percentage of required retention to derive a modelled equivalent area where harvesting is fully excluded. The reserve widths and percent retention amounts are listed in Table 15 along with the calculated area excluded from the THLB to represent riparian areas. Table 15. Riparian areas Description Class Reserve zone width (metres) Reduction (%) Management zone width (metres) RMZ retention (%) Riparian area width (metres) Streams S1 50 100 20 50 60 S2 30 100 20 20 34 S3 20 100 20 20 24 S4/S5 0 - 30 30 10 S6 0 - 20 30 6 Wetlands W1/W5 10 100 40 20 18 W2 10 100 20 20 14 W3/W4 0 - 30 20 6 Lakes L1-B 10 100 0 - 10 L2 10 100 20 25 15 L3/L4 0 - 30 25 7.5 The management of fisheries sensitive watersheds will be discussed later under Section 7.2.10 – ‘Fisheries sensitive watersheds’. However, the management requirements for the protection of dolly varden trout habitat are accounted for in this netdown through increased riparian reserve zone widths. Licensee FSPs specify that within the Niut SRDZ and the South Chilcotin SRDZ, a 20-metre riparian reserve zone will be maintained on streams classified as S4 to protect dolly varden trout populations. For the analysis, the riparian area width applied to S4 streams in these landscape units was increased to 30 metres. In total, 54 833 hectares will be excluded to account for the total riparian areas of 199 820 hectares. Data source and comments: A previously conducted GIS project mapped RRZs and RMZs for streams, lakes, and wetlands in the CNRR. Riparian Classification, RMZs and Riparian Management Areas are derived from the LAO Objectives 20 and 23; CCLUP Objectives for Riparian Management; and the FPPR Sections 47, 48, 49, 50, 52(2) and 53. RMZ reductions are derived from: LAO objectives 21 and 22 - Retention of Trees in a RMZ as well as FSP commitments from the three major licensees (Tolko Industries Ltd., FSP #780; West Fraser Mills Ltd., FSP #755 and BCTS, FSP #828) within the CNRR.`
- FEMIC proposed logic: Niut and South Chilcotin S4 special width requires a reviewed LU/SRDZ overlay to increase S4 riparian width to 30 metres in the Niut and South Chilcotin areas
- Linked source layers:
  - `reg_land_and_natural_resource_stream_classification_car_line` | query=`Stream Classification for the Cariboo Region` | status=`exact_hit` | strategy=`dwds_order`
    - artifact: `data/downloads/bcdc/REG_LAND_AND_NATURAL_RESOURCE_STREAM_CLASSIFICATION_CAR_LINE/STREAM_CLASSIFICATION_CAR_LINE.gpkg`
    - matched by: `exact_text:Stream Classification for the Cariboo Region`
    - top match: `Stream Classification for the Cariboo Region`
  - `rmp_landscape_unit_svw` | query=`RMP_LANDSCAPE_UNIT_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/RMP_LANDSCAPE_UNIT_SVW/RMP_LANDSCAPE_UNIT_SVW.gpkg`
    - matched by: `object_name_suffix:WHSE_LAND_USE_PLANNING.RMP_LANDSCAPE_UNIT_SVW`
    - top match: `Landscape Units of British Columbia - Current`
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`

### 19. Buffered trails

- Parent step id: `thlb_parent_019_buffered_trails`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `8039.000 ha`
- Benchmark cumulative remaining area: `1804681.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved after Williams Lake LU smoke validation. The notebook now models the TSA29 85%-of-corridor rule by shrinking the legal 100 m buffered-trail polygons inward by 7.5 m on each side to yield an 85 m effective exclusion width. Full-TSA validation still pending.
- Supporting prose section: `6.3.6 Buffered trails`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- Draft subrules:
  - `thlb_parent_019_buffered_trails_draft_01` | summary=`The LAO identifies regionally important trails and defines a 50-metre management zone on either side of the trail.` | operation=`exclude` | review=`draft`
  - `thlb_parent_019_buffered_trails_draft_02` | summary=`The LAO specifies that at least 85% of the current forest basal area must be maintained within the buffer.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
  - `thlb_parent_019_buffered_trails_draft_03` | summary=`At least 85% of the area within the 100-metre corridor along trails will not be available for harvest.` | operation=`exclude` | review=`draft`
    - candidate layers: `fadm_bcts_area`
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `10256.537 ha`
- Last notebook remaining area: `1758174.344 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_019_buffered_trails.20260409T035621Z.json`
- Compiled logic:

#### 19.1. Buffered trail areas

- Step id: `thlb_parent_019_buffered_trails_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=30`
- TSR page: `30`
- TSR text: `The LAO identifies regionally important trails and defines a 50-metre management zone on either side of the trail. The LAO specifies that at least 85% of the current forest basal area must be maintained within the buffer. At least 85% of the area within the 100-metre corridor along trails will not be available for harvest. Table 12. Buffered trails Designations Total (ha) Forested (ha) Excluded (ha) LAO buffered trails 46,020 25,372 8,039 Data source and comments: The land base reduction for identified trails reflects the Section 93.4 LAO establishing objectives for the CCLUP, May 19, 2010, amended April 18, 2011, and consolidated to September 6, 2018. Map 10.`
- FEMIC proposed logic: Exclude the linked polygons from THLB where they intersect the working land base; the exact execution mode depends on available data and current implementation support.
- Linked source layers:
  - `whse_land_use_planning_rmp_plan_legal_poly_svw` | query=`WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW` | status=`exact_hit` | strategy=`wfs_fetch`
    - artifact: `data/downloads/bcdc/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW/WHSE_LAND_USE_PLANNING_RMP_PLAN_LEGAL_POLY_SVW.gpkg`
    - matched by: `object_name:WHSE_LAND_USE_PLANNING.RMP_PLAN_LEGAL_POLY_SVW`
    - top match: `Legal Planning Objectives - Current - Polygon`
- Logic mode: `femic_core`

### 20. Wildlife tree retention areas

- Parent step id: `thlb_parent_020_wildlife_tree_retention_areas`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `approved`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `94417.000 ha`
- Benchmark cumulative remaining area: `1710264.000 ha`
- Approval: `soft-approved`
- Approval scope: `single_lu_smoke_subset_williams_lake`
- Approval note: Soft-approved after Williams Lake LU smoke validation. Step 20 now follows TSA29 section 6.4.8 as an aspatial future-WTRA THLB reduction factor while keeping existing mapped WTRA in THLB and deferred from harvest. Full-TSA validation still pending.
- Ratchet note: Soft-approved on the Williams Lake landscape-unit smoke subset using the TSA29 aspatial future-WTRA reduction logic. Keep definitive validation for the later full-TSA run.
- Supporting prose section: `6.4.8 Wildlife tree retention areas`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- Draft subrules:
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_01` | summary=`Wildlife tree retention areas (WTRA) are established within and adjacent to cutblocks to maintain stand-level biodiversity and are discussed in more detail in Section 7.2.4 – ‘Stan` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2020`, `ta_wildlife_mgmt_areas`, `veg_consolidated_cut_blocks_sp`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_02` | summary=`Currently mapped WTRA are recorded in RESULTS (identified by Type = ‘Group’ and Objective = ‘WTR’).` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_wildlife_mgmt_areas`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_03` | summary=`Harvesting of WTRA is only restricted until the regenerating cutblock has reached maturity so the existing mapped WTRA will be included in the THLB but will be deferred from harves` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_wildlife_mgmt_areas`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_04` | summary=`Although individual WTRA can eventually be harvested there will always be WTRA established in conjunction with every cutblock harvested.` | operation=`exclude` | review=`draft`
    - candidate layers: `consolidated_cutblocks_2020`, `ta_wildlife_mgmt_areas`, `veg_consolidated_cut_blocks_sp`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_05` | summary=`In the base case, the land base that will continually be required for WTRA will be modelled as an aspatial THLB reduction factor.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_wildlife_mgmt_areas`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
  - `thlb_parent_020_wildlife_tree_retention_areas_draft_06` | summary=`In total, 94 417 hectares will be excluded to represent future WTRA.` | operation=`exclude` | review=`draft`
    - candidate layers: `ta_wildlife_mgmt_areas`, `whse_wildlife_management_wcp_wildlife`, `whse_wildlife_management_wcp_wildlife_habitat_area`
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `33646.905 ha`
- Last notebook remaining area: `1724527.440 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_020_wildlife_tree_retention_areas.20260409T035939Z.json`
- Compiled logic:

#### 20.1. Future wildlife tree retention area reduction

- Step id: `thlb_parent_020_wildlife_tree_retention_areas_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- TSR page: `37`
- TSR text: `Wildlife tree retention areas (WTRA) are established within and adjacent to cutblocks to maintain stand-level biodiversity and are discussed in more detail in Section 7.2.4 – ‘Stand-level biodiversity’. Currently mapped WTRA are recorded in RESULTS (identified by Type = ‘Group’ and Objective = ‘WTR’). Harvesting of WTRA is only restricted until the regenerating cutblock has reached maturity so the existing mapped WTRA will be included in the THLB but will be deferred from harvest for 80 years. Although individual WTRA can eventually be harvested there will always be WTRA established in conjunction with every cutblock harvested. In the base case, the land base that will continually be required for WTRA will be modelled as an aspatial THLB reduction factor. In total, 94 417 hectares will be excluded to represent future WTRA.`
- FEMIC proposed logic: Apply a final aspatial THLB reduction of the TSR-cited magnitude after the spatially executable steps have completed.
- Logic mode: `femic_core`

### 21. Cultural heritage and archaeological resources

- Parent step id: `thlb_parent_021_cultural_heritage_and_archaeological_resources`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Ratchet state: `compiled`
- Table provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=24`
- Benchmark marginal deduction: `34205.000 ha`
- Benchmark cumulative remaining area: `1676059.000 ha`
- Supporting prose section: `6.4.9 Cultural heritage and archaeological resources.`
- Supporting prose provenance:
  - `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- Draft subrules:
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_01` | summary=`Treat HCA-protected archaeological sites as legally protected features that are not auto-mapped into a public exclusion layer here.` | operation=`review` | review=`draft`
    - field/value mapping notes:
      - Do not infer road, burn-severity, or other generic spatial layers from this prose.
      - Use reviewed permit/FSP practice and adopted overrides if a trusted spatial source is later identified.
  - `thlb_parent_021_cultural_heritage_and_archaeological_resources_draft_02` | summary=`Represent licensee/Tsilhqot'in cultural-heritage exclusions as an aspatial THLB reduction rather than a guessed spatial overlay.` | operation=`aspatial_reduction` | review=`draft`
    - candidate values: `2% of cutblock area`, `34,205 ha total TSR benchmark`
    - field/value mapping notes:
      - This is a benchmark-anchored aspatial reduction step, not a direct public-GIS query.
      - Reference practice inputs: TNG, Tolko FSP #780, West Fraser FSP #755, BCTS FSP #828.
- Current compiled status summary: `ready`=1
- Last notebook run status: `applied`
- Last notebook removed area: `11956.187 ha`
- Last notebook remaining area: `1712571.253 ha`
- Last notebook result JSON: `runtime/logs/tsr/notebook_runs/thlb_parent_021_cultural_heritage_and_archaeological_resources.20260409T040302Z.json`
- Compiled logic:

#### 21.1. Cultural heritage and archaeological resources reduction

- Step id: `thlb_parent_021_cultural_heritage_and_archaeological_resources_compiled_01`
- Kind: `netdown_rule`
- Stage: `LHLB -> THLB`
- Execution class: `projected_harvest_exclusion`
- Run status: `ready`
- TSR provenance: `TSR_2024/Data_Package_2024/29ts_dpkg_2024.pdf#page=37`
- TSR page: `37`
- TSR text: `The Heritage Conservation Act (HCA) recognizes the historical, cultural, scientific, spiritual, and educational value of archaeological sites to First Nations, local communities, and the public. Archaeological sites on both public and private land are protected under the HCA and must not be altered without a permit. A cultural heritage resource is an object, site or location of a traditional societal practice that is of historical, cultural, societal or archaeological significance to the province, community or an Aboriginal People. This can include archaeological sites, structural features, heritage landscape features and traditional use sites. Cultural heritage resources not applicable to the HCA are managed for by the licensees through the cultural heritage resource sections in the applicable FSPs as per FPPR Section 10. Cultural heritage resources are identified by the licensees through information sharing prior to the submission of cutting permit and road permit applications to the ministry. The most common practice by licensees is to manage for these sites by excluding them from the harvest area through boundary amendments and the placement of wildlife tree retention and/or cultural resource management zones. The incremental excluded area required to protect these sites in current practices was discussions with licensees and the Tsilhqot’in National Government. It was estimated that, on average, an additional two percent of the cutblock area was now included in these expanded exclusions and/or reserves. This will be modelled as an aspatial reduction to the THLB. In total, 34 205 hectares will be excluded to represent cultural heritage resources. Data source and comments: Tsilhqot’in National Government Tolko Industries Ltd. - FSP #780; West Fraser Mills Ltd. - FSP #755; and BCTS - FSP #828.`
- FEMIC proposed logic: Apply a final aspatial THLB reduction of the TSR-cited magnitude after the spatially executable steps have completed.
- Logic mode: `femic_core`

