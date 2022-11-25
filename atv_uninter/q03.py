from time import sleep # importa a biblioteca time para aplicar o método sleep() que proporciona um delay desejado
tarifa = dict() # cria-se o cicionário tarifa
def metragem_limpeza(): # cria-se a função metragem_limpeza()
    print('---'*15, ' Menu 1 de 3 - Metragem limpeza ', '---'*15)    # printa menu
    while True: # laço de repetição while   
        try: # tente interagir com o usuario para que o mesmo insira um dado de tipo numérico
            metragem = float(input('Entre com a metragem da casa: ')) # solicita o dado ao usuário
        except: # caso ocorra uma exceção, reponder abaixo
            print('tivemos um problema com os tipos de dados q você digitou. Digite um valor numérico.') # solicita ao usuário digitar somente números       
        else: # caso não ocorra exceções 
            while True: #inicia-se um laço
                if metragem < 30 or metragem > 699: # caso a metragem inserida seja menor que 30 e maior que 699 
                    print('Não aceitamos casas com metragem menor que 30m² ou maior que 700m²!') # imprime informação que o valor está fora da faixa trabalhada pela empresa
                    try: # tente interagir com o usuario para que o mesmo insira um dado de tipo numérico
                        metragem = int(input('Entre com a metragem da casa: '))  # solicita o dado ao usuário
                    except: # caso ocorra uma exceção, reponder abaixo
                         print('tivemos um problema com os tipos de dados q você digitou. Digite um valor numérico.') # solicita ao usuário digitar somente números 
                         metragem = float(input('Entre com a metragem da casa: '))   # solicita o dado ao usuário                      
                else: # caso a metragem inserida pelo usuário esteja na faixa trabalhada pela empresa e livre de erros de exceções 
                    if metragem >=30 and metragem<=299: # se a metragem for maior que 30 e menor ou igual a 299
                        print('Será necessário contratar 1 pessoa. ') # imprime o numero de pessoas conforme a tabela
                        sleep(.4)  # delay de 0.4 s                  
                        tarifa["valor"] = (60+0.3 * metragem) # No dicionário tarifa, criar-se-á uma chave 'valor' que receberá a equação conforme a tabela
                        break # interrompe este laço
                    elif metragem >=300 and metragem<=699: # se a metragem for maior que 300 e menor ou igual a 699
                        print('Será necessário contratar 2 pessoas. ') # imprime o numero de pessoas conforme a tabela
                        sleep(.4) # delay de 0.4 s  
                        tarifa["valor"] = (120+0.5 * metragem) # No dicionário tarifa, criar-se-á uma chave 'valor' que receberá a equação conforme a tabela                   
                        break # interrompe este laço
            break # interrompe este laço
    
def tipo_limpeza(): # cria-se a função tipo()
    print('---'*15, ' Menu 2 de 3 - Metragem limpeza ', '---'*15)  # printa menu
    sleep(.4) # delay de 0.4 s  
    print(""" Entre com o tipo de limpeza:
    B - Básica - Indicada para sujeiras semanais ou quinzenais
    C - Completa (30% a mais)- Indicada para sujeiras antigas e/ou não rotineiras""") # printa menu tipo de limpeza
    tipo = str(input('Tipo :')).upper().strip()[0] # solicita o dado ao usuário do tipo string, transforma-o em maiúsculo, retira-se os espaços e lê-se o primeiro caractere digitado
    while tipo not in 'BC': # enquanto a variavel tipo não estiver entre as letres 'B' ou 'C', executar-se-á abaixo
        print('Erro! Selecione uma opção válida.') # imprime informação que o valor está fora da faixa trabalhada
        tipo = str(input('Tipo :')).upper().strip()[0] # solicita o dado ao usuário do tipo string, transforma-o em maiúsculo, retira-se os espaços e lê-se o primeiro caractere digitado
    if tipo == 'B': # Se o dado lido for "B" 
        print('Você selecionou a limpeza BÁSICA!') # imprime que é tipo básica
        tarifa["tipo"] = 'B'  # No dicionário tarifa, criar-se-á uma chave 'tipo' que receberá a string 'B'
        tarifa["multiplicador"] = 1.00  # No dicionário tarifa, criar-se-á uma chave 'multiplicador' que receberá a um valor float 1.00    
        print('**'*50) # imprime uma divisória de asteríscos
    if tipo == 'C': # Se o dado lido for "C" 
        print('Você selecionou a limpeza COMPLETA!')
        tarifa["tipo"] = 'C' # No dicionário tarifa, criar-se-á uma chave 'tipo' que receberá a string 'C'
        tarifa["multiplicador"] = 1.30 # No dicionário tarifa, criar-se-á uma chave 'multiplicador' que receberá a um valor float 1.30   
        print('**'*50) # imprime uma divisória de asteríscos

def adicional_limpeza(): # cria-se a função tipo()
    
    print('---'*15, ' Menu 3 de 3 - Metragem limpeza ', '---'*15)  # printa menu
    sleep(.4) # delay de 0.4 s  
    print(""" Deseja mais algum adicional? 
    0 - Não desejo mais nada - Encerrar
    1 - Passar 10 peças de roupa - R$10.00
    2 - Limpeza de 1 forno/micro-ondas - R$12.00
    3 - Limpeza de 1 geladeira/Freezer - R$20.00 """)  # printa menu de adicional
    adicional = int(input('>>>> ')) # solicita o dado ao usuário do tipo numérico
    tarifa['adicional'] = list() # cria-se um item nodicionário de chave 'adicional' do tipo lista
    while adicional != 0: # enquanto a variavel adicional for diferente de zero (encerrar menu adicional), faça-se abaixo:
        if adicional == 1: # se adicional = 1
            tarifa["adicional"].append(10.00) # O item  'adicional' do dicionário tarifa,  do tipo lista, receberá este valor, dentro do .append(valor), ao final da lista 
        if adicional == 2: # se adicional = 2
            tarifa["adicional"].append(12.00) # O item  'adicional' do dicionário tarifa,  do tipo lista, receberá este valor, dentro do .append(valor), ao final da lista 
        if adicional == 3: # se adicional = 3
            tarifa["adicional"].append(20.00) # O item  'adicional' do dicionário tarifa,  do tipo lista, receberá este valor, dentro do .append(valor), ao final da lista        
        print('Deseja mais algum adicional?') # imprime a pergunta se deseja mais adicionais
        adicional = int(input('>>>> ')) # inpute que lê a resposta do usuário
    print('**'*50) # imprme divisoria de asteríscos

print('Bem-vindo ao programa de serviços de limpeza do Ivan Felipe De Oliveira Santos Dourado') # boas-vindas ao meu programa
print('**'*50)  # imprme divisoria de asteríscos
metragem_limpeza() # chama função
tipo_limpeza() # chama função
adicional_limpeza() # chama função
total = tarifa['valor'] * tarifa['multiplicador'] + sum(tarifa["adicional"]) # variavel total recebe uma equação com os valores de cada chave do dicionário tarifa, conforme quadros do exercício
print(f'TOTAL: R$ {total:.2f} ( metragem: {tarifa["valor"]} * tipo: {tarifa["multiplicador"]} + adicional: {sum(tarifa["adicional"])} )') # imprime o valor total e o cálculo do preço
        