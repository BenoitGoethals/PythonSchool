import os
import sys

sys.path.insert(0, os.path.abspath('..'))
project = 'school'
copyright = '2023, ABL'
author = 'Ben'
release = '0.0.1'


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']