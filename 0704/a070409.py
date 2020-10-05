import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons
fig,ax=plt.subplots()
l1,=ax.plot([1,2,3,4],[6,5,7,10],label='line 1')
l2,=ax.plot([1,2,3,4],[11,13,14,16],label='line 2')
ax.legend()
check_x_position=0.05
check_y_position=0.04
check_width=0.1
check_height=0.15
rax=plt.axes([check_x_position,check_y_position,check_width,check_height])
check=CheckButtons(rax,labels=['a','b'],actives=[True,False])
def func(label):
    if label =='a':
        l1.set_visible(not l1.get_visible())
    plt.draw()


check.on_clicked(func)
plt.show()