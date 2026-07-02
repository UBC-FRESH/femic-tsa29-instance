from __future__ import annotations

from pathlib import Path
import tomllib

import pytest

from femic.tsr_catalog import TsrAdjudicationOverlayError
from tsa29_femic import tsr_adjudication


def test_pyproject_exposes_tsr_adjudication_entry_point() -> None:
    pyproject = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))

    entry_points = pyproject["project"]["entry-points"][
        "femic.tsr_adjudication_overlays"
    ]

    assert entry_points["tsa29"] == "tsa29_femic.tsr_adjudication:provider_factory"


def test_provider_factory_returns_tsa29_provider() -> None:
    provider = tsr_adjudication.provider_factory()

    assert provider.provider_id == "tsa29"


def test_provider_classifies_tsa29_table3_rows() -> None:
    provider = tsr_adjudication.provider_factory()

    future_roads = provider.classify_land_base_summary_row(label="Future roads")
    proven_rights = provider.classify_land_base_summary_row(
        label="Proven Aboriginal Rights areas"
    )

    assert future_roads is not None
    assert future_roads.land_base_stage == "lhlb_to_thlb"
    assert future_roads.execution_class == "projected_harvest_exclusion"
    assert future_roads.benchmark_role == "deduction"
    assert proven_rights is not None
    assert proven_rights.land_base_stage == "aflb_to_lhlb"
    assert proven_rights.execution_class == "legal_harvest_exclusion"


def test_provider_rejects_legacy_checkpoint_path(tmp_path: Path) -> None:
    provider = tsr_adjudication.provider_factory()

    with pytest.raises(TsrAdjudicationOverlayError, match="Legacy"):
        provider.validate_checkpoint_path(
            instance_root=tmp_path,
            checkpoint_path=tmp_path / "data" / "ria_vri_vclr1p_checkpoint7.feather",
        )


def test_provider_accepts_strict_seam_checkpoint_path(tmp_path: Path) -> None:
    provider = tsr_adjudication.provider_factory()
    checkpoint_path = tmp_path / "data" / "tsr" / "aflb_checkpoint.feather"
    checkpoint_path.parent.mkdir(parents=True)
    checkpoint_path.write_text("placeholder", encoding="utf-8")

    assert provider.is_strict_seam_checkpoint_path(
        instance_root=tmp_path,
        checkpoint_path=checkpoint_path,
    )
    assert not provider.is_strict_seam_checkpoint_path(
        instance_root=tmp_path,
        checkpoint_path=tmp_path / "data" / "checkpoint.feather",
    )


def test_provider_returns_tsa29_reconstruction_gap_interpretation() -> None:
    provider = tsr_adjudication.provider_factory()

    interpretation = provider.reconstruction_gap_interpretation(
        recipe_tsa_id="tsa_29",
        parent_step={
            "parent_step_id": "thlb_parent_002_land_not_administered_by_the_province"
        },
    )

    assert interpretation is not None
    assert interpretation.problem_ownership == "model_endogenous"
    assert interpretation.difference_nature == "strict_logic_overcut"
    assert "ownership interpretation" in interpretation.engineering_interpretation


def test_provider_report_notes_are_tsa29_scoped() -> None:
    provider = tsr_adjudication.provider_factory()

    notes = provider.report_notes(recipe_tsa_id="tsa_29")

    assert len(notes) == 2
    assert "active repair ledger" in notes[0]
    assert provider.report_notes(recipe_tsa_id="tsa_01") == ()
