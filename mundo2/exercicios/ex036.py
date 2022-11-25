valorCasa = float(input('Digite o valor da casa: R$'))
valorSalario = float(input('Digite o seu salário: R$'))
prazo = int(input('Em quantos anos pretende pagar o imóvel? '))

prestacao = valorCasa / (prazo * 12)

if prestacao > valorSalario * .3:
    print(f'Emprestimo negado, a prestação de R${prestacao:.2f} excede o valor de {valorSalario*.3:.2f}')
else:
    print(f'Empréstimo aprovado!')
