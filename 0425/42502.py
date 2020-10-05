x=int(input('input len'))
y=int(input('input wid'))
class rect:
    def __init__(self,len,wid):
        self.__len = x
        self.__wid = y
    def area(self):
        print('面積=',x*y)
    def perimiter(self):
        print('周長=',2*x+2*y)
class squa(rect):
    def __init__(self,x):
        super().__init__(x,x)
d=squa()
if x==y :
    print(d.area())
    print(d.perimiter())
else:
    print(rect.area())
    print(rect.perimiter())






