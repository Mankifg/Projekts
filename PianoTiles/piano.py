from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con
import os

os.system("cls")
lines = []

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1) 
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

for i in range(4):
    print(f"Waiting for {i + 1}. column input... (Press 'a')") 
    keyboard.wait('a')
    lines.append(pyautogui.position()[0])
    print(f"Input {i + 1} received!")
    os.system('cls')

print(f"Waiting for y axe input... (Press 'a')") 
keyboard.wait('a')
y = pyautogui.position()[1]
print(f"Input y received!")
os.system('cls')

x1 = lines[0]
x2 = lines[1]
x3 = lines[2]
x4 = lines[3]

print('System Generated.')
print('Press ENTER to continue.')
keyboard.wait('enter')
os.system('cls')

print(y)

while keyboard.is_pressed('q') == False:
    
    if pyautogui.pixel (x1, y)[0] < 3:
        click(x1, y)
    if pyautogui.pixel(x2,y)[0] < 3:
        click(x2, y)
    if pyautogui.pixel(x3, y)[0] < 3:
        click(x3, y)
    if pyautogui.pixel(x4, y)[0] < 3:
        click(x4, y)
        
print('Break')