num = int(input('Digite um numero inteiro: '))
print('''
        Escolha uma das bases para conversão:
        [1] - Converter para BINÁRIO
        [2] - Converter para OCTAL
        [3] - Converter para HEXADECIMAL
''')
conversao = {1:'Binário', 2:'Octal', 3:'Hexadecimal'}
opcao = int(input('Sua opção: '))

if opcao == 1 :
    print(f'{num} convertido para {conversao[1]} é igual a {bin(num)[2:]}')#[2:] é fatiamento de string. Usa-se a partir do 2° índice em diante.
elif opcao == 2 :
    print(f'{num} convertido para {conversao[2]} é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para {conversao[3]} é igual a {hex(num)[2:]}')
else: 
    print(f'Opção {opcao} é inválida. Digite uma válida.')
