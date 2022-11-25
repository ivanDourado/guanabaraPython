n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n10 = n1 + (10 - 1) * r # fórmula do décimo termo da PA

for c in range(n1, n10 + r, r):
    print(c)
print(f'Razão é {r}', end=' ->')
print('FIM')