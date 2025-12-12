import pyautogui
import time

pyautogui.moveTo(1249, 12, duration =0.9)
time.sleep(2)
pyautogui.click()

time.sleep(1)
pyautogui.screenshot("screenshort.png")

time.sleep(2)
pyautogui. confirm(text='Tela foi Printada', title='Print de Imagem', buttons=['OK', 'Cancel'])

"""
while : True
    pyautogui.screenshort(f"image_{time.time()}.png")
    time.sleep(5)


"""