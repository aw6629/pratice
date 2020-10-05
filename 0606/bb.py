import requests
r=requests.get('http://127.0.0.1:5000')
json=r.json()
print(json)
print(json.get('id'),json.get('name'))