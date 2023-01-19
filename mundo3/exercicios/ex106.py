from time import sleep

c = (   '\033[m',        # 0 - sem cores
        '\033[31m',      # 1 vermelho
        '\033[32m'       # 2 - verde
        '\033[33m',      # 3 - amarelo
        '\033[34m',      # 4 - azul 
        '\033[0;30;45m', # 5 - roxo
        '\033[7;30m'     # 6 - branco 
    )
          

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\' ', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)
    print(c[0], end ='')
    sleep(.3)

comando = ''
while True: 
    titulo('Sistema de Ajuda PyHELP', 2 )
    comando = input('Função ou biblioteca > ')
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
