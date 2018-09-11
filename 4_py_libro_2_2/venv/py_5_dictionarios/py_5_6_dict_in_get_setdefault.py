english_to_french = {}
english_to_french['blue'] = 'bleu'
english_to_french['green'] = 'vert'



# saber si existe una key con operador in
# o el metodo get() que retorna el segundo argumento si no existe

print('blue' in english_to_french)

del english_to_french['blue']
print( english_to_french.get('blue', "oh no existe eso"))


# setdefault busca una key y si no existe la crea

print(english_to_french.setdefault('blue', "azul"))
items = list(english_to_french.items())
print(items)