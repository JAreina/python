a = ("a","b","c","d")
b = (2.20,4.40,1.10,10.10)
c = ("aa",11,22,"bb")

print(a,b,c)
'''
TUPLAS SON INMUTABLES
'''
try:
    a[0]= 1000
except:
    print("\n\tlos valores de las tuplas no pueden cambiar")

print(c[1])
print(a[0])


x = 0
while x < 4:
 print(c[x])
 x = x + 1

