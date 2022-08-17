from email.mime import image
import pyautogui, time
from pynput import keyboard

''' if keyboard.read_key() == "esc":
        break'''

def pageDown():
    pyautogui.keyDown('win')
    pyautogui.press(['pagedown'])
    pyautogui.keyUp('win')

def pageUp():
    pyautogui.keyDown('win')
    pyautogui.press(['pageup'])
    pyautogui.keyUp('win')


def abrirCalculadora():
    pageDown()
    pyautogui.press(['win'])
    time.sleep(2)
    pyautogui.write('calculadora')
    time.sleep(1.1)
    pyautogui.press(['enter'])
    time.sleep(1.5)
    pyautogui.keyDown('win')
    pyautogui.press(['right'])
    pyautogui.keyUp('win')
    pyautogui.moveTo(['1303', '49'])
    pyautogui.click()
    pageUp()

def ctrlC():
    pyautogui.hotkey('ctrlleft', 'c')

def ctrlV():
    pyautogui.hotkey('ctrlleft', 'v')



pyautogui.alert('Agora o computador está sendo controlado')

pyautogui.PAUSE = 0.3
time.sleep(0.5)

abrirCalculadora()

pyautogui.hotkey('alt', 'tab')

while True:
    img = pyautogui.locateCenterOnScreen('captura.png', confidence=0.9)
    time.sleep(0.5)
    print(img)

    time.sleep(5)
    pyautogui.moveTo(['1357', '449'])
    pyautogui.click()
    pyautogui.moveTo(['1196', '385'])
    pyautogui.click()

    pyautogui.click(['1362', '272'])
    while img != None:
        time.sleep(1)
        pyautogui.moveTo(['907', '169'])
        time.sleep(0.25)
        pyautogui.doubleClick()
        ctrlC()
        pageDown()
        time.sleep(1)
        ctrlV()
        time.sleep(1)
        pyautogui.click(['798', '739'])
        pageUp()
        pyautogui.moveTo(['985', '169'])
        pyautogui.doubleClick()
        time.sleep(0.25)
        ctrlC()
        pageDown()
        ctrlV()
        pyautogui.click(['1127', '741'])
        pyautogui.moveTo(['19', '560'])
        pyautogui.doubleClick()
        ctrlC()
        pyautogui.press(['delete'])
        pageUp()
        pyautogui.click(['1066', '169'])
        ctrlV()
        pyautogui.moveTo(['1184', '177'])
        pyautogui.doubleClick()
        time.sleep(5)
        pyautogui.moveTo(['1357', '449'])
        pyautogui.click()
        pyautogui.moveTo(['1196', '385'])
        pyautogui.click()
        break
