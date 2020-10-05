import matplotlib.pyplot as plt

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

x=[0.9,1.1,1.0]
y=[1.0,1.1,1.1]
ax.scatter(x,y)
plt.show()