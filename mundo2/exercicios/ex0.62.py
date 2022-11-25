print('Gerador de PA')
print('-='*20)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 1
a = n1
total = 0
mais = 10
print(f'{n1} -> ', end='')
while mais != 0:
    total += mais
    while c < total:
        a += r
        print(f'{a} -> ', end='' )
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos você que a mais? '))
print(f'FIM! Foram {total} termos exibidos na PA')
