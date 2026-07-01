"""TSA29 strict locked-chain named-pipeline contract handler."""

from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
import json
import os
from pathlib import Path
from typing import Any, Mapping, cast

from femic.glb import build_tsa_raw_glb
from femic.named_pipelines import (
    NamedPipelineError,
    NamedPipelineExecutionPlan,
    NamedPipelineExecutionResult,
    NamedPipelineValidationContract,
    NamedPipelineValidationResult,
    _normalize_float_or_none,
    _normalize_int_or_none,
)
from femic.tsr_catalog import (
    TsrThlbNetdownRecipeRunResult,
    load_tsr_thlb_netdown_recipe,
    run_tsr_thlb_locked_parent_step,
)


CONTRACT_KIND = "tsa29_locked_chain_strict"


def _source_tree_root() -> Path:
    env_value = os.environ.get("FEMIC_SOURCE_ROOT")
    if env_value:
        return Path(env_value).expanduser().resolve()
    for parent in Path(__file__).resolve().parents:
        if (parent / "external" / "femic-public-data").exists():
            return parent
    return Path.cwd().resolve()


def _load_json_mapping(*, path: Path, source_label: str) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise NamedPipelineError(f"Invalid JSON in {source_label}: {exc}") from exc
    if not isinstance(payload, dict):
        raise NamedPipelineError(f"{source_label} must be a mapping.")
    return cast(dict[str, Any], payload)


def _load_locked_chain_entries(
    validation_contract: NamedPipelineValidationContract,
) -> list[Mapping[str, Any]]:
    if validation_contract.locked_chain_ledger_path is None:
        raise NamedPipelineError(
            "Strict validation contract requires `locked_chain_ledger_path`."
        )
    ledger_payload = _load_json_mapping(
        path=validation_contract.locked_chain_ledger_path,
        source_label=str(validation_contract.locked_chain_ledger_path),
    )
    ledger_entries = ledger_payload.get("entries")
    if not isinstance(ledger_entries, list):
        raise NamedPipelineError(
            f"{validation_contract.locked_chain_ledger_path} field `entries` must be a list."
        )
    normalized_entries: list[Mapping[str, Any]] = []
    for entry in ledger_entries:
        if not isinstance(entry, dict):
            raise NamedPipelineError(
                f"{validation_contract.locked_chain_ledger_path} field `entries` must contain mappings."
            )
        normalized_entries.append(entry)
    return normalized_entries


def resolve_locked_chain_strict_row_order(*, seam_id: str) -> int:
    if seam_id in {"scratch", "glb"}:
        return 1
    if seam_id in {"aflb", "aflb_yield_ready"}:
        return 5
    raise NamedPipelineError(
        "Strict validation preflight does not yet support seam "
        f"`{seam_id}` for `{CONTRACT_KIND}`."
    )


def _resolve_locked_chain_entry(
    *,
    validation_contract: NamedPipelineValidationContract,
    row_order: int,
) -> Mapping[str, Any]:
    for entry in _load_locked_chain_entries(validation_contract):
        if _normalize_int_or_none(entry.get("row_order")) == row_order:
            return entry
    raise NamedPipelineError(
        "Strict validation contract is missing locked-chain row "
        f"`{row_order}` in {validation_contract.locked_chain_ledger_path}."
    )


def _resolve_locked_chain_entry_by_parent_step_id(
    *,
    validation_contract: NamedPipelineValidationContract,
    parent_step_id: str,
) -> Mapping[str, Any]:
    normalized_parent_step_id = parent_step_id.strip()
    for entry in _load_locked_chain_entries(validation_contract):
        if str(entry.get("parent_step_id", "")).strip() == normalized_parent_step_id:
            return entry
    raise NamedPipelineError(
        "Strict validation contract is missing parent step "
        f"`{normalized_parent_step_id}` in {validation_contract.locked_chain_ledger_path}."
    )


def _is_reference_only_parent_step(parent_step: Mapping[str, Any]) -> bool:
    parent_kind = str(parent_step.get("parent_kind", "")).strip().casefold()
    execution_class = str(parent_step.get("execution_class", "")).strip().casefold()
    return parent_kind == "milestone" or execution_class == "reference_only"


def _resolve_locked_parent_step_sequence(
    *,
    recipe_path: Path,
    start_after_row_order: int = 1,
    stop_after_parent_step_id: str | None = None,
) -> tuple[Mapping[str, Any], ...]:
    recipe = load_tsr_thlb_netdown_recipe(recipe_path)
    sequence: list[Mapping[str, Any]] = []
    normalized_stop_after = (
        stop_after_parent_step_id.strip()
        if stop_after_parent_step_id is not None
        else None
    )
    found_stop_after = normalized_stop_after is None
    for parent_step in recipe.parent_steps:
        parent_step_id = str(parent_step.get("parent_step_id", "")).strip()
        row_order = _normalize_int_or_none(parent_step.get("row_order"))
        if not parent_step_id or row_order is None:
            raise NamedPipelineError(
                f"Locked THLB recipe contains an invalid parent-step entry: {parent_step!r}"
            )
        if row_order <= start_after_row_order:
            continue
        sequence.append(parent_step)
        if (
            normalized_stop_after is not None
            and parent_step_id == normalized_stop_after
        ):
            found_stop_after = True
            break
    if not found_stop_after:
        raise NamedPipelineError(
            "Strict pipeline stop target is not present in the locked recipe: "
            f"`{normalized_stop_after}`."
        )
    return tuple(sequence)


def _validate_locked_strict_parent_step_execution_contract(
    parent_step: Mapping[str, Any],
) -> Mapping[str, Any]:
    parent_step_id = str(parent_step.get("parent_step_id", "")).strip()
    ratchet_state = str(parent_step.get("ratchet_state", "")).strip().casefold()
    approved = bool(parent_step.get("approved", False)) or ratchet_state in {
        "approved",
        "benchmarked",
    }
    compiled_logic = [
        item for item in parent_step.get("compiled_logic", ()) if isinstance(item, dict)
    ]
    if not approved:
        raise NamedPipelineError(
            "Strict pipeline step is not approved on the locked recipe surface: "
            f"`{parent_step_id}`."
        )
    if not compiled_logic:
        raise NamedPipelineError(
            "Strict pipeline step is missing locked compiled logic: "
            f"`{parent_step_id}`."
        )
    return parent_step


def managed_area_ha_from_checkpoint(checkpoint_path: Path) -> float:
    if not checkpoint_path.exists():
        raise NamedPipelineError(
            f"Strict validation checkpoint not found: {checkpoint_path}"
        )
    gpd = import_module("geopandas")
    checkpoint = gpd.read_feather(checkpoint_path)
    if "thlb_fact" in checkpoint.columns:
        thlb_fact = checkpoint["thlb_fact"].astype(float)
        for area_column in ("_stand_area_sqm", "FEATURE_AREA_SQM", "Shape_Area"):
            if area_column in checkpoint.columns:
                return float(
                    (checkpoint[area_column].astype(float) * thlb_fact).sum() / 10000.0
                )
        for area_column in ("POLYGON_AREA", "GEOMETRY_AREA"):
            if area_column in checkpoint.columns:
                return float((checkpoint[area_column].astype(float) * thlb_fact).sum())
        if "geometry" in checkpoint.columns:
            return float(
                (checkpoint.geometry.area.astype(float) * thlb_fact).sum() / 10000.0
            )
    if "geometry" in checkpoint.columns:
        return float(checkpoint.geometry.area.sum() / 10000.0)
    raise NamedPipelineError(
        "Strict validation checkpoint is missing both managed-area columns and geometry: "
        f"{checkpoint_path}"
    )


def materialize_glb_checkpoint_from_result(
    *,
    instance_root: Path,
    clipped_glb_gdb_path: Path,
    clipped_glb_feature_class: str,
) -> Path:
    gpd = import_module("geopandas")
    checkpoint = gpd.read_file(
        clipped_glb_gdb_path,
        layer=clipped_glb_feature_class,
    )
    if len(checkpoint) == 0:
        raise NamedPipelineError(
            "Raw-source GLB build produced no features for TSA29; cannot materialize "
            "step-001 checkpoint."
        )
    area_sqm = checkpoint.geometry.area.astype(float)
    if "FEATURE_AREA_SQM" in checkpoint.columns:
        checkpoint["FEATURE_AREA_SQM"] = area_sqm
    if "POLYGON_AREA" in checkpoint.columns:
        checkpoint["POLYGON_AREA"] = area_sqm / 10000.0
    if "Shape_Area" in checkpoint.columns:
        checkpoint["Shape_Area"] = area_sqm
    if "GEOMETRY_AREA" in checkpoint.columns:
        checkpoint["GEOMETRY_AREA"] = area_sqm / 10000.0
    checkpoint_path = instance_root / "data" / "tsr" / "glb_checkpoint.feather"
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint.to_feather(checkpoint_path)
    return checkpoint_path


def validate_locked_chain_strict_result(
    *,
    plan: NamedPipelineExecutionPlan,
    tsr_result: TsrThlbNetdownRecipeRunResult,
    tolerance_ha: float = 1e-3,
) -> NamedPipelineValidationResult:
    validation_contract = plan.validation_contract
    if validation_contract is None:
        raise NamedPipelineError(
            "Strict validation contract is required for this validator."
        )
    if validation_contract.locked_chain_ledger_path is None:
        raise NamedPipelineError(
            "Strict validation contract requires `locked_chain_ledger_path`."
        )
    ledger_payload = _load_json_mapping(
        path=validation_contract.locked_chain_ledger_path,
        source_label=str(validation_contract.locked_chain_ledger_path),
    )
    audit_path = getattr(tsr_result, "audit_path", None)
    if audit_path in (None, ""):
        raise NamedPipelineError(
            "Strict validation contract requires a THLB run result with an `audit_path`."
        )
    resolved_audit_path = Path(str(audit_path)).expanduser().resolve()
    if not resolved_audit_path.exists():
        raise NamedPipelineError(
            f"Resolved strict validation audit path not found: {resolved_audit_path}"
        )
    audit_payload = _load_json_mapping(
        path=resolved_audit_path,
        source_label=str(resolved_audit_path),
    )
    ledger_entries = ledger_payload.get("entries")
    if not isinstance(ledger_entries, list):
        raise NamedPipelineError(
            f"{validation_contract.locked_chain_ledger_path} field `entries` must be a list."
        )
    audit_steps = audit_payload.get("steps")
    if not isinstance(audit_steps, list):
        raise NamedPipelineError(f"{resolved_audit_path} field `steps` must be a list.")

    parent_step_totals: dict[str, dict[str, float | int | str | None]] = {}
    for step in audit_steps:
        if not isinstance(step, dict):
            raise NamedPipelineError(
                f"{resolved_audit_path} field `steps` must contain mappings."
            )
        parent_step_id = str(step.get("parent_step_id", "")).strip()
        if not parent_step_id:
            continue
        entry = parent_step_totals.setdefault(
            parent_step_id,
            {
                "row_order": _normalize_int_or_none(step.get("order_index")),
                "parent_label": str(step.get("parent_label", "")).strip() or None,
                "net_removed_area_ha": 0.0,
                "remaining_area_ha": None,
            },
        )
        net_removed_area_ha = _normalize_float_or_none(
            step.get("net_removed_area_ha", step.get("removed_area_ha"))
        )
        if net_removed_area_ha is not None:
            entry["net_removed_area_ha"] = float(
                entry["net_removed_area_ha"] or 0.0
            ) + float(net_removed_area_ha)
        remaining_area_ha = _normalize_float_or_none(step.get("remaining_area_ha"))
        if remaining_area_ha is not None:
            entry["remaining_area_ha"] = remaining_area_ha

    validated_parent_step_count = 0
    max_abs_marginal_delta_ha = 0.0
    max_abs_cumulative_delta_ha = 0.0
    latest_locked_row_order: int | None = None
    latest_locked_parent_step_id: str | None = None
    expected_final_managed_area_ha: float | None = None

    for ledger_entry in ledger_entries:
        if not isinstance(ledger_entry, dict):
            raise NamedPipelineError(
                f"{validation_contract.locked_chain_ledger_path} field `entries` must contain mappings."
            )
        parent_step_id = str(ledger_entry.get("parent_step_id", "")).strip()
        row_order = _normalize_int_or_none(ledger_entry.get("row_order"))
        if not parent_step_id or row_order is None:
            raise NamedPipelineError(
                f"{validation_contract.locked_chain_ledger_path} contains an invalid ledger entry."
            )
        parent_audit = parent_step_totals.get(parent_step_id)
        if parent_audit is None:
            raise NamedPipelineError(
                "Strict validation contract mismatch: missing audited parent step "
                f"`{parent_step_id}` for locked ledger row `{row_order}`."
            )
        expected_net_removed_area_ha = _normalize_float_or_none(
            ledger_entry.get("locked_net_removed_area_ha")
        )
        actual_net_removed_area_ha = _normalize_float_or_none(
            parent_audit.get("net_removed_area_ha")
        )
        expected_marginal_compare = (
            0.0
            if expected_net_removed_area_ha is None
            else expected_net_removed_area_ha
        )
        actual_marginal_compare = (
            0.0 if actual_net_removed_area_ha is None else actual_net_removed_area_ha
        )
        marginal_delta_ha = abs(actual_marginal_compare - expected_marginal_compare)
        max_abs_marginal_delta_ha = max(max_abs_marginal_delta_ha, marginal_delta_ha)
        if marginal_delta_ha > tolerance_ha:
            raise NamedPipelineError(
                "Strict validation contract mismatch at row "
                f"`{row_order}` (`{parent_step_id}`): expected locked marginal "
                f"`{expected_marginal_compare:.3f} ha`, got "
                f"`{actual_marginal_compare:.3f} ha`."
            )
        expected_cumulative_remaining_area_ha = _normalize_float_or_none(
            ledger_entry.get("locked_cumulative_remaining_area_ha")
        )
        actual_cumulative_remaining_area_ha = _normalize_float_or_none(
            parent_audit.get("remaining_area_ha")
        )
        if expected_cumulative_remaining_area_ha is None:
            raise NamedPipelineError(
                "Strict validation contract ledger entry is missing "
                f"`locked_cumulative_remaining_area_ha` for `{parent_step_id}`."
            )
        if actual_cumulative_remaining_area_ha is None:
            raise NamedPipelineError(
                "Strict validation contract mismatch: audited parent step "
                f"`{parent_step_id}` is missing `remaining_area_ha`."
            )
        cumulative_delta_ha = abs(
            actual_cumulative_remaining_area_ha - expected_cumulative_remaining_area_ha
        )
        max_abs_cumulative_delta_ha = max(
            max_abs_cumulative_delta_ha, cumulative_delta_ha
        )
        if cumulative_delta_ha > tolerance_ha:
            raise NamedPipelineError(
                "Strict validation contract mismatch at row "
                f"`{row_order}` (`{parent_step_id}`): expected locked cumulative "
                f"`{expected_cumulative_remaining_area_ha:.3f} ha`, got "
                f"`{actual_cumulative_remaining_area_ha:.3f} ha`."
            )
        latest_locked_row_order = row_order
        latest_locked_parent_step_id = parent_step_id
        expected_final_managed_area_ha = expected_cumulative_remaining_area_ha
        validated_parent_step_count += 1

    actual_final_managed_area_ha = _normalize_float_or_none(
        getattr(tsr_result, "final_managed_area_ha", None)
    )
    if expected_final_managed_area_ha is None or actual_final_managed_area_ha is None:
        raise NamedPipelineError(
            "Strict validation contract requires both expected and actual final managed area."
        )
    final_delta_ha = abs(actual_final_managed_area_ha - expected_final_managed_area_ha)
    max_abs_cumulative_delta_ha = max(max_abs_cumulative_delta_ha, final_delta_ha)
    if final_delta_ha > tolerance_ha:
        raise NamedPipelineError(
            "Strict validation contract mismatch at final managed area: expected "
            f"`{expected_final_managed_area_ha:.3f} ha`, got "
            f"`{actual_final_managed_area_ha:.3f} ha`."
        )

    return NamedPipelineValidationResult(
        contract_kind=validation_contract.contract_kind,
        validated_parent_step_count=validated_parent_step_count,
        latest_locked_row_order=latest_locked_row_order,
        latest_locked_parent_step_id=latest_locked_parent_step_id,
        expected_final_managed_area_ha=expected_final_managed_area_ha,
        actual_final_managed_area_ha=actual_final_managed_area_ha,
        max_abs_marginal_delta_ha=max_abs_marginal_delta_ha,
        max_abs_cumulative_delta_ha=max_abs_cumulative_delta_ha,
    )


def validate_locked_chain_strict_preflight(
    *,
    plan: NamedPipelineExecutionPlan,
    tolerance_ha: float = 1e-3,
) -> Mapping[str, Any]:
    validation_contract = plan.validation_contract
    if validation_contract is None:
        raise NamedPipelineError(
            "Strict validation contract is required for this preflight."
        )
    locked_row_order = resolve_locked_chain_strict_row_order(seam_id=plan.seam_id)
    locked_entry = _resolve_locked_chain_entry(
        validation_contract=validation_contract,
        row_order=locked_row_order,
    )
    locked_parent_step_id = str(locked_entry.get("parent_step_id", "")).strip()
    expected_benchmark_area_ha = _normalize_float_or_none(
        locked_entry.get("locked_cumulative_remaining_area_ha")
    )
    if expected_benchmark_area_ha is None:
        raise NamedPipelineError(
            "Strict validation contract ledger entry is missing "
            f"`locked_cumulative_remaining_area_ha` for row `{locked_row_order}`."
        )

    if plan.seam_id == "scratch":
        glb_result = build_tsa_raw_glb(
            source_root=_source_tree_root(),
            instance_root=plan.instance_root,
            tsa="29",
            stash_public_data_glb=False,
        )
        actual_start_area_ha = float(glb_result.clipped_area_ha)
        area_delta_ha = actual_start_area_ha - expected_benchmark_area_ha
        if abs(area_delta_ha) > tolerance_ha:
            raise NamedPipelineError(
                "Strict validation preflight mismatch for seam "
                f"`{plan.seam_id}` at locked row `{locked_row_order}` "
                f"(`{locked_parent_step_id}`): expected `{expected_benchmark_area_ha:.3f} ha`, "
                f"got `{actual_start_area_ha:.3f} ha`, delta `{area_delta_ha:.3f} ha`."
            )
        return {
            "locked_row_order": locked_row_order,
            "locked_parent_step_id": locked_parent_step_id,
            "expected_benchmark_area_ha": expected_benchmark_area_ha,
            "actual_start_area_ha": actual_start_area_ha,
            "area_delta_ha": area_delta_ha,
            "clipped_glb_gdb_path": glb_result.clipped_glb_gdb_path,
            "clipped_glb_feature_class": glb_result.clipped_glb_feature_class,
            "summary_json_path": glb_result.summary_json_path,
            "summary_markdown_path": glb_result.summary_markdown_path,
        }

    if plan.checkpoint_path is None:
        raise NamedPipelineError(
            "Strict validation preflight requires an explicit checkpoint path for seam "
            f"`{plan.seam_id}`."
        )
    actual_start_area_ha = managed_area_ha_from_checkpoint(plan.checkpoint_path)

    if plan.seam_id == "aflb_yield_ready":
        aflb_checkpoint_path = (
            plan.instance_root / "data" / "tsr" / "aflb_checkpoint.feather"
        )
        aflb_area_ha = managed_area_ha_from_checkpoint(aflb_checkpoint_path)
        aflb_delta_ha = actual_start_area_ha - aflb_area_ha
        if abs(aflb_delta_ha) > tolerance_ha:
            raise NamedPipelineError(
                "Strict validation preflight mismatch for seam `aflb_yield_ready`: expected "
                "yield-ready area to preserve AFLB area from "
                f"`{aflb_checkpoint_path}`; AFLB `{aflb_area_ha:.3f} ha`, "
                f"yield-ready `{actual_start_area_ha:.3f} ha`, "
                f"delta `{aflb_delta_ha:.3f} ha`."
            )

    area_delta_ha = actual_start_area_ha - expected_benchmark_area_ha
    if abs(area_delta_ha) > tolerance_ha:
        raise NamedPipelineError(
            "Strict validation preflight mismatch for seam "
            f"`{plan.seam_id}` at locked row `{locked_row_order}` "
            f"(`{locked_parent_step_id}`): expected `{expected_benchmark_area_ha:.3f} ha`, "
            f"got `{actual_start_area_ha:.3f} ha`, delta `{area_delta_ha:.3f} ha`."
        )

    return {
        "locked_row_order": locked_row_order,
        "locked_parent_step_id": locked_parent_step_id,
        "expected_benchmark_area_ha": expected_benchmark_area_ha,
        "actual_start_area_ha": actual_start_area_ha,
        "area_delta_ha": area_delta_ha,
    }


def _validate_locked_chain_parent_step(
    *,
    validation_contract: NamedPipelineValidationContract,
    parent_step_id: str,
    removed_area_ha: float | None,
    remaining_area_ha: float,
    tolerance_ha: float = 1e-3,
) -> NamedPipelineValidationResult:
    locked_entry = _resolve_locked_chain_entry_by_parent_step_id(
        validation_contract=validation_contract,
        parent_step_id=parent_step_id,
    )
    row_order = _normalize_int_or_none(locked_entry.get("row_order"))
    if row_order is None:
        raise NamedPipelineError(
            "Strict validation contract ledger entry is missing row order for "
            f"`{parent_step_id}`."
        )
    expected_removed_ha = _normalize_float_or_none(
        locked_entry.get("locked_net_removed_area_ha")
    )
    expected_remaining_ha = _normalize_float_or_none(
        locked_entry.get("locked_cumulative_remaining_area_ha")
    )
    locked_parent_step_id = str(locked_entry.get("parent_step_id", "")).strip() or None
    if expected_removed_ha is None or expected_remaining_ha is None:
        if expected_remaining_ha is None:
            raise NamedPipelineError(
                "Strict validation contract ledger entry is missing locked cumulative "
                f"value for row `{row_order}`."
            )
        expected_removed_ha = 0.0
    actual_removed_ha = 0.0 if removed_area_ha is None else removed_area_ha
    marginal_delta_ha = actual_removed_ha - expected_removed_ha
    cumulative_delta_ha = remaining_area_ha - expected_remaining_ha
    if abs(marginal_delta_ha) > tolerance_ha or abs(cumulative_delta_ha) > tolerance_ha:
        raise NamedPipelineError(
            "Strict validation mismatch at row "
            f"`{row_order}` (`{locked_parent_step_id}`): expected marginal "
            f"`{expected_removed_ha:.3f} ha`, got `{actual_removed_ha:.3f} ha`, "
            f"delta `{marginal_delta_ha:.3f} ha`; expected cumulative "
            f"`{expected_remaining_ha:.3f} ha`, got `{remaining_area_ha:.3f} ha`, "
            f"delta `{cumulative_delta_ha:.3f} ha`."
        )
    return NamedPipelineValidationResult(
        contract_kind=validation_contract.contract_kind,
        validated_parent_step_count=row_order,
        latest_locked_row_order=row_order,
        latest_locked_parent_step_id=locked_parent_step_id,
        expected_final_managed_area_ha=expected_remaining_ha,
        actual_final_managed_area_ha=remaining_area_ha,
        max_abs_marginal_delta_ha=abs(marginal_delta_ha),
        max_abs_cumulative_delta_ha=abs(cumulative_delta_ha),
    )


def _run_strict_sequence_from_checkpoint(
    *,
    plan: NamedPipelineExecutionPlan,
    start_checkpoint_path: Path,
    start_validated_row_order: int,
    start_validated_parent_step_id: str,
    start_remaining_area_ha: float,
    runtime_logger: Any,
) -> tuple[Any | None, NamedPipelineValidationResult]:
    validation_contract = plan.validation_contract
    if validation_contract is None:
        raise NamedPipelineError(
            "Strict pipeline sequencing requires a validation contract."
        )
    current_checkpoint_path = start_checkpoint_path
    sequence = _resolve_locked_parent_step_sequence(
        recipe_path=plan.thlb_netdown_recipe_path,
        start_after_row_order=start_validated_row_order,
        stop_after_parent_step_id=plan.target_parent_step_id,
    )
    latest_validation = NamedPipelineValidationResult(
        contract_kind=validation_contract.contract_kind,
        validated_parent_step_count=start_validated_row_order,
        latest_locked_row_order=start_validated_row_order,
        latest_locked_parent_step_id=start_validated_parent_step_id,
        expected_final_managed_area_ha=start_remaining_area_ha,
        actual_final_managed_area_ha=start_remaining_area_ha,
        max_abs_marginal_delta_ha=0.0,
        max_abs_cumulative_delta_ha=0.0,
    )
    last_parent_step_result: Any | None = None
    for parent_step in sequence:
        parent_step_id = str(parent_step.get("parent_step_id", "")).strip()
        parent_label = str(parent_step.get("parent_label", "")).strip() or None
        row_order = _normalize_int_or_none(parent_step.get("row_order"))
        land_base_stage = str(parent_step.get("land_base_stage", "")).strip() or None
        runtime_logger.emit(
            {
                "event_kind": "parent_step_started",
                "parent_step_id": parent_step_id,
                "parent_label": parent_label,
                "row_order": row_order,
                "land_base_stage": land_base_stage,
                "locked_execution_class": str(
                    parent_step.get("execution_class", "")
                ).strip()
                or None,
                "checkpoint_path": current_checkpoint_path,
            }
        )
        if _is_reference_only_parent_step(parent_step):
            remaining_area_ha = managed_area_ha_from_checkpoint(current_checkpoint_path)
            latest_validation = _validate_locked_chain_parent_step(
                validation_contract=validation_contract,
                parent_step_id=parent_step_id,
                removed_area_ha=None,
                remaining_area_ha=remaining_area_ha,
            )
            runtime_logger.emit(
                {
                    "event_kind": "parent_step_finished",
                    "parent_step_id": parent_step_id,
                    "parent_label": parent_label,
                    "row_order": row_order,
                    "land_base_stage": land_base_stage,
                    "run_status": "reference_validated",
                    "remaining_area_ha": remaining_area_ha,
                    "checkpoint_path": current_checkpoint_path,
                    "locked_execution_class": str(
                        parent_step.get("execution_class", "")
                    ).strip()
                    or None,
                }
            )
            continue
        locked_parent_step = _validate_locked_strict_parent_step_execution_contract(
            parent_step
        )
        parent_step_result = run_tsr_thlb_locked_parent_step(
            recipe_path=plan.thlb_netdown_recipe_path,
            parent_step_id=parent_step_id,
            checkpoint_path=current_checkpoint_path,
            runtime_event_sink=runtime_logger.emit,
        )
        last_parent_step_result = parent_step_result
        current_checkpoint_path = parent_step_result.output_path
        latest_validation = _validate_locked_chain_parent_step(
            validation_contract=validation_contract,
            parent_step_id=parent_step_id,
            removed_area_ha=parent_step_result.removed_area_ha,
            remaining_area_ha=parent_step_result.remaining_area_ha,
        )
        runtime_logger.emit(
            {
                "event_kind": "parent_step_finished",
                "parent_step_id": parent_step_result.parent_step_id,
                "parent_label": parent_step_result.parent_label,
                "row_order": row_order,
                "land_base_stage": land_base_stage,
                "run_status": parent_step_result.status,
                "remaining_area_ha": parent_step_result.remaining_area_ha,
                "checkpoint_path": current_checkpoint_path,
                "output_checkpoint_path": parent_step_result.output_path,
                "locked_execution_class": str(
                    locked_parent_step.get("execution_class", "")
                ).strip()
                or None,
            }
        )
    return last_parent_step_result, latest_validation


@dataclass(frozen=True)
class Tsa29LockedChainContractHandler:
    """FEMIC named-pipeline handler for the TSA29 strict locked-chain contract."""

    contract_kind: str = CONTRACT_KIND

    def run_before_default(
        self,
        *,
        plan: NamedPipelineExecutionPlan,
        runtime_logger: Any,
        runtime_event_log_path: Path,
    ) -> NamedPipelineExecutionResult | None:
        if plan.validation_contract is None:
            return None
        runtime_logger.emit(
            {
                "event_kind": "pipeline_validation_preflight_started",
                "validation_contract_kind": plan.validation_contract.contract_kind,
            }
        )
        preflight_result = validate_locked_chain_strict_preflight(plan=plan)
        runtime_logger.emit(
            {
                "event_kind": "pipeline_validation_preflight_finished",
                "validation_contract_kind": plan.validation_contract.contract_kind,
                **preflight_result,
            }
        )
        if plan.seam_id not in {"scratch", "glb", "aflb", "aflb_yield_ready"}:
            return None
        start_checkpoint_path = plan.checkpoint_path
        if plan.seam_id == "scratch":
            glb_checkpoint_path = materialize_glb_checkpoint_from_result(
                instance_root=plan.instance_root,
                clipped_glb_gdb_path=cast(
                    Path, preflight_result["clipped_glb_gdb_path"]
                ),
                clipped_glb_feature_class=cast(
                    str, preflight_result["clipped_glb_feature_class"]
                ),
            )
            start_checkpoint_path = glb_checkpoint_path
            runtime_logger.emit(
                {
                    "event_kind": "pipeline_preflight_resolved",
                    "notes": f"glb_checkpoint_path={glb_checkpoint_path}",
                }
            )
        if plan.target_parent_step_id is not None:
            parent_step_result, validation_result = (
                _run_strict_sequence_from_checkpoint(
                    plan=plan,
                    start_checkpoint_path=cast(Path, start_checkpoint_path),
                    start_validated_row_order=cast(
                        int, preflight_result["locked_row_order"]
                    ),
                    start_validated_parent_step_id=cast(
                        str, preflight_result["locked_parent_step_id"]
                    ),
                    start_remaining_area_ha=cast(
                        float, preflight_result["actual_start_area_ha"]
                    ),
                    runtime_logger=runtime_logger,
                )
            )
            runtime_logger.emit(
                {
                    "event_kind": "pipeline_run_finished",
                    "validated_parent_step_count": (
                        validation_result.validated_parent_step_count
                    ),
                    "latest_locked_row_order": validation_result.latest_locked_row_order,
                    "latest_locked_parent_step_id": (
                        validation_result.latest_locked_parent_step_id
                    ),
                    "expected_final_managed_area_ha": (
                        validation_result.expected_final_managed_area_ha
                    ),
                    "actual_final_managed_area_ha": (
                        validation_result.actual_final_managed_area_ha
                    ),
                    "notes": (
                        "strict seam executed the locked parent-step sequence "
                        "through the requested stop target"
                    ),
                }
            )
            return NamedPipelineExecutionResult(
                plan=plan,
                tsr_thlb_result=None,
                tsr_parent_step_result=parent_step_result,
                validation_result=validation_result,
                runtime_event_log_path=runtime_event_log_path,
            )
        validation_result = NamedPipelineValidationResult(
            contract_kind=plan.validation_contract.contract_kind,
            validated_parent_step_count=cast(int, preflight_result["locked_row_order"]),
            latest_locked_row_order=cast(
                int | None, preflight_result.get("locked_row_order")
            ),
            latest_locked_parent_step_id=cast(
                str | None, preflight_result.get("locked_parent_step_id")
            ),
            expected_final_managed_area_ha=cast(
                float | None, preflight_result.get("expected_benchmark_area_ha")
            ),
            actual_final_managed_area_ha=cast(
                float | None, preflight_result.get("actual_start_area_ha")
            ),
            max_abs_marginal_delta_ha=0.0,
            max_abs_cumulative_delta_ha=abs(
                cast(float, preflight_result.get("area_delta_ha", 0.0))
            ),
        )
        runtime_logger.emit(
            {
                "event_kind": "pipeline_run_finished",
                "validated_parent_step_count": (
                    validation_result.validated_parent_step_count
                ),
                "latest_locked_row_order": validation_result.latest_locked_row_order,
                "latest_locked_parent_step_id": (
                    validation_result.latest_locked_parent_step_id
                ),
                "expected_final_managed_area_ha": (
                    validation_result.expected_final_managed_area_ha
                ),
                "actual_final_managed_area_ha": (
                    validation_result.actual_final_managed_area_ha
                ),
                "notes": (
                    "strict seam validated the locked-chain restart row and "
                    "stopped before the next parent step"
                ),
            }
        )
        return NamedPipelineExecutionResult(
            plan=plan,
            tsr_thlb_result=None,
            validation_result=validation_result,
            runtime_event_log_path=runtime_event_log_path,
        )

    def validate_after_default(
        self,
        *,
        plan: NamedPipelineExecutionPlan,
        tsr_result: TsrThlbNetdownRecipeRunResult,
    ) -> NamedPipelineValidationResult | None:
        return validate_locked_chain_strict_result(plan=plan, tsr_result=tsr_result)


def provider_factory() -> Tsa29LockedChainContractHandler:
    """Return the TSA29 strict locked-chain named-pipeline contract handler."""

    return Tsa29LockedChainContractHandler()


__all__ = [
    "CONTRACT_KIND",
    "Tsa29LockedChainContractHandler",
    "managed_area_ha_from_checkpoint",
    "materialize_glb_checkpoint_from_result",
    "provider_factory",
    "resolve_locked_chain_strict_row_order",
    "validate_locked_chain_strict_preflight",
    "validate_locked_chain_strict_result",
]
