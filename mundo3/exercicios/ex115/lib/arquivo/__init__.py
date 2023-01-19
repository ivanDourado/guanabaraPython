from lib.interface import *


def arquivoExiste(nome):
    caminho = f'/home/jaivan/Documentos/Guanabara_python/mundo3/exercicios/ex115/{nome}'
    nome = caminho
    try:
        a=open(nome, 'rt') #abrir arq (nome, 'ReadText)
        a.close() # fecha arquivo aberto
    except FileNotFoundError: # arq n encontrado
        return False # retorna false 
    else: # senao
        return True # retorna verdadeiro

def criarArquivo(nome):
    try:
        a = open(f'/home/jaivan/Documentos/Guanabara_python/mundo3/exercicios/ex115/{nome}', 'wt+') # 'w' Write, 't' Text, ' + ' se o arq n existe, será criado
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso! ')
   
        
def lerArquivo(nome):
    caminho = f'/home/jaivan/Documentos/Guanabara_python/mundo3/exercicios/ex115/{nome}'
    nome = caminho
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo! ')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';') # os dados serão divididos por ';'
            dado[1] = dado[1].replace('\n', '') # retira a quebra de linha do dado[1]
            print(f'{dado[0]:<30}{dado[1]:>3} anos') # dado[0] = nome ; dado[1] = idade
    finally:
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    caminho = f'/home/jaivan/Documentos/Guanabara_python/mundo3/exercicios/ex115/{arq}'
    arq = caminho
    try:
        a=open(arq, 'at') # 'a' append colocar conteudo dentro do arquivo/ 't' text
    except:
        print('Houve um ERRO na abertura do arquivo! ')
    else:
        try: 
            a.write(f'{nome};{idade}\n') # excrever no arquivo
        except:
            print('Houve um erro na hora de escrever os dados"')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close() # fecha arq
