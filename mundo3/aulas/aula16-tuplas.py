#Variáveis compostas
#Tuplas = variável que guarda vários valores
#tulas são entre parênteses
#tuplas são imutaveis (seus ítens não podem ser alterados)
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
""" print(lanche) # todos
print(lanche[1:]) # ídice 1 ao fim
print(lanche[-1]) #último
print(len(lanche)) # nº de ítens
print(lanche[1:3]) #1 ao 2
print(lanche[:3]) # 0 ao 2
 """

""" for comida in lanche:
    print(f'Eu comerei {comida}')
print('comi pra caramba') """

""" for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
     """
#print(sorted(lanche)) # coloca a tupla em ordem
a = (2,5,4)
b=(5,8,1,2)
c = a + b
print(a)
print(b)
print(c)
print(len(c))#comprimento
print(c.count(5)) # conta quantas vezes aparece o n° 5
print(c.index(8)) # em qual posição encontra-se o n° 8
print(c.index(2,1)) # em qual posição encontra-se o n° 2 a partir do ídice 1
del(c) # apaga a tupla da memória
print(c) # não definida, pois foi deletada na linha acima



