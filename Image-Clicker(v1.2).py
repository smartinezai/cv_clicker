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
        screenshot = pyautogui.screenshot("trial_screenshot.png", region=(600,290,600,550))#1st param is from left to right, second is how low, third param how wide and fourth height
        if screnshot == current_img
        
        screen_np = np.array(screenshot)
        #screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
        print(f"current image index {image_index}")
        
        # Iterate through each image in the database
        #for image_path in images:
        if not os.path.exists(images[image_index]):
            logging.error(f"Image not found at '{images[image_index]}'")
        #    continue  # Skip to the next image if the file doesn't exist
        
        image_path = images[image_index]
        print("current image path "+ image_path)
        # Load the image from the database
        template = cv2.imread(image_path, cv2.IMREAD_COLOR)

        # Perform template match
        # ing
        result = cv2.matchTemplate(screen_np, template, method)

        # Get the location of matches above the specified threshold
        loc = np.where(result >= threshold)

        # Click on the matched locations
        if loc[0].size > 0:
            # Click on the center of the matched template
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
        r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\3.png",
        r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\39.png",
        r"C:\Users\Samantha\Documents\git projects\Python-Image-Clicker\images\395.png",
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
