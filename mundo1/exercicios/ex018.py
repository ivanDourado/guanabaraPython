import math
ang = float(input('Digite o valor do ângulo desejado: '))
cosang = math.cos(math.radians(ang))
sinang = math.sin(math.radians(ang))
tanang = math.tan(math.radians(ang))

print(f'Para o valor de {ang}, temos cosseno de {cosang:.2f} \ne seno de {sinang:.2f} \ne tangente de {tanang:.2f}!')
