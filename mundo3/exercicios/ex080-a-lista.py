#usuario digita 5 valores num; cadastra-os numa lista e sua devida posição (sem usar .sort() );; ao fim, mostra lista ordenada na tela
lista = []
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao fim da lista... ') 
    else:
        position = 0
        while position < len(lista):
            lista.insert(position, num)
            print(f'Adicionado na posição {position}')
            break
print('-='*25)
print(f'Os valores digitados em ordem foram {lista}')

