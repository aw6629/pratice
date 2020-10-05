import re
source='asasdasfasasfasf as 0944556677,dsadasdgejaui dasd 0977885522'
result=re.findall(r'09\d{8}',source)
print(result,type(result))
