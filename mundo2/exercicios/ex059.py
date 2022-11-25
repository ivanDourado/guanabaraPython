v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo Valor: '))
print(''' 
        [1] - Somar 
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos números
        [5] - Sair do programa
''')
opcao = int(input('>>>> Qual é a tua opção? '))

while opcao > 5 or opcao < 1:
    print('Digite um número válido correspondente as opções listadas! ')
    opcao = int(input('>>>> Qual é a tua opção? '))
while opcao >= 1 and opcao <=5:
    maior = v1 
    if opcao == 1:
        print(f'A soma entre {v1} + {v2} é {v1 + v2}')
        break
    if opcao == 2:
        print(f'A multiplicação entre {v1} * {v2} é {v1 * v2}')
        break
    if opcao == 3:
        if v1 == v2:
            print('Os valores são iguais!')
            break
        else:
            if v1 > v2:                
                print(f'{maior} é o maior valor')
                break
            else:
                maior = v2
                print(f'{maior} é o maior valor')
                break
    if opcao == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo Valor: '))
        print(''' 
        [1] - Somar 
        [2] - Multiplicar
        [3] - Maior
        [4] - Novos números
        [5] - Sair do programa
        ''')
        opcao = int(input('>>>> Qual é a tua opção? '))
    if opcao == 5:
        print('Programa encerrado.')
        break




