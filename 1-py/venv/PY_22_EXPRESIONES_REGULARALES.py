import re



str = "JAreina"
print(str)
resultado = re.search(r"ei",str)
print(resultado)


num = "JAreina20__18"
patron = re.compile("\d\d") # dos digitos
print(patron.search(num))

patron2 = re.compile("[A-Z]\d")
print(patron.search("ZDFDFDE12"))



variable= "aldf66234CAKI"
if (re.search("[a-z][1-3].*$",variable)):
    print("encontrado")
else:
    print("no encontrado")



# sub buscar y sustituir por un cero en una cadena

print( re.sub(r"\d","0", "en una 1 dos 2 8 siete 9"))