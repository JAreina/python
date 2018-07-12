from xml.etree.ElementTree import parse

'''
archvios XML
'''

documento = parse("nuevo.xml")
print(documento.getroot())
iterador = documento.getiterator()

print(iterador)

for i in iterador:
    print(i)
    print(i.text)


for elemento in documento.findall("funcion"):
    print(elemento.text)