 #verifica se site está acessível pelo pc usado
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site pudim não está acessível no momento!\033[m')
else:
    print('Acesso realizado com sucesso!')
    # print(site.read()) # lê código do site (curiosidade)