from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
dobro = numeros.dobro(num)
triplo = numeros.triplo(num)

print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {dobro}')
print(f'O triplo de {num} é {triplo}')

""" vantagens:
- organizaçao
- manutenção
- ocultação do código detalhado
- reutilização dos módulos em outros projetos """

""" pacotes (chamado em outras linguagens de biblioteca)
- junção de módulos separados por assuntos; 

cria-se pacotes com uma criação de pastas, e subpastas para módulos


"""