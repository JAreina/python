import time

tiempo_local = time.localtime() # return una tupla
print(tiempo_local)

print(tiempo_local.tm_year)




localtime=time.localtime(time.time())
print(localtime)


print("\n   formato humano\n")

formattedtime=time.asctime(time.localtime(time.time()))
print(formattedtime)


print("\n funciones time \n")

print(time.clock()) # reloj del pc


print("\n actual GMT \n")
print(time.gmtime(time.time()))