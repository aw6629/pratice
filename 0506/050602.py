import numpy as np
arr= np.array(['Mary','John'])
fancy_index=np.where(np.char.startswith(arr,'M'))
print(arr[fancy_index])