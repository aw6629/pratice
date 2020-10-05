import pandas as pd
s=pd.Series(pd.to_datetime('today'))
print(s)
print(s.dt.year.values)