'''
puede incluir:
strings, tuples,
lists, dictionaries, functions, file objects, and any type of number
'''

a = []
b = ["a", "NO", 1, 2.2, True, {"b": 1000}, (1,2,3,4)]
print(b)


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
x.append(1000)
print(x)

i = x.index(1000)
print(i)

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