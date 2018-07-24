print("DINERO A REPARTIR")
dinero = int(input("CUANTO DINERO HAY?\n"))
personas = int(input("cuantos somos ?\n"))
try:
 cantidad = dinero/personas
 print(cantidad ,"/persona")
except ZeroDivisionError:
 print("no hay nadie con quien repartir, al bote")


try:
 file = open('namesList.txt', 'a')
 file.write('EOF')

except IOError:
 print("error end of file")
 file.close()
else:
 print("EOF ESCIRTO")
 file.close()