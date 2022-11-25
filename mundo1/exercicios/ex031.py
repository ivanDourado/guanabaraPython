from time import sleep


distancia = float(input('Digite a distância da sua viagem em quilometros: '))
print('PROCESSANDO...')
sleep(1.8)
print(f'Você está prestes a começar uma viagem de {distancia} km.')
sleep(1.3)
print('-=-' * 20)
print(f'O preço da sua passagem será de R${distancia*0.5:.2f}' if distancia <= 200 else f'O preço da sua passagem será de R${distancia*0.45:.2f}' )
print('-=-' * 20)
