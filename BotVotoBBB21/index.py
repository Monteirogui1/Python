import pyautogui
import time

time.sleep(2)
print("Votando....")

while True:
    time.sleep(2)
    name_vote = pyautogui.locateOnScreen('nome.png', grayscale=True, region=(646, 118, 629, 554))
    if name_vote:
        point = pyautogui.center(name_vote)
        pyautogui.click(point)
        pyautogui.press('end')

    time.sleep(2)
    checkpoint = pyautogui.locateOnScreen('checkpoint.png', grayscale=True, region=(300, 72, 801, 725))
    if checkpoint:
        pointCheck = pyautogui.center(checkpoint)
        pyautogui.click(pointCheck)

    time.sleep(2)
    back = pyautogui.locateOnScreen('back.png', grayscale=True, region=(599, 48, 652, 334))
    if back:
        pback = pyautogui.center(back)
        pyautogui.click(pback)


        time.sleep(2)

        pass
