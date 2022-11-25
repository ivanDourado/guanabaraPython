num = int(input('Digite um numero para \ncalcular o seu fatorial: '))
c = num 
f = 1
print(f'{num}! =', end=' ')
while c > 0:
    print(f' {c} ', end='')
    print(f'x' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
print('\nFIM!')

'''from math import factorial
num = int(input('Digite um numero para \ncalcular o seu fatorial: '))
f = factorial(num)
print(f'O fatorial de {num} é {f}')'''