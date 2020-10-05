import numpy as np
arr=np.array([1,2,3,4,5])
mask=(arr==1) | (arr==3)
print(mask)
print(arr[mask])