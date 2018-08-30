'''
para buscar en un texto se puede usar el modulo re tambien

'''

a = "funciona funciona funciona hola"
print(a.find("ona"))
#devuelve la posicon de la primera coincidencia     5


print(a.find("x"))
# -1 si no encuentra nada
#  segundo argumento el final , hasta donde buscar

b = "aa bb cc"
print(b.find("aa",1))


# RFIND

print(a.rfind("ona"))


#  INDEX , RINDEX

print(a.index("ona"))
print(a.rindex("ona"))


#  COUNT

print(a.count("a"))

#   starstwith   endswith

print(a.startswith("a"))
print(a.endswith("a"))


print(a.endswith(("u","a")))  #  una tupla