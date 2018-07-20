import random
print('\n valor aleatorio lissta \n ')
a = ["1","2","a","b"]
print( random.choice(a))

print('\n valor aleatorio tupla \n ')
b = ("b1","b2","b3",3,4)
print(random.choice(b))

print('\n número aleatorio \n ')
print (random.randrange (1, 1000))
print (random.randrange (1, 1000, 8))# 8 veces


print('\n shuffle \n ') #reasigna indices y reordena lista
print(a)
random.shuffle(a)
print(a)