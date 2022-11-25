from operator import itemgetter
from random import randint
from time import sleep

jogo = {#abre dicionário
    'jogador1': randint(1,6),
    'jogador2': randint(1,6),
    'jogador3': randint(1,6),
    'jogador4': randint(1,6)
} #fecha dicionário
ranking = list() # mas pode ser dict() pois mesmo assim retornará lista; usa-se list para usarmos enumerate()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
print('== Ranking dos Jogadores ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(.9)


""" jogador = dict()
#jogador['jogada'] = randint(0,6)
print(jogador)
print('Valores sorteados: ')

for j in range(1,5):
    jogada = randint(1,6)
    print(f'        O jogador{j} tirou {}')
    sleep(1)
print('-=-='*20)
print('== Ranking dos jogadores ==')
 """
