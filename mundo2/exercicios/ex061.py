print('Gerador de PA')
print('-='*20)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
print(f'{n1} -> ', end='')
a = n1
while c < 10:
    a += r    
    print(' FIM! ' if c == 9 else f'{a} -> ',end='')    
    c += 1
    
#n10 = n1 + (10 - 1) * r


#print(n10)