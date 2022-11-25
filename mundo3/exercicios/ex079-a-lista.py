lista = []
while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor add com sucesso...')
    else:
        print('Valor Duplicado! Não será adicionado.')
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua in 'nN':
        break
print('=-'*25)
lista.sort()
print(f'Você digitoou os valores {lista}')