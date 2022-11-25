s = 0
# c % 3 ==0
cont = 0
contT = 0
for c in range(1, 500):
    if c % 3 == 0 and c % 2 != 0:# se c é multiplo de 3 e se c é ímpar
        s += c
        cont += 1
    contT += 1
    
print(f'Dentre os {contT} numeros,\n o somatório dos {cont} números ímpares múltiplos de 3 no intervalo entre 1 e 500 é de {s}!')
