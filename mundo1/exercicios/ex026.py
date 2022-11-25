frase = str(input('Digite uma frase: '))
print('A letra "a" apareceu {} vezes'.format(frase.lower().count('a')))
# o rAto roeu a roupa do rei de roma
print('A primeira letra "a" apareceu na posição de índice {}!'.format(frase.find('a')))
print('A última letra "a" apareceu na posição de índice {}!'.format(frase.rfind('a')))