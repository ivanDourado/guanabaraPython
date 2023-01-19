def leiaint(msg=0): # cria-se funcao leiaint com msg de param
    while True: # loop 'infinito' enquanto verdadeiro
        try:
            n = int(input(msg))  
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mERRO! Entrada de dados interrompida pelo usuário. \033[m')
            return 'Nenhum'
        else:
            return n
            #print(f'Você acabou de digitar o número {n}') # Printa resultado   


def linha(tam=42):
    return '-'*tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[32mSua opção: \033[m')
    return opc

