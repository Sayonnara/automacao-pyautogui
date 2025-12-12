import pyautogui
import time

#tamanho da minha tela
print(pyautogui.size())

#posiçao atual do cursor
print(pyautogui.position())



#aplicação para vê a posição do mouse em tempo real
"""
Digite o comando python no terminal 
from pyautogui import mouseInfo
mouseInfo()

"""

#mover o mouse
pyautogui.moveTo(1249, 12, duration =0.9)
time.sleep(2)
pyautogui.click()




#movendo o scrool
pyautogui.moveTo(1239, 461, duration = 0.9)
time.sleep(1)
pyautogui.click()



# move o mouse até o ponto desejado
pyautogui.moveTo(1239, 461, duration=1)
pyautogui.click()

# rola a tela 30 vezes para baixo
for i in range(30):
    pyautogui.scroll(-100)  # negativo = descer
    time.sleep(0.1)

print("Processo concluído!")
