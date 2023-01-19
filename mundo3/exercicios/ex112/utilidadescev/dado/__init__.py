# entrada/ validação de dados monetários
def leia_dinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido! \033[m') #inserindo cor 
        else:
            valido= True
            return float(entrada)