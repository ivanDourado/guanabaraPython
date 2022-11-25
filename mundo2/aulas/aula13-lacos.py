#somatório 
'''s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatório foi de {s}')'''

#Contagem
'''n = int(input('Digite um numero: '))
for c in range(0, n+1):# para c no intervalo de 0 a n+1
    print(c)
print('FIM')'''

#contagem regressiva
'''x = int(input('Digite um numero: '))
for c in range(x, 0, -1):
    print(c)
print('FIM')'''

#contagem intercalada
for c in range(0, 8, 2):# inicio: 0 ; fim: 8-1 ; pula: 2 ;
    print(c)
print('FIM')