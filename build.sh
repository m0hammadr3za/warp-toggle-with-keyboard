#!/bin/bash

# Build the executable
pyinstaller --onefile \
            --noconsole \
            script.py

# Rename the .exe file
mv dist/script.exe dist/cloudflare-warp-toggle-shortcut.exe

# Create "executable" directory if it doesn't exist
mkdir -p "Cloudflare warp keyboard shortcut"

# Move the renamed .exe file to the "executable" directory
mv dist/cloudflare-warp-toggle-shortcut.exe "Cloudflare warp keyboard shortcut"/

# Copy assets to "executable" directory
cp -r show-hidden-icons/ "Cloudflare warp keyboard shortcut"/
cp -r toggle-image/ "Cloudflare warp keyboard shortcut"/
cp -r warp-icon/ "Cloudflare warp keyboard shortcut"/

# Cleanup
rm -rf build dist script.spec

echo "Build complete!"
