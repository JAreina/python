
a = [(2,2), (3,3), (4,4)]

resultado = 0

for tupla in a :
    resultado = resultado + (tupla[0] * tupla[1])
print(resultado)


# unpacking

resultado2 = 0

for x , y in a :
    resultado2 = resultado2 + (x * y)

print(resultado2)