import requests
import csv
r=requests.post('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20160101&stockNo=2330',)
print(r.text)
with open(r'c:/tmp/aa.csv') as f:
writer = csv.writer(f)
writer.writerow()