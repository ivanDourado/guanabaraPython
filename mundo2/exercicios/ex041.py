from datetime import date

anoNasc = int(input('Digite o seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNasc

if idade <= 9:
    print(f'''O atleta tem {idade}. Sua categoria é a mirim!''')
elif idade > 9 and idade <= 14:
    print(f'O atleta tem {idade}. Sua categoria é a infantil!')
elif idade > 14 and idade < 20:
    print(f'O atleta tem {idade}. Sua categoria é Sênior')
else :
    print(f'O atleta tem {idade}. Sua categoria é Master')