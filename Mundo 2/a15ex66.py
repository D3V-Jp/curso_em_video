print('\033[4;35mSomador de numeros.\033[m')

count = 0
number = []
while True:
    n1 = int(input('Digite um valor [p/parar 999]: '))
    if n1 == 999:
        break
    number += [n1]
    count += 1 
print(f'Dos {count} numeros digitados, a soma é {sum(number)}!')
# Facil até demais. 13/03/23