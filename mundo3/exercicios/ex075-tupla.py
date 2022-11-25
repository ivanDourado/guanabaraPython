from statistics import mode


n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = (n1, n2, n3, n4)
moda = mode(tupla)

print(f'Vc digitou os valores {tupla}')
print(f'O valor mais exibido foi o {moda}, exibido {tupla.count(moda)} vezes')

if 9 in tupla:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
else:
    print('O valor 9 não foi digitado')

if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado')

print(f'O valor {n2} aparece na {tupla.index(n2) + 1}ª posição.')

print(f'Os valores pares digitados foram ',end='')
cont = 0
par = 0
for numero in tupla:
    if numero % 2 == 0:
        par = numero
        print(f'{par} ',end='')
