import urllib.request as request
import os
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