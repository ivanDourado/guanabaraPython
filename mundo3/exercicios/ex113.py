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
            
 
def leiareal(msg=0):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Por favor, digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mERRO! Entrada de dados interrompida pelo usuário. \033[m')
            return 'Nenhum'
        else:
            return n



n = leiaint('Digite um número inteiro: ') # declara-se var n que recebe a funçao acima q tem msg como parametro
print(f'O valor inteiro digitado foi {n}')
r = leiareal('Digite um número real: ')
print(f'O valor real digitado foi {r}')
