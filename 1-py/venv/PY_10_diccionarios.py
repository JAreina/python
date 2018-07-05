#DICCIONARIOS

# CON LLAVES --- clave valor --- es decir un array asociativo de javascript

dic = {'libro': "ODISEA",
       'autor': "Yo",
       'publicacion': "2018/07/05"}

for elem in dic :
    print(elem)

print(dic)

print(dic['autor'])


print('\n--------------\n')

dic2 = {
    "clave" : ("tupla1", "tupla2"),
    "clave2" : True
}

print(dic2)

print(dic2['clave'][0])


print("\n-----  obtener values  o keys ----\n")

print(dic2.values())
print(dic2.keys())


print("\n---- vaciar diccionario con clear\n")

dic2.clear()

print(dic2)

print("\n-----  hacer una copia del diccionario\n")

dic3 = {
     "clave" : ("tupla1", "tupla2"),
    "clave2" : True
}

dic4 = dic3.copy()

print(dic4)

print("\n-----  método get ------\n")

print(dic.get('libro'))


print("\n-----  actualizar ------\n")

print(dic)
nuevo_autor = {'autor': "TÚ"}

dic.update(nuevo_autor)

print(dic)

