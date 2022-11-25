from datetime import date
worker = dict()
ctps = ' '
ano_atual = date.today().year
while ctps != 0:
    worker['nome'] = str(input('Nome: '))
    worker['idade'] = ano_atual - (int(input('Ano de Nascimento: ')))
    worker['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
    if worker['ctps'] == 0:
        break
    worker['contratação'] = (int(input('Ano de contratação: ')))
    worker['salário'] = float(input('Salário: R$'))
    worker['aposentadoria'] = worker['idade'] + ((worker['contratação'] + 35) - ano_atual)
    break
print('-=' *25)
print(worker.items())
for i ,v in worker.items():
    print(f'- {i} tem o valor de {v}')

# nome, anonasc/idade , ctps , anocontrat, salario
# ctps =! 0 , mostra ano e contratação, else mostra nada
#idade de aposentadoria, pos 35 anos de colaboraçao