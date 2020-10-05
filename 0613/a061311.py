import numpy as np
import  math
x=np.arange(-5,5,1.01)
sigma=1
y=1/(sigma*math.sqrt(2**math.pi))*math.e**(-1/(2*sigma)*x**2)
sigma=1.5
z=1/(sigma*math.sqrt(2*math.pi))*math.e**(-1/(2*sigma**2)*x**2)
import matplotlib.pyplot as plt
fig,(ax0,ax1)=plt.subplots(nrows=1,ncols=2)
ax0.set_title('fig1')
ax0.plot(x,y,label='sigma=1')
ax0.legend(loc='right')
ax1.set_title('fig2')
ax1.plot(x,z,label='sigma=1.5')
ax1.legend(loc='right')
plt.show()