import pyautogui, time

pyautogui.alert('Agora o computador está sendo controlado')

pyautogui.PAUSE = 0.3
abrirCalculadora()
pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')
while True:
    time.sleep(1)
    pyautogui.moveTo(['1357', '449'])
    pyautogui.click()
    pyautogui.moveTo(['1196', '385'])
    pyautogui.click()
    time.sleep(4)
    pyautogui.moveTo(['1359', '163'])
    pyautogui.click()
    time.sleep(20)
    pyautogui.moveTo(['1359', '163'])
    pyautogui.click()
    time.sleep(20)
    pyautogui.moveTo(['1359', '163'])
    pyautogui.click()
    time.sleep(30)
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
    pyautogui.moveTo(['19', '560'])
    pyautogui.doubleClick()
    ctrlC()
    pyautogui.press(['delete'])
    pageUp()
    pyautogui.click(['1066', '169'])
    ctrlV()
    pyautogui.moveTo(['1184', '177'])
    pyautogui.doubleClick()
    time.sleep(5)