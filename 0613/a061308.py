import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

mu=0
std=1
x=np.arange(-3,3,0.01)
y=stats.norm.pdf(x,mu,std)
plt.figure(figsize=(10,5))
plt.plot(x,y)
plt.grid(b=True,color='red')
plt.title('N D')
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-10,10,-1,1])
plt.show()