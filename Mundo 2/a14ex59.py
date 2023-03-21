from time import sleep
sair = False

n1 = ''
n2 = ''
while not sair:
    if not (n1 and n2):
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um segundo valor: '))
    
    sleep(1)
    print(''' -=-=-=-
        [1] SOMAR
        [2] MULTIPLICAR 
        [3] MAIOR
        [4] DIGITAR NOVOS NUMEROS
        [5] SAIR DO PROGRAMA''')
    print('-=-=-=-')
    opcao = int(input('Qual sua opção: '))

    if opcao <= 5:
        if opcao == 1:
            print('{} + {} = {}'.format(n1,n2,n1+n2))
            sleep(2)
            continue
        elif opcao == 2:
            print('{} x {} = {}'.format(n1,n2,n1*n2))
            sleep(2)
            continue
        elif opcao ==4:
            n1 = n2 = False  
            print('-=-=-=-')
            continue        
        elif opcao == 5:
            print('O programa será fechado! Em 1 segundo.')
            sleep(1)
            break
        if opcao == 3:
            if n1 > n2:
                print('{} é maior que {}.'.format(n1,n2))
                sleep(2)
            else:
                print('{} é maior que {}.'.format(n2,n1))
                sleep(2)
    else: print('Por favor seleciona uma opção VALIDA!')
    sleep(1.9)
# Não precisei de ajuda, consegui tirar de letra. 09/03/23