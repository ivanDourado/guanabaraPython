#listas entre [] 
#são mutáveis
""" lanche = ['Suco', 'Hamburguer', 'Churrasco']
lanche.append('Cookie')# insere item no final da lista

lanche[0] = 'Vitamina' #substitui o ítem no índice 0 

lanche.insert(0,'suco') # insere um novo elemento na posição informada

del lanche[4] # deleta o indice 4 [cookie] da lista lanche

lanche.pop(2) # deleta o indice 2 [hamburguer] da lista lanche; por padrão elimina o último, quando sem parâmetro

lanche.remove('suco') # elimina  ítem pelo seu valor/conteudo; retorna erro se elemento inexiste

if 'pizza' in lanche: # se houver piiza na lista lanches
    lanche.remove('pizza')#remove 'pizza' da lista lanche

valores = list(range(4,11)) # cria uma lista a partir de 4 até 10
valores1 = [8,2,5,4,9,3,0]
valores1.sort() #ordena de forma crescente
valores1.sort(reverse=True) #ordena de forma decrescente
len(valores1) # retorna quantos elementos possui a lista valores1

print(lanche)
print(valores)
print(valores1) """

""" num = [2,5,9,1]
num[2] = 3 # substitui o valor do elemento do indice 2 com o valor 3
num.append(7) # insere o valor 7 ao final da lista
#num.sort() # ordena de forma crescente
num.sort(reverse=True) #imprime a lista em ordem decrescente
num.insert(2,2) # na posição de índice 2, insere o valor 0, mantendo os demais valores, arrastando-os para o ńdice seguinte
#num.pop() # o método .pop() por padrao elimina o último ítem da lista. Mas se tiver parâmetro(x), este eliminará o elem. de indice x
#num.pop(2) # elimina o Element de indice 2
num.remove(2) # remove o 1º elemento 2 , do início ao fim

if 4 in num:
    num.remove(4)
else:
    print('Não achei o num 4')
print(num) """
valores = [] # inicia lista vazia
valores1 = list() # tbm inicia lista vazia
valores1.append(5)
valores1.append(9)
valores1.append(4)

print(valores1) 
""" 
print(f'Os valores são ', end='')
for valor in valores1:
    print(f'{valor} ', end=' ') """

""" 
for chave, valor in enumerate(valores1):
    print(f'No índice {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista') 
"""
# inserir valores na lista, ao fim, pelo teclado
""" for item in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for indice, valor in enumerate(valores):
    print(f'No índice {indice} encontrei o valor {valor}!')
print('Cheguei ao final da lista.') """

""" a= [2,3,4,7]
#b = a # b recebe a e fica ligada a a. Ou seja, se altera b, altera-se a e vice-versa
b = a[:] # cria-se uma cópia a qual b recebe todos os elementos de a. uma não está ligada a outra
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}') """