from random import randint
palpite = int(input('Digite seu palpite entre 0 e 10: '))
jogadaPc = randint(0,10)
contador = vitorias = derrotas = 0
while palpite <= 10:
    while palpite != jogadaPc:
        print(f'Não foi dessa vez, tente novamente! A máquina jogou {jogadaPc}, e você {palpite}.')
        contador += 1
        derrotas += 1
        palpite = int(input('Digite seu palpite entre 0 e 10: '))
        jogadaPc = randint(0,10)        
    vitorias += 1
    print(f'Parabéns! seu palpite foi {palpite} igual ao da máquina, {jogadaPc}. Foram {contador + 1} palpites para vencer. Você venceu {vitorias} vezes contra {derrotas} da máquina!')
    break
if palpite > 10:
    print(f'Valor inválido. Digite um número entre 0 e 10!')



