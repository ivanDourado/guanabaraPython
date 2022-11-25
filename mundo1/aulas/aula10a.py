'''nome = str(input('Digite o seu nome: '))
if nome == 'Ivan':
    print('Belíssimo nome!')
print(f'Bem-vindo, {nome}!')'''
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2

print(f'A sua média foi de {m:.1f} pontos')
'''if m >= 6.0:
    print('Sua média foi boa!')
else:
    print('Deu mole! Melhore na próxima.')
'''
print('Sua média foi boa!' if m>= 6 else 'Deu mole! Melhore na próxima.')