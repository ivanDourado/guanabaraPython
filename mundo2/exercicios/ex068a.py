from random import randint
vitorias = 0
while True:
    jogada_usuario = int(input('Digite um valor: '))
    jogada_pc = randint(0,10)
    aposta = ' '
    while aposta not in 'PIÍ':
        aposta = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    soma = jogada_usuario + jogada_pc
    print(f'Vc jogou {jogada_usuario} e o PC {jogada_pc}. Total: {soma}')
    print('Deu PAR!' if soma % 2 == 0 else 'Deu Ímpar!')
    if aposta == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            print('-='*15)
            vitorias += 1
        else:
            print('Você perdeu!')
            print('-='*15)            
            break
    elif aposta in 'IÍ':
        if soma % 2 == 1:
            print('Você venceu!')
            print('-='*15)
            vitorias += 1
        else:
            print('Você perdeu!')
            print('-='*15)
            break    
    print('Vamos jogar novamente...')
print(f'GAME OVER! VC venceu {vitorias} vezes.')
            


