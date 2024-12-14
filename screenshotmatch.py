import cv2
import numpy as np
import pyautogui
import threading
import time
import win32gui
import win32con
import keyboard
import os
import logging

# Global variable to indicate if the killswitch is activated
killswitch_activated = False

# Set up logging
logging.basicConfig(filename='clicker.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# Function to minimize the command prompt window (Windows-specific)
def minimize_cmd_window():
    try:
        # Find the command prompt window by its class name
        hwnd = win32gui.FindWindow("ConsoleWindowClass", None)
        if hwnd != 0:
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMqIZE)
    except Exception as e:
        logging.error(f"Error minimizing command prompt window: {e}")

# Function to monitor the killswitch key
def monitor_killswitch(killswitch_key):
    global killswitch_activated
    while True:
        if keyboard.is_pressed(killswitch_key):
            logging.info("Killswitch activated.")
            killswitch_activated = True
            break
        time.sleep(0.1)

# Function to search for images on the screen and click on them if found
def search_and_click(images, threshold=0.79, click_delay=2.9, killswitch_key='q'):
    # Set the template matching method
    method = cv2.TM_CCOEFF_NORMED

    # Start monitoring the killswitch key in a separate thread
    killswitch_thread = threading.Thread(target=monitor_killswitch, args=(killswitch_key,))
    killswitch_thread.start()
    image_index = 0  
    while not killswitch_activated:
        minimize_cmd_window()  # Minimize the command prompt window
        # Capture the screen image
        print(f"current index {image_index}")
        current_img = cv2.imread(images[image_index], cv2.IMREAD_COLOR)
        current_np = np.array(current_img)
        screenshot = pyautogui.screenshot("trial_screenshot.png", region=(900,290,600,450))#1st param is from left to right, second is how low, third param how wide and fourth height
        screenshot_np = np.array(screenshot)
        print("line before checking")
        if (screenshot_np == current_np).all():
            pyautogui.press("space")
            image_index += 1
            time.sleep(click_delay)  # Delay between clicks
            # Check if killswitch is activated after each click
            if killswitch_activated:
                break
        # Check if killswitch is activated after processing each image
            if killswitch_activated:
                break

        # Check if killswitch is activated after processing all images
        if killswitch_activated:
            break

    logging.info("Exiting the loop.")

# Main function to execute the script
def main():
    # List of image paths to search for on the screen
    # Replace these with the paths to your actual images
    image_paths = [
        r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\region3.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\3.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\39.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\395.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\1.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\26495.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\0.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\02.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\01.png",
        #r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\018.png",
        #r"C:\path\to\image2.png",
        # Add more image paths as needed
    ]

    # Call the function with the list of image paths and optional parameters
    search_and_click(image_paths)

# Entry point of the script
if __name__ == "__main__":
    main()
