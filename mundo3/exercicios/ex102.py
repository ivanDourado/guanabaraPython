from time import sleep

def fatorial(num=1, show=False):
    """ 
    -> Calcula o fatorial de um número;
    :param n: O numero a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return> O valor d fatorial de um numero n.
    """
    f = 1
    for c in range(num,0,-1):
        f *=c
    if show == False:
        return f
    else:
        c=num
        while c > 0:
            print(f'{c} ',end='',flush=True)
            print(f' x ' if c > 1 else ' = ', end='')
            sleep(.3)
            c -= 1
        return f' = {f}'

print(f'{fatorial(6, True)}')
print(f'{fatorial(6, False)}')
help(fatorial)
            

            