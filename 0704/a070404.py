import seaborn as sns
df=sns.load_dataset('iris')
df_setosa=df.query('species=="setosa"')
df_vesicolor=df.query('species=="versicolor"')
df_virginica=df.query('species=="virginica"')

import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax=fig.add_subplot(1,1,1,projection='3d')
ax.scatter(df_setosa['sepal_length'],df_setosa['sepal_width'],df_setosa['petal_length'],label='setosa')
ax.scatter(df_vesicolor['sepal_length'],df_vesicolor['sepal_width'],df_vesicolor['petal_length'],label='vesicolor')
ax.scatter(df_virginica['sepal_length'],df_virginica['sepal_width'],df_virginica['petal_length'],label='virginica')
ax.legend()
plt.show()