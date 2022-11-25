l = float(input('Digite a largura em metros da parede: '))
h = float(input('digite a altura em metros da parede: '))
area = l * h 
rendimentoTintaM2porLitro = 2
tintaUsada = area * (1/rendimentoTintaM2porLitro)

print(f'{tintaUsada} L')
