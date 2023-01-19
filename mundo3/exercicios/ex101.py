from datetime import date

ano_atual = date.today().year
anoNasc = int(input('Digite o ano de seu nascimento: '))
idade = ano_atual - anoNasc

def voto(anoNasc):
    if idade < 16:
        return f'Com {idade} anos: Voto NEGADO!'
    elif idade >= 16 and idade < 18:
        return f'Com {idade} anos: Voto OPCIONAL!'
    elif idade >= 18:
        return f'Com {idade} anos: Voto OBRIGATÓRIO! '

print(f'{voto(anoNasc)}')