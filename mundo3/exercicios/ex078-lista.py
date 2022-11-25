#ler (input) 5 valores numericos; guardar (append) em lista (list()); 
#ao fim, mostrar maior (max(lista)) e menor (min(lista)) valor e suas posições (enumerate(lista))
lista = list()
for posicao in range(0,5):
    lista.append(int(input(f'Digite um número para a posição {posicao}: ')))
    
print('-='*15)
print(f'a lista é {lista}. ')
print(f'O maior valor digitado é {max(lista)} nas posições: ',end='')

for posicao, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{posicao}... ',end='')
    
print(f'\nO menor valor digitado foi {min(lista)} nas posições: ',end='')

for posicao, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{posicao}... ',end='')
