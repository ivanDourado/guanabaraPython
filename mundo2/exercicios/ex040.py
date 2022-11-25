n1 = float(input('Digite a 1° nota: '))
n2 = float(input('Digite sua 2° nota: '))
media = (n1 + n2) / 2
if media < 5 :
    print(f'Reprovado com média {media}!')
elif media >= 5 and media < 7 : 
    print(f'Recuperação com média {media}')
else:
    print(f'Aprovado com média {media}')