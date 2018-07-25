'''

INMUTABLES
'''
import re

a = "Marte y Júpiter\t"
print(len(a))
aa = a.split()
print(aa)
print(a.replace("Marte","CENSURADO"))
print(a)



regexpr = re.compile(r"\t")
b = regexpr.sub("...", a) # sustituir tab por ...
print(b)


vida = "vida"
print("el planeta",aa[0], "tiene",vida )


c = 19
d = "cadena"
print("numero --> %d string --> %s" % (c,d)) #c sprintf