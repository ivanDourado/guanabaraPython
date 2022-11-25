


from math import floor


carteiraBrl = float(input('Digite quanto você tem: '))
cotacaoUsd = 3.27
compraUsd = floor(carteiraBrl / cotacaoUsd)

print(f'Com o valor de R${carteiraBrl}\n é possivel adquirir US${compraUsd} \n na cotacao do dolar de R${cotacaoUsd}!')
