import pyautogui
import time 
time.sleep(3)
count=1
while count<=10:
    pyautogui.typewrite("Love You twoo😍😍😍" +str(count))
    pyautogui.press("enter")
    count=count+2
