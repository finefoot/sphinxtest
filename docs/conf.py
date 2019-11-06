import os
import sys
sys.path.insert(0, os.path.abspath("../src"))

project = "Fibonacci"
copyright = "2019"
extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
