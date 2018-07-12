import json
'''
ARCHIVOS JSON
'''

'''
con esto guardalo como file
'''
with open("archivo.json") as file:
    dato = json.load(file)
print(dato)
print("......\n")

print(dato['members'][0]['powers'][0])