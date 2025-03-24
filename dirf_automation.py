import pyautogui
import time

time.sleep(5)

for i in range(400):
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.typewrite(f"{time.strftime('%Y_%m_%d %H_%M_%S')}")
    time.sleep(1)
    pyautogui.press("enter")



