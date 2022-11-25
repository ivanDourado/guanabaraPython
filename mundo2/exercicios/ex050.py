s = 0
cont = 0 # conador geral
contP = 0#contador de pares
for c in range(0,6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 ==0:
        s += n
        contP += 1
    cont += 1
print(f'O somatório dos {contP} n° pares dentre os {cont} informados é de {s}! ')