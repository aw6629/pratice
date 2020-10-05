import pandas as pd
df=pd.DataFrame({'x':[0,1,1,1,2,3,7,3]})
print(df['x'].value_counts())
print(df['x'].value_counts().sort_index())
print(df['x'].value_counts().sort_values())
