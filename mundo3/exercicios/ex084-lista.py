temporaria = []
principal = []
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    temporaria.append(nome)
    temporaria.append(peso)
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        elif temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    
    continua = str(input('Quer continuar? [S/N]  ')).upper().strip()[0]
    if continua in 'nN':
        break
            
print('-='*30)
print(f'Ao todo vc cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor}. Peso de', end=' ')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')
#lista.index(elemento)