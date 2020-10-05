import pandas as pd
s1=pd.Series(data=[1,2,3],index=['d','b','c'])
s2=pd.Series(data=[1,2,3],index=['a','b','d'])
print(s1.equals(s2))