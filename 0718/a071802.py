# import pandas  as pd
# s=pd.Series(['2020/01/01','2020/01/02'],dtype='datetime64[ns]')
# print(s+pd.DateOffset(years=1))

import pandas as pd
s=pd.Series(['2020/01/01','2020/01/02'],dtype='datetime64[ns]')
print(s-pd.to_datetime('2020/01/31'))