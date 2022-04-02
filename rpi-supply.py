#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

SKUs = ('SC0510', 'CM4104000', 'CM4102000')
COLOR = '\033[93m'
BOLD = '\033[1m'
COLOREND = '\033[0m'
user_agent = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0'}

html = requests.get('https://rpilocator.com?instock', headers=user_agent)
response = BeautifulSoup(html.text, 'html.parser')
# html = open('rpilocator.html', 'r')
# response = BeautifulSoup(html.text, 'html.parser')
# html.close()


print('Following SKUs are in supply:')
for supply in response.find_all('tr', class_='table-success'):
    SKU = supply.th.text.split()[0]
    if SKU in SKUs:
        print(COLOR + BOLD + SKU + ', ' + supply.td.text + COLOREND)
    else:
        print(SKU + ', ' + supply.td.text)