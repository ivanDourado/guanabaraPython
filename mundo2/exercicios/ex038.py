
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

menor = n1

if n2 < n1 :
    menor = n2
    print(f'{n2} é menor que {n1}')

maior = n1 

if n2 > n1:
    maior = n2
    print(f'{n2} é maior que {n1}')
elif n1 == n2:
    print('Ambos são iguais!')
