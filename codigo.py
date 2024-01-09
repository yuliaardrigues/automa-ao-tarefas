import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

pyautogui.press("win")
time.sleep(1)

pyautogui.write("chrome")
time.sleep(1)

pyautogui.press("enter")
time.sleep(5)

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
time.sleep(1)

pyautogui.press("enter")
time.sleep(10)

pyautogui.click(x=467, y=409)

pyautogui.write("rodriguesyulia25@gmail.com")

pyautogui.press("tab")

pyautogui.write("123456")

pyautogui.click(x=701, y=569)
time.sleep(5)

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

  pyautogui.click(x=494, y=287)

  pyautogui.write(tabela.loc[linha, "codigo"])
  pyautogui.press("tab")

  pyautogui.write(tabela.loc[linha, "marca"])
  pyautogui.press("tab")

  pyautogui.write(tabela.loc[linha, "tipo"])
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")

  obs = tabela.loc[linha, "obs"]
  if not pandas.isna(obs):
    pyautogui.write(obs)

  pyautogui.press("tab")
  pyautogui.press("enter")

  pyautogui.scroll(5000)
  
