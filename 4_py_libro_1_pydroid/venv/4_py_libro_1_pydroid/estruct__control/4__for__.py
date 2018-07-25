sum = 0
for i in range(1,10):
    print("valor {}".format(i))
    sum = sum+i
    print (sum)
    
#sum = 0
#counter = 1

print(" \n     BREAK     ::::::::::::\n")

list1 = ["London","Paris","New York","Berlin"]
for each in list1:
 str1 = each
 for s in str1:
     if (s =="o"):
        break
     print (s)
 print( "\n")


print(" \n     CONTINUE    ::::::::::::\n")

movies = ["P.S I Love You", "Shutter Island", "Les Miserables Play",
"King's Speech", "Forest Gump"]
for each in movies:
        if (each== "Les Miserables Play"):
                continue
        print (each)
   
        
             

print(" \n     pass   ::::::::::::\n")                       
def fun():
        pass
for each in "Australia":
        pass
