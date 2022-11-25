from random import randint
from time import sleep

print('''
            Digite o número correspondente a sua escolha:
            [1] - Pedra
            [2] - Papel
            [3] - Tesoura
''')
escolhaUsuario = int(input('Digite o número correspondente à sua escolha: '))
escolhaPc = randint(1,3)
jogada = {1:'Pedra', 2:'Papel', 3:'Tesoura'}

print('JO')
sleep(.5)
print('KEN')
sleep(.5)
print('PO!!!')

if escolhaUsuario == escolhaPc:
    print(f'Empate! Ambos escolheram {jogada[escolhaPc]}')
else:
    if escolhaUsuario == 1 and escolhaPc ==2:
        print('-='*20)
        print(f'Máquina ganhou! {jogada[escolhaPc]} ganha de {jogada[escolhaUsuario]}!')
        print('-='*20)
    elif escolhaUsuario == 1 and escolhaPc == 3:
        print('-='*20)
        print(f'Você ganhou! {jogada[escolhaUsuario]} ganha de {jogada[escolhaPc]}!')
        print('-='*20)
    elif escolhaUsuario == 2 and escolhaPc == 1: 
        print('-='*20)
        print(f'Você ganhou! {jogada[escolhaUsuario]} ganha de {jogada[escolhaPc]}!')
        print('-='*20)
    elif escolhaUsuario == 2 and escolhaPc == 3: 
        print('-='*20)
        print(f'Máquina ganhou! {jogada[escolhaPc]} ganha de {jogada[escolhaUsuario]}!')
        print('-='*20)
    elif escolhaUsuario == 3 and escolhaPc == 1:
         print('-='*20)
         print(f'Máquina ganhou! {jogada[escolhaPc]} ganha de {jogada[escolhaUsuario]}!')
         print('-='*20)
    elif escolhaUsuario == 3 and escolhaPc == 2:
        print('-='*20)
        print(f'Você ganhou! {jogada[escolhaUsuario]} ganha de {jogada[escolhaPc]}!')
        print('-='*20)

    




print(escolhaPc) 
