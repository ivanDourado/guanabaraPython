""" def mensagem(msg):
    print('--'*10)
    print(msg)
    print('--'*10)

def mostraLinha():
    print('--'*10)

def soma(a,b):
    print(f'A = {a} e B = {b}')
    s=a+b
    print(f'A soma A + B = {s}')
 """
#empacotar paramns
""" def contador(*num):#* é um asterisco de desempacotar: todos os possiveis parametros passados serão recebidos por num # criar-se-á uma tupla com todos os parametros
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim!') """
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

# com listas 
valores = [7,2,5,0,4]
#dobrar valores da lista:
""" def dobra(lista): # minha alternativa com for
    lista_dobrada = list()
    for i,v in enumerate(lista):
        dobro_valor = v*2
        lista_dobrada.append(dobro_valor)
    print(lista_dobrada) """
#alternativa do profesor com while
def dobra(lista):
    position = 0 
    while position < len(lista):
        lista[position] *= 2
        position += 1


dobra(valores)
print(valores)



""" mensagem('Sistema de alunos')
mostraLinha()
soma(b=5,a=6) """
""" contador(5,6,7)
contador(44,5,2,9,78) """