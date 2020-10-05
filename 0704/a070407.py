import pandas as pd
df=pd.read_csv(r'c:\tmp\elcand.csv',names=['c0','c1','c2','c3','c4','c5','c6','c7','c8','birthYear','c10','c11','c12','c13','c14','c15'])
df['age']=99-df.birthYear
df.hist(column='age',bins=df.age.max()-df.age.min())
import matplotlib.pyplot as plt
plt.show()