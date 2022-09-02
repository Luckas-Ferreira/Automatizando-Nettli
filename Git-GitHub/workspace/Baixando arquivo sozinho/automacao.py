import pyautogui, time

def pageDown():
    pyautogui.keyDown('win')
    pyautogui.press(['pagedown'])
    pyautogui.keyUp('win')

def pageUp():
    pyautogui.keyDown('win')
    pyautogui.press(['pageup'])
    pyautogui.keyUp('win')


def ctrlC():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press(['c'])
    pyautogui.keyUp('ctrlleft')

def ctrlV():
    pyautogui.keyDown('ctrlleft')
    pyautogui.press(['v'])
    pyautogui.keyUp('ctrlleft')

pyautogui.PAUSE = 0.5
pyautogui.alert('não mexa')
time.sleep(1)

pyautogui.moveTo(['1283', '48'])
pyautogui.click()
time.sleep(1)
pyautogui.press(['win'])
time.sleep(1)
pyautogui.moveTo(['632', '70'])
pyautogui.write('chrome')
pyautogui.press(['enter'])
time.sleep(4)
pyautogui.write('https://www.dattebane.com/pagina/Boruto%20Download?fb_comment_id=1253609204688788_1573330012716704#1%C2%AA%20Temporada')
pyautogui.press(['enter'])
time.sleep(6)
pyautogui.moveTo(['1360', '149'])
pyautogui.click()
pyautogui.moveTo(['1090', '708'])
time.sleep(6)
pyautogui.doubleClick()
pyautogui.click()