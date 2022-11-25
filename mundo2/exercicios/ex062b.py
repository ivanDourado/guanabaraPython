print(f'Gerador de PA')
print('=-' * 20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while contador <= total:
        print(f'{termo} -> ',end='')
        termo += razao
        contador +=1
    print('PAUSA')
    mais = int(input('Quantos termos desejas adicionar? '))
print(f'Prograssão finalizada com {total} termos mostrados')