#maior e menor peso lido
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1:# se for a primeira pessoa
        maior = peso #maior recebe peso
        menor = peso #menor recebe peso        
    else: # senão for a prmeira pessoa
        if peso > maior:  # se peso inserido maior que maior(peso digitado anteriormente)
            maior = peso # maior recebe novo valor para peso
        if peso < menor: # se peso inserido menor que menor(peso digitado anteriormente)
            menor = peso # menor recebe novo valor para peso
print(f'O maior peso lido foi de {maior} kg ')
print(f'e o menor foi de {menor}kg')