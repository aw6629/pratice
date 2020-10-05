import numpy as np
arr=np.arange(1,13).reshape(3,4)
print(arr)

row=np.array([0,1,2])
col=np.array([2,1,3])
print(arr[row,col])