# digitar varios valores num int(input('Digite um numero: )) ; cadastre-os na lista [ lista.appent(input ) ] ; se já existir ( if num in lista: n add)  o referido numero, não sera add; 
# ao fim, exibir todos os valores únicos em ordem crescente [.sort()]
#ao fim de cada adiçao, perguntar se quer continuar
lista = [] # cria lista
continua = 'S' # inicializa variavel continua de modo a ser inicialmente aceita no laço while
num = '' #inicializa var

while continua in 'sS': # enquanto var continua tem valor 's' ou 'S'
    num = int(input('Digite um valor: ')) # # var num recebe valor digitado pelo usuario
    if num in lista: # se o numero digitado já pre-existe na lista, faça-se o que está abaixo
        print('Valor duplicado! Não será add...')   # printa essa msg     
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0] # maiuscula; retira espaços; acc só 1ª letra   # pergunta se quer continuar    
    else: # caso contrário       
        lista.append(num) # add o num no fim da lista
        print('Valor adicionado com sucesso... ') # printa essa msg
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0] # maiuscula; retira espaços; acc só 1ª letra  # pergunta se quer continuar       

lista.sort() # ordena em ordem crescente
print(f'Fim. sua lista é {lista}') # imprime a lista já ordenada crescentemente

