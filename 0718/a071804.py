# import pandas as pd
# s1=pd.Series(data=[1,2,3])
# s2=pd.Series(data=[1,2,3])
# s3=s1+s2
# print(s3)
#
# import pandas as pd
# s1=pd.Series(data=[1,2,3],index=['a','b','c'])
# s2=pd.Series(data=[1,2,3],index=['a','b','d'])
# s3=s1+s2
# print(s3)

import pandas as pd
s1=pd.Series(data=[1,2,3],index=['a','b','c'])
s2=pd.Series(data=[1,2,3],index=['a','b','d'])
s3=s1.add(s2,fill_value=0)
print(s3)