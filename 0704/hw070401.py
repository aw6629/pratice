import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.widgets import CheckButtons
fig ,ax =plt.subplots()
df=sns.load_dataset('iris')
df_setosa=df.query('species=="setosa"').sort_values(['sepal_length'])
df_versicolor=df.query('species=="versicolor"').sort_values(['sepal_length'])
df_virginica=df.query('species=="virginica"').sort_values(['sepal_length'])

l0,=ax.plot(df_setosa['sepal_length'],df_setosa['sepal_width'],label='setosa')
l1,=ax.plot(df_versicolor['sepal_length'],df_versicolor['sepal_width'],label='versicolor')
l2,=ax.plot(df_virginica['sepal_length'],df_virginica['sepal_width'],label='virginica')
lines=[l0,l1,l2]
rax = plt.axes([0.05, 0.04, 0.1, 0.15])
labels = [str(line.get_label()) for line in lines]
check = CheckButtons(rax, labels, actives=[False,False,False])
def func(label):
    index = labels.index(label)
    lines[index].set_visible(not lines[index].get_visible())
    plt.draw()

check.on_clicked(func)

plt.show()