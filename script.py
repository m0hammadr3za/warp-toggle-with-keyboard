import keyboard
import subprocess
import threading

def toggle_warp():
    try:
        # Check the status of WARP
        status = subprocess.check_output("warp-cli status", shell=True).decode()

        if "Connected" in status:
            # If WARP is connected, disconnect it
            print("Connecting to WARP...")
            subprocess.run("warp-cli disconnect", shell=True)
            print()
        elif "Disconnected" in status:
            # If WARP is disconnected, connect it
            print("Disconnecting from WARP...")
            subprocess.run("warp-cli connect", shell=True)
            print()
    except Exception as e:
        print(f"An error occurred: {e}")

def listen_for_keys():
    keyboard.add_hotkey("ctrl+shift+x", toggle_warp)
    print("Listening for Ctrl + Shift + X to toggle Cloudflare WARP...\n")
    keyboard.wait()

# Run the listener in a separate thread
threading.Thread(target=listen_for_keys).start()
