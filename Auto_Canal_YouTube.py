"""
Automação do meu canal do YuoTube - Security_set

Públicação de vídeos do canal em páginas do Facebook relacionadas ao assunto.

URL = https://www.youtube.com/channel/UCrjfIUShndbnJtMroKTT4gg
"""

from selenium import webdriver
import pyautogui
import pyperclip
# from selenium.webdriver.common.keys import Keys
import time
from LoginFace import email, passwd
from colorama import Fore, Back, Style

PagFacebook = ['https://www.facebook.com/groups/608492105999336/?multi_permalinks=2027845070730692',
               'https://www.facebook.com/groups/CryptoRoot',
               'https://www.facebook.com/groups/python',
               'https://www.facebook.com/groups/python.brasil']


print(32 * '=')
print(Fore.BLUE + 'Bem-Vindo ao script de automação' + Style.RESET_ALL)
print('Cariador:', Fore.BLUE + 'Carlos H. B. S. Campos' + Style.RESET_ALL)
print(32 * '=')
info = input(Fore.GREEN + 'LINK VIDEO YOU-TUBE:' + Style.RESET_ALL)

msgY = f"""
{info}
Venha conhecer o canal Security_Set no YouTube.
"""
PFacebook = webdriver.Chrome()

PFacebook.get('https://www.facebook.com/')


def loginfacebook():
    PFacebook.find_element_by_id('email').send_keys(email)
    time.sleep(2)
    PFacebook.find_element_by_id('pass').send_keys(passwd)
    time.sleep(2)
    PFacebook.find_element_by_name('login').click()


def ajustespagina():
    pyautogui.click(x=978, y=24)
    time.sleep(3)
    pyautogui.click(x=411, y=79)


def msg():
    pyperclip.copy(msgY)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.click(x=662, y=628)
    time.sleep(5)


def post():
  for paginas in PagFacebook:
      PFacebook.get(paginas)
      time.sleep(8)
      x = PagFacebook.index(paginas)
      if x == 0:
          pyautogui.click(x=426, y=456)
          time.sleep(4)
          msg()

      elif x == 1:
          pyautogui.click(x=440, y=504)
          time.sleep(4)
          msg()
      elif x == 2:
          pyautogui.click(x=430, y=419)
          time.sleep(4)
          msg()

      elif x == 3:
          pyautogui.click(x=414, y=419)
          time.sleep(4)
          msg()


def Pincipal():
    loginfacebook()
    time.sleep(5)
    ajustespagina()
    time.sleep(1)
    post()


try:
    if __name__ == '__main__':
        Pincipal()
except Exception as err:
    print(f'Erro apresentado: {err}, favor corrigi-lo.')