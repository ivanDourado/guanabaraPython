ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'nN':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('--' * 15)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
print('--'*25)
while True:
    opc = int(input('Coloque o número do aluno que deseja ver as notas (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    else:
        print(f'As notas de {ficha[opc][0]} foram {ficha[opc][1]} .')
print('>>> Volte Sempre <<<')