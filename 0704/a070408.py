import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread(r'c:\tmp\a1.jpg')
print(type(img))
r=img.ravel()
plt.hist(r,bins=256)
plt.show()