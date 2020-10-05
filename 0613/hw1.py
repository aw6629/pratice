import pandas as pd
import matplotlib.pyplot as plt
df =pd.read_csv(r'c:\tmp\elcand.csv',names=['c0','c1','c2','c3','c4','c5','name','c7','gender','birthYear','c10','c11','c12','c13','elected','c15'])
df['age']=99-df['birthYear']
print(df['age'])
print(df['age'].value_counts().sort_index())
plt.bar(df['age'].value_counts().sort_index())
plt.show()