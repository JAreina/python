'''

son inmultables pueden contener objetos mutables
'''

a = ()
b = (2,3,2,2,44,55,1,["a","b"], False,3.3)
print(b)

c = [99,88,77]
e = tuple(c)
print(c)
print(e)
print("max : ", max(c))

d = list(e)
print(e)
print(d)


print( 33 in b)
print(b[0])

print("count",b.count(2)) # veces que esta el elemento 2
print("index", b.index(3.3)) # argumento el elemento buscado


print("\n UNIR TUPLAS \n")

t1 = (1,2,3)
t2 = (4,5,6)

print(t1 +  t2)

print("\n COPIA DE TUPLAS")

t3 = t1[:]
print(t3)

t3 = t1 * 1
print(t3)

t3 = t1 + ()
print(t3)


print("\n tuplas de un solo elemetno\n")


x = 3
y = 4
print( (x + y) )# This adds x and y.
#7
print( (x + y,)) # Including a comma indicates the parentheses denote a tuple.
#(7,)
print( () ) # To create an empty tuple, use an empty pair of parentheses.
#()


print("   ---------unpacking --------\n")


(one, two, three, four) = (1, 2, 3, 4)
print(one)
#1
print(two)
#2

one, two, three, four = 11, 22, 33, 44
print(one)
print(four)

# similar a esto
one = 1
two = 2
three = 3
four = 4


print( "\n   *      \n")

x = (1, 2, 3, 4)
a, b, *c = x
print( a, b, c)
#(1, 2, [3, 4])
a, *b, c = x
print(a, b, c)
#(1, [2, 3], 4)
*a, b, c = x
print(a, b, c)
#([1, 2], 3, 4)
a, b, c, d, *e = x
print( a, b, c, d, e)
#(1, 2, 3, 4, [])



#Packing and unpacking can be performed using list delimiters as well:
[a, b] = [1, 2]
[c, d] = 3, 4
[e, f] = (5, 6)
(g, h) = 7, 8
i, j = [9, 10]
k, l = (11, 12)
print( a )
#1
print([b, c, d])
#[2, 3, 4]
print((e, f, g))
#(5, 6, 7)
print(h, i, j, k, l)
#(8, 9, 10, 11, 12)