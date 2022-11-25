print(f'''{'=-'*12}
Bem-vindo a Loja do Ivan Felipe De Oliveira Santos Dourado! \nRU:3357756
''')#enunciado com nome e RU, precedido com '=-' multiplicado por 8 para fins estéticos
valor_produto = float(input('Entre com o valor do produto: '))#solicita que o usuário insira o valor do tipo float (ponto flutuante)

qtd_produto = int(input('Entre com a quantidade do produto: '))#solicita que o usuário insira a quantidade de produtos por meio e um valor do tipo inteiro (integer)

valor_sem_frete = valor_produto * qtd_produto #variável valor sem frete criada a fim de evitar reescrita de código

if qtd_produto < 11:#1º condicional, se a quantidade for menor que 11 produtos
  valor_total = valor_sem_frete + 30 # insere o valor de 30 para essa condição
  print(f'O valor sem frete foi: {valor_sem_frete:.2f}') #exibir somente até a 2º casa decimal após o ponto
  print(f'O valor com frete foi: {valor_total:.2f}')
elif qtd_produto >=11 and qtd_produto < 101:#2º condicional, se a quantidade for entre 11 e 100 produtos
  valor_total =  valor_sem_frete + 60 # insere o valor de 60 para essa condição
  print(f'O valor sem frete foi: {valor_sem_frete:.2f}') #exibir somente até a 2º casa decimal após o ponto
  print(f'O valor com frete foi: {valor_total:.2f}')
elif qtd_produto >= 101 and qtd_produto < 1001:#3º condicional, se a quantidade for entre 101 e 1000 produtos
  valor_total = valor_sem_frete + 120  # insere o valor de 120 para essa condição
  print(f'O valor sem frete foi: {valor_sem_frete:.2f}') #exibir somente até a 2º casa decimal após o ponto
  print(f'O valor com frete foi: {valor_total:.2f}')
elif qtd_produto>=1001:#4º condicional, se a quantidade for maior ou ingual à 1001 produtos
  valor_total = valor_sem_frete + 240 # insere o valor de 2440 para essa condição
  print(f'O valor sem frete foi: {valor_sem_frete:.2f}') #exibir somente até a 2º casa decimal após o ponto
  print(f'O valor com frete foi: {valor_total:.2f}')