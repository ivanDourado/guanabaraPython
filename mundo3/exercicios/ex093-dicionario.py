jogador = dict()
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = list()
    for c in range(0,jogador['partidas']):
        jogador['gols'].append(int(input(f'Quantos gols {jogador["nome"]} marcou na partida {c+1}? ')))
    jogador['total'] = sum(jogador['gols'])
    break
print('-='*20)
print(jogador)
print('-='*20)
print(jogador.items())
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*25)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas. ')
for i,v in enumerate(jogador['gols']):
    print(f'==> Na partida {i+1}, {jogador["nome"]} fez {jogador["gols"][i]} gols. ')
print(f'Foi um total de {jogador["total"]} gols.')
