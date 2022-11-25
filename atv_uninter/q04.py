from time import sleep # importa a biblioteca time para aplicar o método sleep() que proporciona um delay desejado

colaboradores = list() # # cria-se o lista colaboradores
funcionario = dict() # cria-se o dicionário funcionario
id = 7401 # inicializa variavél Id, para ocorrer seu incremento na linha l.86
def cadastrar_funcionario(id): # cria-se função com parâmetro id
    print(f""" {'**'*30}
    {'--'*15} Menu Cadastrar Funcionário  {'--'*15}  
     """) # printa menu
    funcionario["código"] = id # No dicionário funcionário, criar-se-á uma chave 'código' que receberá o valor id (paramero da função)
    funcionario["nome"] = str(input('Por favor entre com o Nome: ')) # No dicionário funcionário, criar-se-á uma chave 'nome' que receberá o valor string inserido pelo usuário
    funcionario["setor"] = str(input('Por favor entre com o setor: ')).upper().strip()[0] # No dicionário funcionário, criar-se-á uma chave 'setor' que receberá o valor string inserido pelo usuário
    funcionario["salário"] = float(input('Por favor entre com o salário: ')) # No dicionário funcionário, criar-se-á uma chave 'salário' que receberá o valor float inserido pelo usuário
    colaboradores.append(funcionario.copy()) # na lista colaboradores, ao seu final de comprimento, receberá como último ítem uma cópia do dicionário funcionário
    {'**'*30}

def consultar_funcionários(): # cria-se função
    opcao = '' # inicializa variavél opcao de modo a iniciar o laço while
    while opcao != 4: # enquanto a opcao for distinta de 4 
        print(f""" {'**'*30}
        {'--'*15} Menu Consultar Funcionário {'--'*15}
        Escolha a opção desejada:
        1) Consultar Todos os Funcionários
        2) Consultar Funcionário por Id
        3) Consultar Funcionário(s) por Setor
        4) Retornar  
        """) # printa menu
        opcao = int(input('>>>> ')) # solicita o dado ao usuário
        if opcao == 1: # se opcao = 4
            for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
                for key, value in funcionario.items(): # para cada chave e valor em funcionário
                    print(f'O campo {key} tem valor {value}.') # imprime  chave e valor
                    sleep(.4)
                print('-'*10)
        if opcao == 2: # se opcao = 2
            busca = int(input('Digite o ID do Funcionário: (999 para parar) ')) # burcar ID
            print('--'*15)
            if busca == 999: # se valor = 999 , interrompe
                break
            for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
                for k,v in funcionario.items(): # para cada chave e valor em funcionário
                    if busca == funcionario["código"]: # se busca for igual ao valor da chave 'código'
                        print(f'{k} : {v}') # imprime  chave e valor
                print() # pula linha
        if opcao == 3: # se opcao = 3
            busca = str(input('Digite o setor dos Funcionários: (999 para parar) ')).upper().strip()[0] # burcar setor
            print('--'*15) # imprime divisoria 
            if busca == 999: # se valor = 999 , interrompe
                break
            for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
                for k,v in funcionario.items(): # para cada chave e valor em funcionário
                    if busca == funcionario["setor"]: # se busca for igual ao valor da chave 'setor'
                        print(f'{k} : {v}')  # imprime  chave e valor
                print() # pula linha
        if opcao == 4: # se opcao = 4
            break # interrompe
          

def remover_funcionario():  # cria-se função
     print(f""" {'**'*30}
    {'--'*15} Menu Remover Funcionário  {'--'*15}  
     """)# printa menu
     remove = int(input('Digite o código/ID do funcionário a ser removido: ')) # solicita o dado ao usuário[id]
     for funcionario in colaboradores: #para cada funcionario (dict) em colaboradores(list)
        for k,v in funcionario.items(): # para cada chave e valor em funcionário
            if k == "código" and remove == v: # se a chave = código e valor = remove
                colaboradores.remove(funcionario) # remove-se o item funcionario (dict) da lista colaboradores
   
print(f""" Bem vindo ao controle de funcionários do Ivan Felipe de Oliveira Santos Dourado
    RU: 3357756
{'**'*30} """) # boas- vindas ao meu programa
opcao = '' # inicializa opçao
while opcao != 4: # se opcao diferente de 4, faça-se :
    print(f""" {'--'*15} Menu Principal {'--'*15}
        1. Cadastrar Funcionário
        2. Consultar Funcionários(s)
            1) Consultar Todas as Funcionários
            2) Consultar Funcionário por Id
            3) Consultar Funcionário(s) por Setor
            4) Retornar
        3. Remover Funcionário
        4. Sair  """)    # printa menu
    opcao = int(input('>>>> ')) # solicita o dado ao usuário do tipo numérico
    if opcao == 1: #se opcao = 1
        cadastrar_funcionario(id) #chama função cadastro com parametro
        id +=1 # incremento do ID para cada fncionario novo cadastrado
    if opcao == 2: #se opcao = 2
        consultar_funcionários() #chama função consulta
    if opcao == 3: #se opcao = 3
        remover_funcionario() #chama função remove
    if opcao == 4: #se opcao = 4
        print('>>> Obrigado! Volte Sempre <<<') # imprime saudaçao de termino da aplicação
        break #Interrompe laço e aplicação   
    {'**'*30}

