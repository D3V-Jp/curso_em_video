from random import randint
print('\033[4;35mJogo do impar ou par.\033[m')

while True:
    print('=-'*20)
    computer = randint(0,10)
    younumber = int(input('Qual número você vai jogar: '))
    soma = computer + younumber
    escolha = 'nada'
    

    while escolha not in 'IiPp':
        escolha = str(input('Você quer ser Impar (i) ou Par (p): ')).strip()[0]


    par = False
    impar = False
    if soma % 2 == 0:
        par = True
    else: 
        impar = True

    if (escolha in 'Pp' and par == True):
        print(f'Parabéns, você acertou! O computador escolheu {computer} e você {younumber} que juntos são {soma} que da um numero Par!')
        print('Vamos mais uma partida!')
    elif (escolha in 'Ii' and impar == True):
        print(f'Parabéns, voce acertou! O computador escolheu {computer} e você {younumber} que juntos são {soma} que da um numero Impar!')
        print('Vamos mais uma partida!')
    else:
        print(f'Infelizmente você errou! O computador sorteou {computer} e você {younumber} que juntos são {soma}.  ')
        break
# Nao achei dificil. 13/03/23