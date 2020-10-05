class Base:
    def f1(self):
        print('Base::f1()')
class Derived(Base):
    def f1(self):
        print('Derived :: f1()')
    def f2(self):
        f1()

d=Derived()
d.f2()