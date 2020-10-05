birthday=[]
with open(r'c:\tmp\elcand.csv',encoding='UTF-8') as f:
    while True:
        s=f.readline()
        if not s:
            break
        data=s.split(',')
        birthday.append(int(data[9]))
ages=[99-x for x in birthday]
print('avg=',sum(ages)/len(ages))