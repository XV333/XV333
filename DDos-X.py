import pyautogui
import os

# Get the current screen size
screen_size = pyautogui.size()

# Take a screenshot of the entire screen
screenshot = pyautogui.screenshot(region=(0, 0, screen_size[0], screen_size[1]))

# Save the screenshot to the Pictures folder
screenshot.save(os.path.join(os.path.expanduser("~/Pictures"), "screenshot.png"))
