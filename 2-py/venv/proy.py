import urllib.request as request
import urllib.request as urlopen
import os
from bs4 import BeautifulSoup
import re

# VERIFICAR HTTPS

req = request.Request('http://python.org')
resultado = request.urlopen(req)

print(resultado.geturl())
resultado.close()


# peso pagina  de los headers de una petición


url2 = "https://python.org"
sitio = request.urlopen(url2)
meta = sitio.info()
print(meta)
print("content-Length", int(sitio.headers['content-length'])/1024)

archivo = open("http.txt","w")
archivo.write(str(meta) )
archivo.close()
sitio.close()
print("tamaño archivo 'http.txt': ",os.stat("http.txt").st_size)



# www

sitio = request.urlopen(url2)
print(sitio.geturl())


#meta description

soup = BeautifulSoup(sitio,"html.parser")
print(soup)
descripcion = soup.find('meta',attrs={'name':'description'})
print("DESCRIPCION:",descripcion.get('content'))

sitio.close()

# TITLE
print("\n :::::::::::::::: obtener title ::::::::::::::::. \n")
sitio = request.urlopen(url2)

s = BeautifulSoup(sitio,"html.parser")
print(s.html.head.title.string)

print("\n :::::::::::::::: obtener etiqueta title y contenido ::::::::::::::::. \n")
titulo = soup.find("title")
print(titulo)

sitio.close()

# obtener palabras claves
print("\n :::::::::::::::: PALABRAS CLAVE ::::::::::::::::. \n")
sitio = request.urlopen(url2)
sou = BeautifulSoup(sitio,"html.parser")

palabras_claves = sou.find('meta',attrs={'name':'keywords'})
print("KEYWORDS:",palabras_claves.get('content'))

lista = palabras_claves.get("content").split()
print(lista)


for palabra in lista :
     # cuantas veces aparece cada palabra en la pagina
    print(palabra ,len(sou.findAll(text=re.compile(palabra))))

sitio.close()

#    atributo alt
print("\n :::::::::::::::: IMAGENES ::::::::::::::::. \n")
sitio = request.urlopen(url2)
sou = BeautifulSoup(sitio,"html.parser")
cont = 0
for img in sou.findAll('img') :
     # cuantas veces aparece cada palabra en la pagina
    print("imagen " ,cont, ":", img["src"])
    print("alt", cont, ":",img.get("alt","no tiene"))
    cont +=1



sitio.close()


print("\n :::::::::::::::: h1 ::::::::::::::::. \n")
sitio = request.urlopen(url2)
sou = BeautifulSoup(sitio,"html.parser")

for h1 in sou.find_all('h1') :
     # cuantas veces aparece cada palabra en la pagina
    print("H1 : "  ":", h1)
    print(h1.get("class", "NO TIENE CLASE"))

print("TOTAL H1 :", len(sou.find_all('h1')))

sitio.close()


print("\n :::::::::::::::: enlaces ::::::::::::::::. \n")
sitio = request.urlopen(url2)
enlaces = []
sou = BeautifulSoup(sitio,"html.parser")
elementos = sou.select('a')

for a in elementos :
    enlac = a.get('href')
    print("link : "  ":", enlac)
    if enlac.startswith('http') :

        enlaces.append(enlac)

print("enlaces  :", enlaces)
print("total enlaces :" , len(enlaces))
sitio.close()

for enlace in enlaces[:10]:
    peticion = request.urlopen(enlace)

    print(enlace , "--> status", peticion.code)


print("\n :::::::::::::::: encontrar archivos en sistema operativo ::::::::::::::::. \n")

for archivo in os.listdir('/home/juan/PycharmProjects/2-py/venv'):
    if ( archivo.endswith(".txt")):
        print("encontrado", os.path.join('/home/juan/PycharmProjects/2-py/venv',archivo))


print("\n :::::::::::::::: favicon ::::::::::::::::. \n")

url3 = "http://python.org"
sitio = request.urlopen(url3)

sou = BeautifulSoup(sitio,"html.parser")

icono_enlace = sou.find('link',rel='icon')
print(icono_enlace)
link = url3+"/"+icono_enlace['href']
icono = request.urlopen(link)


with open("test.ico","wb") as ico :
    try:
        ico.write(icono.read())
        print("hecho")
    except:
        print("ERRORR")
sitio.close()

print("\n :::::::::::::::: google analytics ::::::::::::::::. \n")
url3 = "http://python.org"
sitio = request.urlopen(url3)

sou = BeautifulSoup(sitio,"html.parser")
if( sou.findAll(text=re.compile("google-analytics"))):
    print("tiene google analytics")
else :
    print("NO tiene google analytics")
sitio.close()


print("\n :::::::::::::::: IDIOMA::::::::::::::::. \n")
url3 = "http://python.org"
sitio = request.urlopen(url3)

sou = BeautifulSoup(sitio,"html.parser")
idioma = sou.find("html")['lang']
print(idioma)

sitio.close()

print("\n :::::::::::::::: charset ::::::::::::::::. \n")
url3 = "http://python.org"
sitio = request.urlopen(url3)

sou = BeautifulSoup(sitio,"html.parser")
caracteres = sou.find("meta")['charset']
print(caracteres)

info = sitio.info()

print(info)

sitio.close()


print("\n :::::::::::::::: viewport ::::::::::::::::. \n")
url3 = "http://python.org"
sitio = request.urlopen(url3)

sou = BeautifulSoup(sitio,"html.parser")
META =  sou.find('meta',attrs={'name': 'viewport'})
print("VIEWPORT", META.get("content"))