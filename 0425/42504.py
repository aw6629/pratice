
Employee = type('EmployeeTypeName',(),{'id':0,'salary':lambda emp:10_0000 if emp.id ==1 else 3_0000})
emp=Employee()
print(emp.id)
print(emp.salary())
emp.id =1
print(emp.id)
print(emp.salary())