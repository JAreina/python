'''
HERENCIA
hay herencia múltiple
'''


class Clase:
    hecho = True
    objetivo = "Función"
    anio = 2018

    def mostrar(this):
        obj = ' HECHO : {}, OBJETIVO: {}' \
              ' AÑO: {}'.format(this.hecho,this.objetivo,this.anio)
        return obj

#fin de la clase

class FuncionPublica(Clase): #hereda de la clase Clase


    # CONSTRUCTOR
    def  __init__(self,ok,duracion,destino,sueldo):
         self.ok = ok
         self.duracion = duracion
         self.destino = destino
         self.sueldo = sueldo

    def empezar(self):
        print("empezar :", self.destino)

    def terminar(self):
        print("BUENA SUERTE ", self.duracion)



juan = FuncionPublica(False,"toda la vida","a sabar",1800)
#metodos heredados de Clase
print(juan.objetivo)
print(juan.anio)


class Dos:
    dos = "DOS"
    def dos(self):
        print("metodo dos")


class Tercera(Clase,Dos):
    hereda = "de dos clases"

tercera = Tercera()
print(tercera.mostrar())
print(tercera.dos())