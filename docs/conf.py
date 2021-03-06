import os
import sys
sys.path.insert(0, os.path.abspath("../src"))

project = "PROJECT"
copyright = "2017, AUTHOR"

extensions = ["sphinx.ext.autodoc"]
nitpicky = True
templates_path = ["_templates"]
html_theme = "sphinx_rtd_theme"
html_theme_options = {"collapse_navigation": True}
