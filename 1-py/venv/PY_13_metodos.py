"""
self :  como this
este mismo objeto  ejecuta los metodos
el contexto ,


"""


class FuncionPublica:
     ok = True
     duracion = "SIEMPRE"
     destino = "aventura"
     sueldo = 1300



     def empezar(self):
         print("empezar :" , self.destino)
     def terminar(self):
          print("BUENA SUERTE ", self.duracion)

juan = FuncionPublica()
juan.empezar()

print(juan.ok)
print(juan.terminar())