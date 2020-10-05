import numpy as np
arr=np.array([1,2,3,4],dtype=np.uint8)
print(arr[1:])
x=arr[1:]
x[0]=99
print(arr)
print(x)