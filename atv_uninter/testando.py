from time import sleep
tarifa = dict()
def metragem_limpeza(): 
    print('---'*15, ' Menu 1 de 3 - Metragem limpeza ', '---'*15)    
    while True:   
        try:
            metragem = float(input('Entre com a metragem da casa: '))
        except:
            print('tivemos um problema com os tipos de dados q você digitou. Digite um valor numérico.')        
        else:
            while True:
                if metragem < 30 or metragem > 699:
                    print('Não aceitamos casas com metragem menor que 30m² ou maior que 700m²!')
                    try:
                        metragem = int(input('Entre com a metragem da casa: '))
                    except:
                         print('tivemos um problema com os tipos de dados q você digitou. Digite um valor numérico.')
                         metragem = float(input('Entre com a metragem da casa: '))                         
                else:
                    if metragem >=30 and metragem<=299:
                        print('Será necessário contratar 1 pessoa. ')
                        sleep(.4)                    
                        tarifa["valor"] = (60+0.3 * metragem) 
                        break
                    elif metragem >=300 and metragem<=699:
                        print('Será necessário contratar 2 pessoas. ')
                        sleep(.4)
                        tarifa["valor"] = (120+0.5 * metragem)                     
                        break
            break
    
def tipo_limpeza():
    print('---'*15, ' Menu 2 de 3 - Metragem limpeza ', '---'*15)
    sleep(.4)
    print(""" Entre com o tipo de limpeza:
    B - Básica - Indicada para sujeiras semanais ou quinzenais
    C - Completa (30\%\ a mais)- Indicada para sujeiras antigas e/ou não rotineiras""")
    tipo = str(input('Tipo :')).upper().strip()[0]    
    while tipo not in 'BC':
        print('Erro! Selecione uma opção válida.')
        tipo = str(input('Tipo :')).upper().strip()[0]
    if tipo == 'B':
        print('Você selecionou a limpeza BÁSICA!')
        tarifa["tipo"] = 'B'
        tarifa["multiplicador"] = 1.00        
        print('**'*50)
    if tipo == 'C':
        print('Você selecionou a limpeza COMPLETA!')
        tarifa["tipo"] = 'C'
        tarifa["multiplicador"] = 1.30
        print('**'*50)

def adicional_limpeza():
    
    print('---'*15, ' Menu 3 de 3 - Metragem limpeza ', '---'*15)
    sleep(.4)
    print(""" Deseja mais algum adicional? 
    0 - Não desejo mais nada - Encerrar
    1 - Passar 10 peças de roupa - R$10.00
    2 - Limpeza de 1 forno/micro-ondas - R$12.00
    3 - Limpeza de 1 geladeira/Freezer - R$20.00 """)
    adicional = int(input('>>>> '))
    tarifa['adicional'] = list()
    while adicional != 0:
        if adicional == 1:
            tarifa["adicional"].append(10.00)
        if adicional == 2:
            tarifa["adicional"].append(12.00) 
        if adicional == 3:
            tarifa["adicional"].append(20.00)        
        print('Deseja mais algum adicional?')
        adicional = int(input('>>>> '))
    print('**'*50)

print('Bem-vindo ao programa de serviços de limpeza do Ivan Felipe De Oliveira Santos Dourado')
print('**'*50)
metragem_limpeza()
tipo_limpeza()
adicional_limpeza()
total = tarifa['valor'] * tarifa['multiplicador'] + sum(tarifa["adicional"])
print(f'TOTAL: R$ {total:.2f} ( metragem: {tarifa["valor"]} * tipo: {tarifa["multiplicador"]} + adicional: {sum(tarifa["adicional"])} )')
