import numpy as np
arr=np.array([1,2,3])
print(np.sum(arr))
arr=np.array([1,2,np.nan])
print(np.sum(arr))
print(np.nansum(arr))
print(np.nanmean(arr))