'''

if
'''

a = 1000
b = False
if a == 1000 or a > 999 and not b:
    print("verdadero")

aa = 1000
bb = True
if aa != 1000 or aa > 999 and not bb:
    print("es verdadero")
else :
    print("es falso")



grade = 92
if grade >= 90:
 letterGrade = 'A'
if grade >=80:
 letterGrade = 'B'
print (letterGrade)
# sobreescribe la variable  no es correcto
# mejor usar elif

grade = 72
if grade >= 90:
 letterGrade = 'A'
elif grade >=80:
 letterGrade = 'B'
elif grade >=70:
 letterGrade = 'C'
elif grade >=60:
 letterGrade = 'D'
else:
 letterGrade = 'E'
print (letterGrade)


print( " if anidados")
value = 50
if value < 200:
   print ('Value is less than 200')
   if value < 150:
       print ('Value is less than 150')
       if value < 100:
           print ('Value is less than 100')
           if value == 50:
             print ('Value is 50')



print( " if anidados 2")
value = 50000
if value < 200:
   print ('Value is less than 200')
   if value < 150:
       print ('Value is less than 150')
       if value < 100:
           print ('Value is less than 100')
           if value == 50:
             print ('Value is 50')
else:
    print("el valor es mayor de 200")

print( "operador ternario ")

age = 23
print ('Eligible to buy alcohol' if age >=18 else 'Ineligible to buy alcohol')