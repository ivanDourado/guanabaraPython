#usuario digita 5 valores num; cadastra-os numa lista e sua devida posição (sem usar .sort() );; ao fim, mostra lista ordenada na tela
lista = []
for cont in range(0,5):
    num = int(input('Digite um valor: '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionafo ao final de lista... ')
    else:
        posicao = 0
        while posicao < len(lista):
            if num <= lista[posicao]:
                lista.insert(posicao ,num)
                print(f'Adicionado na posição {posicao} da lista... ')
                break
            posicao += 1
print('-='*25)
print(f'Os valores digitados em ordem foram {lista}')



""" print(lista.index(num) )# indice do elemento
 """
#print(lista)
#lista().index()
# lista.index(num, min(lista), max(lista)) # indice do elemento