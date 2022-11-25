print('Gerador de PA')
print('-='*20)
n1 = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = n1
contador = 1
total = 0
mais =10
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} -> ',end='')
        termo += razao
        contador+=1
    print('PAUSA')
    mais = int(input('Quantos termos deseja adicionar? '))
print(f'Progressão finalizada com {total} termos exibidos.')