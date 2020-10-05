import numpy as np
arr=np.array([1,2,3],dtype=np.uint8)
arr=arr+255
print(arr)

arr=arr.astype(np.int32)
arr=arr+255
print(arr)