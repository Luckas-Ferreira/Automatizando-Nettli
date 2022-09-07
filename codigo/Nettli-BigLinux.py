#Inicio

from email.mime import image
import pyautogui, time

pyautogui.alert('Agora o computador está sendo controlado')
pyautogui.PAUSE = 0.7

time.sleep(0.5)

def EncontrarCalculadora():
    calculadora = pyautogui.locateCenterOnScreen('codigo/imagens/Calculadora.png')
    while True: 
        if calculadora == None:
            pyautogui.keyDown('alt')
            pyautogui.click('tab')
            time.sleep(0.5)
        else:
            pyautogui.keyUp('alt')
            break

def ctrlC():
    pyautogui.hotkey('ctrlleft', 'c')
def ctrlV():
    pyautogui.hotkey('ctrlleft', 'v')
def ctrlA():
    pyautogui.hotkey('ctrl', 'a')

time.sleep(1)
pyautogui.hotkey('alt', 'tab')
6

pyautogui.moveTo(['1357', '449'])
pyautogui.click()
pyautogui.moveTo(['1195', '439'])
pyautogui.click()


while True:
    img = pyautogui.locateCenterOnScreen('codigo/imagens/Captura1.png', confidence=0.9)
    verification = pyautogui.locateCenterOnScreen('codigo/imagens/Verificacao2.png')
    if verification == None:
        pyautogui.click(['1364', '157'])
        
    time.sleep(0.5)

    while img != None:
        time.sleep(1)
        pyautogui.click(['231', '45'])
        pyautogui.moveTo(['904', '173'])
        pyautogui.doubleClick()
        ctrlC()
        EncontrarCalculadora()
        ctrlV()

        pyautogui.click(['813', '693'])
        pyautogui.hotkey('alt', 'tab')
        pyautogui.moveTo(['982', '173'])
        pyautogui.doubleClick()
        ctrlC()

        EncontrarCalculadora()
        ctrlV()
        pyautogui.press('enter')
        pyautogui.doubleClick(['383', '423'])
        ctrlA()
        ctrlC()

        pyautogui.press(['delete'])
        pyautogui.hotkey('alt', 'tab')
        pyautogui.doubleClick(['1060', '173'])
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
