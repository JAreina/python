print("Welcome to Python!")
print("hola","adios",sep="|")

a = b = c = 1892
print(a,b,c, sep='-')


print("misma dirección de memoria")
print(id(a))
print(id(b))
print(id(c))

d,e,f = "d","e","f"
print(d,e,f, sep='--')

print(id(d))
print(id(e))
print(id(f))

