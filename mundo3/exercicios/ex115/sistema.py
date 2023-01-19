from time import sleep
from lib.interface import *
from lib.arquivo import *


arq = 'cursoemvideo.txt'
""" if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    criarArquivo(arq) """
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # opção de listar o conteudo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema. Volte sempre! ')
        break
    else:
        print('\033[31mErro! Digite uma opção válida!\033[m')
    sleep(.9)

#menu.menu()