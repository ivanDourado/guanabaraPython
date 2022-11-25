from datetime import date
from math import fabs

anoNasc = int(input('Digite seu ano de nascimento: '))
sexoBiologico = {1:'Masculino', 2:'Feminino'}

print('''
     Digite o número correspondente ao teu sexo biológico:
     [1] - Masculino
     [2] - Feminino
''')
sexo = int(input("Digite o número correspondente: "))

anoAtual = date.today().year # retorna o ano atual
idade = anoAtual - anoNasc
spaceTime = fabs(18 - idade) # retorna sempre o módulo do numero ou operação

if sexo == 2:
     print(f'Pessoas do sexo {sexoBiologico[2]} estão dispensadas do alistamento militar obrigatório.')
else:
     if anoAtual - anoNasc < 18:
          print(f'Sua ano de nascimento de {anoNasc} e idade {idade} indicam que você ainda se alistará em {spaceTime} anos')
     elif anoAtual - anoNasc == 18:
          print(f'Sua ano de nascimento de {anoNasc} e idade {idade} indicam  que você precisa se alistar esse ano')
     else : 
          print(f'Sua ano de nascimento de {anoNasc} e idade {idade} indicam  que você está atrasado para se alistar em {spaceTime} anos')