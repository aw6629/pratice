import requests
param={'a':10,'b':20}
r=requests.post('http://localhost:5000/add',param)
print(r.text)