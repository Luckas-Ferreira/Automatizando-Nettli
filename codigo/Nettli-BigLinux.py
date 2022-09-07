#Inicio

from email.mime import image
import pyautogui, time

pyautogui.alert('Agora o computador está sendo controlado')
pyautogui.PAUSE = 0.5

time.sleep(0.5)

def TelaInicial():
    while True: 
        verificacaoInicial = pyautogui.locateCenterOnScreen('codigo/imagens/Verificacao1.png')
        print(verificacaoInicial)
        while verificacaoInicial != None:
            pyautogui.moveTo(['1357', '449'])
            pyautogui.click()
            pyautogui.moveTo(['1195', '439'])
            pyautogui.click()
            break

def EncontrarCalculadora():
    while True:
        calculadora = pyautogui.locateCenterOnScreen('codigo/imagens/Calculadora.png', confidence=0.7)
        if calculadora == None:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')              
            time.sleep(0.2)
        else:
            pyautogui.keyUp('alt')
            break

def EncontrarNavegador():
    while True:
        calculadora = pyautogui.locateCenterOnScreen('codigo/imagens/Navegador.png', confidence=0.7)
        if calculadora == None:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')              
            time.sleep(0.2)
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

pyautogui.hold('alt', 'tab')
EncontrarNavegador()

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

        pyautogui.click(['813', '733'])
        EncontrarNavegador()
        pyautogui.moveTo(['982', '173'])
        pyautogui.doubleClick()
        ctrlC()

        EncontrarCalculadora()
        ctrlV()
        pyautogui.press('enter')
        pyautogui.doubleClick(['381', '464'])

        ctrlA()
        ctrlC()
        pyautogui.press(['delete'])

        EncontrarNavegador()
        pyautogui.doubleClick(['1060', '173'])
        pyautogui.press(['del'])
        
        ctrlV()
        pyautogui.moveTo(['1163', '173'])
        pyautogui.doubleClick()
        TelaInicial()

#Fim!