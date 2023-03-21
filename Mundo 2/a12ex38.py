n1 = int(input('Escolha o primeiro valor para comparação:  '))
n2 = int(input('Escolha o segundo valor para comparação:  '))

if n1>n2:
    print('{} é maior que {}'.format(n1,n2))
elif n2>n1:
    print('{} é menor que {}'.format(n1,n2))
else: print('Ambos valores são iguais.')

# É muito simples. 23/02/23