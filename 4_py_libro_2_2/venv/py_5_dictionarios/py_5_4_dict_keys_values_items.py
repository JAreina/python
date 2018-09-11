english_to_french = {}
english_to_french['blue'] = 'bleu'
english_to_french['green'] = 'vert'
print("blue : ", english_to_french['blue'])

# keys()

llaves = list(english_to_french.keys())
print(llaves)

# values()

valores = list(english_to_french.values())
print(valores)


# items() devuelve como tuplas (llave , valor)

items = list(english_to_french.items())
print(items)