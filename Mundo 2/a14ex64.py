print('\033[4;35mSomador de numeros.\033[m') 


number = []
contador = 0
confirm = 0


print('-='*20)
while confirm != 1:
    n1 = int(input('Digite um número: '))
    confirm = int(input('Se deseja parar digite 1 ou qualquer outro numero para prosseguir: '))

    number += [n1]
    contador += 1

    
print('-='*20)
print('Ao todo foram digitados {} números que somados dão {}!'.format(contador,sum(number)))
print('-='*20)

# Achei facil, nada demais para raciocinar. 12/03/23