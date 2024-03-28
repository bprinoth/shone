# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

import datetime

# -- Project information -----------------------------------------------------

# The full version, including alpha/beta/rc tags
from shone import __version__

release = __version__

project = "shone"
author = "Brett M. Morris, Jens Hoeijmakers"
copyright = f"{datetime.datetime.now().year}, {author}"  # noqa: A001

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named "sphinx.ext.*") or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.doctest',
    'sphinx.ext.mathjax',
    'sphinx_automodapi.automodapi',
    'sphinx_automodapi.smart_resolver',
    'sphinx.ext.autosectionlabel',
    "matplotlib.sphinxext.plot_directive",
    "numpydoc",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# Treat everything in single ` as a Python reference.
default_role = 'py:obj'

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'astropy': ('https://docs.astropy.org/en/stable/', None),
    'matplotlib': ('http://matplotlib.org/stable', None),
}
# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# By default, when rendering docstrings for classes, sphinx.ext.autodoc will
# make docs with the class-level docstring and the class-method docstrings,
# but not the __init__ docstring, which often contains the parameters to
# class constructors across the scientific Python ecosystem. The option below
# will append the __init__ docstring to the class-level docstring when rendering
# the docs. For more options, see:
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#confval-autoclass_content
autoclass_content = "both"

# -- Other options ----------------------------------------------------------

github_issues_url = 'https://github.com/bmorris3/shone/issues/'

release = __version__
dev = "dev" in release

html_copy_source = False
html_theme = 'sphinx_book_theme'

html_theme_options = {
    "github_url": "https://github.com/bmorris3/shone",
    "use_edit_page_button": True,
    "use_download_button": True,
    "repository_url": "https://github.com/bmorris3/shone",
    "repository_branch": "main",
    "path_to_docs": "docs",
}

html_context = {
    "default_mode": "light",
    "to_be_indexed": ["stable", "latest"],
    "is_development": dev,
    "github_user": "bmorris3",
    "github_repo": "shone",
    "github_version": "main",
    "doc_path": "docs",
    "display_github": True,
    "conf_py_path": "docs/",
}

html_logo = "logo/logo.png"
html_favicon = "logo/logo.ico"

autosectionlabel_prefix_document = True

numpydoc_show_class_members = False
autodoc_inherit_docstrings = True

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '{0}'.format(project)

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'

# Prefixes that are ignored for sorting the Python module index
modindex_common_prefix = ["shone."]

suppress_warnings = ['autosectionlabel.*']
