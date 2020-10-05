import requests
html=requests.get('http://localhost:5000/')
x=html.text
from bs4 import BeautifulSoup
bs=BeautifulSoup(x,'html.parser')
h1=bs.find('h1')
print(h1)
print(h1['class'])