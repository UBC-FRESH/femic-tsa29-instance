"""TSA29 TSR adjudication overlay provider."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any

from femic.tsr_catalog import (
    TsrAdjudicationOverlayError,
    TsrLandBaseSummaryRowClassification,
    TsrReconstructionGapInterpretation,
)


PROVIDER_ID = "tsa29"


def _row(
    land_base_stage: str,
    execution_class: str,
    benchmark_role: str,
) -> TsrLandBaseSummaryRowClassification:
    return TsrLandBaseSummaryRowClassification(
        land_base_stage=land_base_stage,
        execution_class=execution_class,
        benchmark_role=benchmark_role,
    )


TABLE3_ROW_CLASSIFICATIONS: dict[str, TsrLandBaseSummaryRowClassification] = {
    "total tsa area": _row("reference_target", "reference_only", "reference_total"),
    "land not administered by the province": _row(
        "glb_to_aflb", "drop_from_universe", "deduction"
    ),
    "non-forest": _row("glb_to_aflb", "drop_from_universe", "deduction"),
    "roads and landings": _row("glb_to_aflb", "drop_from_universe", "deduction"),
    "analysis forest land base": _row(
        "glb_to_aflb", "reference_only", "reference_cumulative"
    ),
    "parks, protected areas, area-base tenures": _row(
        "aflb_to_lhlb", "legal_harvest_exclusion", "deduction"
    ),
    "old growth management areas": _row(
        "aflb_to_lhlb", "legal_harvest_exclusion", "deduction"
    ),
    "wildlife habitat areas": _row(
        "aflb_to_lhlb", "legal_harvest_exclusion", "deduction"
    ),
    "critical habitat for fish": _row(
        "aflb_to_lhlb", "legal_harvest_exclusion", "deduction"
    ),
    "lakeshore management": _row(
        "aflb_to_lhlb", "legal_harvest_exclusion", "deduction"
    ),
    "community areas of special concern": _row(
        "aflb_to_lhlb", "legal_harvest_exclusion", "deduction"
    ),
    "proven aboriginal rights areas": _row(
        "aflb_to_lhlb", "legal_harvest_exclusion", "deduction"
    ),
    "areas considered inoperable": _row(
        "lhlb_to_thlb", "projected_harvest_exclusion", "deduction"
    ),
    "sites with low growing timber potential": _row(
        "lhlb_to_thlb", "projected_harvest_exclusion", "deduction"
    ),
    "non-merchantable timber profiles": _row(
        "lhlb_to_thlb", "projected_harvest_exclusion", "deduction"
    ),
    "recreation features": _row(
        "lhlb_to_thlb", "projected_harvest_exclusion", "deduction"
    ),
    "growth and yield permanent sample plots": _row(
        "lhlb_to_thlb", "projected_harvest_exclusion", "deduction"
    ),
    "riparian areas": _row("lhlb_to_thlb", "projected_harvest_exclusion", "deduction"),
    "buffered trails": _row("lhlb_to_thlb", "projected_harvest_exclusion", "deduction"),
    "wildlife tree retention areas": _row(
        "lhlb_to_thlb", "projected_harvest_exclusion", "deduction"
    ),
    "cultural heritage and archaeological resources": _row(
        "lhlb_to_thlb", "projected_harvest_exclusion", "deduction"
    ),
    "timber harvesting land base": _row(
        "lhlb_to_thlb", "reference_only", "reference_cumulative"
    ),
    "future roads": _row("lhlb_to_thlb", "projected_harvest_exclusion", "deduction"),
    "long-term thlb": _row(
        "reference_target", "reference_only", "reference_cumulative"
    ),
}


def _interpretation(
    problem_ownership: str,
    difference_nature: str,
    engineering_interpretation: str,
    recommended_next_move: str,
) -> TsrReconstructionGapInterpretation:
    return TsrReconstructionGapInterpretation(
        problem_ownership=problem_ownership,
        difference_nature=difference_nature,
        engineering_interpretation=engineering_interpretation,
        recommended_next_move=recommended_next_move,
    )


RECONSTRUCTION_GAP_INTERPRETATIONS: dict[str, TsrReconstructionGapInterpretation] = {
    "thlb_parent_002_land_not_administered_by_the_province": _interpretation(
        "model_endogenous",
        "strict_logic_overcut",
        "The strict lane is using a broader ownership interpretation than the reviewed bridge, so it is cutting too much area here.",
        "Tighten the strict ownership mapping and separate the dedicated title/treaty exclusions from the generic F_OWN ownership classes.",
    ),
    "thlb_parent_003_non_forest": _interpretation(
        "model_endogenous",
        "reviewed_bridge_semantics",
        "The strict lane is only doing a narrow direct waterbody removal here, while the reviewed lane is carrying a much broader non-forest interpretation; in addition, this early GLB-to-AFLB comparison is conditioned by checkpoint1/AFLB initialization rather than a literal raw-GLB replay.",
        "Decide and document the intended strict non-forest semantics before changing code again; this is not just a missing-data problem, and the current stepwise delta should be read as a baseline-conditioned diagnostic rather than a literal raw-GLB replay.",
    ),
    "thlb_parent_004_roads_and_landings": _interpretation(
        "mixed",
        "accepted_aspatial_bridge",
        "The TSR itself says existing roads, trails, and landings are modeled non-spatially through partial AFLB reductions because the features are too small and incomplete to track cleanly at landscape scale. The strict lane should therefore be judged against the documented aspatial benchmark first, with the narrow permanent-road overlays treated as supporting evidence only.",
        "Keep the documented step-4 aspatial AFLB fallback in place unless you later adopt a better exact road-footprint contract.",
    ),
    "thlb_parent_006_parks_protected_areas_area_base_tenures": _interpretation(
        "mixed",
        "strict_logic_undercut",
        "The strict lane is lighter than the reviewed lane here, likely because tenure and ownership semantics are still not fully aligned.",
        "Refine the strict tenure/ownership logic first, then reassess whether any supporting data gaps remain material.",
    ),
    "thlb_parent_007_old_growth_management_areas": _interpretation(
        "model_endogenous",
        "strict_logic_overcut",
        "The strict lane is likely treating OGMA area too broadly relative to the reviewed TSA29 interpretation.",
        "Tighten the OGMA logic before looking for new data; this looks like an over-selection problem.",
    ),
    "thlb_parent_008_wildlife_habitat_areas": _interpretation(
        "model_endogenous",
        "strict_logic_overcut",
        "The strict lane is selecting far more wildlife-area land than either the reviewed lane or the TSR benchmark supports.",
        "Audit the strict no-harvest selection logic and keep conditional/modified zones out unless the TSR clearly says otherwise.",
    ),
    "thlb_parent_009_critical_habitat_for_fish": _interpretation(
        "model_endogenous",
        "strict_logic_overcut",
        "The strict lane is applying a much broader legal fish-objective surface than the reviewed lane or TSR benchmark supports.",
        "Narrow the strict fish-habitat interpretation; this is one of the clearest strict overcut seams in the whole ladder.",
    ),
    "thlb_parent_010_lakeshore_management": _interpretation(
        "data_exogenous",
        "missing_or_blocked_data",
        "This step depends on a trusted Class A lake discriminator that the current public-input lane still does not have.",
        "Keep the reviewed skip or a tiny aspatial fallback unless a trustworthy lake-class source appears.",
    ),
    "thlb_parent_011_community_areas_of_special_concern": _interpretation(
        "model_endogenous",
        "reviewed_bridge_semantics",
        "The strict literal source choice is not reproducing the reviewed meaning of this step at all.",
        "Fix the strict semantics/source interpretation instead of treating this as a pure missing-data problem.",
    ),
    "thlb_parent_012_proven_aboriginal_rights_areas": _interpretation(
        "data_exogenous",
        "missing_or_blocked_data",
        "The strict lane still lacks a trustworthy public boundary source for this step.",
        "Keep this as a reviewed skip or documented fallback until a real source is available.",
    ),
    "thlb_parent_013_areas_considered_inoperable": _interpretation(
        "reviewed_bridge_choice",
        "accepted_reviewed_override",
        "The reviewed lane uses accepted derived-attribute and calibrated bridge logic here that the strict checkpoint1 lane does not share.",
        "Keep the accepted reviewed bridge unless you explicitly decide to port its late-stage derived attributes into strict semantics.",
    ),
    "thlb_parent_014_sites_with_low_growing_timber_potential": _interpretation(
        "mixed",
        "missing_late_stage_semantics",
        "The strict lane is blocked because this is late-stage curve-ready logic, not because the universe of land is inherently unknowable.",
        "Bridge or port the late-stage curve logic explicitly; do not mislabel this as a simple raw-data problem.",
    ),
    "thlb_parent_015_non_merchantable_timber_profiles": _interpretation(
        "model_endogenous",
        "missing_late_stage_semantics",
        "The strict lane is missing the later broadleaf-leading yield logic that the reviewed lane applies here.",
        "Port the reviewed late-stage logic or keep this as an explicit bridge/fallback step.",
    ),
    "thlb_parent_016_recreation_features": _interpretation(
        "mixed",
        "partial_strict_logic",
        "The strict lane only captures part of the reviewed recreation exclusion logic.",
        "Low-priority cleanup: improve strict logic if this step later matters to the remaining gap.",
    ),
    "thlb_parent_017_growth_and_yield_permanent_sample_plots": _interpretation(
        "data_exogenous",
        "weak_public_coverage",
        "The strict lane undercuts here, but the public PSP geometry signal is weak and the absolute area is small.",
        "Treat this as a lower-priority data-coverage seam unless a better PSP source becomes available.",
    ),
    "thlb_parent_018_riparian_areas": _interpretation(
        "mixed",
        "missing_or_blocked_data",
        "The strict lane is still missing some of the lake-class and special-case riparian inputs that the reviewed bridge used.",
        "Improve source coverage first, then revisit the strict riparian logic if the gap remains large.",
    ),
    "thlb_parent_019_buffered_trails": _interpretation(
        "reviewed_bridge_choice",
        "accepted_reviewed_override",
        "The reviewed lane uses an accepted equivalent-corridor bridge here, while the strict lane currently does not reproduce that bridge.",
        "Keep the accepted bridge unless you explicitly decide to formalize the same equivalent-corridor logic in strict mode.",
    ),
    "thlb_parent_020_wildlife_tree_retention_areas": _interpretation(
        "reviewed_bridge_choice",
        "accepted_aspatial_bridge",
        "This step is intentionally being modeled as an aspatial future-WTRA bridge rather than an exact mapped exclusion.",
        "Keep the documented aspatial fallback unless a better exact contract is deliberately adopted later.",
    ),
    "thlb_parent_021_cultural_heritage_and_archaeological_resources": _interpretation(
        "reviewed_bridge_choice",
        "accepted_aspatial_bridge",
        "This step is intentionally being modeled as an aspatial THLB bridge rather than a single exact spatial layer.",
        "Keep the documented aspatial fallback unless a defensible exact spatial contract is introduced later.",
    ),
    "thlb_parent_023_future_roads": _interpretation(
        "reviewed_bridge_choice",
        "accepted_skip_or_noop",
        "The accepted TSA29 closeout keeps this as an explicit 0 ha no-op tail step after step 21.",
        "Leave it alone unless you intentionally reopen the reviewed closeout decision.",
    ),
}


@dataclass(frozen=True)
class Tsa29TsrAdjudicationProvider:
    """TSA29-owned TSR adjudication overlay provider."""

    provider_id: str = PROVIDER_ID

    def classify_land_base_summary_row(
        self, *, label: str
    ) -> TsrLandBaseSummaryRowClassification | None:
        return TABLE3_ROW_CLASSIFICATIONS.get(label.casefold())

    def validate_checkpoint_path(
        self, *, instance_root: Path, checkpoint_path: Path
    ) -> None:
        _ = instance_root
        if re.search(
            r"ria_vri_vclr1p_checkpoint\d+(?:-tsa[\w-]+)?\.feather$",
            checkpoint_path.name,
            flags=re.IGNORECASE,
        ):
            raise TsrAdjudicationOverlayError(
                "Legacy `ria_vri_vclr1p_checkpoint*.feather` inputs are disabled for "
                "TSA29 strict/workbench validation. Use an explicit validated TSA29 "
                "checkpoint under `data/tsr/` instead."
            )

    def is_strict_seam_checkpoint_path(
        self, *, instance_root: Path, checkpoint_path: Path
    ) -> bool:
        resolved_instance_root = instance_root.expanduser().resolve()
        resolved_checkpoint_path = checkpoint_path.expanduser().resolve()
        strict_root = (resolved_instance_root / "data" / "tsr").resolve()
        try:
            resolved_checkpoint_path.relative_to(strict_root)
        except ValueError:
            return False
        return resolved_checkpoint_path.suffix.casefold() == ".feather"

    def reconstruction_gap_interpretation(
        self, *, recipe_tsa_id: str, parent_step: dict[str, Any]
    ) -> TsrReconstructionGapInterpretation | None:
        if recipe_tsa_id.strip() != "tsa_29":
            return None
        parent_step_id = str(parent_step.get("parent_step_id", "")).strip()
        return RECONSTRUCTION_GAP_INTERPRETATIONS.get(parent_step_id)

    def report_notes(self, *, recipe_tsa_id: str) -> tuple[str, ...]:
        if recipe_tsa_id.strip() != "tsa_29":
            return ()
        return (
            "For the current TSA29 adjudication pass, this report is an active repair ledger: once a parent step is understood well enough to choose an actionable next move, land that change before moving to the next step.",
            "Only leave a step as analysis-only when the chosen action is explicitly to defer, keep a reviewed bridge for now, or wait on missing data/source improvements.",
        )


def provider_factory() -> Tsa29TsrAdjudicationProvider:
    """Return the TSA29 TSR adjudication overlay provider."""

    return Tsa29TsrAdjudicationProvider()


__all__ = [
    "PROVIDER_ID",
    "RECONSTRUCTION_GAP_INTERPRETATIONS",
    "TABLE3_ROW_CLASSIFICATIONS",
    "Tsa29TsrAdjudicationProvider",
    "provider_factory",
]
