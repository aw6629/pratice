import seaborn as sns
df=sns.load_dataset('iris')
import pandas as pd
pd.set_option('max_rows',None)
print(df,type(df))
