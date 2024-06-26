from os import listdir, path, stat
import cv2
import matplotlib.pyplot as plt
from math import floor, ceil
from Temple import Temple
import mss
import numpy as np
import keyboard as kb
import time


CLIENT_TXT = r'C:\Program Files (x86)\Steam\steamapps\common\Path of Exile\logs\Client.txt'
INCURSION_KEYBIND = 'v'

# Assumes English, need support for other languages as well
ALVA_OPENING_INCURSION_QUOTES = [
    r"Alva, Master Explorer: Let's go.",
    r"Alva, Master Explorer: Time to go.",
    r"Alva, Master Explorer: It's time!"
]
ALVA_FINISHED_INCURSION_QUOTE = r"Alva, Master Explorer: Good job, exile."


class IncursionApp():
    def __init__(self):
        # Need to read from a config file
        self.path_to_client_txt = CLIENT_TXT
        self.incursion_keybind = INCURSION_KEYBIND
        
        self.last_file_change = 0
        self.sct = None
        self.f = None
    
    def run(self):
        # Setting up screenshotting
        with mss.mss() as self.sct:
            self.watch_client_txt()
    
    def watch_client_txt(self):
        """
        Monitoring client.txt for any changes
        """
        while True:
            latest_change = stat(self.path_to_client_txt).st_mtime
            if self.last_file_change != latest_change:
                self.last_file_change = latest_change
                self.read_client_txt()
    
    def read_client_txt(self):
        """
        Reading client.txt to check for Alva opening an Incursion.
        """
        with open(self.path_to_client_txt, 'rb') as self.f:
            last_line = str(self.f.readlines()[-1])
            # May break if Client.txt does not track datetime with the setting turned off
            if any(quote in last_line for quote in ALVA_OPENING_INCURSION_QUOTES) and last_line.count(':') == 3:
                self.wait_for_keybind()
            f.close()
    
    def wait_for_keybind(self):
        """
        Once the Incursion is open, watching for the relevant keybind that opens the Incursion menu, then a screenshot is taken.
        """
        while True: # Replace with reading the last line of the file for Alva End quote?
            if kb.is_pressed(self.incursion_keybind):
                time.sleep(0.25) # Faster time? How long until window appears?
                monitor = self.sct.monitors[1] # Replace with proper way to get the game window
                screenshot = np.array(self.sct.grab(monitor))[..., :-1] # Remove alpha channel
                screenshot = screenshot[..., ::-1] # BGR to RGB
                screenshot = crop_to_incursion_menu(screenshot)
                hsv_image = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)
                test = Temple(hsv_image)
                print(test)
                print()
                break


if __name__ == '__main__':
    client = IncursionApp()
    client.run()
    exit()

    # Batch testing
    # count = 0
    # folder_dir = r'Images\UncompressedSteam'
    # for filename in listdir(folder_dir):
    #     count += 1
    #     print(filename, count)
    #     path_to_image = path.join(folder_dir, filename)
    #     image = cv2.imread(path_to_image)[..., ::-1] # RGB
    #     hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    #     test = Temple(hsv_image)
    #     print(test)
    #     print()
