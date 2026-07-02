"""TSA29-owned FEMIC instance catalog provider."""

from __future__ import annotations

from dataclasses import dataclass
from importlib import resources
from typing import Any

import yaml


@dataclass(frozen=True)
class Tsa29InstanceCatalogProvider:
    """Expose the TSA29 installable instance catalog entry to FEMIC."""

    provider_id: str = "tsa29"

    def load_catalog_payload(self) -> dict[str, Any]:
        resource = resources.files("tsa29_femic.resources").joinpath(
            "instance_catalog.yaml"
        )
        payload = yaml.safe_load(resource.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("TSA29 instance catalog payload must be a mapping.")
        return payload


def provider_factory() -> Tsa29InstanceCatalogProvider:
    """Return the TSA29 instance catalog provider."""

    return Tsa29InstanceCatalogProvider()
