from random import randint


numeros = list()
num_par = list()
def sorteia():
    for c in range(0,5):
        numeros.append(randint(0,10))
    print(numeros)    

sorteia()

def somaPar():
    for v in numeros:
        if v % 2 == 0:
            num_par.append(v)
    print(f'Dentre os valores sorteados, são pares os números {num_par}.')
    print(f'A soma entre os {len(num_par)} valores pares é {sum(num_par)}')

somaPar()
 