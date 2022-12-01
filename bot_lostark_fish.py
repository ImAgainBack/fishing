#----------------------INITIALISATION----------------------
from pyautogui import * 
import pyautogui 
import time 
import random
import win32api, win32con
import keyboard
from pynput.keyboard import Listener
#----------------------INITIALISATION----------------------

print("im starting")
# RGB: (247, 210, 157)
#X:  957 Y:  577 RGB: (249, 209, 158)
time.sleep(5) #prog waits 5s to switch screen
win32api.SetCursorPos((1910,900)) #coords for mouse start position
#keyboard.press('s')
#keyboard.release('s') #buff on fishing
#sleep(4) #waits 4s
keyboard.press('e')
keyboard.release('e')
time.sleep(1)
print("start")
i=1 #counts how many fish he cought
while True: #infinite loop
    
    if keyboard.is_pressed('q') == False:
        pic = pyautogui.screenshot(region=(950,550,21,41)) #takes a screenshot in coords (950,550,21,41)
        width, height = pic.size

        #loop to search pixel yellow of exclamation point in water
        #wehen fish appears
        for x in range(0, width, 5): #loop from 0 to 5
            for y in range(0, height, 10): #loop from 0 to 10
                r, g, b = pic.getpixel((x, y)) #collecting RGB value of pixel
                #print(r,g,b)
                    
                
                if (r in range(240,255)) and (g in range(195,217)) and (b in range(153,157)): #ifg rgb pixel corresponds to a given rgb value
                    p= random.uniform(0.2,0.6) #radom float between 0.2 and 0.6 not to detect that it is a bot
                    n= round(p,2)
                    stop =1
                    sleep(n)
                    keyboard.press('e')
                    keyboard.release('e')
                    #catches fish
                    print("catch fish ",i)
                    i=i+1
                    sleep(6.5)
                    keyboard.press('e') #throws fishing tool
                    keyboard.release('e')
                    sleep(5)
                    break


