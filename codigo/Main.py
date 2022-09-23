import pyautogui, time

class Nettli:

    def ctrlC(self):
        pyautogui.hotkey('ctrlleft', 'c')
    
    def ctrlV(self):
        pyautogui.hotkey('ctrlleft', 'v')
    
    def ctrlA(self):
        pyautogui.hotkey('ctrl', 'a')
    
    def EncontrarNavegador(self):
        while True:
            navegador1 = pyautogui.locateCenterOnScreen('codigo/imagens/Navegador2.png', confidence=0.7)
            if navegador1 == None:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')              
                time.sleep(0.3)
            else:
                pyautogui.keyUp('alt')
                break
    
    def EncontrarCalculadora(self):
        while True:
            calculadora = pyautogui.locateCenterOnScreen('codigo/imagens/Calculadora.png', confidence=0.7)
            if calculadora == None:
                pyautogui.keyDown('alt')
                pyautogui.press('tab')              
                time.sleep(0.2)
            else:
                pyautogui.keyUp('alt')
                break
    
    def TelaInicial(self):
        pyautogui.PAUSE=0.4
        while True: 
            verificacaoInicial = pyautogui.locateCenterOnScreen('codigo/imagens/Verificacao1.png')
            print(verificacaoInicial)
            while verificacaoInicial != None:
                pyautogui.moveTo(['1357', '449'])
                pyautogui.click()
                pyautogui.moveTo(['1195', '439'])
                pyautogui.click()
                return False
