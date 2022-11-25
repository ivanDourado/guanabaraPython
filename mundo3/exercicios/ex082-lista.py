lista = []
pares = list()
impares = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    continua = str(input('Quer continuar? [S/N]  '))    
    if continua in 'nN':
        break
print('-='*25)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')