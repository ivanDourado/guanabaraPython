n = 1
par = impar = 0
while n != 0:#flag = ponto/condição de parada
    n = int(input('Digite um valor: '))
    if n != 0:       
        if n % 2 == 0:
            par += 1
        else:  
            impar += 1
print(f'VOcê digitou {par} nḿeros pares e {impar} números ímpares!')

'''r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM!')
'''
'''c = 1 
while c < 10:
    print(c)
    c += 1'''