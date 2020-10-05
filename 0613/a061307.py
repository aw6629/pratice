import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r'c:\tmp\dataset1.txt')
df1=df.sort_values(by=['x'])
plt.plot(df1.x,df1.y)
plt.show()