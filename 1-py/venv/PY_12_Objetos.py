"""
OBJEJTOS : ATRIBUTOS Y METODOS



"""
class Clase:
    hecho = True
    objetivo = "Función"
    anio = 2018

    def mostrar(this):
        obj = ' HECHO : {}, OBJETIVO: {}' \
              ' AÑO: {}'.format(this.hecho,this.objetivo,this.anio)
        print(obj)


si = Clase()
print(si.objetivo)

anioo = si.__getattribute__("anio")
print(anioo)



si.mostrar()