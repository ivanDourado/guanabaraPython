from time import sleep

#com for
""" def contador(i,f,p):
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if p > 0:
        for c in range(i,f+1,p):
            print(f'{c} ', end='')
            sleep(.3)
        print('FIM!')
        print('-='*25)
        sleep(.3)
    else:
        for c in range(i,f-1,p):
            print(f'{c} ', end='')
            sleep(.3)
        print('FIM!')
        print('-='*25)
        sleep(.3) """
# com while 
def contador(i,f,p):
    print('-='*20)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(.5)
            cont -= p
        print('Fim!')
    print('-='*20)

            

# de 1 a 10 de 1 em 1

contador(0,100,10)
contador(10,0,2)
print('-='*20)
print(f'Agora é a sua vez de personalizar a cantagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)

