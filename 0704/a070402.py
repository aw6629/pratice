import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(1,1,1 ,projection='3d')
x=[0.9,1.1,1.0]
y=[2.0,1.1,1.1]
z=[0.9,1.0,1.0]
ax.scatter(x,y,z)
plt.show()