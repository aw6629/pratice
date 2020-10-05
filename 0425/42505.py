dic={'id':1,'name':'D'}
from collections import namedtuple
Employee=namedtuple('EmployeeTypename','id name')
e=Employee(**dic)
print(e.id)
print(e.name)
