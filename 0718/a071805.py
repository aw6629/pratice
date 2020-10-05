import pandas as pd
s1=pd.Series(data=[1,2,3])
s2=pd.Series(data=[3,1,2])
s3=s1.combine(s2,max)
print(s3)