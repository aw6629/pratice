import requests
r=requests.get('https://www.cns11643.gov.tw/searchQ.jsp',params={'ID':0,'SN':'王'})
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.content,'html.parser')
meta=soup.find('meta',itemprop='description')
content=meta['content']
import  re
split=re.split(r' | ',content)
strStrok=split[8]
stroke=strStrok[0]
print(int(stroke))