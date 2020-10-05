import pandas as pd
df=pd.DataFrame({'address':['Kao','Tainan'],'salary':['50000','100000']},index=['Mary','Aa'])
print(df)
print(df['address'])
print(df.loc['Mary'])
print(df.loc['Mary']['address'])