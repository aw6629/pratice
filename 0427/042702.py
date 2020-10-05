import csv
with open(r'c:\tmp\elcand.csv',encoding='UTF-8') as f:
    l = []
    allcsvdata=csv.reader(f)
    for x in list(allcsvdata):
        y=x[14]
        if y == '*':
            l.append(99-int(x[9]))
    print(sum(l)/len(l))