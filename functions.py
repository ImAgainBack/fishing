#----------------------INITIALISATION----------------------#
from pyautogui import * 
import pyautogui as pg
#include functions.py
import time 
import random
import win32api, win32con
import keyboard
from pynput.keyboard import Listener
import cv2
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
from pyclick import HumanClicker

x_map,y_map = 1740, 167
x_player, y_player = 958, 515
#----------------------INITIALISATION----------------------#

def findlog():
    i=0
    logs = np.empty((0,2),int)
    for log in pg.locateAllOnScreen("img/log.png", confidence=0.70):
        
        #x_new,y_new = x_map - log.left, y_map- log.top
        logs = np.append(logs, np.array([[log.left, log.top]]),axis=0)

    return logs


def draw_rectangle(log):
    screenshot = pg.screenshot() #region=(1595,40,300,250)
    screenshot = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)
    cv2.rectangle(
    screenshot,
    (log.left, log.top),
    (log.left + log.width, log.top + log.height),
    (0, 0, 255),
    2)

def distance(logs):
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
    return x_tomove,y_tomove

def giga_loop():
    p= random.uniform(0.5,1.1)
    hc = HumanClicker()
    waiting_secs=0
    while True:
        coords = pg.locateCenterOnScreen("img/mushroom.png", confidence=0.7)
        #print(coords)
        logs = findlog()
        travel_x, travel_y = distance(logs)[0], distance(logs)[1]
        #print("etap1")
        if coords != None:
            hc.move((coords),p)
            pg.leftClick()
            sleep(6)
            wait= pg.locateOnScreen("img/wait.png", confidence=0.8)
            #print(wait, "11111111111111111")
            #print("etap2")
            while wait != None:
                #print("in while loop")
                sleep(1)
                #print("waiting... ", waiting_secs)
                waiting_secs+=1
                wait= pg.locateOnScreen("img/wait.png", confidence=0.8)
                #print(wait)

                
        elif abs(travel_x)>=abs(travel_y):
            if travel_x>0:
                hc.move((x_player-800,y_player),p)
                pg.leftClick()
                sleep(4)
                break
            elif travel_x<0:
                hc.move((x_player+800,y_player),p)
                pg.leftClick()
                sleep(3)
                break
            else:
                break

        elif abs(travel_y)>abs(travel_x):
            if travel_y>0:
                hc.move((x_player,y_player-200),p)
                pg.leftClick()
                break
            elif travel_y<0:
                hc.move((x_player,y_player+200),p)
                break
            else:
                break
        else:
            break
