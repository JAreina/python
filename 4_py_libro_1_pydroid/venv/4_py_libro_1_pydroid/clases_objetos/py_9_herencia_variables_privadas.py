'''The private variable
Python doesn't have real private methods, so two underlines at the beginning make a
variable and a method private.
'''
class A:
    __amount = 45
    def __info(self):
       print ("I am in Class A")
    def hello(self):
       print( "Amount is ",A.__amount)
a = A()
a.hello()
a._A__info()
print (a._A__amount)