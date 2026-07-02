from __future__ import annotations

from importlib import metadata

from tsa29_femic.instance_catalog import provider_factory


def test_instance_catalog_provider_metadata() -> None:
    provider = provider_factory()

    assert provider.provider_id == "tsa29"
    payload = provider.load_catalog_payload()
    assert payload["support_repos"][0]["repo_id"] == "femic-public-data"
    assert payload["instances"][0]["builtin_id"] == "tsa29"
    assert payload["instances"][0]["target_dirname"] == "femic-tsa29-instance"


def test_package_exposes_instance_catalog_entry_point() -> None:
    entry_points = metadata.entry_points().select(group="femic.instance_catalogs")
    matches = [
        entry_point for entry_point in entry_points if entry_point.name == "tsa29"
    ]
    assert matches
    assert matches[0].value == "tsa29_femic.instance_catalog:provider_factory"
