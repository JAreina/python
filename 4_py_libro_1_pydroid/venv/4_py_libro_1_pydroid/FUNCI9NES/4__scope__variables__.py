def func():
   a =12
#  JAreina
   print ('''Inside the function the value of
 a is acting as local variable''', a)

 
a= 10
func()
print ('''Outside function the value of a is
 acting as global variable''',a)


#  JAreina

print(" \n   global keyword  ::::::::::\n")
def func():
    global k
    k=k+7
    print ("variable k is now global",k)
k=10
func()
print ("Accessing the value of k outside the function",k)