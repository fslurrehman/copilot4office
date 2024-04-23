# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'copilot4office'
copyright = '2024, Faisal Rehman'
author = 'Faisal Rehman'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
    ]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys

# Calculate the path to the root of the project, `copilot4office`
docs_base = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(docs_base, '..', '..'))

# Add the `presentation` package to the path
sys.path.insert(0, os.path.join(project_root, 'presentation'))
