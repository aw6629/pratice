import requests
r=requests.get('https://www.googleapis.com/books/v1/volumes?q=python')
json=r.json()
item=json['items']
pos=0
while pos<len(item):
    try:
        sub=item[pos]['volumeInfo']['subtitle']
        print('title:',item[pos]['volumeInfo']['title'])
        print('subtitle',sub)
        pos=pos+1
    except:
        print('title:',item[pos]['volumeInfo']['title'])
        pos = pos + 1