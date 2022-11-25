lista = []
continua = 'S'
cont = 0
while continua not in 'nN':
    num = int(input('Digite um valor: '))
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    lista.append(num)
    cont += 1
lista.sort(reverse=True)
print('-='*25)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 foi encontrado na lista! ')
else:
    print('O valor 5 não foi encontrado na lista! ')


