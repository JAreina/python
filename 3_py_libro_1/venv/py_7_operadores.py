
'''

MATEMATICOS
'''

print( 3 % 2)
print( 3.0 % 2)
print("DIVISION" ,3 / 2)
print("floor division", 3 // 2 ) # redondea hacia abajo
print(2 ** 2)

'''
prioridad operadores 

parentesis
exponentes,
multiplicacion
division
suma
resta
'''

a  = 2 + 2 * 5
print(a)
a  = (2 + 2) * 5
print(a)


print (5 - 6 * 2)
print ((5 - 6) * 2)


print (3 ** 3 * 5) #135
print (3** (3 * 5)) # 14348907


'''
OPERADORES COMPARACION
'''


z = 5
y = 5

print ( z == y)
print( 10 == 10.0)

print( z != y )
#print( z <> y ) no soportado version 3.5

print( z > y )
print( z >= y )


z += 100
print( z )



'''
OPERADORES LOGICOS
'''
print("OPERADORES LOGICOS \n")
print(5 == 5 and 10 == 10) # true
print(5 == 5 and 7 < 6) # false
print(5 == 5 and 7 == 7 and 6 < 7) #v
print(5 == 5 or 7 < 6) # v
print(5 == 5 or 7 < 6 or 5 >10)##v
print(not (5 == 5))#f
print(not (5 == 6))#v