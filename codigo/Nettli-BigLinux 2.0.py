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
pyautogui.doubleClick(['1356', '380'])
pyautogui.click(['1195', '394'])

while True:
    img = pyautogui.locateCenterOnScreen('codigo/imagens/Captura1.png', confidence=0.9)
    verification = pyautogui.locateCenterOnScreen('codigo/imagens/Verificacao2.png')
    if verification == None:
        pyautogui.click(['1358', '157'])
        
    time.sleep(0.5)
    print(img)
    pyautogui.PAUSE = 0.2
    while img != None:
        #Procura o valor exato em forma crescente.
        pyautogui.click(['231', '45'])
        pyautogui.click(['1105', '178'])
        pyautogui.click(['1106 ','166'])
        while True:
            #Verifica se o botão "Confirmar" está verde.
            confirmar = pyautogui.locateCenterOnScreen('codigo/imagens/Confirmar.jpeg', confidence=0.9)
            if confirmar == None:
                pyautogui.click(['1106', '166'])    
                
            else:
                #Quando encontra o botão verde, confirma
                pyautogui.moveTo(['1163', '173'])
                pyautogui.doubleClick()
                
                #Volta para a tela inicial
                BigLinux.TelaInicial()
                break
        break   
#Fim!
