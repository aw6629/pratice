# import pandas as pd
# s= pd.Series(pd.date_range(start='2020/01/01',end='2020/01/31'))
# print(s)
# import  pandas as pd
# s= pd.Series(['2020/01/01','2020/01/31'],dtype='datetime64[ns]')
# print(s)
import pandas as pd
s=pd.Series(['2020/01/01','2020/01/02'])
print(s)
s=s.astype('datetime[ns]')
print(s)