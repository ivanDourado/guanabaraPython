sexo = str(input('Digite seu sexo biológico [M/F]: ')).upper()

while sexo != 'M' and sexo != 'F':
    print('Digite um valor válido')
    break
if sexo == 'M':
    print('Masculino')
elif sexo == 'F':
    print('Feminino')
