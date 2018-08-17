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



print("\n split :::::::::::::::::\n")


aa = "fechas previstas"
bb = aa.split()
print(bb)


cc = "la le li lo lu"
dd = cc.split(" l")
print(dd) #['la', 'e', 'i', 'o', 'u']


ee = cc.split(" ",1)
print(ee) #['la', 'le li lo lu']


ff = cc.split(None, 1)
print(ff)


print("\n   JOIN :::::::::: \n")

gg = "---".join(["a", "b", "c"])
print(gg)