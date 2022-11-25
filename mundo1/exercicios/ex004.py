obj = input("Digite algo: ")
print(f'É um numero? {obj.isnumeric()}')
print(f'É uma letra? {obj.isalpha()}')
print(f'É um alfanumerico? {obj.isalnum()}')
print(f'Está em maiusculo? {obj.isupper()}')
print(f'Está em minusculo? {obj.islower()}')
print(f'Está capitalizada? {obj.istitle()}') # Possui letras maiusculas e minusculas