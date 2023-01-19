import utilidadescev.moeda as moeda
from utilidadescev.dado import leia_dinheiro
p = leia_dinheiro("Digite o preço: R$ ")
moeda.resumo(p, 35, 22)
