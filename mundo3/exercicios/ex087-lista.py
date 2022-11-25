matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = []
col_2 = []
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite o valor em [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares.append(matriz[linha][coluna])        
print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {sum(pares)}.')
for linha in range(0,3):
    for coluna in range(0,3):
        if coluna == 2:
            col_2.append(matriz[linha][coluna])
print(f'A soma dos valores da 3ª coluna é {sum(col_2)}.')
print(f'O maior valor da 2ª linha é {max(matriz[1])}.') 