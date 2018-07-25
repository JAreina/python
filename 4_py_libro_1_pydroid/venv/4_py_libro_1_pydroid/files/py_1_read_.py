file_input = open("jareina.txt",'r')
all_read = file_input.read()
print("\nLEE  \n")
print( all_read)
file_input.close() 



#  JAreina

print(" \n   readline()  \n")
file_input = open("jareina.txt",'r')

print (file_input.readline())

print (file_input.readline())

print (file_input.readline())

file_input.close()



print(" \n   readline(numero) ::::::::::::::: \n")

file_input = open("jareina.txt",'r')

print ( file_input.readline(10))

print  (file_input.readline(2))

file_input.close()



print(" \n   readlines()  ::::::::::: \n")

file_input = open("jareina.txt",'r')

print  (file_input.readlines())


file_input.close()




file_input = open("jareina.txt",'r')

lineas = file_input.readlines()
print(lineas)


print(lineas[1])
file_input.close()