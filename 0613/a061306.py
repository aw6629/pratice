import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
mu=0
std=1
x=np.arange(-3,3,0.01)
y=stats.norm.pdf(x,mu,std)
plt.plot(x,y)
plt.show()