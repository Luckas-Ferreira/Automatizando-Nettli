from email.mime import image
import pyautogui, time

pyautogui.alert('Agora o computador está sendo controlado')
pyautogui.PAUSE = 0.3
time.sleep(0.5)

def pageDown():
    pyautogui.keyDown('win')
    pyautogui.press(['pagedown'])
    pyautogui.keyUp('win')

def pageUp():
    pyautogui.keyDown('win')
    pyautogui.press(['pageup'])
    pyautogui.keyUp('win')

def abrirNavegador():
    pyautogui.press(['win'])
    time.sleep(2)
    pyautogui.write('chrome')
    pyautogui.press(['enter'])
    time.sleep(6)
    pyautogui.write('https://www.nettli.com/user/ptc')
    time.sleep(0.5)
    pyautogui.press(['enter'])

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

def fechar():
    pass
def ctrlC():
    pyautogui.hotkey('ctrlleft', 'c')

def ctrlV():
    pyautogui.hotkey('ctrlleft', 'v')
def ctrlA():
    pyautogui.hotkey('ctrl', 'a')

abrirNavegador()
abrirCalculadora()

time.sleep(1)
pyautogui.moveTo(['1357', '449'])
pyautogui.click()
pyautogui.moveTo(['1196', '385'])
pyautogui.click()


contador = 0
while True:
    img = pyautogui.locateCenterOnScreen('codigo/captura2.png', confidence=0.9)
    verification = pyautogui.locateCenterOnScreen('codigo/Verificacao2.png')
    if verification == None:
        pyautogui.click(['1364', '157'])
    print(contador)
    if contador > 10:
        pyautogui.hotkey(['ctrl', 'shift', 'w'])
        abrirNavegador()
    time.sleep(0.5)
    
    while img != None:
        time.sleep(1)
        pyautogui.moveTo(['907', '169'])
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
        ctrlC()
        pageDown()
        ctrlV()
        pyautogui.click(['1127', '741'])
        ctrlA()
        ctrlC()
        pyautogui.press(['delete'])
        pageUp()
        pyautogui.doubleClick(['1066', '169'])
        pyautogui.press(['del'])
        ctrlV()
        pyautogui.moveTo(['1184', '177'])
        pyautogui.doubleClick()
        time.sleep(5)
        pyautogui.moveTo(['1357', '449'])
        pyautogui.click()
        pyautogui.moveTo(['1196', '385'])
        pyautogui.click()
        contador += 1
        break
