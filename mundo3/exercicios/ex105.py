def notas(*notas, sit=False):
    """ 
    -> Função para analisar notas e situações de vários alunos. 
    :param *notas: uma ou mais notas dos anulos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não add a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print(notas)
    total = len(notas)
    maior = max(notas)
    menor = min(notas)
    media = sum(notas)/len(notas)

    turma = {
        'total': total,
        'maior': maior,
        'menor': menor,
        'média': media
    }
    if sit == True:
        if media <6:
            turma["situação"] = 'RUIM'
        elif media >=6 and media < 7:
            turma["situação"] = 'RAZOÁVEL'
        else:
            turma["situação"] = 'BOA'
            
    return turma



resp = notas(5.5,9.5,6,6.5, sit=True)
print(resp)
# help(notas)