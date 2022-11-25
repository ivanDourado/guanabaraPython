#tabuada de vários nº/cada /inserção do usuário.
#flag = nº negativo

""" num = int(input('Quer ver a taboada de qual valor? '))
cont = 0
while cont <= 10:
    if num < 0:
        break
    print(f'{num} x {cont} = {num*cont}')
    cont += 1
print('fim') """
while True:
    num = int(input('Quer ver a taboada de qual valor? '))
    cont = 0
    if num < 0:
        break
    while cont <= 10:
        print(f'{num} x {cont} = {num*cont}')
        cont += 1
print('Fim da taboada')




