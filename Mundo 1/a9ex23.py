import random
n1 = (random.randint(0,2000))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print('Você Sorteou o número {}!'.format(n1))
print('Sua unidade é de {}'.format(u))
print('Sua dezena é de {}'.format(d))
print('Sua centena é de {}'.format(c))
print('Seu milhar de {}'.format(m))
# Extreme diff, precisei copiar. 02-07-2022