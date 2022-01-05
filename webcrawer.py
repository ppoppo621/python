# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
r = requests.get('https://www.wayfair.com/kitchen-tabletop/pdp/7025-kitchen-pantry-hqv1042.html')
print(r.text)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,'lxml')
soup.h2
soup.string

import requests
r=requests.get('http://www.zurifurniture.com/bar/lush-bar-stool')
print(r.text)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text,"lxml")
price=soup.find_all('span','prod_saleprice')
title=soup.find_all('h1','productTile')

dict={}
for title1 in title:
for price1 in price:
print(title1.string)
print(price1.string)
dict={'ProductName':[title1.string],'Price':[price1.string]}

import pandas as pd
table = pd.DataFrame(dict