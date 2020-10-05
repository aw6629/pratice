import pandas as pd
s1=pd.Series([3,4])
s2=pd.Series([1,2])
s1=s1.append(s2)
print(s1)
print(s1.iloc[0:2],type(s1.iloc[0]))
print(s1.iat[0],type(s1.iat[0]))