from math import hypot
co = float(input('Digite o comprimento do Cateto oposto em cm: '))
ca= float(input('Digite o comprimento do cateto adjacente em cm: '))
hip = hypot(co, ca)

print(f'A hipotenusa vale {hip} cm')