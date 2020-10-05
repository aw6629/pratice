class B1:
    def f1(self):
        print('B1::f1')
    def f2(self):
        print('B1::f2')
class B2:
    def f1(self):
        print('B2::f1')
    def f3(self):
        print('B2::f2')

class C1(B1,B2):
    def f1(self):
        print(C1.__bases__)
        print(C1.__class__)
        self.__class__.__bases__[1].f1(self)
c=C1()
c.f1()
c.f2()
c.f3()