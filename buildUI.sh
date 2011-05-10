#! /bin/sh
# Calls pyuic4 to compile the Qt4 .ui files into .py files

#Build the Asset Editing Dialog
pyuic4 src/asset.ui -o src/asset_dialog.py

#Build the New Asset Prompt Dialog
pyuic4c src/newAsset.ui -o src/new_asset_dialog.py
