



a = "JAreina"

# como un split

b = list(a)

b[3:] = [] # elimina de la cadena desde la posicion al final

b.reverse()

print(b)
c = "".join(b) # volver la lista a cadena otra vez
print(c)