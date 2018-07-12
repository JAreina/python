import json
'''
ARCHIVOS JSON
'''


with open("archivo.json") as file:
    dato = json.load(file)
print(dato)