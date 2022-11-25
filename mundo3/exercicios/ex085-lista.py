""" lista_par = []
lista_impar = []
pos = 1
for c in range(0,7):
    num = int(input(f'Digite o {pos}º valor: '))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    pos += 1
print('-='*30)
print(f'Os valores pares digitados foram: {lista_par}')
print(f'Os valores ímpares digitados foram: {lista_impar}') """
lista = []
lista_par = []
lista_impar = []
for c in range(1,8):
    lista.append(int(input(f'Digite o {c}º valor: ')))    
    
for i, v in enumerate(lista):
        if v % 2 == 0:
            lista_par.append(v)
        else:
            lista_impar.append(v)
        
print('-='*30)
lista_impar.sort()
lista_par.sort()
print(f'os numeros digitados foram {lista}')
print(f'Os valores ímpares digitados foram: {lista_impar}')
print(f'Os valores pares digitados foram: {lista_par}')

