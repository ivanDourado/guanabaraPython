def ficha(jog='<desconhecido>', gol=0): # recebe 2 parametros opcionais
    print('--'*15)
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

nome = input('Nome do jogador: ')
gols = input('Número de gols: ') # deixei string por padrão pois permite inserir valores vazios
if gols.isnumeric(): # retorna true se o conteudo da string é numerico
    gols = int(gols) # converte o tipo da variavel para int
else: # caso contrario
    gols = 0 # valor passa a ser zero
if nome.strip() == '': # se nome retirado todos os espaços é vazio
    ficha(gol=gols) # o parametro da função receberá o conteudo que o usuario estrevei
else: # senão
    ficha(nome, gols) # os parametros da função serão os vlores digitados pelo usuario
    

