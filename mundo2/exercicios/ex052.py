num_p = int(input('Digite um número: '))
cont_tot = 0
#soma = 0
for c in range(1, num_p + 1):
    if num_p % c == 0:
        print('\033[33m', end='')
        cont_tot += 1
        
    else:
        print('\033[31m', end='')
    print(f'{c} ', end='')
print(f'\033[m O numero {num_p} foi divisível {cont_tot} vezes')
if cont_tot == 2:    
    print(f'O num {num_p} é primo')
else:
    print(f'O num {num_p} não é primo!')
#print(f'Soma dos numeros primos anteriores é {soma}')

