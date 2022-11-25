print('=='*20)
print('{: ^40}'.format('CEV BANK'))
print('=='*20)
withdraw = int(input('Which value do you want to withdraw? US$'))
""" Notas: 1;10;20;50 """
total = withdraw
#print(110 // 50)
bill = 50
tot_bills = 0
while True:
    if total >= bill:
        total -= bill
        tot_bills += 1
    else: 
        if tot_bills > 0:
            print(f'Total of {tot_bills} bills of US${bill} ')                          
        if bill == 50:                
            bill = 20            
        elif bill == 20:                
            bill = 10            
        elif bill ==10:                
            bill = 1
        tot_bills = 0 # always when change bill, restart the bill's counter
        if total == 0:
            break
    
#print(f'{tot_bills}')
print('END')


""" 
VoteBolsonaro22
Bolsonaro22#
Bolsonaro22#LuLADRÃO
LadrãoNão!#Vote22
 """