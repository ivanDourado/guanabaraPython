import ex107moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {ex107moeda.metade(p):.2f}')
print(f'O dobro de {p} é {ex107moeda.dobro(p):.2f}')
print(f'Aumentando 10% temos {ex107moeda.aumentar(p, 10):.2f}')
print(f'Reduzindo 13% temos {ex107moeda.diminuir(p, 13):.2f}')