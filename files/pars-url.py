from googlesearch import search
from time import sleep as wait
from colorama import Fore, init;init()
from random import randint as grn
import os

os.system('cls || clear')
query = input('Уведіть ключові слова : ')
list_url = []
list_colors = [Fore.RED, Fore.CYAN, Fore.GREEN, Fore.YELLOW, Fore.MAGENTA]

while 1:
    try:
        col = int(input('Уведіть кількість запросів за сеанс : '))
        break
    except ValueError:
        print('Це не число! Уведіть будьласка числове значення.')
try:
    for j in search(query, tld="co.in", num=col, stop=col, pause=2):
        list_url.append(j)
except:
    print('Увімкніть інтернет')
if list_url != []:
    for i in list_url:
        wait(0.1)
        g = list_colors[grn(0, len(list_colors)-1)]
        print(g, end='')
        print('\r', i, '\n')
        g = list_colors[grn(0, len(list_colors)-1)]
        print(g, end='')
else:
    print('Empty')
input('\nНатисніть Enter для того аби вийти з программи\n')

try:    
    os.remove('.google-cookie')
except FileNotFoundError:
    pass