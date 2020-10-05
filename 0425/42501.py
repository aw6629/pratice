class Base:
    def __init__(self):
        print('1')
class Derived(Base):
    def __init__(self):
        super().__init__()
        print('2')
        super.__init__()
d=Derived()
