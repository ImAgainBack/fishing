#----------------------INITIALISATION----------------------#
from pyautogui import * 
import pyautogui as pg
import sys
import functions;
import time 
import random
import win32api, win32con
import keyboard
from pynput.keyboard import Listener
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image

#----------------------INITIALISATION----------------------#


 #coord of map region=(1595,40,300,250)
 #player on map coords X: 1740 Y:  167 RGB: (130, 231, 143)
 #player X:  958 Y:  515 RGB: (101, 104, 100)

sleep(2)


logs = functions.findlog()

#print(functions.distance(logs)[1])


#------------------moving mouse to log---------------------#

while True:
    functions.giga_loop()


        


#pg.moveTo(x_player+x_tomove+60, y_player+y_tomove)
#cv2.imshow('Screenshot', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows 




"""new_2d=0
new_val=0
print(len(logs))
for row in logs:
    print("new_2d",new_2d,"\n")
    new_2d+=1
    for col in row:
        print(col, "new_val", new_val)
        new_val+=1
"""
