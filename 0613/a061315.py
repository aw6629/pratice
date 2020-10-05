import  numpy as np
arr=np.array([0,1,1,1,2,3,7,3])
element,count=np.unique(arr,return_counts=True)
for x,y in zip(element,count):
    print(x,':',y)