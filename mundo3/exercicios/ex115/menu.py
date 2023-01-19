def menu():
    opcao =''
    while opcao !=3:
        print('--'*20)
        print('MENU PRINCIPAL'.center(40))
        print('--'*20)
        print("""\033[33m1 -\033[m \033[34mVer pessoas cadastradas\033[m
\033[33m2 -\033[m \033[34mCadastrar nova Pessoa\033[m    \033[33m
3 -\033[m \033[34mSair do Sistema\033[m""")
        print('--'*20)
        try:
            opcao = int(input('\033[33mSua Opção: \033[m \033[32m'))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um numero inteiro de 0 a 3\033[m')
        except KeyboardInterrupt:
            print('\033[0;31mO usuario pinterrompeu o programa\033[m')
        else:
            if opcao <=3 and opcao >=1:
                print('\033[m--'*20)
                print(f'OPÇÃO {opcao}'.center(40))
                print('--'*20)
                if opcao ==3:
                    print(f'\033[mFim do programa, volte sempre.')
                    break
            else:
                print('\033[0;31mDigite um numero inteiro de 0 a 3, conforme menu.\033[m')


#menu()