from random import randint, shuffle

alunos = ['Ivan', 'Jaiana', 'Juca', 'Soco'] 
ordem = [True, False]

rand = randint(0,1)

alunos.sort(reverse=ordem[rand]) # ordem alfabetica crescente ou decrescente
# shuffle(alunos) # aleatório

print(alunos)

