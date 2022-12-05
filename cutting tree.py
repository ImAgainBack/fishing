#----------------------INITIALISATION----------------------
from pyautogui import * 
import pyautogui as pg
import time 
import random
import win32api, win32con
import keyboard
from pynput.keyboard import Listener
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
#----------------------INITIALISATION----------------------


 #coord of map region=(1595,40,300,250)
 #player X: 1740 Y:  167 RGB: (130, 231, 143)
i=0
sleep(2)
screenshot = pg.screenshot() #region=(1595,40,300,250)
screenshot = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)
for log in pg.locateAllOnScreen("img/log.png", confidence=0.70):
    #print(log)
    cv2.rectangle(
        screenshot,
        (log.left, log.top),
        (log.left + log.width, log.top + log.height),
        (0, 0, 255),
        2
    )
    i+=1
print(i)
cv2.imshow('Screenshot', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows 

#finds all logs on screen
