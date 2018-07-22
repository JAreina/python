a = {
    "a": 1000,
    "b": 2000,
    "c": 3000
}

print(a["c"])

a["c"] = 9999

print(a["c"])


print("\n   BORRAR ELEMENTO DICT \n")

print(a)
del a["a"]
print(a)


print("\n   funciones DICT \n")

print(len(a))

print("\n  convertir dict a string \n")

print(str(a))

print("\n  clear \n")

a.clear()

print(a)


print("\n  get \n")

b = {
    "aa": "z",
    "bb": "y",
    "cc": "x"
}

print(b.get("bb"))


print("\n  items \n")

print(b.items())

print("\n  values \n")

print(b.values())


print("\n  keys \n")

print(b.keys())


for llave in b:
    print(llave)

for llave,valor in b.items():
    print(llave, " : ", valor)