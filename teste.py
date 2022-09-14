import pyautogui, time



while True:
    confirmar = pyautogui.locateCenterOnScreen('codigo/imagens/Confirmar.jpeg', confidence=0.9)
    if confirmar == None:
        pyautogui.click(['1096', '178'])
        pyautogui.click(['1096', '166'])
        pyautogui.click(['1096', '166'])
        time.sleep(0.5)
    else:
        pyautogui.moveTo(['1163', '173'])
        pyautogui.doubleClick()
        BigLinux.TelaInicial()
        break