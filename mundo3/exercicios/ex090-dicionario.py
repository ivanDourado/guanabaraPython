aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
aluno['situação'] = str(input('Situação: '))

#['nome':'Felipe', 'media':9, 'situação':'aprovado']
print(f'O nome é {aluno["nome"]}')
print(f'Média = {aluno["media"]}')
print(f'Situação = {aluno["situação"]}')