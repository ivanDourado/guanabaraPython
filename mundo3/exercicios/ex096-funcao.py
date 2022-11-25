print('Controle de terrenos')
print('=='*15)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

def area(l,c):
    a = l * c
    print(f'A área do terreno é {a} m².')

area(l, c)