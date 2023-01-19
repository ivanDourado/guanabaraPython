def leiaint(msg=0): # cria-se funcao leiaint com msg de param
    ok = False #inicializa variavel ok = false
    valor = 0 #inicializa variavel valor = 0
    while True: # loop 'infinito' enquanto verdadeiro
        n = input(msg) # n = input retorna stringo por padrao
        if n.isnumeric():  # se o conteudo da string for numérico
            valor = int(n) # este é convertido para tipo int
            ok = True # ok = verdadeiro
        else: # senão
            print('\033[0;31mERRO! Digite um número inteiro válido\033[m') # imprime msg de erro na cor vermelha
        if ok: # se ok = true
            break # interrompe o laço
    return valor # fora do laço, ao fim da função, retorna o novo valor da var valor

n = leiaint('Digite um número: ') # declara-se var n que recebe a funçao acima q tem msg como parametro
print(f'Você acabou de digitar o número {n}') # Printa resultado