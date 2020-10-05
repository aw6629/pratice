import numpy as np
import  math
x=np.arange(-5,5,1.01)
sigma=1
y=1/(sigma*math.sqrt(2**math.pi))*math.e**(-1/(2*sigma)*x**2)
sigma=1.5
z=1/(sigma*math.sqrt(2*math.pi))*math.e**(-1/(2*sigma**2)*x**2)
import matplotlib.pyplot as plt
plt.subplot(121)
plt.plot(x,y,label='sigma=1')
plt.subplot(122)
plt.plot(x,z,label='sigma=1.5')
plt.legend(loc='right')
plt.show()