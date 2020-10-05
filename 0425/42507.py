class Base:
    def __init__(self,id):
        print(f'id={id}')
class Derived(Base):
    pass

d= Derived(10)