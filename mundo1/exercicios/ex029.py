from time import sleep

print('-=-' * 20)
radar = float(input('Digite a velocidade do seu carro: '))

print('PROCESSANDO...')
sleep(2)
print('-=-' * 20)
if radar <= 80.0:
    print('Velocidade legal, dirija com segurança!')
else:
    multa = (radar - 80.0) * 7
    print('Velocidade acima da permitida em {}. Sua multa é de R${}.'.format(radar - 80, multa))