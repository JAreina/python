cont = 0
sum = 0
while (cont < 10):
     print(cont,  "::::::::::::")
     sum = sum + cont
     print (sum)
     cont = cont +  1
     
     
s = 0
while True:
   data = int(input("DI NÚMERO, \n\t CERO SALIR:\n\v"))
   if data == 0:
      break
   s = s+data
print ("Suma : ", s)


print("\n\t       otra condicion\t\n")
s = 0
ban = 1
while ban ==1:
   data = int(input("DI NÚMERO, \n\t CERO SALIR:\n\v"))
   if data == 0:
      ban = 0
   s = s+data
print ("Suma : ", s)



print("\n   break      :::::::::::::::::::\n")

a= ['a', 'b', 'c', 'd']
es= "c"
for esto in a:
     if(esto == es):
          print("sale")
          break
     print (esto)