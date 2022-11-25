frase = 'Curso em Video Python'

print(frase[9:21:2]) # começa em 9, termina em 21, pula de 2 em 2(adotando o 2°)
print(frase[15:])# inica o inicio até o final
print(frase[9::3])# começa no 9 e pula de 3-3

print(len(frase)) #len = length 
print(frase.count('o'))# conta o caractere "o"
print(frase.count('o',0,13))#conta o caractere 'o' do indice 0 ao 13
print(frase.find('deo'))# indica o indice q começou a sequencia 'deo'
print(frase.find('video'))#Se a string não existe: retorna -1; se existe, retorna o indice de inicio
print('curso' in frase)#existe 'curso' em frase? se sim: True; se não: False
print(frase.replace('python', 'Android'))#troca a string 'python' por 'Android' 
print(frase.upper())
print(frase.lower())
print(frase.capitalize())# primeiro caractere da String em maiúsculo, restante em minúsculo
print(frase.title())#Analise das strings por palavras, onde houver espaços terá uma quebra de palavras. todas as letras iniciais serão maiúsculas.
print(frase.strip())#remove espaços inúteis antes do inicio da string e após o término do texto.
print(frase.rstrip())#remove espaços inúteis após o término do texto, 'r' de right.
print(frase.lstrip())#remove espaços inúteis antes do inicio da string. 'l' de left.
#dividir strings
print(frase.split())#retorna um array de string, sendo cada palavra um elemento da string, começando com indice 0. E cada string, tem seu 1° char de indice 0.
print('-'.join(frase))