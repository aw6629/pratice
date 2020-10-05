import re
source='A123456789'
result=re.fullmatch(r'^[A-Z][1-2]\d{8}$',source)
if result:
    print('Match')
    print(result,type(result))
else   :
    print('Not Match')