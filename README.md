# Cloudflare Warp Toggle Shortcut

This program is designed for Windows 11 users who use Cloudflare Warp and want to toggle the Warp connection quickly and easily using a keyboard shortcut(ctrl+shift+x by default).

## How Does It Work

The program relies on image recognition to find specific UI elements on your Windows 11 desktop. When you trigger the keyboard shortcut which by default is ctrl+shift+x, the program performs the following steps:

1. It locates and clicks the "Show Hidden Icons" button in the Windows taskbar.
2. It finds the Cloudflare Warp icon in the taskbar and clicks on it.
3. It identifies and clicks the toggle button to turn Cloudflare Warp on or off.
4. It closes the Cloudflare Warp window.
5. Finally, it restores the cursor to its original position.

## Requirements

Before running `script.py`, you need to have python and the following packages installed:

-   python
-   pyAutoGUI
-   keyboard
-   opencv-python

You can install the required packages using pip:

```bash
pip install pyautogui keyboard opencv-python
```

To run `build.sh` you also need to have the following package:

-   Pyinstaller

You can install it using pip:

```bash
pip install pyinstaller
```

## Building the Executable with `build.sh`

The `build.sh` script is used to create an executable file from `script.py` using PyInstaller.

## Running the Executable at Startup in Windows

To run the Cloudflare Warp Toggle Shortcut executable at startup in Windows, follow these steps:

1. Put the Cloudflare warp keyboard shortcut where you want to store the application

2. Press Win + R to open the Run dialog.

3. Type shell:startup and press Enter. This will open the Startup folder.

4. Paste a shortcut to the cloudflare-warp-toggle-shortcut.exe executable into the Startup folder.

Now, the Cloudflare Warp Toggle Shortcut will run automatically when you start Windows.

## Disclaimer

The provided script and build process create a functional Cloudflare Warp toggle shortcut. However, you can customize the script and replace the images with your own if they differ from the default Windows 11 UI.
