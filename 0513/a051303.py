import pandas as pd
df=pd.read_csv(r'c:\tmp\elcand.csv',names=['c0','c1','c2','c3','c4','c5','name','c7','gender','birthYear','c10','c11','c12','c13','elected','c15'])
df['age']=99-df.birthYear
sample =df.sample(30)
print(sample)
sample_describe = sample['age'].describe()
sample_mean = sample_describe['mean']
sample_std = sample_describe['std']
print(sample_mean-1.96*sample_std,sample_mean+1.96*sample_std)