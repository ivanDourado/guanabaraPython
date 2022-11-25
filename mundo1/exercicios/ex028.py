import random
from time import sleep
print('-=-' * 20)
n = int(input('Em que número eu pensei de 0 a 5? '))
print('-=-' * 20)

nm = random.randint(0 ,5)

print('PROCESSANDO...')
sleep(3)

if (n == nm):
    print(f'PARABÉNS! Você conseguiu me vencer, pensei {n} mesmo!')
else:
    print(f'Não foi dessa vez! Eu pensei {nm} e não {n}')