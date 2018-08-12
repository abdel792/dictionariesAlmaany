# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "dictionariesAlmaany",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Dictionaries Almaany"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""
	This addon helps get the meaning of single words from www.almaany.com website.
	Press nvda+windows+d, dictionaries almaany dialog will be displayed, and you will be standing on an edit field
	if when pressing this command, you were standing on a selected word, the word will be put in the edit field
	otherwise, enter in the edit field the word you want, tab an choose the dictionary you want and press enter
	the meaning of the word will be displayed in a separate browseable message box.
	"""),
	# version
	"addon_version" : "1.1",
	# Author(s)
	"addon_author" : u"Ibrahim Hamadeh <ibra.hamadeh@hotmail.com>",
	# URL for the add-on documentation support
	"addon_url" : "https://github.com/ibrahim-h/dictionariesAlmaany.git",
	# Documentation file name
	"addon_docFileName" : "readme.html",
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "dictionariesAlmaany", "*.py"), ]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
