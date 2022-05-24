import pyautogui
import time

time.sleep(3)
print('Jogando....')

while True:
    moeda = pyautogui.locateOnScreen('moeda.png')
    if moeda:
        point = pyautogui.center(moeda)
        pyautogui.click(point)

    else:
        print('Moeda não encontrada!!')