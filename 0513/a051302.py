import math
def combination(n,r):
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
MAX=300
positive =1/2
negative= 1-positive
x=[]
y=[]
for i in range(MAX+1):
    c=combination(MAX,i)
    x.append(i)
    y.append(c*(positive**i)*(negative**(MAX-i)))

import matplotlib.pyplot as plt
plt.bar(x,y)
plt.show()


