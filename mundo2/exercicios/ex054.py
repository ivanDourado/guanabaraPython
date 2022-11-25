#maioridade e menoridade
from datetime import date

anoAtual = date.today().year
tot_maior = 0
tot_menor = 0
for pessoa in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {pessoa}ª pessoa: '))
    idade = anoAtual - nasc

    print(f'Essa pessoa tem {idade} anos')
    if idade >= 21:
        tot_maior += 1
        print('Essa pessoa é maior')
    else:
        tot_menor += 1
        print('Essa pessoa é menor')
print(f'Há {tot_maior} pessoas maiores e {tot_menor} pessoas menores!')