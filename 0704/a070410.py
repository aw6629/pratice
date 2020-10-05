from matplotlib.widgets import  Slider
import numpy as np
import matplotlib.pyplot as plt
sigma_min=-10
sigma_max=10
sigma_init=1
x=np.arange(-10,10,.1)
fig,ax=plt.subplots()

slider_ax=plt.axes([0.1,0.05,0.8,0.05])
plt.axes(ax)
import scipy.stats as stats
mu=0
std=1
y=stats.norm.pdf(x,mu,sigma_init)
normal_distribution_plot,=plt.plot(x,y)
a_slider=Slider(slider_ax,'sigma',sigma_min,sigma_max,valinit=sigma_init)
def slider_changed(sigma):
    y=stats.norm.pdf(x,mu,sigma)
    normal_distribution_plot.set_ydata(y)
    fig.canvas.draw_idle()

a_slider.on_changed(slider_changed)
plt.show()