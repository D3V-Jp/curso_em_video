from time import sleep
list = ('Lápis' , 1.75,
        'Anel' , 5.00,
        'Papel', 0.50,
        'Caneta', 2.00,
        'Mochila', 20.00,
        'Regua', 2.00,
        'Estojo', 10.00,
        'Livro', 34.90,
        'Lápis d/cor', 13.33)

print('-'*40)
print(f'{"Lista de valores":^40}')
print('-'*40)
for item in range(0,len(list)):
    sleep(0.2)
    if item % 2 == 0:
        print(f'{list[item]:.<30}', end='')
    else:
        print(f'R$ {list[item]}')
print('-'*40)
# 16/03/23

