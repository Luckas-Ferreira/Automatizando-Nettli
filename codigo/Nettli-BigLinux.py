#Inicio

from email.mime import image
import pyautogui, time
from Main import *
BigLinux = Nettli()

pyautogui.alert('Agora o computador está sendo controlado')
pyautogui.PAUSE = 0.5

pyautogui.hotkey('alt', 'tab')
time.sleep(1)

BigLinux.EncontrarNavegador()
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
    print(img)
    while img != None:
        time.sleep(1)
        pyautogui.click(['231', '45'])
        pyautogui.moveTo(['904', '173'])
        pyautogui.doubleClick()
        BigLinux.ctrlC()
        BigLinux.EncontrarCalculadora()
        BigLinux.ctrlV()

        pyautogui.click(['813', '733'])
        BigLinux.EncontrarNavegador()
        pyautogui.moveTo(['982', '173'])
        pyautogui.doubleClick()
        BigLinux.ctrlC()

        BigLinux.EncontrarCalculadora()
        BigLinux.ctrlV()
        pyautogui.press('enter')
        pyautogui.doubleClick(['381', '464'])

        BigLinux.ctrlA()
        BigLinux.ctrlC()
        pyautogui.press(['delete'])

        BigLinux.EncontrarNavegador()
        pyautogui.doubleClick(['1060', '173'])
        pyautogui.press(['del'])
        
        BigLinux.ctrlV()
        pyautogui.moveTo(['1163', '173'])
        pyautogui.doubleClick()
        BigLinux.TelaInicial()
        break

#Fim!