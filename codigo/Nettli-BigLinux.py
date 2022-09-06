#Inicio

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
    pyautogui.click(['411', '744'])
    time.sleep(6)
    pyautogui.write('https://www.nettli.com/user/ptc')
    time.sleep(0.5)
    pyautogui.press(['enter'])
    time.sleep(0.5)
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('alt', 'tab')
    

def abrirCalculadora():
    pyautogui.click(['553', '750'])
    time.sleep(2)
    pyautogui.hotkey('win', 'right')
    pyautogui.moveTo(['1301', '26'])
    pyautogui.click()
    pyautogui.hotkey('alt', 'tab')

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
pyautogui.moveTo(['1195', '439'])
pyautogui.click()


while True:
    img = pyautogui.locateCenterOnScreen('codigo/Captura1.png', confidence=0.9)
    verification = pyautogui.locateCenterOnScreen('codigo/Verificacao2.png')
    if verification == None:
        pyautogui.click(['1364', '157'])
        
    time.sleep(0.5)

    while img != None:
        time.sleep(1)
        pyautogui.moveTo(['904', '143'])
        pyautogui.doubleClick()
        ctrlC()
        pyautogui.hotkey('alt', 'tab')
        ctrlV()
        pyautogui.click(['813', '693'])
        pyautogui.hotkey('alt', 'tab')
        pyautogui.moveTo(['982', '142'])
        pyautogui.doubleClick()       
        ctrlC()
        pyautogui.hotkey('alt', 'tab')
        ctrlV()
        pyautogui.press('enter')
        pyautogui.doubleClick(['383', '423'])
        ctrlA()
        ctrlC()
        pyautogui.press(['delete'])
        pyautogui.hotkey('alt', 'tab')
        pyautogui.doubleClick(['1060', '144'])
        pyautogui.press(['del'])
        ctrlV()
        pyautogui.moveTo(['1163', '143'])
        pyautogui.doubleClick()
        time.sleep(12)

        pyautogui.moveTo(['1357', '449'])
        pyautogui.click()
        pyautogui.moveTo(['1195', '439'])
        pyautogui.click()
        
        break
#Fim!
