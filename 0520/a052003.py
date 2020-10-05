import random
for x in range(10_0000):
    ans=int(random.random()*99+1)
    if ans <1 or ans>99:
        print('bug')