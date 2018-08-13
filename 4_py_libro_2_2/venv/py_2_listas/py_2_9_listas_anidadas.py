import copy

m = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
print( m[0])
#[0, 1, 2]
print(m[0][1])
#1
print(m[2])
#[20, 21, 22]
print(m[2][2])
#22



nested = [0]
original = [nested, 1]
print(original)
#[[0], 1]  la lista anidadas es mutable

nested[0] = "posicion cero"
print(original)
try:
 nested[1] = "posicion uno"
 print(original)
except :
 print("IndexError   .::::.............")

nested.append("posicion uno")
print(original)


original[0][0]= "nested cambiado"
print(original)

print("\n DEEP COPIAS \n")
original = [[0], 1]
shallow = original[:]

deep = copy.deepcopy(original)
print(original)
print(deep)

print("\ncambiar un valor en una y no cambia en la otra lista\n")

original[0] = "añadidido en original"
print(original)
print(deep)




