import pandas as pd
df=pd.read_csv(r'c:\tmp\201501.txt',skiprows=1)
print(df['收盤價'])
df=df.query('收盤價==收盤價')
print(df)