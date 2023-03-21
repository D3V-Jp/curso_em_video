print('\033[4;35mSequencia de Fibonacci.\033[m') 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
termo = int(input('Quantos termos deseja ver: '))
n1 = 0
n2 = 1
n3 = 0


while True:
    print('{} → {}'.format(n1,n2), end='') 
    for c in range(1,(termo+1) - 2):
        n3 = n1 + n2
        print(' → {}'.format(n3), end='')
        n1 = n2 
        n2 = n3
    break
print(' → Fim.')

# Exigiu um raciocinio avançado. 12/03/23