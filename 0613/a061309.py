from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r'c:\windows\fonts\mingliu.ttc',size=14)
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
plt.title('常態分配',fontproperties=font)
plt.xlabel('x')
plt.ylabel('y')
plt.axis([-10,10,-1,1])
plt.show()