n1 = int(input('Qual numero você quer converter? > '))
conversor = int(input('''Quer converter para qual? 
(1)Hexadecimal 
(2)Binario 
(3)Octal > '''))
y = 3

if conversor <= y:
    if conversor == 1:
        print('Seu valor em Hexadecimal fica {} > '.format(hex(n1)))
    if conversor == 2:
        print('Seu valor é igual a {}'.format(bin(n1)))
    if conversor == 3:
        print('Seu valor em Octal fica {} > '.format(oct(n1)))
else: print('f')
# Essa vai ser dificil em questao logica, nao terminei a12, dia 22/02/23
# Era só usar algo que ja existia no python para converter (era facil desde o inicio). 23/02/22
# Esse codigo ta totalmente falho, nao use como exemplo pra nada. 23/02/22
