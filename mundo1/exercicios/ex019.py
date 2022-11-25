import random

alunos = ['Jaiana', 'Ivan', 'Juca', 'Soco']

rand = random.randint(0, 3)
'''rand = random.choice(alunos)# choice escolha aleatoria dentro do array'''
print(alunos[rand])