class B1:
    def f1(self):
        print('B1::f1')
class B2(B1):
    def f1(self):
        print('B2::f1')
class B3(B2):
    def f1(self):
        # print('B3::f1')
        super(B2,self).f1()
class B4(B3):
    pass
c=B4()
c.f1()