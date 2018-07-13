listaa = [100,200,300]

try :

    print(listaa[100])
except IndexError:
    print("error en el indice de la lista")
    try :
        print(listaa[0] / 0)

    except ZeroDivisionError:
        print("division por cero")
finally:
    print("finalmente")
