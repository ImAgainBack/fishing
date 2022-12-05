#----------------------INITIALISATION----------------------#
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
#----------------------INITIALISATION----------------------#


 #coord of map region=(1595,40,300,250)
 #player on map coords X: 1740 Y:  167 RGB: (130, 231, 143)
 #player X:  958 Y:  515 RGB: (101, 104, 100)

sleep(2)

#------------------finding log-----------------------------#
x_player, y_player = 958, 515
i=0
x_map,y_map = 1740, 167
logs = np.empty((0,2),int)
screenshot = pg.screenshot() #region=(1595,40,300,250)
screenshot = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)
for log in pg.locateAllOnScreen("img/log.png", confidence=0.70):
    
    #x_new,y_new = x_map - log.left, y_map- log.top
    logs = np.append(logs, np.array([[log.left, log.top]]),axis=0)
    
    #print(logs)
    """
    cv2.rectangle(
        screenshot,
        (log.left, log.top),
        (log.left + log.width, log.top + log.height),
        (0, 0, 255),
        2
    )
    """
    i+=1
print(i)
line=0
total_distance1=999
for row in logs:
    x_new= x_map- logs[line][0]
    y_new= y_map-logs[line][1]
    total_distance= abs(x_new)+ abs(y_new)
    if total_distance<total_distance1:
        total_distance1=total_distance
        x_tomove, y_tomove = x_new, y_new
    line+=1
    print(x_tomove,y_tomove)
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
#------------------finding log-----------------------------#

#------------------moving mouse to log---------------------#

pg.moveTo(x_player+x_tomove+60, y_player+y_tomove)
#cv2.imshow('Screenshot', screenshot)
cv2.waitKey(0)
cv2.destroyAllWindows 

#gives closest tree on screen coords
