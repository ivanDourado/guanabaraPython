preco = float(input('Digite o valor do produto: R$'))
print('''
        Opções de pagamento: 
        [1] - À Vista no dinheiro/cheque com 10% de desconto.
        [2] - À vista no cartão com 5% de desconto.
        [3] - Em até 2x no cartão, preço normal.
        [4] - 3x ou mais no cartão com 20% de juros.
''')
pagamento = int(input('Digite o número correspondente a forma de pagamento: '))
parcelas = int(input('Quantas parcelas?'))

formas = {1:'À vista no dinheiro.', 2:'À vista no cartão.', 3:'Em até 2x no cartão, preço normal.',  4:'3x ou mais no cartão. 20% de juros.'}

if pagamento == 1:
    preco -= preco * 0.1
    print(f'Pagamento {formas[pagamento]} de R${preco}. Terá 10% de desconto, ficando {preco:.2f}')
elif pagamento == 2: 
    preco -= preco * 0.05
    print(f'Pagamento {formas[pagamento]} de R${preco}. Terá 5% de desconto, ficando {preco:.2f}')
elif pagamento == 3 and parcelas <= 2: 
    print(f'Pagamento {formas[pagamento]} Ficando por {parcelas}x de {preco/parcelas}')
elif pagamento == 4 and parcelas >= 3: 
    preco *= 1.2
    print(f'Pagamento {formas[pagamento]} Total de R${preco} com {parcelas}x de {preco/parcelas:.2f}')
else:
    print('Opção de pagamento e/ou número de parcelas inválidas.')






