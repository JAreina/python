listaa = [100,200,300]

try :

    print(listaa[100])
except IndexError:
        print("error en el indice de la lista")
        try :
            #print(listaa[0] / 2)
             print(listaa[0]/ 0)
        except ZeroDivisionError:
            print("division por cero")
        else:
            print("hola soy else ") # si sale bien el try de la division se ejecuta
finally :
    print("finalmente")


# HEREDA DE Exception

class MiExcepcion(Exception):
    def __init__ (self,x):
        print("ERROR DICE: ",x)

try :
    if 1:   # cero es False
     raise MiExcepcion("ERROR LANZADO")
except MiExcepcion:
    print("error")


