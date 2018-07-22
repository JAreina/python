a = [1,2,3,4,5,6,7]
print(a)

'''
valores pueden cambiar

'''

a[0]= 10000
print(a)
print(a[1:2])
print(a[0])


print("longitud de la lista:",len(a))

x=0
while x < len(a):
 print(a[x])
 x += 1


print("máximo -->", max(a))
print("minimo -->", min(a))


print("\n CONVERTIR LISTA A TUPLA\n")


b = tuple(a)
print("TUPLA --> ",b)
print("LISTA --> ",a)

print(b[0])