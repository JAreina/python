a = open("texto.txt","r")
print(a.read())

print("\n")
a = open("texto.txt","r")
print(a.read(18))

print("\n")
a = open("texto.txt","r")
print(a.readline())

for line in a:
 print(line)

 print("\n")
a = open("texto.txt","r")
for line in a:
 print(line)