continua = 'S'
soma = media = cont = maior = menor = 0
while continua in 'sS':
    num = int(input('digite um numero: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    continua = str(input('Deseja contnuar? [S/N] ')).upper().strip()[0]
media = soma / cont
print(f'Você digitou {cont} numeros e a média foi {media}.\nO maior valor foi de {maior} e o menor foi {menor}.')