#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.


import urllib.request #Biblioteca que checa o site

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError: #urllib.error.URLError é o nome do erro
#    Caso dê erro
    print('O site não está disponível.')
else:
#   Caso não dê erro
    print('O site está disponível.')
#   print(site.read()) #Mostra o html do site