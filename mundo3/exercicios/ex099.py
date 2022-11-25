from time import sleep

#lista = [5,4,27,8,4,9,55,10,25]
def maior(* num):
    print('-='*25)
    print('\nAnalisando os valores passados...')
    cont = maior = 0
    for v in num:
        print(f'{v} ', end='', flush=True)
        sleep(.4)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor dentre os {cont} é {maior}!')

maior()
maior(5,4,27,8,4,9,55,10,25)
maior(5,9,7)

