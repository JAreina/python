def func(passArgument):
   print (passArgument) 
str = "hello all"
func(str)




def sum(a, b):
   c = a+b
   return c
x = 10
y = 50
print ("Result of addition ", sum(x,y)) 



def info(name, age=50):
   print ("Name", name) 
   print ("age", age) 
info("John", age=28)
info("James") 


def variable_argument( var1, *vari):
 print ("Out-put is",var1) 
 for var in vari:
   print (var)
variable_argument(60)
variable_argument(100,90,40,50,60)



def infocity(**var):
 print (var)
 for key, value in var.items():
     print ("%s == %s" %(key,value)) 
infocity(name="l4w", age = 20, city="Los Angeles")
infocity(name="John",age=45, city="London", sex="male", medals=0)

