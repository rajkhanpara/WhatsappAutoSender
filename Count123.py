import pyautogui
import time 
time.sleep(3)
count=1
while count<=10:
    pyautogui.typewrite("Love You twooððð" +str(count))
    pyautogui.press("enter")
    count=count+2
