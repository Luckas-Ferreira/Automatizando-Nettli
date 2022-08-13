import pyautogui, time

class acoes:
    def __init__(self):
        self.abrirCalculadora()
        self.ctrlC()
        self.ctrlV()
        self.pageDown()
        self.pageUp()

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
        pyautogui.keyDown('ctrlleft')
        pyautogui.press(['c'])
        pyautogui.keyUp('ctrlleft')

    def ctrlV():
        pyautogui.keyDown('ctrlleft')
        pyautogui.press(['v'])
        pyautogui.keyUp('ctrlleft')

    