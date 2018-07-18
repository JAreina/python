'''
string sucession de caracteres indice empieza en cero
'''

a = "Siempre es buen día"

print(a[0])
print(a[17])

'''
substring
'''

b = a[11:15]
c = a[16:]
print(b,c)


'''
concatenacion
'''

d = "BUENOS"
e = "días"
f = d +" "+ e
print(f)
print(b + c)



'''
print format como en lenguaje c
'''

numero = 10
print("Estos son %d %s" % (numero, d))






