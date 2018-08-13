'''

LISTAS SON COMO LOS ARRAYS PERO MÁS FLEXIBLES Y PODEROSOS
puede incluir DIFERENTES TIPOS DE ELEMENTOS :
strings, tuples,
lists, dictionaries, functions, file objects, and any type of number
'''

a = []
b = ["a", "NO", 1, 2.2, True, {"b": 1000}, (1,2,3,4)]
print(b)
print(len(b))


'''
Obtain a slice using [m:n] e, 
- m is the inclusive starting point 
- n is the exclusive ending point. 
An [:n] slice r starts at its beginning,
an [m:] slice goes to a list’s end.
'''

x = ["first", "second", "third", "fourth"]
print(x[0]) #'first'
print(x[2])#'third'
print(x[-1])#'fourth'
print( x[-2])#'third'
print( x[1:-1])#['second', 'third']
print(x[0:3])#['first', 'second', 'third']
print( x[-2:-1])#['third']
print( x[:3])#['first', 'second', 'third']
print( x[-2:])#['third', 'fourth']


print("\n x[:]  ::::::::::::::::\n")
yy = x[:]
print(x)
print(yy)



x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x[1] = "two" # sustituir la posicion 1 de la lista por "two
x[8:9] = []  # borrar el ultimo
print(x)

x[5:7] = [6.0, 6.5, 7.0] # añadir en posicion 5 -- [1, 'two', 3, 4, 5, 6.0, 6.5, 7.0, 8]
print(x) #[1, 'two', 3, 4, 5, 6.0, 6.5, 7.0, 8]
print(x[5:]) #[6.0, 6.5, 7.0, 8]


x.clear()
x = [1,2,3,4,5,6,7,8]
print(len(x))
x.reverse()
print(x)



y = max(x)
print(y)
print(min(x))




x.insert(0,2222)
print(x)
x.remove(2222)
print(x)

bb = x.pop()
print("pop : ",bb)
print(x)

print("esta el valor 2 en lista ? ", 2 in x)

del x[0]

x.sort()
print("Sort", x)

print(x)
for aa in x :
    print(aa)


print("\n MODIFICAR LISTAS :::::::::::::::\n")

x = [1, 2, 3, 4]
x[len(x):] = [5, 6, 7]
print(x)   #[1, 2, 3, 4, 5, 6, 7]
x[:0] = [-1, 0]
print(x)  #[-1, 0, 1, 2, 3, 4, 5, 6, 7]
x[1:-1] = [] #entre el primer elemento y el ultimo elemento borra
print(x)


print("\n APPEND   ::::::::::::\n")

x.append(1000)
print(x)


x = [1, 2, 3, 4]
y = [5, 6, 7]
x.append(y)
print(x)#[1, 2, 3, 4, [5, 6, 7]]

print("\n  INDEX :::::::::::::::\n")
i = x.index(1)
print(i)

print("\n  EXTEND :::::::::::::::\n")
x = [1, 2, 3, 4]
y = [5, 6, 7]
x.extend(y)
print(x) #[1, 2, 3, 4, 5, 6, 7]


print("\n  INSERT :::::::::::::::\n")
x = [1, 2, 3]
x.insert(2, "hello")
print(x) #[1, 2, 'hello', 3]
x.insert(0, "start") # EN LA POSICION CERO INSERTA ANTES DE LA POSICION
x.insert(1,"antes del uno")
print(x) #['start', 1, 2, 'hello', 3]

x.insert(-1, "en -1")
print(x)

print("\n DEL    ::::::::::::\n")

del x[0]
print(x)
del x[:2]
print(x)

print("\n REMOVE    ::::::::::::\n")

x = [1, 2, 3, 4, 3, 5]
x.remove(3)
print(x) #[1, 2, 4, 3, 5]
x.remove(3)
print(x) #[1, 2, 4, 5]

print("\n REVERSE   ::::::::::::\n")
x = [1, 3, 5, 6, 7]
x.reverse()
print(x)

print("\n sort   ::::::::::::\n")
x = [3, 8, 4, 0, 2, 1]
print(x)
x.sort() #cambia original
print(x)
# hacer copia

a = [23,32,1,8,77]
y = a[:]
print(a)
y.sort()
print(y)

# con string
x = ["Life", "Is", "Enchanting"]
print(x)
x.sort()
print(x)

try:
    x = [1, 2, 'hello', 3]
    x.sort()
except:
    print("error de ordenacion")

# ordenar lista de listas
x = [[3, 5], [2, 9], [2, 3], [4, 1], [3, 2]]
print(x)
x.sort()
print(x)
