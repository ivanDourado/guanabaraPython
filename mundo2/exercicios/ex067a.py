while True:
    print('--'*20)
    n = int(input('Quer ver a taboada de qual valor? '))
    if n < 0:
        print('--'*20)
        break
    print('--'*20)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Programa taboada encerrado. Volte Sempre!')
print('--'*20)