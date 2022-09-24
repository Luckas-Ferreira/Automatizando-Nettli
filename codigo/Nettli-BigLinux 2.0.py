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
    pyautogui.PAUSE = 0.2
    while img != None:
        pyautogui.click(['231', '45'])
        while True:
            confirmar = pyautogui.locateCenterOnScreen('codigo/imagens/Confirmar.jpeg', confidence=0.9)
            if confirmar == None:
                pyautogui.click(['1105', '178'])
                pyautogui.click(['1105', '178'])
                pyautogui.click(['1106 ','166'])
                pyautogui.click(['1106', '166'])  
                pyautogui.click(['1106', '166'])   
                
            else:
                pyautogui.moveTo(['1163', '173'])
                pyautogui.doubleClick()
                BigLinux.TelaInicial()
                break
        break   
#Fim!