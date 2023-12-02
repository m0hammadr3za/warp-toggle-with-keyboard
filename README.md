# WARP Toggle With Keyboard

This program is designed for Windows 11 users who use Cloudflare Warp and want to control their Warp connection using a keyboard shortcut (ctrl+shift+x by default), without manually clicking on the toggle button.

## How Does It Work

This is a simplified version using direct commands instead of UI interaction. When you press ctrl+shift+x, the program executes commands to toggle the Warp connection status.

## Requirements

Before running `script.py`, ensure you have Python installed along with these packages:

-   keyboard
-   subprocess
-   threading

To run `build.bat`, you need:

-   pyinstaller

## Running the Executable at Startup in Windows

To have the Cloudflare Warp Toggle Shortcut run at startup in Windows:

1. Place the executable where you want.
2. Press Win + R, type shell:startup, and press Enter to open the Startup folder.
3. Paste a shortcut to the WARP toggle with keyboard.exe into this folder.

The Cloudflare Warp Toggle Shortcut will now automatically run when you start Windows.
