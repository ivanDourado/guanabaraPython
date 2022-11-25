maiores = homens = meninas_menor_20 = 0
while True:
    print('--'*20)
    print('CADASTRE UMA PESSOA')
    print('--'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]    
    print('--'*20)
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if idade <= 20 and sexo == 'F':
        meninas_menor_20 += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continua == 'N':
        break
print('--'*20)
print(f'''O total de pessoas com mais de 18 anos: {maiores}\nAo todo temos {homens} homem(s) cadastrados \nE temos {meninas_menor_20} mulher(es) com menos de 20 anos''')
#print(f'Maiores: {maiores}; homens: {homens}; meninas<20: {meninas_menor_20}. ')    