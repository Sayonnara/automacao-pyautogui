import pyautogui
import time

# Abre o menu iniciar
pyautogui.press("winleft")

time.sleep(1)

# Digita "calculadora"
pyautogui.write("calculadora", interval=0.10)

time.sleep(1)

# Pressiona ENTER para abrir
pyautogui.press("enter")


# Espera 2 segundos
time.sleep(5)

# Fecha
pyautogui.hotkey("alt", "f4")