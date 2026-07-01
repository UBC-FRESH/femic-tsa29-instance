from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
import tomllib

import pytest

from femic import named_pipelines
from tsa29_femic import locked_chain


def _write_ledger(path: Path, entries: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"entries": entries}, indent=2), encoding="utf-8")


def _plan(
    instance_root: Path,
    *,
    seam_id: str = "aflb_yield_ready",
    checkpoint_path: Path | None = None,
    target_parent_step_id: str | None = None,
) -> named_pipelines.NamedPipelineExecutionPlan:
    ledger_path = instance_root / "config" / "tsr" / "thlb_locked_chain_ledger.json"
    return named_pipelines.NamedPipelineExecutionPlan(
        runbook_path=instance_root / "runbooks" / "pipelines" / "tsa29.yaml",
        instance_root=instance_root,
        pipeline_id="tsr.thlb_strict",
        pipeline_label="TSR strict THLB product lane",
        seam_id=seam_id,
        checkpoint_path=checkpoint_path,
        run_profile_path=None,
        overlay_paths=(),
        parameter_files=(),
        validation_contract=named_pipelines.NamedPipelineValidationContract(
            contract_kind="tsa29_locked_chain_strict",
            locked_chain_ledger_path=ledger_path,
            comparison_report_path=None,
            required_recipe_path=instance_root
            / "workbench"
            / "tsr"
            / "thlb_netdown.locked.recipe.yaml",
        ),
        target_parent_step_id=target_parent_step_id,
        user_registry_path=None,
        instance_registry_path=None,
        explicit_registry_paths=(),
        thlb_netdown_recipe_path=instance_root
        / "workbench"
        / "tsr"
        / "thlb_netdown.locked.recipe.yaml",
        source_layers_recipe_path=instance_root
        / "config"
        / "tsr"
        / "source_layers.recipe.yaml",
        execution_mode="reconstructed",
    )


def test_entry_point_metadata_registers_contract_provider() -> None:
    payload = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    assert (
        payload["project"]["entry-points"]["femic.named_pipeline_contracts"][
            "tsa29_locked_chain_strict"
        ]
        == "tsa29_femic.locked_chain:provider_factory"
    )


def test_provider_factory_returns_strict_contract_handler() -> None:
    handler = locked_chain.provider_factory()

    assert handler.contract_kind == "tsa29_locked_chain_strict"


def test_resolve_locked_chain_strict_row_order() -> None:
    assert locked_chain.resolve_locked_chain_strict_row_order(seam_id="scratch") == 1
    assert locked_chain.resolve_locked_chain_strict_row_order(seam_id="glb") == 1
    assert locked_chain.resolve_locked_chain_strict_row_order(seam_id="aflb") == 5
    assert (
        locked_chain.resolve_locked_chain_strict_row_order(seam_id="aflb_yield_ready")
        == 5
    )

    with pytest.raises(
        named_pipelines.NamedPipelineError, match="does not yet support"
    ):
        locked_chain.resolve_locked_chain_strict_row_order(seam_id="lhlb_curve_ready")


def test_validate_locked_chain_strict_result_accepts_matching_audit(
    tmp_path: Path,
) -> None:
    instance_root = tmp_path / "instance"
    audit_path = instance_root / "runtime" / "audit.json"
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(
        json.dumps(
            {
                "steps": [
                    {
                        "parent_step_id": "thlb_parent_005_analysis_forest_land_base",
                        "order_index": 5,
                        "net_removed_area_ha": 0.0,
                        "remaining_area_ha": 800.0,
                    }
                ]
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    _write_ledger(
        instance_root / "config" / "tsr" / "thlb_locked_chain_ledger.json",
        [
            {
                "row_order": 5,
                "parent_step_id": "thlb_parent_005_analysis_forest_land_base",
                "locked_net_removed_area_ha": None,
                "locked_cumulative_remaining_area_ha": 800.0,
            }
        ],
    )

    result = locked_chain.validate_locked_chain_strict_result(
        plan=_plan(instance_root),
        tsr_result=SimpleNamespace(audit_path=audit_path, final_managed_area_ha=800.0),
    )

    assert result.contract_kind == "tsa29_locked_chain_strict"
    assert result.validated_parent_step_count == 1
    assert result.latest_locked_row_order == 5
    assert result.expected_final_managed_area_ha == pytest.approx(800.0)


def test_validate_locked_chain_strict_result_rejects_mismatch(tmp_path: Path) -> None:
    instance_root = tmp_path / "instance"
    audit_path = instance_root / "runtime" / "audit.json"
    audit_path.parent.mkdir(parents=True, exist_ok=True)
    audit_path.write_text(
        json.dumps(
            {
                "steps": [
                    {
                        "parent_step_id": "thlb_parent_005_analysis_forest_land_base",
                        "order_index": 5,
                        "net_removed_area_ha": 10.0,
                        "remaining_area_ha": 790.0,
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    _write_ledger(
        instance_root / "config" / "tsr" / "thlb_locked_chain_ledger.json",
        [
            {
                "row_order": 5,
                "parent_step_id": "thlb_parent_005_analysis_forest_land_base",
                "locked_net_removed_area_ha": None,
                "locked_cumulative_remaining_area_ha": 800.0,
            }
        ],
    )

    with pytest.raises(named_pipelines.NamedPipelineError, match="mismatch at row `5`"):
        locked_chain.validate_locked_chain_strict_result(
            plan=_plan(instance_root),
            tsr_result=SimpleNamespace(
                audit_path=audit_path,
                final_managed_area_ha=790.0,
            ),
        )


def test_validate_locked_chain_preflight_uses_checkpoint_area(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    instance_root = tmp_path / "instance"
    checkpoint_path = instance_root / "data" / "tsr" / "aflb_yield_ready.feather"
    _write_ledger(
        instance_root / "config" / "tsr" / "thlb_locked_chain_ledger.json",
        [
            {
                "row_order": 5,
                "parent_step_id": "thlb_parent_005_analysis_forest_land_base",
                "locked_net_removed_area_ha": None,
                "locked_cumulative_remaining_area_ha": 800.0,
            }
        ],
    )
    monkeypatch.setattr(
        locked_chain,
        "managed_area_ha_from_checkpoint",
        lambda path: 800.0,
    )

    result = locked_chain.validate_locked_chain_strict_preflight(
        plan=_plan(instance_root, checkpoint_path=checkpoint_path)
    )

    assert result["locked_row_order"] == 5
    assert result["actual_start_area_ha"] == pytest.approx(800.0)


def test_handler_routes_locked_sequence_before_default_runner(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    instance_root = tmp_path / "instance"
    checkpoint_path = instance_root / "data" / "tsr" / "glb_checkpoint.feather"
    _write_ledger(
        instance_root / "config" / "tsr" / "thlb_locked_chain_ledger.json",
        [
            {
                "row_order": 1,
                "parent_step_id": "thlb_parent_001_total_tsa_area",
                "locked_net_removed_area_ha": None,
                "locked_cumulative_remaining_area_ha": 1000.0,
            },
            {
                "row_order": 2,
                "parent_step_id": "thlb_parent_002_land_not_administered_by_the_province",
                "locked_net_removed_area_ha": 200.0,
                "locked_cumulative_remaining_area_ha": 800.0,
            },
        ],
    )
    plan = _plan(
        instance_root,
        seam_id="glb",
        checkpoint_path=checkpoint_path,
        target_parent_step_id="thlb_parent_002_land_not_administered_by_the_province",
    )
    monkeypatch.setattr(
        locked_chain,
        "managed_area_ha_from_checkpoint",
        lambda path: 1000.0 if path == checkpoint_path else 800.0,
    )
    monkeypatch.setattr(
        locked_chain,
        "load_tsr_thlb_netdown_recipe",
        lambda path: SimpleNamespace(
            parent_steps=(
                {
                    "parent_step_id": "thlb_parent_001_total_tsa_area",
                    "row_order": 1,
                    "parent_kind": "milestone",
                    "execution_class": "reference_only",
                },
                {
                    "parent_step_id": "thlb_parent_002_land_not_administered_by_the_province",
                    "row_order": 2,
                    "approved": True,
                    "compiled_logic": ({"step_id": "step_002"},),
                },
            )
        ),
    )
    monkeypatch.setattr(
        locked_chain,
        "run_tsr_thlb_locked_parent_step",
        lambda **kwargs: SimpleNamespace(
            parent_step_id="thlb_parent_002_land_not_administered_by_the_province",
            parent_label="Land not administered by the Province",
            output_path=instance_root
            / "data"
            / "tsr"
            / "strict_chain"
            / "02_thlb_parent_002_land_not_administered_by_the_province.feather",
            status="applied",
            removed_area_ha=200.0,
            remaining_area_ha=800.0,
        ),
    )
    event_payloads: list[dict[str, object]] = []
    runtime_logger = SimpleNamespace(emit=event_payloads.append)

    result = locked_chain.provider_factory().run_before_default(
        plan=plan,
        runtime_logger=runtime_logger,
        runtime_event_log_path=instance_root / "runtime" / "events.log",
    )

    assert result is not None
    assert result.tsr_thlb_result is None
    assert result.validation_result is not None
    assert result.validation_result.validated_parent_step_count == 2
    assert any(
        item.get("event_kind") == "pipeline_validation_preflight_started"
        for item in event_payloads
    )
