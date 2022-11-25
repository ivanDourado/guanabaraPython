v1 = int(input('Digite o prmeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
# verificando o menor
menor = v1
if v2 < v3 and v2<v1:
    menor = v2
if v3 < v2 and v3 < v1:
    menor = v3
#verificando o maior
maior = v1
if v2 > v3 and v2 > v1:
    maior = v2
if v3 > v2 and v3 > v1:
    maior = v3
print(f'O menor valor foi de {menor}')
print(f'O maior valor foi de {maior}')

