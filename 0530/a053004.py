import re
source='1+2*3'
result=re.split(r'([\+\-\*\/])',source)
print(result)