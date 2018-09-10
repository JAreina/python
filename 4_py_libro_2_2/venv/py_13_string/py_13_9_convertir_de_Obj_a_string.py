

# funcion repr(obj) usado con listas y otros objetos

# funcion __str___

a = [1,2,3,4,66]
print(repr(a))

print("metodo str", a.__str__())

b = [33]
b.append(55)

print('X --> ' + repr(b))



print(repr(len))