'''

desordenado conjunto  de objetos
de claves sin valores

no admite duplicados

se puede usar in para indagar la existencia en el conjunto de un objeto

'''

a = set([1,2,3,4,1,2,3,4])
print(a)

a.pop()
print(a)

a.add(1000)
print(a)

b = set([1,2])
print("diferencia",a.difference(b))


c = a.union(b)
print(c)


print("__str__ :" ,a.__str__())

d = a.symmetric_difference(b)
print(d)


a.clear()
print(a)

print(7 in a)

#JAreina