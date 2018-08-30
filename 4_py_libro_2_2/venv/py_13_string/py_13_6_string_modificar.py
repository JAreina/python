

print("\n   REPLACE\n")

a = "hola futuro"
print(a)
b = a.replace("hola","Es el")
print(b)

print("\n   MAKETRANS  Y TRANSLATE \n")


c = "888 000"
transform = c.maketrans("000","777")
print(transform)
print(c.translate(transform))

print("\n   LOWER   UPPER \n")

d = "hola"
print(d.upper())
print(d.lower())


print(d.center(40))
print(d.rjust(100))
print(d.ljust(300))
print(d.expandtabs(40))
print(d.zfill(50))
print(d.capitalize())
print(d.partition(","))
print(d.title())
print(d.swapcase())
print(d.split(":"))
print(d.casefold())
print(d.rpartition("--"))