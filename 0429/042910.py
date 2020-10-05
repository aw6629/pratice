import numpy as np
arr=np.arange(0,10)
t=np.where(arr<5)
print(t)
print(type(t))
print(arr[t] **2)
