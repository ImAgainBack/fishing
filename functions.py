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
from pyclick import HumanClicker

x_map,y_map = 1740, 167
x_player, y_player = 958, 515
#----------------------INITIALISATION----------------------#

def findlog():
    i=0
    logs = np.empty((0,2),int)
    for log in pg.locateAllOnScreen("img/log.png", confidence=0.70): #hardcoded img 
        logs = np.append(logs, np.array([[log.left, log.top]]),axis=0) #putting all logs found in a minimap 2d list with
                                                                        # 2col and inf rows
    return logs 


def draw_rectangle(log): #just drawing rectangles to test if finds what you need
    screenshot = pg.screenshot() #region=(1595,40,300,250)
    screenshot = cv2.cvtColor(np.array(screenshot),cv2.COLOR_RGB2BGR)
    cv2.rectangle(  #rectangle function in cv2
    screenshot,
    (log.left, log.top), #top left coords of your "log" picture
    (log.left + log.width, log.top + log.height), #bottom right coords of your "log" picture
    (0, 0, 255), #color
    2) #thickness

def distance(logs): #computes and finds the closest "log" to your caracter
    line=0
    total_distance1=999 #random high value
    for row in logs: #loop to compare with 2d array given by findlog() function
        x_new= x_map- logs[line][0]
        y_new= y_map-logs[line][1]
        total_distance= abs(x_new)+ abs(y_new) #abs() function gives absolute value
        if total_distance<total_distance1:
            total_distance1=total_distance
            x_tomove, y_tomove = x_new, y_new #returning values x and y coords the closest to your caracter
        line+=1
    return x_tomove,y_tomove

def giga_loop(): #main loop
    p= random.uniform(0.5,1.1) #random value generator between 0.5 and 1.1 
    hc = HumanClicker() #library
    while True:
        coords = pg.locateCenterOnScreen("img/mushroom.png", confidence=0.7)  #finding text of the tree, if finds, going to click and chop it
        logs = findlog()
        travel_x, travel_y = distance(logs)[0], distance(logs)[1]  #taking x and y coords of the closest log
        if coords != None:  #if finds a tree (mushroom)
            hc.move((coords),p) #moves the cursor to it with random time p, between 0.5 and 1.1 
            pg.leftClick() #left click
            sleep(6) #waits 6s for the caracter to move
            wait= pg.locateOnScreen("img/wait.png", confidence=0.8) #searching for a special pattern "wait"
            while wait != None: #if finds "wait" just waits
                sleep(1)
                wait= pg.locateOnScreen("img/wait.png", confidence=0.8) #takes new screenshot
                
                
        elif abs(travel_x)>=abs(travel_y): #pathfinding if x coord higher than y, will click on x coords
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

        elif abs(travel_y)>abs(travel_x): #pathfinding if y coord higher than x, will click on y coords
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
