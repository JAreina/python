tup1 = (1,2,3,4.6, "hello", "a")
print(tup1)
a = 1,2,3
tup1 = 1,2,3,4     
#  JAreina

print(type(tup1))
print(tup1)

print(type(a))
print(a)


A= ("a", "b", "c", "d")

print(A[0])

print(A[-1])



#  JAreina
print("slice ___________\n")

print(A[1:3])



print(A[ : 2 ])




print(A[ :-2])



print("unpack tuplas _________\n")

tup2= (1,2,3)

a,b,c = tup2

print(a)
print(b)
print(c)



print("funciones __________\n")


tup3= ("C", "Python", "java","html")

print(len(tup1))


print("max de la tupla_______\n")
t2 = (781,82,13,74,510)

print(max(t2))

print(min(t2))


tup2 = ('aa', 'z', "az")

print(max(tup2))



#  JAreina
print("convert a string or list into a tupla\n")
str3 = "JAreina"

print( tuple(str3))



print("borra tupla\n")

tup10 = (1,2,3)

print(tup10)

del tup10
tup10 ="nueva variable"
print(tup10)



#  JAreina
print("operaciones con tuplas \n")
a1 = ("YO", "TÚ", "ÉL")

a2 = ("ella", "tos")

print(a1 + a2)



print("multiplica \n")


language = ("Python","html")

a =language*2

print(a)

print(id(a[0]))

print(id(a[2]))

#  JAreina
print(id(a[1]))

print( id(a[3]))




