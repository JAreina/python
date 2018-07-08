'''
FICHEROS
'''

def abrir_archivo(nombre,modo):

    return open(nombre,modo)


def escribir(archivo,modo,texto):
    fich = abrir_archivo("nuevo","a")
    fich.write(texto)
    fich.write("\n")
    cerrar(fich)

def cerrar(archivo):
    archivo.close()



def leer(archivo):
    fich = abrir_archivo(archivo,"r")
    linea = fich.readline()
    while linea != "":
        print(linea)
        linea = fich.readline()
    cerrar(fich)

escribir("nuevo","a", "En un lugar de la Mancha")
escribir("nuevo","a", "En un lugar de la Mancha")


leer("nuevo")