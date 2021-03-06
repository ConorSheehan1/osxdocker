# -*- coding: utf-8 -*-
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Standard Library
import os
import sys

# osxdocker
from osxdocker import __version__

sys.path.insert(0, os.path.abspath("../.."))


# -- Project information -----------------------------------------------------
project = "osxdocker"
copyright = "2020, Conor Sheehan"
author = "Conor Sheehan"


# The short X.Y version.
version = __version__
# The full version, including alpha/beta/rc tags.
release = version

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones. Order matters! https://github.com/agronholm/sphinx-autodoc-typehints/issues/15
extensions = [
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

# https://github.com/readthedocs/readthedocs.org/issues/2569#issuecomment-485117471
master_doc = "index"
autodoc_default_flags = ["members"]
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_use_param = True
