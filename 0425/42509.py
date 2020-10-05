class Employee:
    def __setattr__(self, key, value):
        if key == 'id':
            super().__setattr__(key,value)
        else:
            raise Exception('illegal')
e=Employee()
e.id=1
print(e.id)
e.name='B'