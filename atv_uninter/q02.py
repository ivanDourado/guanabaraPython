print(f'''Bem vindo à Sorveteria do Ivan Felipe de Oliveira Santos Dourado
RU: 3357756
{'--'*23 +'Cardápio'+'--'*23}
| Código | Descrição            | Tamanho P (500 mL) | Tamanho M (1000 mL) | Tamanho G (2000 mL) |
|   TR   | Sabores Tradicionais |     R$ 6,00        |      R$ 10,00       |      R$ 18,00       |
|   ES   | Sabores Especiais    |     R$ 7,00        |      R$ 12,00       |      R$ 21,00       |
|   PR   | Sabores Premium      |     R$ 8,00        |      R$ 14,00       |      R$ 24,00       |
 {'--'*23 +'--------'+'--'*23}''') #cabeçalho do exercício e menu de opções da sorveteria

valido = True # inicialização da variavel valido com valor boleano verdadeiro
contador = 0 # inicialização da variavel contador para aferir o total da conta
while valido: #se for válido
  tamanho_pote = str(input('Entre com o tamanho do pote desejado (P/M/G): ')).upper() #variavel recebe um valor string  inserido pel usuário # upper() torna maiúsculo
  codigo_sabor = str(input('Entre com o código do sabor desejado (TR/ES/PR): ')).upper() #variavel recebe um valor string  inserido pel usuário # upper() torna maiúsculo
  if (tamanho_pote == 'P' or tamanho_pote == 'M' or tamanho_pote == 'G') and (codigo_sabor == 'TR' or codigo_sabor == 'ES' or codigo_sabor == 'PR'): # se os valores inseridos pelo usuário forem válidos, segundo a regra de negócio
    valido = True # variavél valido recebe True
    if codigo_sabor == 'TR': # se o código for 'TR'
      if tamanho_pote == 'P': # se o tamanho for 'P'
        valor = 6.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor TRADICIONAL {tamanho_pote} de R$6,00') # imprime escolha do usuário e seu respectivo valor
      elif tamanho_pote == 'M':# se o tamanho for 'M'
        valor = 10.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor TRADICIONAL {tamanho_pote} de R$10,00') # imprime escolha do usuário e seu respectivo valor
      else: # se o tamanho for 'G'
        valor = 18.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor TRADICIONAL {tamanho_pote} de R$18,00') # imprime escolha do usuário e seu respectivo valor
    elif codigo_sabor =='ES': # se o código for 'ES'
      if tamanho_pote == 'P':# se o tamanho for 'P'
        valor = 7.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor ESPECIAL {tamanho_pote} de R$7,00') # imprime escolha do usuário e seu respectivo valor
      elif tamanho_pote == 'M':# se o tamanho for 'M'
        valor = 12.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor ESPECIAL {tamanho_pote} de R$12,00') # imprime escolha do usuário e seu respectivo valor
      else:# se o tamanho for 'G'
        valor = 21.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor ESPECIAL {tamanho_pote} de R$21,00') # imprime escolha do usuário e seu respectivo valor
    else:# se o código for 'PR'
      if tamanho_pote == 'P':# se o tamanho for 'P'
        valor = 8.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor PREMIUM {tamanho_pote} de R$8,00') # imprime escolha do usuário e seu respectivo valor
      elif tamanho_pote == 'M':# se o tamanho for 'M'
        valor = 14.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor PREMIUM {tamanho_pote} de R$14,00') # imprime escolha do usuário e seu respectivo valor
      else:# se o tamanho for 'G'
        valor = 24.0 # valor do respectivo tamanho e sabor
        contador += valor # contador recebe seu valor presente acrescido do valor da opção do usuário
        print(f'Você escolheu um sovete sabor PREMIUM {tamanho_pote} de R$24,00') # imprime escolha do usuário e seu respectivo valor
    
    print('--'*20)
    novo_pedido = str(input('Deseja pedir mais alguma coisa? (S/N): ')).upper() #confirmação de novo pedido
    if novo_pedido == 'S': # se o usuário inserir string 'S' ou 's'
      continue # continue deixa de ler o código acaixo e reinicia o loop
    else: # se o unuário inserir 'N' ou outro valor distinto de 'S' ou 's'
      print(f'O total a ser pago é: R$ {contador:.2f}') #fechamento da conta com o total consumido em reais
    break
  else: #caso contrário (valores de código e / ou tamano inválidos)
    print('Tamanho ou código inválidos!') # imprimir informativo de erro de código e/ou tamanho do pote
    continue # continue deixa de ler o código e reinicia o loop
