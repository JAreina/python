'''

sentencia del
metodos : clear, copy, get, has_key, items, keys,
update, and values


keys deben ser inmutables tipos : numeros, string o tuplas
values cualquier objeto
'''

x = {1: "one", 2: "two"}
print(x)

x["uno"]= 111
print(x)
x[("Delorme", "Ryan", 1995)] = (1, 2, 3)

print(x)

lista = list(x.keys())

print("KEYS :" ,lista)


print("\n obtener una posicion \n")

print(x[2])
print(x.get(2,"si no existe escribe esto"))
print(x.get(20,"si no existe escribe esto"))


cc = x.copy()
print(cc)

print(id(x))
print(id(x))

ccc = cc
print(id(ccc))
