sal = float(input('Digite o seu salário: R$'))


if sal <= 1250:
    sal *= 1.15
else:
    sal *= 1.1

print(f'O novo salário reajustado será de R${sal:.2f} !')
    