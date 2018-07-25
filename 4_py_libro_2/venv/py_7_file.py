import os

f = open("secret","w")
print(f)

es_para_escribir = f.writable()
print(es_para_escribir)

f.write("hola\n")

f.close()


f = open("secret", "r")
l = f.readline()
print(l)


def ruta():
  ruta_actual = os.getcwd()
  print(ruta_actual)


print("\n CREAR ARCHIVO EN EL S. OPERATIVO \n")
ruta()
cambiar_a = "/home/juan"
cambiar_aa = os.path.join("/","home","juan/","nuevo.txt")
print(cambiar_aa)

os.chdir(cambiar_a)
ruta()

archivo_nuevo = open(cambiar_aa,"w")

archivo_nuevo.write("hola hola")

archivo_nuevo.close()

archivo_nuevo = open(cambiar_aa,"r")
print(archivo_nuevo.readline())

archivo_nuevo.close()