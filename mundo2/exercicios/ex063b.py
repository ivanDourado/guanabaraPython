print('--'*20)
print('Sequência de Fibonacci')
print('--'*20)
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = t2 + t1
cont = 3
print('~~'*20)
while cont <= num:
    t3 = t2 + t1
    print(f'{t3} -> ',end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM!')
print('~~'*20)
