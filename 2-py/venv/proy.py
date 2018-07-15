import urllib.request as request
# VERIFICAR HTTPS

req = request.Request('http://python.org')
resultado = request.urlopen(req)

print(resultado.geturl())


