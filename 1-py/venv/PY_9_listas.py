#listas

lista = [22,33,44]
lista2 = [1, 'JAreina',4.4]

print("----------")
for elem in lista2 :
    print(elem)


lista2.append(390)

lista2[0] = "cambiado"
print("----- pop -----")
for elem in lista2 :
    print(elem)

eliminado = lista2.pop()
print(eliminado, "ha sido eliminado")

print("----------")
for elem in lista2 :
    print(elem)
print("-----extend -----")

lista3 = [1,2,3]
lista4 = [4,5,6]

lista3.extend(lista4)

for elem in lista3 :
    print(elem)
print("----- del -----")


eliminar_lista = [1,'a','b','c']
print(eliminar_lista)

del eliminar_lista[1]
print(eliminar_lista)


print("----- remove -----")

eliminar_lista.remove(1) #remueve el elemento con ese valor no el indice
print(eliminar_lista)


print("----- cuantos  elementos hay igual a este del argumento en la lista-----")
lista5 = [33,77,65,44,33,22]
print(lista5.count(33))

print('---- sort ----')

lista5.sort()
print(lista5)


print('---- sort reverse ----')

lista5.sort(reverse= True)
print(lista5)

print('---- indices negativos ----')
#indices negativos

lista6 = [1,2,3,4,5,6,7,8,9,0]

print(lista6[-4])  #posicion del ultimo elemento -2 el penultimo etc

