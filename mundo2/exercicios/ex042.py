print('-=-' * 20 )
print('Analisador de triângulos ')
print('-=-' * 20)
cores = {
        'limpa':'\033[m', 
        'azul':'\033[34m',
        'amarelo':'\033[33m',
        'vermelho':'\033[31m',
        'verde':'\033[32m' 
        }
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
'''
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b
'''
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2: 
    print(f'{cores["verde"]}Os segmentos podem formar triângulo{cores["limpa"]}!', end=' ')
    if s1 == s2 == s3 :
        print('Triâmgulo equilátero!')
    elif s1 != s2 != s3 != s1:
        print('Triâgulo escaleno!')
    else:
        print('Triangulo isóceles!')
else:
    print(f'{cores["vermelho"]}Os segmentos não podem formar triângulo{cores["limpa"]}!')