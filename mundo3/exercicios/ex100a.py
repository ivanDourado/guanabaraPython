from random import randint # importa randint da biblioteca random
from time import sleep # importa o método sleep da biblioteca time

numeros = list() # cria-se lista numeros

def sorteia(lista): # cria-se função sorteia que receberá uma lista como parametro
    print('Sorteando 5 Números da lista: ',end='') # printa o que a função executará
    for cont in range(0,5): # realizaremos 5 iterações ( de 0 a 4)
        n = randint(0,10) # n recebe um numero aleatório entre 0 e 10
        numeros.append(n) # n é adicionado ao final da lista números
        print(f'{n} ',end='', flush=True) # Respectivamente: imprimimos o n, evitamos a quebra de linha, e habilitamos que se imprima cada ítem por vez no intervalo delimitado abaixo
        sleep(.3) # a cada 0.3 segundos será impresso no console o n
    print('\nPRONTO!') # printa para indicar o fim da funçao

def somaPar(lista): # cria-se função SomaPar que receberá uma lista como parametro
    soma = 0 # inicializa variavel soma com 0
    c = 0 # inicializa variavel c com 0 (contar os pares)
    for valor in lista: # para cada valor na lista
        if valor % 2 == 0: # se o valor for par (divisão por 2 dê resto 0)
            soma += valor # variavel soma é acrescida do novo valor par 
            c += 1 # var c é acrescida em 1
    print(f'Somando os {c} valores pares de {lista} temos {soma}') # imprimi-se o nº de valores pares, a sua lista completa, e a soma de seus valores


sorteia(numeros) # chama a função sorteia com a lista numeros como parametro
somaPar(numeros) # chama a função somaPar com a lista numeros como parametro