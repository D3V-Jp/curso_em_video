from time import sleep

print('\033[4;35mTabuada V3.\033[m')
while True:
    print('=-'*20)
    n1 = int(input('Que tabuada deseja ver [Digite 0 p/parar]: '))
    count = 1
    if n1 <= 0:
        print('O programa será encerrado em 1 segundos.')
        sleep(1)
        break

    print('=-'*20)
    while count <= 10:
        sleep(0.5)
        print(f'{n1} x {count} = {n1*count}')
        count += 1
# Achei facil. 13/03/23