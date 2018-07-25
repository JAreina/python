a = "hello yo"

print( len(a))


b= ' '
print( len(b))

#subscript operator  acceder a una posicion  [ ]

print(a[0])

print(a[-8])


#Slicing for substrings

print(  a[0:1])


print(a[ : :-1]) # imprime string al reves

# metodos string

print("count_________________\n")
str1 = 'abcdefabcdef'

cuantas = str1.count("e")

print(cuantas)
cuantas2 = str1.count("e",6,12)

print(cuantas2)
print("find_________________\n")


str2 = "peace begins with a smi"
donde = str2.find("with")


print(donde)

print("rfind______________\n")

str3 = "what we think, we become"

d= str3.rfind("we")

print(d)

print("lower  upper Capitalize  title________\n")
name = "JUAN juan"

a0 =name.lower()


a1 = name.upper()


print(a0, '\n',a1)



e = "the game"
f= e.capitalize()
print(f)



t = 'genesis of a new realm of possibility.'
p= t.title()
print(p)



i = 'Genesis Of A New Realm Of Possibility.'
g = i.swapcase()
print(g)