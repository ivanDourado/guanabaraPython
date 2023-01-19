import traitlets


def metade(p=0, format=False):
    res = p/2
    return res if not format else moeda(res)


def dobro(p=0, format=False):
    res=p*2
    return res if not format else moeda(res) 


def aumentar(p=0, t=0, format=False):
    res=p * (1+t/100)
    return res if not format else moeda(res) 


def diminuir(p=0, t=0, format=False):
    res=p - p*t/100
    return res if not format else moeda(res) 


def moeda(p=0, moeda='R$', format=False):
    return f'{moeda}{p:>.2f}'.replace('.', ',')

def resumo(p=0, a=0 , r=0):
    titulo = 'RESUMO DO VALOR'
    print('--'*20)
    print(titulo.center(40))
    print('--'*20)
    print(f'Preço analisado: \t', f'{moeda(p)}')
    print(f'Dobro do Preço: \t', f'{dobro(p, True)}')
    print(f'Metade do Preço: \t', f'{metade(p, True)}')
    print(f'Aumento de {a}%: \t', f'{aumentar(p, a, True)}')
    print(f'Redução de {r}%: \t', f'{diminuir(p, r, True)}')
    print('--'*20)    


#resumo(2,100,50)
