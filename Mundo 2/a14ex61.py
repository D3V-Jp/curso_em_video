a = int(input('Primeiro termo da PA: ').strip())
b = int(input('Razão da PA: ').strip())
c = a
print('{}, '.format(a), end='')
while a != c + 9 * b:
    a = a + b
    print('{}, '.format(a), end='')
print('Fim')
# peguei a resposta pois não estou com cabeça para estudar. 09/03/23