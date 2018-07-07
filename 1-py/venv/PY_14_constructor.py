'''
constructor

'''


class FuncionPublica:


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
print(juan.duracion)