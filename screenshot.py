import os
import time
import pyautogui

def take_screenshot(save_folder):
   
    os.makedirs(save_folder, exist_ok=True)

   
    timestamp = time.strftime("%Y%m%d_%H%M%S")

   
    screenshot = pyautogui.screenshot()

   
    save_path = os.path.join(save_folder, f"screenshot_{timestamp}.png")
    screenshot.save(save_path)
    print(f"Screenshot saved: {save_path}")



