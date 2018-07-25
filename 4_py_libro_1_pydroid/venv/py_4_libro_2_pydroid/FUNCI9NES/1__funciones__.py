def helloWorld():
   """ This is Hello World Program"""
   print ("You are in Hello World")
helloWorld()



def func(passArgument):
   print (passArgument)

str = "argumentoooooo"
func(str)


#  JAreina
def sum(a, b):
   c = a+b
   return c
x = 10
y = 50
print ("RESULTADO\n\t ", sum(x,y))



print("\n   argumento por defecto\n")
def info(name, age=650):
   print ("Name", name)

   print ("age", age)

#  JAreina
info("John", age=28)
info("James")



print("\n    argumentos variabless\n")

def variable_argument( var1, *vari):

      print( "PRIMER ARGUMENTO",var1)

      for var in vari:

         print (var)

 
#  JAreina
variable_argument(60)

variable_argument(100,90,40,50,60)


print("\n   key value variables args\n")
def infocity(**var):

 print("ARGS:",var)

 for key, value in var.items():

  print( "%s == %s" %(key,value))
  
  
infocity(name="l4w", age = 20, city="Los Angeles")

#  JAreina
infocity(name="John",age=45, city="London", sex="male", medals=0)