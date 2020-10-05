import requests
html=requests.get('http://localhost:5000/')
x=html.text
from bs4 import BeautifulSoup
bs=BeautifulSoup(x,'html.parser')
tag=bs.find(string='Header')
print(tag)
print(tag.find_parent())