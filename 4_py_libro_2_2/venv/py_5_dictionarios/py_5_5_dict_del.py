english_to_french = {}
english_to_french['blue'] = 'bleu'
english_to_french['green'] = 'vert'


# del   borrar un par clave-valor

items = list(english_to_french.items())
print(items)

del english_to_french['blue']

items = list(english_to_french.items())
print(items)
