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