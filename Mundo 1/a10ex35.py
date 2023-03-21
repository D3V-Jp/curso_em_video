from time import sleep
from random import randint

print('-='*20)
r1 = int(input('Reta n1 > '))
r2 = int(input('Reta n2 > '))
r3 = int(input('Reta n3 > '))
print('-='*20)
print('PROCESSANDO..')
sleep(0.5)
print('PROCESSAMENTO {}%..'.format(randint(0,80)))
sleep(0.5)
print('PROCESSAMENTO {}%..'.format(randint(81,99)))
sleep(0.6)
print('PROCESSAMENTO 100% CONCLUIDO.')
print('-='*20)

# verificar menor reta
menor = r1
if r2<r3 and r2<r1:
    menor = r2
if r3<r2 and r3<r1:
    menor = r3
# verificando maior reta
maior = r1
if r2>r3 and r2>r1:
    maior = r2
if r3>r2 and r3>r1:
    maior = r3
# verificando menor reta 2
menor2 = r1
if r2<maior and r2>menor:
    menor2 = r2
if r3<maior and r3>menor:
    menor2 = r3
# calculando menores retas
print('...-'*20)
if menor + menor2 >= maior:
    print('É possivel formar SIM um triangulo.')
else: print('Infelizmente NÃO será possivel formar um triangulo com essas retas.')
print('...-'*20)
# confused diff. tem uma forma muito mais simples de fazer:
# if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2 ( jeito simples ). 09-07-2022