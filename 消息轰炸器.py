import pyautogui
import time

times = 1000
time.sleep(2)
for i in range(times):
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    # time.sleep(0.01)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    # time.sleep(0.01)
    pyautogui.keyDown('enter')
    # time.sleep(0.01)
    pyautogui.keyUp('enter')
    # time.sleep(0.01)
    print(i)
