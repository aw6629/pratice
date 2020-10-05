import  numpy as np
import  pandas as pd
arr=np.array([10,20,30,40])
s=pd.Series(arr,index=['a','b','c','d'])
print(s)
s=pd.Series(np.arange(1,10))
print(s)