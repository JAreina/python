'''The key-value pair is called an item. The key and value are separated by a colon (:), and
each item is separated by a comma (,). The items are enclosed by curly braces ({ }). An
empty dictionary can be created just by using curly braces ({ }). Key features of the
dictionary are:
The key of the dictionary can not be changed
A string, int, or float can be used as a key
A tuple that does not contain any list can be used as a key
Keys are unique
Values can be anything, for example, list, string, int, and so on
Values can be repeated
Values can be changed
A dictionary is an unordered collection, which means that the order in which you
have entered the items in a dictionary may not be retained and you may get the
items in a different order
Operations on the dictionary
As you know, a dictionary is mutable
'''

port = {22: "SSH", 
             23: "Telnet" , 
             53: "DNS", 
             80: "HTTP"
             }
print(port)              
print(port[53])      

      
print("\n  borrar un item    \n")
del port[23]
print(port)
 # borrar  diccionario:   del port
 
 
print("\n  actualizar un item    \n")
port[53] = "Xxxxxxxxxxx"
print(port)
                                                
print("\n  añadir un item    \n")
port["añade"] = "AÑADIDO"
print(port)

print("\n    FUNCIONES    \n")
print("\n    len()    \n")
print("length", len(port))


print("\n   CONVERTIR  DIC A STRING str()    \n")
print("to string", str(port))




print("\n  max(dict) min(dict)_______     \n")

dic ={"1":1,"a":2}
print(max(dic))
print(min(dic) )

 

print("\n  convertir list a dictionary______     \n")
   
port2=[[80,"http"],[20,"ftp"],[23,"telnet"],[443,"https"],[53,"DNS"]]

print(port2)

print( dict(port2))

print("\n   operador  in \n")

port1888= {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}

key = int(input("di un número @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n"))

if key in port1888:

 print ("eso es posible que exista")
else :

 print ("ese número es inexistente")



print("\n   copy()  \n")

aaa={'iron-man':"Tony", "CA":"Steve","BW":"Natasha"}

print(aaa)
aaaa = aaa.copy()
print(aaaa)



print("\n diferencias copy y =  ...........\n")

A1 = {'iron-man':"Tony", "CA":"Steve","BW":"Natasha"}
A2= A1

print(A2)

copia= A1.copy()
print(copia)
print(id(A1))
print(id(A2))
print(id(copia))


print("\n    get()    ....................\n")


sol = A1.get('iron-man',"No encontrado")

print(sol)


print("\n    setdefault()    ....................\n")

print(A1)
A1.setdefault("jareina", "yo")
A1.setdefault(888)
print(A1)


print("\n    has_key()    ....................\n")

#print(A1.has_key(80))



print("\n    keys()    ....................\n")


print(A1.keys())

print("\n    values()    ....................\n")

print(A1.values())




print("\n    update()    ....................\n")
port777= {22: "SSH", 23: "telnet", 80: "Http" }
print(port777)
port222= {53 :"DNS", 443 : "https"}
port777.update(port222)
print(port777)



print("\n    items()    ....................\n")
dict1 = d={1:'one',2:'two',3:'three'}
print(d)
print(dict1.items())




print("\n    clear()    ....................\n")

print(dict1.clear())


print("\n    RECORRER DICT CON FOR    ....................\n")


portu = {21: "FTP", 22 :"SSH", 23: "telnet", 80: "http"} 
for each in portu:
    print(each)
for k,v in portu.items():
     print (k," : ", v)

print("\n    iteritems()    ....................\n")
    
#portu.iteritems(): print (k," : ", v)