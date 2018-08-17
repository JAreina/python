'''

string no es modificable
'''


a = """ HOLA """
print(a)
b = 'Funciona'
c = "río"

print(b,c)

# 28 de Julio de 2018    JAreina

d = "SE PUEDE 'SE PUEDE' "
print(d)
print("longitud de la cadena :", len(d))

'''
string secuencia de caracteres
'''

print(d[0])
print(d[-2])
print(d[3:8])


x = "HOLA\n"
xx= x[:-1]  # eliminar el salto de línea
print(x)
print(xx)

e = """ "FUTURE" 'FUTURO' """
print(e)

f = ''' "presente" y 'futuro' '''
print(f)


print("\n CONCATENACION \n")

b = "222222"
c = "333333"

d = b + c

print(d)


print("\n  MULTIPLICACION\n")

print( b * 10)


print("\n secuenias de escape \n")


print( " \n aaaaa \t bbbbb \"  \a  \\   ccccc \f ddddd")


print("\n secuenias de escape  unicode python 3 \n")

unicode_a ='\N{LATIN SMALL LETTER A}'
print(unicode_a)
#'a'
unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
print(unicode_a_with_acute)
#'á'
print("\u00E1")
#'á'



print("abc\n")
print("abc\n", end="")
print("no hay salto de linea despues del segundo abc")
