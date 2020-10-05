import random
bingonum=int(random.random()*99+1)
while True:
    x=int(input('guess a number'))
    if x>bingonum:
        print('smaller')
    elif x<bingonum:
        print('bigger')
    else:
        print('bingo')
        break