a = float('123.456')
print(a)
#123.456

try:
 b = float('xxyy')
except :
    print("error de valor")


c = int('3333')
print(c)
#3333

try:
 d = int('123.456')
except :
    print("valor no valido para integer")


e = int('10000', 8)

print("10000 en base 8 : ",e)
#4096

f = int('101', 2)
print("valor de 101 en base 2 : ",f)
#5

g = int('ff', 16)
print("valor de hexadecimal ff a entero :",  g)
#255

try:
 int('123456', 6)
except :
    print("error al pasarlo a base 6 ")
