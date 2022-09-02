import pyautogui, sys, time

def pageDown():
    pyautogui.keyDown('win')
    pyautogui.press(['pagedown'])
    time.sleep(0.5)
    pyautogui.keyUp('win')

'''x, y = pyautogui.position()
print(x, y)'''

def abrirCalculadora():
    pageDown()
    time.sleep(0.2)
    pyautogui.press(['win'])
    time.sleep(2)
    pyautogui.write('calculadora')
    time.sleep(1)
    pyautogui.press(['enter'])
    time.sleep(1.5)
    pyautogui.keyDown('win')
    pyautogui.press(['right'])
    time.sleep(0.2)
    pyautogui.keyUp('win')
    time.sleep(0.2)
    pyautogui.moveTo(['1303', '49'])
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pageUp()

abrirCalculadora()
