'''

son inmultables
'''

a = ()
b = (2,3,2,2,44,55,1,["a","b"], False,3.3)
print(b)

c = [99,88,77]
e = tuple(c)
print(c)
print(e)


d = list(e)
print(e)
print(d)


print( 33 in b)
print(b[0])

print("count",b.count(2)) # veces que esta el elemento 2
print("index", b.index(3.3)) # argumento el elemento buscado