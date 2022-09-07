class Nettli:

    def __init__(self):
        self.EncontrarNavegador()

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


BigLinux = Nettli()
BigLinux.EncontrarNavegador()