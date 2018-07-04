def saludar():
    print("hola")


for i in range(1,3):
 saludar()


def multiplicar(num1,num2):
    print(num1 * num2)

multiplicar(100,100)
multiplicar('A',100)


def sumar_dos_numeros(a,b):  #snake case
    return a+b

print(sumar_dos_numeros(1,2))