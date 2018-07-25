import ctypes
 
 
s = 'JAreina'
b = 'cambiao'
 
direccion = id(b)

print(direccion)
valor =ctypes.cast(direccion,ctypes.py_object).value

print(valor)