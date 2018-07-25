def sum1(a,b):
    try:
        c = a+b
        return c
    except :
         return "Error in sum1 function"
def divide(a,b):
    try:
        c = a/b
        return c
    except :
        return "Error in divide function"
print (divide(10,0))

print (sum1(10,0))


print('\n   try varias exceptiones :::::::::::\n')

def divide1():
    try:
        num = int(input("Enter the number "))
        c = 45/num        
        print(c )   
    except ValueError :        
        print ("Value is not int type")

    except ZeroDivisionError :
       print ("Don't use zero")

    else:
      print ("result is ",c)

divide1()






try:
    num = int(input("Enter the number "))
    re = 100/num
except:
    print( "Something is wrong")
else:
    print ("result is ",re)
finally :
    print( "finally program ends")
   
  
print("\n  excepcion argumento \n")

try:
    num = int(input("Enter the number "))
    re = 100/num
    print( re)
except Exception as e :
    print( e, type(e))
   
  
  
print("\n  lanzar excepcion  \n")

try :
	68/0
except ZeroDivisionError as e :
	print(type(e))
	raise ZeroDivisionError(' uuuu error')