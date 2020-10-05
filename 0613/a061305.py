import numpy as np
import math
x=np.arange(-3,3,0.01)
y=1/math.sqrt(2*math.pi)*math.e**-((1/2)*x**2)
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show()