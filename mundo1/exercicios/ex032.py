from time import sleep
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
print('PROCESSANDO...')
sleep(1.8)
if ano == 0:
    ano = date.today().year # ano = biblioteca date . metodo today() . year (ano) # buscar o ano atual
print('-=-' * 20)
print(f'O ano {ano} é bissexto!' if ano % 4 == 0 and (ano % 100 != 0) or ano % 400 == 0 else f'O ano {ano} não é bissexto!')

'''print('PROCESSANDO...')  #forma extensa
#sleep(1.8)
print('-=-' * 20)
if ano == 0:
    ano = date.today().year # ano = biblioteca date . metodo today() . year (ano) # buscar o ano atual
if ano % 4 == 0 and (ano % 100 != 0) or ano % 400 == 0:
   print(f'O ano {ano} é bissexto!' )
else:
     print(f'O ano {ano} não é bissexto!')'''
