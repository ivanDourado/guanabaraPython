from curses.ascii import alt


peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5 : 
    print(f'Seu IMC é de {imc}. Se ventar forte tu voa')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc}. Tá bem demais.')
elif imc >= 25 and imc < 30 :
    print(f'Seu IMC é de {imc}. Olha as banhas saindo!')
elif imc >= 30 and imc <= 40 :
    print(f'Seu IMC é de {imc}. Você já possui massa planetária.' )