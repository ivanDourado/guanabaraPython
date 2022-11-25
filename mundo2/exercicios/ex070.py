print('--'*15)
print(' '*5+'Super Cheap Store'+' '*5)
print('--'*15)
total = cheaper = pricey = amount = more_than_1000 = 0
cheaper_prod = ''
pricey_prod = ''
while True:
    prod = str(input('Product Name: '))
    price = float(input(' Price: US$'))
    total +=1
    amount += price
    if price > 1000:
        more_than_1000 += 1  
        
    if total == 1:
        cheaper = price
        cheaper_prod = prod
        pricey_prod = prod
    else:
        if price < cheaper:
            cheaper = price
            cheaper_prod = prod
        elif price > pricey:
            pricey = price
            pricey_prod = prod        
      
    continua = ' '
    while continua not in 'YN':
        continua = str(input('Continue? [Y/N]: ')).upper().strip()[0]
    if continua == 'N':
        break
print('{:-^40}'.format('END OF PROGRAM'))
print(f'The total of shopping is US${amount}. \nThere are {total} products  ')
print(f'{more_than_1000} products costs more than US$1000.')
print(f'The most cheaper product is {cheaper_prod} and it costs US${cheaper}')
print(f'The most pricey product is {pricey_prod} and it costs US${pricey}')


    
