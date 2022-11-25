cont = soma = num = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont+=1
print(f'Foram exibidos {cont} números, e o somatório destes foi de {soma}. ')

