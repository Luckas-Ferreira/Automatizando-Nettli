import pyautogui
pyautogui.PAUSE = 1
pyautogui.hotkey('alt', 'tab')
pyautogui.keyDown('ctrl')
pyautogui.keyDown('shift')
pyautogui.keyDown('w')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('shift')
pyautogui.keyUp('w')