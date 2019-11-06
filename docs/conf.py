import os
import sys
sys.path.insert(0, os.path.abspath("../src"))

project = "Fibonacci"
copyright = "2017, AUTHOR"

extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_theme_options = {"collapse_navigation": True}
