novo_num = cont = soma = 0
novo_num  = int(input('Digite um número [999 para parar]: '))
while novo_num != 999:
    soma += novo_num
    cont += 1
    novo_num = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} e a soma entre eles, sem contar o flag [999], foi de {soma}. ')
