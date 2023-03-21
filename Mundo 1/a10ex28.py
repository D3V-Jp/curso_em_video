from random import randint
from time import sleep

n1 = randint(0,5)
print(n1)
print('-=-'*20)
print('Vamos começar, ESCOLHA UM NÚMERO de 0 a 5.')
n2 = int(input('Escolhe um número > '))
print('.. Processando sua resposta')
print('-=-'*20)
sleep(2)
if n1 == n2:
    print('Correto o número escolhido era realmente o {}'.format(n1))
else: print('o número correto era o {}'.format(n1))
print('-=-'*20)
# Low diff. 08-07-2022