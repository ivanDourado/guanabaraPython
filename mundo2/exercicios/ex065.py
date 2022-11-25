soma = media = maior = menor = cont = 0
continua = 'S'
while continua == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1    
    if cont == 1:
        maior = menor = num
    else:
        if maior > num:
            maior = num
        elif menor < num:
            menor = num
    continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]# maiuscula; retira espaço; acc 1ª letra
media = soma / cont
print(f'Você digitou {cont} números e a média foi de {media}.\nO maior numero foi {maior} e o menor foi {menor}.')


