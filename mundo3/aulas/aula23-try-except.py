#Exception = exeção

try:# tente
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
                #""" except Exception as erro: # se der erro # pode-se ter um exception para cada classificação de exceção/erro (type, value, class, OS)
                # print(f'O problema encontrado foi {erro.__class__}') # classe do erro """
except (ValueError, TypeError):
    print('tivemos um problema com os tipos de dados q você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir o numero por 0')
except KeyboardInterrupt:
    print('P usuario preferiu não informar os dados')
else: # se der certo
    print(f'O resultado é {r}')
finally: # finalmente / acontece se der certo ou errado (sempre)
    print('<< Volte Sempre >>')