a = open("archivo.txt","w")

lista = []
articulo = ""

while(articulo != "0"):
    articulo = input("incluye un articulo\n")
    if(articulo != "0"):
        lista.append(articulo+"\n")


for art in lista:
    a.write(art)
a.close()