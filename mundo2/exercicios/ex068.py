#par ou impar
from random import randint
vitorias = 0
while True:
    print('-='*20)
    print('Vamos Jogar Par ou Ímpar!')
    print('-='*20)
    resultado = 0
    jogada_pc = randint(1,11)
    jogada_usuario = int(input('Digite um valor: '))
    soma = jogada_pc + jogada_usuario
    aposta = ' '
    while aposta not in 'PI':
        aposta = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    descricao_resultado = 0
    if soma % 2 == 0:
        resultado = 'P'
        descricao_resultado = 'PAR'
    else:
        resultado = 'I'
        descricao_resultado = 'ÍMPAR'
    print(f'Você jogou {jogada_usuario} e a máquina {jogada_pc}.\nO total de {soma} deu {descricao_resultado}')
    if resultado == aposta:
        print('Você venceu!\nVamos jogar novamente...')
        print('-='*20)
        vitorias +=1
        continue
    if resultado != aposta:
        print('Você Perdeu!')
        print('-='*20)
        print(f'Game Over! Você venceu {vitorias} vezes.')
        break
print('-='*20)