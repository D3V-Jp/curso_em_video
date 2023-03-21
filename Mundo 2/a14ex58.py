from random import randint

print('O computador sorteou um numero de 0 a 10, adivinhe qual foi!')

you = 0
computer = randint(0,10)
tentativas = 0
while not you == computer:
    you = int(input('Qual numero o computador deve ter sorteado: '))
    if you > computer:
        print('Menos.. tente denovo!')
        tentativas += 1
        continue
    else: 
        print('Mais.. tente denovo!')
        tentativas += 1
print('Você acertou! Após {} tentativas.'.format(tentativas))

# Eu poderia fazer de uma forma mais simples usando Break, porem eu preferi fazer com os recursos que me foram apresentados até o momento. 09/03/23.