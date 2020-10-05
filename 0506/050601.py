import numpy as np
import time
start=time.time()
arr=np.arange(100_0000)
arr=np.where(arr%2==0,arr+1,arr-1)
print(time.time()-start)


def odd_even(data):
    if data%2 ==0:
        return data +1
    else:
        return data -1
start1=time.time()
arr=np.arange(100_0000)
m_func = np.vectorize(odd_even)
arr=m_func(arr)
print(time.time()-start1)