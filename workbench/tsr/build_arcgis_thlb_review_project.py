from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import arcpy


BLANK_APRX = Path(
    r"C:\Program Files\ArcGIS\Pro\Resources\ArcToolBox\Services\routingservices\data\Blank.aprx"
)


@dataclass(frozen=True)
class LayerSpec:
    name: str
    source_path: Path
    geometry_family: str
    transparency: int
    draw_order: int


def _layer_source_from_gpkg(path: Path) -> Path:
    return path / path.stem


def _classify_layer(path: Path) -> tuple[str, int, int]:
    name = path.stem.upper()
    if "STANDS" in name:
        return "polygon", 75, 0
    if "FRAGMENTS" in name:
        return "polygon", 82, 5
    if "FADM_TSA" in name:
        return "polygon", 0, 1000
    if "FWA_LAKES" in name:
        return "polygon", 35, 120
    if "ROAD" in name or "HIGHWAY" in name:
        return "line", 0, 900
    if "CUT_BLOCK" in name:
        return "polygon", 55, 700
    if "OGMA" in name:
        return "polygon", 45, 760
    if "PARK" in name or "PROTECTED" in name:
        return "polygon", 40, 780
    if "WILDLIFE" in name or "UNGULATE" in name or "WHA" in name:
        return "polygon", 50, 770
    if "TERRAIN" in name or "BURN" in name or "VISUAL" in name:
        return "polygon", 55, 740
    if "BOUNDARIES" in name or "TFL" in name or "BCTS" in name:
        return "polygon", 25, 850
    if "TENURE" in name or "LIC" in name:
        return "polygon", 45, 730
    if "BEC" in name or "VEG_COMP" in name:
        return "polygon", 70, 200
    if "CONTOUR" in name:
        return "point", 0, 950
    return "polygon", 60, 500


def discover_layer_specs(instance_root: Path) -> list[LayerSpec]:
    root = instance_root.resolve()
    specs: list[LayerSpec] = []

    context_layers = [
        root / "data" / "shp" / "tsa29.shp" / "stands.shp",
        root / "output" / "patchworks_tsa29_validated" / "fragments" / "fragments.shp",
    ]
    for path in context_layers:
        if not path.exists():
            continue
        geometry_family, transparency, draw_order = _classify_layer(path)
        specs.append(
            LayerSpec(
                name=path.stem,
                source_path=path,
                geometry_family=geometry_family,
                transparency=transparency,
                draw_order=draw_order,
            )
        )

    bcdc_root = root / "data" / "downloads" / "bcdc"
    for gpkg in sorted(bcdc_root.rglob("*.gpkg")):
        geometry_family, transparency, draw_order = _classify_layer(gpkg)
        specs.append(
            LayerSpec(
                name=gpkg.stem,
                source_path=_layer_source_from_gpkg(gpkg),
                geometry_family=geometry_family,
                transparency=transparency,
                draw_order=draw_order,
            )
        )

    specs.sort(key=lambda item: (item.draw_order, item.name.casefold()))
    return specs


def _write_layer_file(source_path: Path, layer_file: Path, layer_name: str) -> Path:
    layer_file.parent.mkdir(parents=True, exist_ok=True)
    temp_layer_name = f"tmp_{layer_name}".replace(" ", "_").replace("-", "_")
    if arcpy.Exists(temp_layer_name):
        arcpy.management.Delete(temp_layer_name)
    if arcpy.Exists(str(layer_file)):
        arcpy.management.Delete(str(layer_file))
    arcpy.management.MakeFeatureLayer(str(source_path), temp_layer_name)
    arcpy.management.SaveToLayerFile(temp_layer_name, str(layer_file), "ABSOLUTE")
    arcpy.management.Delete(temp_layer_name)
    return layer_file


def _apply_layer_defaults(layer: object, spec: LayerSpec) -> None:
    try:
        layer.name = spec.name
    except Exception:
        pass
    try:
        layer.transparency = spec.transparency
    except Exception:
        pass


def build_arcgis_review_project(instance_root: Path) -> tuple[Path, Path]:
    if not BLANK_APRX.exists():
        raise FileNotFoundError(f"ArcGIS Pro blank template not found: {BLANK_APRX}")

    root = instance_root.resolve()
    workbench_root = root / "workbench" / "tsr" / "arcgis"
    layer_file_root = workbench_root / "layers"
    project_path = workbench_root / "tsa29_thlb_review.aprx"
    manifest_path = workbench_root / "tsa29_thlb_review_manifest.json"
    workbench_root.mkdir(parents=True, exist_ok=True)

    if project_path.exists():
        project_path.unlink()

    aprx = arcpy.mp.ArcGISProject(str(BLANK_APRX))
    aprx.saveACopy(str(project_path))
    aprx = arcpy.mp.ArcGISProject(str(project_path))
    map_obj = aprx.listMaps()[0]
    map_obj.name = "TSA29 THLB Review"

    added_layers = []
    tsa_boundary_layer = None
    for spec in discover_layer_specs(root):
        layer_file = _write_layer_file(
            spec.source_path,
            layer_file_root / f"{spec.name}.lyrx",
            spec.name,
        )
        map_obj.addLayer(arcpy.mp.LayerFile(str(layer_file)), "TOP")
        layer = map_obj.listLayers()[0]
        _apply_layer_defaults(layer, spec)
        if "FADM_TSA" in spec.name.upper():
            tsa_boundary_layer = layer
        added_layers.append(
            {
                "name": spec.name,
                "source_path": str(spec.source_path),
                "geometry_family": spec.geometry_family,
                "transparency": spec.transparency,
                "draw_order": spec.draw_order,
                "layer_file": str(layer_file),
            }
        )

    if tsa_boundary_layer is not None:
        try:
            map_obj.defaultCamera.setExtent(tsa_boundary_layer.getExtent())
        except Exception:
            pass

    aprx.save()
    manifest_path.write_text(
        json.dumps(
            {
                "project_path": str(project_path),
                "layer_count": len(added_layers),
                "layers": added_layers,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return project_path, manifest_path


if __name__ == "__main__":
    instance_root = Path(__file__).resolve().parents[2]
    project_path, manifest_path = build_arcgis_review_project(instance_root)
    print(project_path)
    print(manifest_path)
