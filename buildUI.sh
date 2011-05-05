#! /bin/sh
# Calls pyuic4 to compile src/asset.gui into src/asset_dialog.py

#Build the Asset Editing Dialog
pyuic4 src/asset.ui -o src/asset_dialog.py
