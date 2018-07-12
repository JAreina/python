import csv

'''
archivos csv
'''


archivo= open("archivo2.csv","w")
datos = csv.writer(archivo)
lista = ["JAreina", 2018]

for i in range(0,10):
     lista[1] = lista[1]+1
     datos.writerow(lista)

archivo.close()


'''
LEER ARCHIVOS CSV
'''

leer = open("archivo2.csv","r")
leido = csv.reader(leer)

for (campo1,campo2) in leido :
    print(campo1,campo2)

leer.close()