a = ["re",67, True,"JAreina"]

b,c,d,e = a

print(a)
print(b)
print(c)
print(d)
print(e)


print(" ACCEDER _____\n")

print(a[0])
print(a[-1])


print("SLICE __...._____\n")
#<list-name>[start : stop : step]

print(a[1:2])
print(a[1:3 :1])

list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

print(list1[1:13:3])


print("actualizar __...._____\n")
print(a)
a[2] = False
print(a)




print("borrar__...._____\n")
print(a)
del a[2] 
print(a)




print("añadir__...._____\n")
print(a)
print(list1)
u = a + list1
print(u)





print("multiplicar__...._____\n")
print(a)
h = a * 2
print(h)
for i in h:
	print(id(i))
	
	
if "JAreina" in h :
	print(1)
	
print("\nFUNCIONES LIST  \n")

print(len(h))
print(list1)
print(max(list1))
print(min(list1))



print("\n convertir a una lista\n")
tup1 = ("a","b","c")

print(tup1)
print( list (tup1))



print("\n   sorted    \n")
list11= [2, 3, 0, 3, 1, 4, 7, 1]

print(list11)
print(  sorted (list11) )





print("\n append a una lista\n")

e = [ ]

e.append(45)

print(e)




print("\n extend una lista\n")

e.extend("añadido")
print(e)

t = (1,2,3)
e.extend(t)
print(e)



print("\n  count    \n")

list12 = ["a","c","b","c","a","h","l", 1, 2, 3, 4]

print(list12.count ("a"))



print("\n    index     \n")

OS = ['kali', 'Ubuntu', 'debian', 'RHEL', 'Centos']

print (OS.index("debian"))



print(  "\n   insert   \n")
A = ['iron-man', 'hulk', 'Thor']

print(A)
A.insert (0,"Captain-America")


print(A)


print(" \n    remove    \n")


Avengers1 = ["Iron-man","Thor","Loki","hulk"]


print( Avengers1)
Avengers1.remove ("Loki")



print( Avengers1)




print("  \n    pop    \n")

print( Avengers1)

Avengers1.pop()


print( Avengers1)


Avengers1.pop(0)

print( Avengers1)



print("\n    sort     \n")

list8 = [5, 6, 7, 1, 4, 2, 0, 4, 2, 8]

print(list8)
list8.sort()


print(list8)



print("\n    sort   reverse  \n")
print(list8)
list8.sort (reverse=True)

print(list8)



list22 = [ "1", "a","@#", "nm"]

print(list22)
list22.sort()
# ascendente
 
print(list22)
 
list22.sort(reverse= True)
# descendente
 
print(list22)



print("\n   ordenar por segundo valor de cada tupla  \n")


aa = [("a",4),("b",1),("v",5),("f",2)]

'''
The tuples in the list contain two values, and you want to sort the list according to the

second value of tuples.
'''
def fun1(x):

            return x[1]


aa.sort(key= fun1)

print(aa) 



print("  \n  reverse \n")

print(A)

A.reverse()


print(A)





print("\n   llenar list 1   __ \n")
lista1= [2,3,4,5,6]

lista2 = []

for each in lista1:

            lista2.append(each*each)

print(lista1)
print(lista2)


print("\n   llenar list 2  ______\n")

lista3 =   [each*each for each in lista2]

print( lista3)

print("  Pares 1  ________     \n")

list189 = [2,3,4,5,6]

list222 = []

for each in list189:

            if each%2== 0:

                        list222.append(each*each)

print( list222)



print("  Pares  2  ________     \n")

hh = [each*each for each in list189 if each%2 == 0]


print(hh)



print("\nacceder al string hola \n ")

list1888 = ["abc",[2,3,("adios","hola")],1,2,3]


print(list1888[1][2][1])
