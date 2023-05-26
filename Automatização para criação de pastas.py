# Automatização para criação de pastas

import pyautogui
import time

pyautogui.PAUSE = 2

#caminhoOrigem = (input("Digite a pasta de origem "))
nomeArtista = (input("Qual é o nome do artista? "))
artista = nomeArtista.upper()
numeroArtista = (input("Qual é o número do artista? "))
morphOrigem = (input("Qual é a pasta de origem dos Morphs? "))

# Acessando a pasta de origem

pyautogui.click(x=988, y=1054)
pyautogui.click(x=255, y=118)
pyautogui.write("D:\METAMORPHOSE DOS FAMOSOS\BACKUP_METAMORPHOSE_2023")
pyautogui.press("enter")

time.sleep(3)

# Copiando uma pasta de modelo

pyautogui.click(x=408, y=180)
pyautogui.press("end")
pyautogui.hotkey("ctrl","c")
pyautogui.click(x=1900, y=977)
pyautogui.hotkey("ctrl","v")

time.sleep(20)

# Renomeando a pasta

pyautogui.click(x=408, y=180)
pyautogui.press("end")
pyautogui.hotkey("shift","f10")
pyautogui.press("up")
pyautogui.press("up")
pyautogui.press("enter")
pyautogui.write(numeroArtista+"_"+artista)
pyautogui.press("enter")
pyautogui.press("enter")

# Apagando e colando novo conteudo na pasta "Morph"

pyautogui.click(x=408, y=180)
pyautogui.press("down")
pyautogui.press("enter")

time.sleep(30)

pyautogui.click(x=334, y=181)
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("del")

pyautogui.click(x=1436, y=114)
pyautogui.write(morphOrigem)
pyautogui.press("enter")

pyautogui.click(x=323, y=217)
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl","c")

pyautogui.click(x=1436, y=114)
pyautogui.write("D:\METAMORPHOSE DOS FAMOSOS\BACKUP_METAMORPHOSE_2023")
pyautogui.press("enter")
pyautogui.click(x=408, y=180)
pyautogui.press("end")
pyautogui.press("enter")
pyautogui.click(x=408, y=180)
pyautogui.press("down")
pyautogui.press("enter")
pyautogui.click(x=1900, y=977)
pyautogui.hotkey("ctrl","v")

time.sleep(15)

# Apagando e renomaeando conteudo na pasta "Intro"

pyautogui.click(x=22, y=114)
pyautogui.press("down")
pyautogui.press("enter")

pyautogui.click(x=408, y=180)
pyautogui.hotkey("del")

pyautogui.click(x=328, y=215)
pyautogui.hotkey("del")

pyautogui.click(x=408, y=180)
pyautogui.hotkey("shift","f10")
pyautogui.press("up")
pyautogui.press("up")
pyautogui.press("enter")
pyautogui.write("INTRO "+artista)
pyautogui.press("enter")

# Apagando e renomeando arquivos na pasta "Arquivos Filmora"

pyautogui.click(x=22, y=114)
pyautogui.press("down")
pyautogui.press("enter")

pyautogui.click(x=408, y=180)
pyautogui.hotkey("del")

pyautogui.click(x=408, y=180)
pyautogui.hotkey("shift","f10")
pyautogui.press("up")
pyautogui.press("up")
pyautogui.press("enter")
pyautogui.write("PROJETO "+artista+" 2")
pyautogui.press("enter")

pyautogui.click(x=335, y=217)
pyautogui.hotkey("shift","f10")
pyautogui.press("up")
pyautogui.press("up")
pyautogui.press("enter")
pyautogui.write("PROJETO "+artista)
pyautogui.press("enter")