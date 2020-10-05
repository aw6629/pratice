l=[0,1,1,1,2,3,7,3]
import collections
counter= collections.Counter(l)
print(counter,type(counter))
# for x in counter.most_common():
#     print(x[0],x[1])
for k,v in counter.items():
    print(k,v)
l=sorted(counter.items(),key =lambda t:t[1])
print(l)
for x in l:
    print(x[0],x[1])