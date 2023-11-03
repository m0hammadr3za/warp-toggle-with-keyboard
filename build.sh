#!/bin/bash

# Build the executable
pyinstaller --onefile \
            --noconsole \
            --add-data "show-hidden-icons;show-hidden-icons" \
            --add-data "warp-icon;warp-icon" \
            --add-data "toggle-image;toggle-image" \
            script.py

# Rename the .exe file
mv dist/script.exe dist/cloudflare-warp-toggle-shortcut.exe

# Create "executable" directory if it doesn't exist
mkdir -p executable

# Move the renamed .exe file to the "executable" directory
mv dist/cloudflare-warp-toggle-shortcut.exe executable/

# Cleanup
rm -rf build dist script.spec

echo "Build complete!"
