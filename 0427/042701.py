import csv
import math
with open(r'c:\tmp\elcand.csv',encoding='UTF-8') as f:
    l = []
    allcsvdata=csv.reader(f)
    for x in list(allcsvdata):
        year=x[9]
        l.append(99-int(year))
    avg=sum(l)/len(l)
    l=[(x-avg)**2 for x in l]
    s=sum(l)/len(l)
    print(math.sqrt(s))

