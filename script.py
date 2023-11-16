import os
import time
import keyboard
import pyautogui

def toggle_warp():
    # save cursor position
    origin_x, origin_y = pyautogui.position()

    # Find and click on windows "show hidden icons"
    show_hidden_icons_location = find_location('show-hidden-icons')
    if show_hidden_icons_location:
        show_hidden_icons_center = pyautogui.center(show_hidden_icons_location)
        pyautogui.click(show_hidden_icons_center)
    else:
        print("Clouldn't find windows show hidden icons button!")
        return
    
    # Find and click on warp app icon in taskbar
    warp_icon_location = find_location('warp-icon')

    if warp_icon_location:
        warp_icon_center = pyautogui.center(warp_icon_location)
        pyautogui.click(warp_icon_center)
    else:
        print("Couldn't find cloudflare warp in taskbar!")
        return
    
    # Find and click on toggle button
    toggle_image_location = find_location('toggle-image')

    if toggle_image_location:
        toggle_image_center = pyautogui.center(toggle_image_location)
        pyautogui.click(toggle_image_center)
    else:
        print("Couldn't find cloudflare warp connection toggle button!")
        return
    
    # Close warp window
    pyautogui.click(show_hidden_icons_location.left - 30, pyautogui.center(show_hidden_icons_location).y)

    # Return the cursor to the original position
    pyautogui.moveTo(origin_x, origin_y)

def find_location(images_directory):
    full_images_directory = os.path.join(os.getcwd(), images_directory)
    images_to_search = [os.path.join(full_images_directory, f) for f in os.listdir(full_images_directory) if f.endswith('.png')]

    for image_file in images_to_search:
        location = pyautogui.locateOnScreen(image_file, confidence=0.8)
        if location:
            return location

    return None

def on_key_event(e):
    if keyboard.is_pressed('x') and keyboard.is_pressed('ctrl') and keyboard.is_pressed('shift'):
        toggle_warp()
        time.sleep(1)

def main():
    keyboard.hook(on_key_event)
    keyboard.wait()

if __name__ == "__main__":
    main()