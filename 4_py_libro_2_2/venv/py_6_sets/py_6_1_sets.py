'''

desordenado conjunto  de objetos
de claves sin valores

no admite duplicados

se puede usar in para indagar la existencia en el conjunto de un objeto

the items in a set must be
immutable and hashable. This means that ints, floats, strings,
and tuples can be members of a set, but lists,
dictionaries, and sets themselves can’t.

'''

a = set([1,2,3,4,1,2,3,4])
print(a)

a.pop()
print(a)

a.add(1000)
print("ADD :",a)


a.remove(4)
print("REMOVE : " ,a)


b = set([1,2])
print("diferencia : ",a.difference(b))


c = a.union(b)
print("UNION :",c)


z = a | b # union
print("union | : ", z)


print("__str__ :" ,a.__str__())

d = a.symmetric_difference(b)
print("symmetric_difference :",d)
x = a ^ b  # symmetric difference elements that are in one set or the other but
#not both.
print("symmetric difference ^ : ", x)


print("\n interseccion : \n")
zz = set([66,77,88,200,100])
xx = set([99,100,200])
yy = zz & xx
print("INTERSECCION : ",yy)

a.clear()
print("CLEAR :",a)

print("ESTÁ 7 EN a ? :", 7 in a)

#JAreina