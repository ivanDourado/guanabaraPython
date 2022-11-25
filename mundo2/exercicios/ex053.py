#palíndromo
frase = str(input('Digite uma frase:')).strip().upper() #retirei os espaços, e transformei-a em maiúscula
palavras = frase.split() # separo cada palavra em uma lista de palavras
junto = ''.join(palavras) #junto todas as palavras com um '' (vazio), deixando-as coladas. Eliminando os espaços internos
inverso = junto[::-1] # forma para resolver sem o for| ::-1 (:começa do inicio, :termina no fim, -1 de trás para frente)

#inverso = ''
# | numero de letras - 1 = indice total 0 a frase.length -1 || -1 pois desconsidera o ultimo numero [2, 1 , 0, '( n conta )-1']|| -1 regressivo, volta 1 letra
'''for letra in range(len(junto) - 1, -1, -1): # inverso da frase
    inverso += junto[letra] # add o inverso na variavel inverso'''


if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
print(junto, inverso)
#print(f'Voce digitou {frase}\n {palavras}\n{junto}')
