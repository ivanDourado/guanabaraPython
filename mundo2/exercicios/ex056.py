media = 0
soma_idade = 0
maiorIdadeHomem = 0
NomeHomemVelho = ''
total_donzelas = 0
for pessoa in range(1, 5):
    print('-'*5,f'{pessoa}ª PESSOA', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        NomeHomemVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        NomeHomemVelho = nome
    if sexo in 'Ff' and idade < 20:
        total_donzelas += 1 
media = soma_idade / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maiorIdadeHomem} anos, seu nome é {NomeHomemVelho}')
print(f'Há {total_donzelas} moças com idade inferior a 20 anos')

