print('\033[4;35mMenores valores e media.\033[m')

number = []
contador = 0

confirm = 's'
while confirm in 'Ss':

    num = int(input('Digite um número: '))
    number += [num]
    contador += 1

    media = sum(number) / len(number)
    maior = max(number)
    menor = min(number)

    confirm = str(input('Quer continuar [S/N]: ')).strip()[0]
    if confirm in 'SsNn':
        continue
    else:
        while confirm not in 'SsNn':
            confirm = str(input('Por favor selecione uma opção valida [S/N]: ')).strip()[0]
        continue


print('Você digitou {} numeros e a média foi de {:.2f}.'.format(contador,media))
print('Dos numeros digitados o maior foi {} e o menor {}.'.format(maior,menor))
# Algumas variaveis tava dando valor 0 nao sei porque. 12/03/23