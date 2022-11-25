#Variáveis compostas = dicionários
# dicionários são, de certa forma, como listas, só que seus idíces ao invés de serem numéricos, são literais (personalizados)
# tuplas()
#listas[]
#dicionários{}
#declarando dicionario

""" dados = dict()
dados = {} # outra forma
dados1 = {'nome': 'Jai', 'idade': 25} # declara dicionario já com indices e valores
dados1['sexo'] = 'M'# cria-se um novo elemento de indice 'sexo de valor 'M' ao fim do dicionario
del dados1['idade'] # elimina-se o indice idade e seu valor
print(dados1) # print de todo o dicionario
print(dados1['nome']) # print do dicionario dados1 de índice 'nome'
#print(dados1['idade']) # print do dicionario dados1 de índice/elemento 'nome'

filme = {
    'titulo': 'Star Wars',
    'Ano':1997,
    'diretor':'George Lucas'
}
print(filme.values()) # retorna tds os valores do dicionário
print(filme.keys()) # retorna tds as chaves do dicionário
print(filme.items()) # retorna tds os itens do dicionário
# valor: valor da chave; chave: nome do elemento/indice ;item: (chave : valor)
 """
""" for chave, valor in filme.items():
    print(f'O {chave} é {valor}.')
 """
# lista contendo dicionários
""" locadora = []
locadora.append({
        'titulo':'Star Wars',
        'Ano':1977,
        'diretor':'George Lucas'
    })
locadora.append({
        'titulo':'Avengers',
        'Ano':2012,
        'diretor':'Joss Whedon'
    })
locadora.append({
        'titulo':'Matrix',
        'Ano':1999,
        'diretor':'Wachowski'
    })

print(locadora)
print(locadora[0]['titulo'])
print(locadora[1]['titulo'])
print(locadora[2]['Ano']) """

""" pessoas = {
    'nome':'Gustavo',
    'sexo':'M',
    'idade':22
}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') # necessita usar aspas duplas para diferenciar das aspas simples do f''
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for chave in pessoas.keys():
    print(chave)
for valor in pessoas.values():
    print(valor)

for chave, valor in pessoas.items(): # no dicionário não precisa usar enumerate, basta fazer o for sobre o dicionario com o metodo .items()
    print(f'{chave} = {valor}')

#criar um dicionario dentro de uma lista
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['uf']) """
estado = dict()
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
for estado in brasil:
    for uf, sigla in estado.items():
        print(f'O campo {uf} tem valor {sigla}.')