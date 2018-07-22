a = "en un lugar de la Mancha. En un lugar de la Mancha"

print("\n capitalize(str)\n")

print(str.capitalize(a))
a = a[:1].upper() + a[1:]
print(a)


print("\n center(num)\n")

print(a.center(100)) #espacios
print(a.center(100, "-")) #lo que quieras

print("\n count('')\n")


b = "En un lugar de la Mancha"
print(b.count("e"))
print("\n count('letra',empieza,termina)\n")
print(b.count("n", 2 , len(b)))

print("\n find('')\n")

c = "En otro lugar de la Mancha de nuevo"
print(c.find("En")) # devuelve el index of , menos uno si no encuentra
print(c.find("aa"))


print("\n isalpha()\n")

d = "hola"
print(d.isalpha())
e = "1"
print(e.isalpha())

print("\n join()\n")

name = ['a',"b","c"]
j = '|'
print(j.join(name))


print("\n len(str)\n")
message = "Join me for the party tonight"
print(len(message))



print("\n split() genera una lista\n")


f= "a,b,c,d,e,f,g"

print(f.split(","))
#JAreina