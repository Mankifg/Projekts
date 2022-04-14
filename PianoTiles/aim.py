from pyautogui import *
import pyautogui
import time
import keyboard as kb
import random
import win32api, win32con

print('go left up')
kb.wait('enter')
x1, y1 = pyautogui.position()[0], pyautogui.position()[1]
print('go right down')
kb.wait('enter')
x2, y2 = pyautogui.position()[0], pyautogui.position()[1]
print('start ?')
kb.wait('enter')


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 195)

while kb.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if b == 255 and r == 71 and g == 0:
                flag = 1
                click(x+x1, y+y1)
                time.sleep(0.05)
                break

        if flag == 1:
            break