from __future__ import annotations

from importlib.util import find_spec
from pathlib import Path


project = "femic-tsa29-instance"
author = "UBC-FRESH"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx.ext.autosummary"]
autosummary_generate = True
templates_path = ["_templates"]
exclude_patterns = ["_build"]

if find_spec("sphinx_rtd_theme"):
    html_theme = "sphinx_rtd_theme"
else:
    html_theme = "alabaster"

_static_dir = Path(__file__).with_name("_static")
html_static_path = ["_static"] if _static_dir.exists() else []
