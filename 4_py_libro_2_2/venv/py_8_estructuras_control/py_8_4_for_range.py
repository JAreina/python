a = [1,44,-4, 0 , 99, -3, 55, -46]

for i in range(len(a)):
    if a[i] < 0 :
        print("NEGATIVO: posicion {0} : valor: {1}".format(i, a[i]))



    # rangos con dos argumentos

print(list(range(44,66))) # no incluye el numero 66

print(list(range(-77,-66)))

print(list(range(444,66))) # lista vacia

# hacia atras

print(list(range(88,66,-1)))