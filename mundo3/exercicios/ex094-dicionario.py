from itertools import count
from operator import itemgetter
from statistics import mean


#ler: nome, sexo, idade; guardalos num dicionário; guardar tds os dict numa list
#a) qnts pessoas foram cadastradas ; b) a média de idade do grupo; c) uma lista com tds as mulheres; d)uma lista com todas as pesoas com idade acima da média

dados = list()
pessoa = dict()
idade_acima_media = list()
idades = list()
mulheres = list()
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while pessoa['sexo'] not in 'mMfF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    pessoa['idade'] = int(input('Idade: '))
    idades.append(pessoa['idade'])
    resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    while resp not in 'sSnN':
        print('ERRO! Por favor, responda apenas apenas S ou N.')
        resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
    dados.append(pessoa.copy())
    if resp in 'Nn':
        break
print('-='*30)

print(dados)
print(pessoa)
print(idades)
print(f'A) Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'B) A média de idade é de {mean(idades)} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in dados:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]} ', end='')
print()

print(f'D) A lista das pessoas que estão acima da média: ')
for p in dados:
    if p["idade"] >= mean(idades):
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')

print(f'')