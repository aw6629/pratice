import pandas as pd
df=pd.read_csv(r'c:\tmp\201501.txt',skiprows=1)
df=df.query('收盤價==收盤價')
df['year']=(df.日期.str[:3]).astype(int)
df.year=df.year+1911
df.year=df.year.astype(str)
df['month_date']=df.日期.str[3:]
df['DT']=(df.year+df.month_date).astype('datetime64[ns]')
df=df.set_index('DT')
df.index.name='Date'
df['Open']=df['開盤價']
df['High']=df['最高價']
df['Low']=df['最低價']
df['Close']=df['收盤價']

import matplotlib.pyplot as plt
import mplfinance as mpf

mc=mpf.make_marketcolors(up='r',down='g')
s=mpf.make_mpf_style(marketcolors=mc)
mpf.plot(df,type='candle',style=s)
plt.show()