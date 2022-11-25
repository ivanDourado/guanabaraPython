from time import sleep

print('-=-' * 20)
num = int(input('Digite um numero: '))
print('PROSSESSANDO...')
sleep(2)
print('-=-' * 20)
print(f'O numero {num} é PAR!' if num % 2 == 0 else f'O numero {num} é ímpar!')
print('-=-' * 20)
