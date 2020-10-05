import pandas as pd
df=pd.read_csv(r'c:\tmp\elcand.csv',names=['c0','c1','c2','c3','c4','c5','c6','c7','c8','birthYear','c10','c11','c12','c13','c14','c15'])
df['age']=99-df.birthYear
s=df.age.value_counts().sort_index()
import matplotlib.pyplot as plt
plt.bar(s.index,s)
plt.show()