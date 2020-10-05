import requests
html=requests.get('http://localhost:5000/')
x=html.text
from bs4 import BeautifulSoup
bs=BeautifulSoup(x,'html.parser')
h2=bs.find('h1',class_='h1css')
print(h2)
h2=bs.find('h1',{'class':'h1css'})
print(h2)